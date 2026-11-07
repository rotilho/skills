#!/usr/bin/env python3
"""Run an argv command in a detached systemd user service and track its result."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import uuid


def write_status(job, values):
    target = job / "status.json"
    temporary = job / (".status.json.tmp." + str(os.getpid()))
    temporary.write_text(json.dumps(values, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, target)


def read_status(job):
    return json.loads((job / "status.json").read_text(encoding="utf-8"))


def notify(job, state):
    try:
        subprocess.run(["notify-send", "Background job " + state,
                        "Result: " + str(job / "status.json")],
                       stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=False, timeout=5)
    except (OSError, subprocess.TimeoutExpired):
        pass


def worker(job, command, cwd):
    status = read_status(job)
    status.update(state="running", started_at=time.time())
    write_status(job, status)
    child = None
    stopping = False

    def stop(signum, frame):
        nonlocal stopping
        stopping = True
        if child is not None and child.poll() is None:
            child.terminate()

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        with (job / "output.log").open("ab", buffering=0) as output:
            child = subprocess.Popen(command, cwd=cwd, stdin=subprocess.DEVNULL,
                                     stdout=output, stderr=subprocess.STDOUT,
                                     start_new_session=True)
            while child.poll() is None:
                if stopping:
                    try:
                        child.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        child.kill()
                    break
                time.sleep(.1)
            code = child.wait()
    except Exception as error:
        with (job / "output.log").open("ab") as output:
            output.write(("job runner error: " + str(error) + "\n").encode())
        code = 1
    state = "cancelled" if stopping else ("succeeded" if code == 0 else "failed")
    status.update(state=state, exit_status=code, finished_at=time.time())
    write_status(job, status)
    notify(job, state)
    return 0 if state == "succeeded" else (143 if state == "cancelled" else code or 1)


def runtime_environment_args():
    # Preserve command lookup and pass only desktop-session routing values.
    names = ("PATH", "DBUS_SESSION_BUS_ADDRESS", "DISPLAY", "WAYLAND_DISPLAY",
             "XDG_RUNTIME_DIR", "XAUTHORITY")
    return ["--setenv=" + name + "=" + os.environ[name]
            for name in names if os.environ.get(name)]


def start(args):
    command = args.command
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        raise SystemExit("start requires a command after --")
    cwd = Path(args.cwd).expanduser().resolve(strict=True)
    if not cwd.is_dir():
        raise SystemExit("--cwd must be a directory")
    root = Path(args.state_dir).expanduser() if args.state_dir else Path(
        os.environ.get("XDG_STATE_HOME", Path.home() / ".local/state")) / "codex-long-running-jobs"
    root.mkdir(parents=True, exist_ok=True)
    root = root.resolve()
    job = root / str(uuid.uuid4())
    job.mkdir(mode=0o700)
    unit = "codex-job-" + job.name
    status = {"id": job.name, "unit": unit, "state": "queued", "cwd": str(cwd),
              "command": command, "created_at": time.time(), "exit_status": None}
    write_status(job, status)
    invocation = [sys.executable, str(Path(__file__).resolve()), "_worker",
                  str(job), str(cwd), "--", *command]
    try:
        subprocess.run(["systemd-run", "--user", "--collect", "--service-type=exec",
                        "--expand-environment=no", "--working-directory", str(cwd),
                        "--property=KillMode=control-group", "--property=TimeoutStopSec=10",
                        "--unit", unit,
                        *runtime_environment_args(), "--", *invocation],
                       check=True, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError) as error:
        status.update(state="failed", exit_status=127, finished_at=time.time())
        write_status(job, status)
        raise SystemExit("could not start systemd user job: " + str(error))
    print("id: " + job.name)
    print("path: " + str(job))
    print("unit: " + unit)


def cancel(job):
    status = read_status(job)
    if status["state"] in ("queued", "running"):
        try:
            stopped = subprocess.run(["systemctl", "--user", "stop", status["unit"]],
                                     check=False, stdin=subprocess.DEVNULL)
        except OSError as error:
            raise SystemExit("could not stop systemd user job: " + str(error))
        if stopped.returncode:
            raise SystemExit("systemctl stop failed with exit status " + str(stopped.returncode))
        status = read_status(job)
        if status["state"] in ("queued", "running"):
            status.update(state="cancelled", exit_status=143, finished_at=time.time())
            write_status(job, status)
    print(json.dumps(read_status(job), indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    begin = sub.add_parser("start")
    begin.add_argument("--cwd", required=True)
    begin.add_argument("--state-dir")
    begin.add_argument("command", nargs=argparse.REMAINDER)
    inspect = sub.add_parser("status")
    inspect.add_argument("job_dir")
    stop = sub.add_parser("cancel")
    stop.add_argument("job_dir")
    internal = sub.add_parser("_worker")
    internal.add_argument("job_dir")
    internal.add_argument("cwd")
    internal.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.action == "start":
        start(args)
    elif args.action == "status":
        print(json.dumps(read_status(Path(args.job_dir)), indent=2))
    elif args.action == "cancel":
        cancel(Path(args.job_dir))
    else:
        command = args.command[1:] if args.command and args.command[0] == "--" else args.command
        raise SystemExit(worker(Path(args.job_dir), command, args.cwd))


if __name__ == "__main__":
    main()
