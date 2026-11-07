import json
import contextlib
import io
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/job.py"
from importlib.util import module_from_spec, spec_from_file_location
SPEC = spec_from_file_location("job_helper", SCRIPT)
JOB_HELPER = module_from_spec(SPEC)
SPEC.loader.exec_module(JOB_HELPER)


class JobTests(unittest.TestCase):
    def make_job(self, root, command):
        job = root / "job with spaces"
        job.mkdir()
        (job / "status.json").write_text(json.dumps({
            "id": "job-test", "unit": "codex-job-test", "state": "queued",
            "cwd": str(root), "command": command, "exit_status": None,
        }))
        return job

    def run_worker(self, job, root, command):
        return subprocess.run([sys.executable, str(SCRIPT), "_worker", str(job),
                               str(root), "--", *command], check=False)

    def status(self, job):
        return json.loads((job / "status.json").read_text())

    def test_success_preserves_argv_and_logs_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result_file = root / "literal path with spaces.txt"
            command = [sys.executable, "-c",
                       "import pathlib,sys; pathlib.Path(sys.argv[1]).write_text(repr(sys.argv[2:])); print('done')",
                       str(result_file), "two words", "$(not a shell)"]
            job = self.make_job(root, command)
            result = self.run_worker(job, root, command)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result_file.read_text(), "['two words', '$(not a shell)']")
            self.assertEqual(self.status(job)["state"], "succeeded")
            self.assertIn(b"done", (job / "output.log").read_bytes())

    def test_failure_records_exit_status_and_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            command = [sys.executable, "-c", "import sys; print('failure'); sys.exit(7)"]
            job = self.make_job(root, command)
            result = self.run_worker(job, root, command)
            self.assertEqual(result.returncode, 7)
            status = self.status(job)
            self.assertEqual((status["state"], status["exit_status"]), ("failed", 7))
            self.assertIn(b"failure", (job / "output.log").read_bytes())

    def test_sigterm_during_job_records_cancelled(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            command = [sys.executable, "-c", "import time; time.sleep(30)"]
            job = self.make_job(root, command)
            proc = subprocess.Popen([sys.executable, str(SCRIPT), "_worker", str(job),
                                     str(root), "--", *command])
            deadline = time.time() + 5
            while self.status(job)["state"] != "running" and time.time() < deadline:
                time.sleep(.02)
            proc.send_signal(signal.SIGTERM)
            self.assertEqual(proc.wait(timeout=6), 143)
            self.assertEqual(self.status(job)["state"], "cancelled")

    def test_start_uses_literal_argv_and_safe_absolute_systemd_launch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cwd = root / "work dir"
            cwd.mkdir()
            old_cwd = Path.cwd()
            os.chdir(root)
            try:
                with patch.dict(os.environ, {"PATH": "/test/bin"}, clear=True):
                    with patch.object(JOB_HELPER.subprocess, "run") as run, contextlib.redirect_stdout(io.StringIO()):
                        JOB_HELPER.start(type("Args", (), {
                            "cwd": str(cwd), "state_dir": "relative state",
                            "command": ["--", "./build tool", "$HOME/literal"],
                        })())
                argv = run.call_args.args[0]
                self.assertIn("--expand-environment=no", argv)
                self.assertIn("--service-type=exec", argv)
                self.assertIn("--working-directory", argv)
                self.assertIn(str(cwd), argv)
                self.assertIn("--property=KillMode=control-group", argv)
                self.assertIn("--property=TimeoutStopSec=10", argv)
                self.assertIn("--setenv=PATH=/test/bin", argv)
                self.assertIn("$HOME/literal", argv)
                job_dir = Path(argv[argv.index("--") + 4])
                self.assertTrue(job_dir.is_absolute())
                self.assertEqual((job_dir / "status.json").exists(), True)
            finally:
                os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
