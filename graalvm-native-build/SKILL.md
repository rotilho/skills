---
name: "graalvm-native-build"
version: "1.1.1"
description: "Build or debug GraalVM Native Image in disposable containers matching the project toolchain. Use for native compilation, static musl linking, or reachability-metadata failures; skip ordinary JVM builds."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "build"
---

# GraalVM Native Build

Build native binaries while keeping GraalVM, compilers, musl, and package installs inside disposable containers. Host toolchain installation requires an explicit request.

## Establish the requested outcome and build shape

Distinguish a working native build from a diagnosis/reproduction report. For a working-build request, fix relevant application or metadata failures and rerun the affected build. For diagnosis-only work, reproduce within the authorized scope and report the failure and proposed correction without editing source. Image packaging and runtime testing depend on the requested outcome; do not claim application behavior from compilation alone.

Inspect relevant CI setup, Dockerfiles, build files, native-build notes, and existing `META-INF/native-image` metadata. Identify the distribution, Java feature version, native task/profile, options, linking mode, and metadata inputs. Search existing paths with `rg`, for example:

```bash
rg -n 'nativeCompile|native-image|graal|GRAAL|JAVA_HOME|NATIVE_IMAGE_OPTIONS|musl|--static|native:compile' .github build.gradle.kts README.md
```

Adapt paths to the repo. Missing paths are not a build failure. Use CI settings or the user's explicit target; report any local overrides.

## Select and verify the builder

Prefer disposable Podman; use Docker when Podman is unavailable. Match the project's GraalVM distribution and Java version. For static musl, use the corresponding `*-muslib` image:

- `container-registry.oracle.com/graalvm/native-image:<java-feature>-muslib` for CI using `graalvm/setup-graalvm` with `distribution: graalvm`.
- `ghcr.io/graalvm/native-image-community:<java-feature>-muslib` when CI or the user targets Community Edition.

Set `builder_image` accordingly and print actual versions; tags can differ between distributions:

```bash
podman run --rm --pull=missing --entrypoint /bin/bash "$builder_image" -lc 'java -version && native-image --version'
```

Use `--pull=never` only when the cached image is known to be sufficient. Keep downloads/caches in dedicated mounts rather than the host toolchain.

## Run the project's build

Mount only what the build needs, using absolute paths and the project's wrapper/native task:

```bash
podman run --rm --pull=missing \
  -v /absolute/path/to/project:/workspace/project \
  -v /tmp/project-gradle:/gradle-home \
  -e GRADLE_USER_HOME=/gradle-home \
  --entrypoint /bin/bash \
  "$builder_image" \
  -lc 'cd /workspace/project && ./gradlew --no-daemon nativeCompile'
```

For Maven, use its wrapper and native command, replace the cache mount with `/tmp/project-m2:/m2`, and set `MAVEN_OPTS=-Dmaven.repo.local=/m2`. Docker uses equivalent mounts/environment. On SELinux hosts, add `--security-opt label=disable` only when mount access requires it.

- Read [metadata and Testcontainers guidance](references/metadata-and-testcontainers.md) when generating/diagnosing agent output or when selected tests require containers. Existing metadata does not automatically require another tracing run. Preserve CI-required generation steps.
- Read the matching [failure guidance](references/build-failures.md) after capturing a native-image or linker error. Reproduce original options before trying a minimal override, and disclose it.

Container socket access and Ryuk failures are environment issues. Do not bypass them by installing host GraalVM. If disabling Ryuk for a run, clean up the test containers it leaves behind.

## Verify and report the result

For a successful build, inspect the binary from the host and report its path and size:

```bash
file build/native/nativeCompile/<binary>
ldd build/native/nativeCompile/<binary> || true
```

For static Linux output, check that `file` reports static linking and `ldd` reports no dynamic executable. Build an application image only when packaging is requested and the binary passes the required checks. Run the project's native smoke check before claiming it works at runtime; a compile-only result should say runtime behavior was not verified.

Report the distribution and versions, effective options and overrides, artifact/linking evidence or confirmed failure, relevant metadata/container-test results, and source edits separately from build outputs. Repair failures caused by authorized fixes and complete the affected verification; stop at the user's diagnosis or review boundary when that is the requested result.
