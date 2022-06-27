from typing import List
import concurrent.futures
import multiprocessing
from concurrent.futures import Future


class Run_Concurrent():
    def __init__(self) -> None:
        self.futures_list: List[Future] = []
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=(2 * multiprocessing.cpu_count() + 1))

    def append_task(self, func, *args):
        future = self.executor.submit(func, *args)
        self.futures_list.append(future)

    def run(self):
        results = []
        with self.executor:
            for future in self.futures_list:
                try:
                    res = future.result(timeout=60)
                    results.append(res)
                except Exception:
                    results.append(None)
            return results
