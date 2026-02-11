import time
from ultrawork_skeleton.runner import ParallelRunner

def task(name, duration=0.1):
    time.sleep(duration)
    return f"{name}-done"

def test_parallel_runner_runs_three_tasks_in_parallel():
    runner = ParallelRunner(max_workers=3)
    results = runner.run([
        lambda: task("t1", 0.2),
        lambda: task("t2", 0.1),
        lambda: task("t3", 0.15),
    ])
    assert len(results) == 3
    assert any("t1" in str(r) for r in results)
