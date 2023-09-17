from typing import List


def is_valid_matrix_graph(graph: List[List[int]]) -> bool:
    if not isinstance(graph, list):
        return False

    for row in graph:
        if not isinstance(row, list):
            return False
        for column in row:
            if not isinstance(column, int):
                return False

    return True
