from typing import List


from src.exceptions import InvalidArgumentTypeError
from src.utils.graph_utils import is_valid_matrix_graph


class FloydWarshallAlgorithm:

    @staticmethod
    def __update_distance(graph: List[List[int]], start_node: int, intermediate_node: int, end_node: int) \
            -> List[List[int]]:
        if start_node == end_node:
            graph[start_node][end_node] = 0

        else:
            graph[start_node][end_node] = (
                min(graph[start_node][end_node],
                    graph[start_node][intermediate_node] + graph[intermediate_node][end_node])
            )
        return graph

    @staticmethod
    def __recursive(graph: List[List[int]], intermediate_node=0, start_node=0, end_node=0) -> List[List[int]]:
        max_length = len(graph)

        if intermediate_node >= max_length:
            return graph

        elif start_node >= max_length:
            return FloydWarshallAlgorithm.__recursive(graph, intermediate_node + 1, 0, 0)

        elif end_node >= max_length:
            return FloydWarshallAlgorithm.__recursive(graph, intermediate_node, start_node + 1, 0)

        else:
            graph = FloydWarshallAlgorithm.__update_distance(graph, start_node, intermediate_node, end_node)
            return FloydWarshallAlgorithm.__recursive(graph, intermediate_node, start_node, end_node + 1)

    @staticmethod
    def __iterative(graph: List[List[int]]) -> List[List[int]]:
        max_length = len(graph)
        for intermediate_node in range(max_length):
            for start_node in range(max_length):
                for end_node in range(max_length):
                    FloydWarshallAlgorithm.__update_distance(graph, start_node, intermediate_node, end_node)
        return graph

    @staticmethod
    def execute(graph: List[List[int]], use_recursion=False):
        if is_valid_matrix_graph(graph):
            return FloydWarshallAlgorithm.__recursive(graph) \
                if use_recursion else FloydWarshallAlgorithm.__iterative(graph)

        else:
            raise InvalidArgumentTypeError("Graph must be a List[List[int]].")
