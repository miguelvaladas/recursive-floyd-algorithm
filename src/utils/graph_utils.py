from typing import List


def is_valid_matrix_graph(graph: List[List[int]]) -> bool:
    """
    Utility function that validates if the input graph is of a valid type (List[List[int]]).

    :param graph: A list to represent the graph.
    :return: A boolean to indicate if the input graph is valid.
    """
    if not isinstance(graph, list):
        return False

    for row in graph:
        if not isinstance(row, list):
            return False
        for column in row:
            if not isinstance(column, int):
                return False

    return True
