import timeit
import tracemalloc
from typing import List

import psutil

from src.floyd_warshall_algorithm import FloydWarshallAlgorithm
from src.utils.constants import NO_PATH
from src.utils.file_utils import write_to_file

LIGHT_TEST_GRAPH = [
    [0, 5, NO_PATH, 10],
    [NO_PATH, 0, 3, NO_PATH],
    [NO_PATH, 1, 0, 1],
    [3, NO_PATH, NO_PATH, 0]
]

HEAVY_TEST_GRAPH = [
    [0, 4, 7, 14, 16, 10, 7, 4, 10],
    [NO_PATH, 0, 4, 11, 12, 6, 8, 1, 7],
    [4, NO_PATH, 0, 7, 10, 15, NO_PATH, 9, 3],
    [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, 2, 3, NO_PATH],
    [2, NO_PATH, 8, 6, 0, 5, NO_PATH, 17, 11],
    [NO_PATH, NO_PATH, 14, 12, 6, 0, NO_PATH, 23, 17],
    [NO_PATH, 4, 8, 15, 13, 7, 0, 5, 11],
    [NO_PATH, NO_PATH, 3, 10, 13, 18, 3, 0, 6],
    [5, NO_PATH, 9, 4, 19, 24, NO_PATH, 6, 0]
]


def _execute_performance_tests(graph: List[List[int]]):
    number_of_runs = 10_000

    with open('../../../recursive-floyd-algorithm/docs/performance_test_results.txt', 'w') as file:
        tracemalloc.start()
        for i in range(3):
            tracemalloc.clear_traces()

            if i == 0:
                test_graph_type = "light" if graph == LIGHT_TEST_GRAPH else "heavy"
                write_to_file(file, f"Testing {test_graph_type} test graph:\n")

            recursive_time = timeit.timeit(lambda: FloydWarshallAlgorithm.execute(graph, use_recursion=True),
                                           number=number_of_runs)
            write_to_file(file, f"Recursive memory usage (current, peak): {tracemalloc.get_traced_memory()}")
            write_to_file(file, f"Recursive running time over {number_of_runs} runs: {recursive_time}")
            write_to_file(file, f"CPU usage percentage after recursion task: {psutil.cpu_percent(interval=None)}")

            tracemalloc.clear_traces()

            iterative_time = timeit.timeit(lambda: FloydWarshallAlgorithm.execute(graph), number=number_of_runs)
            write_to_file(file, f"Iterative memory usage (current, peak): {tracemalloc.get_traced_memory()}")
            write_to_file(file, f"Iterative running time over {number_of_runs} runs: {iterative_time}")
            write_to_file(file, f"CPU usage percentage after iterative task: {psutil.cpu_percent(interval=None)}")

            number_of_runs *= 5

        tracemalloc.stop()


if __name__ == '__main__':
    _execute_performance_tests(LIGHT_TEST_GRAPH)
    _execute_performance_tests(HEAVY_TEST_GRAPH)
