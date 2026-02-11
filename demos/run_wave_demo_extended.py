#!/usr/bin/env python3
"""Extended end-to-end demo: Wave 1-3 parallel scheduling skeleton (enhanced)."""
import time
import os
import sys

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


def run_extended_demo():
    # Wave 1/2 context (demo purposes)
    pm = PlanManager()
    waves = [
        {"name": "Wave 1", "description": "Discovery (demo)", "tasks": ["discover-a", "discover-b"]},
        {"name": "Wave 2", "description": "Planning (demo)", "tasks": ["plan-a", "plan-b"]},
        {"name": "Wave 3", "description": "Prototype (demo)", "tasks": ["proto-a", "proto-b"]},
    ]
    pm.add_plan("demo_extended", "End-to-end extended Wave demo", waves)

    # Wave 3 prototype: three parallel tasks to showcase concurrency
    tasks = [make_task("proto-a", 0.25), make_task("proto-b", 0.15), make_task("proto-c", 0.20)]
    runner = ParallelRunner(max_workers=3)
    results = runner.run(tasks)
    print("Extended Wave 3 parallel results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    run_extended_demo()
