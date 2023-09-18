from typing import List

from src.exceptions import InvalidArgumentTypeError
from src.utils.graph_utils import is_valid_matrix_graph


class FloydWarshallAlgorithm:
    """
    Class that implements the Floyd Warshall algorithm to find the shortest path
    between all pairs of nodes in a graph, both in an iterative and recursive way.

    Methods:
    - __update_distance: Updates the distance between two nodes.
    - __recursive: A recursive implementation of finding the shortest path between all pairs of nodes.
    - __iterative: An iterative implementation of finding the shortest path between all pairs of nodes.
    - execute: Method for executing the algorithm with a flag to opt for the use of recursion.
    """

    @staticmethod
    def __update_distance(graph: List[List[int]], start_node: int, intermediate_node: int, end_node: int) \
            -> List[List[int]]:
        """
        Private method to update the distance between a pair of nodes (start_node and end_node) in a graph
        if a shorter path is found using an intermediate node.

        :param graph: A list to represent the graph.
        :param start_node: The current starting node.
         :param intermediate_node: The current intermediate node.
        :param end_node: The current end_node.
        :return: Updated graph with the shortest distance between the start_node and end_node.
        """
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
        """
        Private method that implements the Floyd Warshall algorithm using recursion.

        :param graph: A list to represent the graph.
        :param intermediate_node: The current intermediate node.
        :param start_node: The current starting node.
        :param end_node: The current end_node.
        :return: Updated graph with the shortest distance between the start_node and end_node.
        """
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
        """
        Private method that implements the Floyd Warshall algorithm in an iterative way.

        :param graph: A list to represent the graph.
        :return: Updated graph with the shortest distance between the start nodes and end nodes.
        """

        max_length = len(graph)
        for intermediate_node in range(max_length):
            for start_node in range(max_length):
                for end_node in range(max_length):
                    FloydWarshallAlgorithm.__update_distance(graph, start_node, intermediate_node, end_node)
        return graph

    @staticmethod
    def execute(graph: List[List[int]], use_recursion=False):
        """
        Main method to execute the Floyd Warshall algorithm with a flag to indicate the intent to use recursion.

        :param graph: A list to represent the graph.
        :param use_recursion: Flag to indicate the use of recursion.
        :raises InvalidArgumentTypeError: If the input graph is not valid (type List[List[int]]).
        """
        if is_valid_matrix_graph(graph):
            return FloydWarshallAlgorithm.__recursive(graph) \
                if use_recursion else FloydWarshallAlgorithm.__iterative(graph)

        else:
            raise InvalidArgumentTypeError("Graph must be a List[List[int]].")
