import unittest
from unittest.mock import patch

from src.exceptions import InvalidArgumentTypeError
from src.floyd_warshall_algorithm import FloydWarshallAlgorithm
from src.utils.constants import NO_PATH


class Test(unittest.TestCase):
    """
    FIRST_GRAPH example:
                       10
                  (0)------->(3)
                   |         /|\
                 5 |          |
                   |          | 1
                  \|/         |
                 (1)------->(2)
                       3           """
    FIRST_GRAPH = [
        [0, 5, NO_PATH, 10],
        [NO_PATH, 0, 3, NO_PATH],
        [NO_PATH, NO_PATH, 0, 1],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]
    FIRST_GRAPH_EXPECTED_RESULT = [
        [0, 5, 8, 9],
        [NO_PATH, 0, 3, 4],
        [NO_PATH, NO_PATH, 0, 1],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

    SECOND_GRAPH = [
        [0, 4, NO_PATH, 7, NO_PATH],
        [NO_PATH, 0, 6, 8, NO_PATH],
        [NO_PATH, NO_PATH, 0, NO_PATH, 2],
        [NO_PATH, 4, 7, 0, NO_PATH],
        [3, NO_PATH, NO_PATH, NO_PATH, 0]
    ]

    SECOND_GRAPH_EXPECTED_RESULT = [
        [0, 4, 10, 7, 12],
        [11, 0, 6, 8, 8],
        [5, 9, 0, 12, 2],
        [12, 4, 7, 0, 9],
        [3, 7, 13, 10, 0]
    ]

    THIRD_GRAPH = [
        [0, 1, 3, NO_PATH, NO_PATH, 8],
        [NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH, 6],
        [NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 5],
        [NO_PATH, NO_PATH, 10, 1, 0, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 2, 0]
    ]

    THIRD_GRAPH_EXPECTED_RESULT = [
        [0, 1, 3, 10, 9, 7],
        [NO_PATH, 0, 18, 9, 8, 6],
        [NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, 17, 0, 7, 5],
        [NO_PATH, NO_PATH, 10, 1, 0, 6],
        [NO_PATH, NO_PATH, 12, 3, 2, 0]
    ]

    FOURTH_GRAPH = [
        [0, NO_PATH, 64, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 13, NO_PATH],
        [NO_PATH, 0, 38, NO_PATH, NO_PATH, NO_PATH, 46, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, 0, 97, NO_PATH, NO_PATH, 37, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, 0, 30, 28, 16, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 51, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 33, 31, 49, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 4],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 77, NO_PATH, 0, 14],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 39, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]
    ]

    FOURTH_GRAPH_EXPECTED_RESULT = [
        [0, NO_PATH, 64, 161, 66, 189, 90, 220, 13, 27],
        [NO_PATH, 0, 38, 135, 165, 163, 46, 194, 212, 198],
        [NO_PATH, NO_PATH, 0, 97, 127, 125, 37, 156, 174, 160],
        [NO_PATH, NO_PATH, NO_PATH, 0, 30, 28, 16, 59, 77, 63],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, 51, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 74, 0, 33, 31, 49, 35],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 43, NO_PATH, 94, 0, NO_PATH, 4],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 53, NO_PATH, 77, NO_PATH, 0, 14],
        [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 39, NO_PATH, 90, NO_PATH, NO_PATH, 0]
    ]

    FIFTH_GRAPH = [
        [0, -1, NO_PATH, -2],
        [NO_PATH, 0, 6, NO_PATH],
        [NO_PATH, NO_PATH, 0, NO_PATH],
        [NO_PATH, -3, 7, 0]
    ]

    FIFTH_GRAPH_EXPECTED_RESULT = [
        [0, -5, 1, -2],
        [NO_PATH, 0, 6, NO_PATH],
        [NO_PATH, NO_PATH, 0, NO_PATH],
        [NO_PATH, -3, 3, 0]
    ]

    def test_execute_throws_InvalidArgumentTypeError(self):
        graph = "abc"

        self.assertRaises(InvalidArgumentTypeError, FloydWarshallAlgorithm.execute, graph)

    @patch('src.floyd_warshall_algorithm.FloydWarshallAlgorithm._FloydWarshallAlgorithm__recursive')
    def test_execute_calls_recursive(self, mock_recursive):
        graph = [
            [1, 3],
            [4, 3]
        ]

        FloydWarshallAlgorithm.execute(graph, use_recursion=True)

        mock_recursive.assert_called_once()

    @patch('src.floyd_warshall_algorithm.FloydWarshallAlgorithm._FloydWarshallAlgorithm__iterative')
    def test_execute_calls_iterative(self, mock_iterative):
        graph = [
            [1, 3],
            [4, 3]
        ]

        FloydWarshallAlgorithm.execute(graph)

        mock_iterative.assert_called_once()

    def test_recursive_returns_expected_result_on_4_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.FIRST_GRAPH, use_recursion=True)

        self.assertEqual(self.FIRST_GRAPH_EXPECTED_RESULT, result)

    def test_iterative_returns_expected_result_on_4_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.FIRST_GRAPH)

        self.assertEqual(self.FIRST_GRAPH_EXPECTED_RESULT, result)

    def test_recursive_returns_expected_result_on_5_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.SECOND_GRAPH, use_recursion=True)

        self.assertEqual(self.SECOND_GRAPH_EXPECTED_RESULT, result)

    def test_iterative_returns_expected_result_on_5_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.SECOND_GRAPH)

        self.assertEqual(self.SECOND_GRAPH_EXPECTED_RESULT, result)

    def test_recursive_returns_expected_result_on_6_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.THIRD_GRAPH, use_recursion=True)

        self.assertEqual(self.THIRD_GRAPH_EXPECTED_RESULT, result)

    def test_iterative_returns_expected_result_on_6_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.THIRD_GRAPH)

        self.assertEqual(self.THIRD_GRAPH_EXPECTED_RESULT, result)

    def test_recursive_returns_expected_result_on_12_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.FOURTH_GRAPH, use_recursion=True)

        self.assertEqual(self.FOURTH_GRAPH_EXPECTED_RESULT, result)

    def test_iterative_returns_expected_result_on_12_vertices_matrix(self):
        result = FloydWarshallAlgorithm.execute(self.FOURTH_GRAPH)

        self.assertEqual(self.FOURTH_GRAPH_EXPECTED_RESULT, result)

    def test_iterative_returns_expected_result_on_negative_numbers_graph(self):
        result = FloydWarshallAlgorithm.execute(self.FIFTH_GRAPH)

        self.assertEqual(self.FIFTH_GRAPH_EXPECTED_RESULT, result)

    def test_recursive_returns_expected_result_on_negative_numbers_graph(self):
        result = FloydWarshallAlgorithm.execute(self.FIFTH_GRAPH, use_recursion=True)

        self.assertEqual(self.FIFTH_GRAPH_EXPECTED_RESULT, result)


if __name__ == '__main__':
    unittest.main()
