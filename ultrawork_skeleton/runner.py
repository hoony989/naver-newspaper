from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, List, Any

class ParallelRunner:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def run(self, tasks: List[Callable[[], Any]]):
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_task = {executor.submit(t): t for t in tasks}
            for fut in as_completed(future_to_task):
                try:
                    results.append(fut.result())
                except Exception as e:
                    results.append({"error": str(e)})
        return results
