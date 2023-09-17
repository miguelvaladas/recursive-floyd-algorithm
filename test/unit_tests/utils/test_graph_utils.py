import unittest

from src.utils.graph_utils import is_valid_matrix_graph


class Test(unittest.TestCase):

    def test_is_valid_matrix_graph_returns_true(self):
        graph = [
            [1, 3],
            [4, 3]
        ]

        result = is_valid_matrix_graph(graph)

        self.assertTrue(result)

    def test_is_valid_matrix_graph_returns_false(self):
        graph = [
            [1, 3],
            [4, "abc"]
        ]

        result = is_valid_matrix_graph(graph)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
