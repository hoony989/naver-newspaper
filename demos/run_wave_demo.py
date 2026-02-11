#!/usr/bin/env python3
"""End-to-end demo: Wave 1-3 parallel scheduling skeleton."""
import time
import sys
import os

# Ensure local package path is importable when running from repo root
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ultrawork_skeleton.plan import PlanManager
from ultrawork_skeleton.runner import ParallelRunner


def make_task(name: str, duration: float):
    def _task():
        time.sleep(duration)
        return f"{name}-done"
    return _task


def run_demo():
    # Step 1: create a tiny plan and waves (demo purposes only)
    pm = PlanManager()
    waves = [
        {"name": "Wave 1", "tasks": ["t1", "t2", "t3"]}
    ]
    pm.add_plan("demo", "End-to-end Wave demo", waves)

    # Step 2: build 3 parallel tasks as a demonstration
    tasks = [make_task("t1", 0.2), make_task("t2", 0.1), make_task("t3", 0.15)]
    runner = ParallelRunner(max_workers=3)
    results = runner.run(tasks)
    print("Wave demo results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    run_demo()
