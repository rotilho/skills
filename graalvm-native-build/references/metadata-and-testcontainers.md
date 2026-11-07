# Reachability metadata and containerized tests

Use the metadata section when the project requires agent output or when diagnosing tracing failures. Read the container section only when the selected tests need Testcontainers. Reuse the distribution, image, and mounts established by the main workflow.

## Generate or consume metadata

When CI uses the native-image agent, run the same metadata-producing task before `nativeCompile`.

If investigating a tracing-agent regression or warning, first create the smallest Java repro that triggers the same agent path and run it inside the matching builder image. Prefer this before a full Gradle, Cucumber, or integration-test metadata run so you can separate a GraalVM agent bug from application startup cost.

Reuse the builder command with the project's metadata-producing task, such as `./gradlew -Pagent test --no-daemon --info --fail-fast` when that is how the project enables the agent.

If the project does not already wire the generated metadata into the build, append `-H:ConfigurationFileDirectories=<actual-agent-output>` to its existing native-image options inside the builder.

## Tests that require containers

If the metadata-producing tests use Testcontainers, discover the active host container socket, mount it into the builder, and set `DOCKER_HOST` to the mounted path. Verify access from inside the builder. For Podman, set `TESTCONTAINERS_HOST_OVERRIDE=host.containers.internal` when mapped service ports must resolve to the host instead of builder-local `localhost`.

Verify both socket consumers: the builder uses `DOCKER_HOST`, while the host daemon resolves the socket bind mount requested for the sibling Ryuk container. A renamed builder-only path can pass a socket API probe yet fail when the daemon tries to mount that nonexistent host path. Prefer mounting the socket at its actual host path inside the builder and using that same path in `DOCKER_HOST`; if paths must differ, set `TESTCONTAINERS_DOCKER_SOCKET_OVERRIDE` to the daemon-visible host path. Run one small real container-backed test before the full suite to verify socket access, Ryuk startup, and mapped-port reachability together.

Keep the builder network isolated when tests require fixed application ports already occupied on the host; `host.containers.internal` can still reach published test-service ports. If Ryuk still fails its callback connection after socket and network checks, use `TESTCONTAINERS_RYUK_DISABLED=true` only for that run and clean up its test containers afterward.

If socket access fails, report that as an environment issue. If Ryuk is disabled, clean up any test containers that the failed run leaves behind. Do not bypass either issue by installing GraalVM on the host.
