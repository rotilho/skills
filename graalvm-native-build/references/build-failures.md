# Native build failures

Use the matching symptom after capturing the actual build failure. Keep diagnosis-only requests read-only; apply source/metadata changes and rerun when a working build is the authorized outcome.

- `x86_64-linux-musl-gcc not found`: use the `*-muslib` native-image image for static musl builds.
- The GHCR Community `latest` or feature tag may be older than the Oracle GraalVM tag used by `graalvm/setup-graalvm`; verify versions instead of assuming it is the newest available GraalVM.
- `cannot find -lstdc++`: the build is not using a complete musl-capable native-image image or its musl toolchain is not on `PATH`.
- undefined glibc symbols such as `__libc_single_threaded`, `__memcpy_chk`, or `__fprintf_chk`: the link is mixing glibc static libraries into a musl build; switch to the official muslib image or fix the container toolchain path.
- `MissingReflectionRegistrationError`: generate reachability metadata with the same task CI uses, add missing metadata, or remove the reflection path.
- `Could not find option 'MaxRAMPercentage'`: first reproduce the failure with the project's CI `NATIVE_IMAGE_OPTIONS`, then rerun with the smallest local override, such as removing the unsupported `-R:MaxRAMPercentage=...` option for the current GraalVM image. Report the override explicitly because CI may be pinned to a different native-image version or may need its option updated.
- native-image runs out of memory: reduce native-image parallelism or adjust the project's native-image options; report the exact memory failure and machine/container limit.
