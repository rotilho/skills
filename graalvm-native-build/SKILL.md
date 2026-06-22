---
name: "graalvm-native-build"
version: "1.0.0"
description: "Compile GraalVM native-image applications locally in disposable Podman or Docker builder containers. Use when the user asks to build a native binary, run Gradle nativeCompile or Maven native compilation, reproduce CI native-image builds, build static musl binaries, generate or use reachability metadata, or debug native-image linker and metadata failures without installing GraalVM tooling on the host."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "build"
  style: "concise"
---

# GraalVM Native Build

Build GraalVM native binaries locally while keeping GraalVM, native-image, musl, compilers, and package installs inside disposable containers.

## When to use

Trigger for requests like:
- compile this app with GraalVM locally
- run `nativeCompile`, `nativeTest`, or Maven native compilation
- reproduce the CI native-image build
- build a static musl native image
- generate or consume native-image reachability metadata
- debug native-image linker, reflection, metadata, or missing toolchain errors

Do not use for ordinary JVM tests, Docker image pulls, or application container builds unless the request involves GraalVM Native Image.

## Core promise

Produce or diagnose a local native binary using the project's build settings as closely as practical, without installing GraalVM or native build tooling on the host.

## Hard constraints

- Inspect the project first. Prefer CI workflow files, `Dockerfile`, `build.gradle(.kts)`, `pom.xml`, README native-build notes, and existing `META-INF/native-image` metadata.
- Do not install GraalVM, compilers, musl, or package-manager dependencies on the host unless the user explicitly asks.
- Prefer disposable `podman run --rm` containers. Use `docker run --rm` only when Podman is unavailable.
- Use the project's CI Java feature version and native-image options instead of guessing.
- For static musl builds, prefer `ghcr.io/graalvm/native-image-community:<java-feature>-muslib`, for example `ghcr.io/graalvm/native-image-community:25-muslib`.
- Keep downloaded dependencies and build caches outside the host toolchain, usually in container mounts such as `/tmp/<project>-gradle` or `/tmp/<project>-m2`.
- If tests need Testcontainers, pass the host container socket into the builder container instead of switching to host GraalVM.
- If the native build fails because of application code or metadata, fix the smallest relevant code or metadata issue and rerun the focused native build.

## Workflow

### 1. Read the build shape

Look for:
- CI native-image setup
- Java or GraalVM version
- `NATIVE_IMAGE_OPTIONS`
- `nativeCompile`, `nativeTest`, `native:compile`, or Spring Boot native profiles
- static linking flags such as `--static` and `--libc=musl`
- reachability metadata in `META-INF/native-image` or `build/native/agent-output`

Use `rg` first:

```bash
rg -n "nativeCompile|native-image|graal|GRAAL|JAVA_HOME|NATIVE_IMAGE_OPTIONS|musl|--static|native:compile" .github .gitlab-ci.yml Dockerfile* build.gradle* pom.xml README* -S
```

Ignore missing paths from that search; the useful hits are what matter.

### 2. Choose the runtime and image

Prefer Podman:

```bash
command -v podman docker
```

For a static musl Java 25 build, verify or pull:

```bash
podman run --rm --pull=missing --entrypoint /bin/bash ghcr.io/graalvm/native-image-community:25-muslib -lc 'java -version && native-image --version && command -v x86_64-linux-musl-gcc || true'
```

Use `--pull=never` only when the local image is known to be sufficient.

### 3. Build the container command

Mount only what the build needs:

```bash
podman run --rm --pull=missing --security-opt label=disable \
  -v /absolute/path/to/project:/workspace/project \
  -v /tmp/project-gradle:/gradle-home \
  -e GRADLE_USER_HOME=/gradle-home \
  --entrypoint /bin/bash \
  ghcr.io/graalvm/native-image-community:25-muslib \
  -lc 'cd /workspace/project && ./gradlew --no-daemon nativeCompile'
```

For Maven, mount a Maven cache and run the project's native command:

```bash
podman run --rm --pull=missing --security-opt label=disable \
  -v /absolute/path/to/project:/workspace/project \
  -v /tmp/project-m2:/m2 \
  -e MAVEN_OPTS="-Dmaven.repo.local=/m2" \
  --entrypoint /bin/bash \
  ghcr.io/graalvm/native-image-community:25-muslib \
  -lc 'cd /workspace/project && mvn -Pnative native:compile'
```

Use Docker with the same mounts and environment if Podman is unavailable.

### 4. Generate metadata when required

When CI uses the native-image agent, run the same metadata-producing task before `nativeCompile`.

For Gradle:

```bash
podman run --rm --pull=missing --security-opt label=disable \
  -v /absolute/path/to/project:/workspace/project \
  -v /tmp/project-gradle:/gradle-home \
  -e GRADLE_USER_HOME=/gradle-home \
  --entrypoint /bin/bash \
  ghcr.io/graalvm/native-image-community:25-muslib \
  -lc 'cd /workspace/project && ./gradlew -Pagent test --no-daemon --info --fail-fast'
```

Then point the native build at the generated metadata when the project does not already copy it into `src/main/resources/META-INF/native-image`:

```bash
export NATIVE_IMAGE_OPTIONS="--static --libc=musl -H:ConfigurationFileDirectories=/workspace/project/build/native/agent-output/test"
```

### 5. Support Testcontainers from inside the builder

If the metadata-producing tests use Testcontainers, mount the host container socket and set `DOCKER_HOST`. For nested rootless Podman runs, disable Ryuk because the reaper container may start successfully but fail the callback connection to the test JVM inside the builder container.
Also set `TESTCONTAINERS_HOST_OVERRIDE=host.containers.internal` so mapped service ports resolve to the host running Podman, not to `localhost` inside the builder container.

For rootless Podman:

```bash
podman run --rm --pull=missing --security-opt label=disable \
  -v /absolute/path/to/project:/workspace/project \
  -v /tmp/project-gradle:/gradle-home \
  -v /run/user/1000/podman/podman.sock:/run/user/1000/podman/podman.sock \
  -e DOCKER_HOST=unix:///run/user/1000/podman/podman.sock \
  -e TESTCONTAINERS_RYUK_DISABLED=true \
  -e TESTCONTAINERS_HOST_OVERRIDE=host.containers.internal \
  -e GRADLE_USER_HOME=/gradle-home \
  --entrypoint /bin/bash \
  ghcr.io/graalvm/native-image-community:25-muslib \
  -lc 'cd /workspace/project && ./gradlew -Pagent test --no-daemon --info --fail-fast'
```

If socket access fails, report that as an environment issue. If Ryuk is disabled, clean up any test containers that the failed run leaves behind. Do not bypass either issue by installing GraalVM on the host.

### 6. Verify the artifact from the host

Check the binary outside the builder container:

```bash
file build/native/nativeCompile/<binary>
ldd build/native/nativeCompile/<binary> || true
```

For a static Linux binary, `file` should report `statically linked` and `ldd` should report `not a dynamic executable`.

If the project packages the binary into an application image, build that image only after the binary exists and has passed these checks.

## Common failures

- `x86_64-linux-musl-gcc not found`: use the `*-muslib` native-image image for static musl builds.
- `cannot find -lstdc++`: the build is not using a complete musl-capable native-image image or its musl toolchain is not on `PATH`.
- undefined glibc symbols such as `__libc_single_threaded`, `__memcpy_chk`, or `__fprintf_chk`: the link is mixing glibc static libraries into a musl build; switch to the official muslib image or fix the container toolchain path.
- `MissingReflectionRegistrationError`: generate reachability metadata with the same task CI uses, add missing metadata, or remove the reflection path.
- Testcontainers cannot connect to Docker: mount the host container socket and set `DOCKER_HOST`; verify the socket from inside the builder.
- Testcontainers connects to Podman but fails with `Could not connect to Ryuk`: set `TESTCONTAINERS_RYUK_DISABLED=true` for the disposable builder run and clean up leftover test containers after failures.
- Testcontainers starts a service container but JDBC or HTTP checks connect to `localhost:<mapped-port>` and fail: set `TESTCONTAINERS_HOST_OVERRIDE=host.containers.internal` so the builder reaches host-mapped ports.
- `Could not find option 'MaxRAMPercentage'`: first reproduce the failure with the project's CI `NATIVE_IMAGE_OPTIONS`, then rerun with the smallest local override, such as removing the unsupported `-R:MaxRAMPercentage=...` option for the current GraalVM image. Report the override explicitly because CI may be pinned to a different native-image version or may need its option updated.
- native-image runs out of memory: reduce native-image parallelism or adjust the project's native-image options; report the exact memory failure and machine/container limit.

## Verification

Before finishing, confirm:
- the build ran inside `podman run --rm` or `docker run --rm`, not host GraalVM tooling
- the GraalVM Java version matches CI or the user's requested version
- native-image options match CI or are explicitly called out as local overrides
- static musl builds used a `*-muslib` image
- metadata was generated or supplied when the project requires it
- Testcontainers socket and Ryuk handling were tested when metadata tests need containers
- the binary path, size, `file`, and `ldd` results were reported
- any source changes are listed separately from container setup or build-output changes

## Examples

Should trigger:
- "Build this Gradle app with GraalVM nativeCompile locally."
- "Use a disposable container to reproduce the static musl native-image build."
- "Debug this MissingReflectionRegistrationError from the native binary."

Should not trigger:
- "Run the normal JVM unit tests."
- "Build the app Docker image from an existing binary."
- "Install GraalVM on my host machine."
