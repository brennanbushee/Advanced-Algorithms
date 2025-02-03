# test_weakest_strong_link.py

import unittest


def weakest_strong_link(strength):
    """
    Finds the weakest strong link in the matrix with optimized performance.

    A weakest strong link is:
    - The weakest (smallest) link in its row.
    - The strongest (largest) link in its column.

    Args:
        strength (List[List[int]]): A 2D matrix representing link strengths.

    Returns:
        int: The weakest strong link if it exists, otherwise -1.
    """
    rows = len(strength)
    cols = len(strength[0]) if rows > 0 else 0

    # Precompute the maximum values for each column
    col_max_values = [max(strength[row][col] for row in range(rows)) for col in range(cols)]

    for i in range(rows):
        # Find the minimum in the current row and its column index
        row_min_value = min(strength[i])
        col_index = strength[i].index(row_min_value)

        # Compare with precomputed column maximum
        if row_min_value == col_max_values[col_index]:
            return row_min_value

    return -1


class TestWeakestStrongLink(unittest.TestCase):

    def test_example_cases(self):
        self.assertEqual(weakest_strong_link([[1, 2, 3],
                                              [4, 5, 6],
                                              [7, 8, 9]]), 7)
        self.assertEqual(weakest_strong_link([[9, 8, 10], [6, 15, 4]]), -1)

    def test_single_element(self):
        self.assertEqual(weakest_strong_link([[5]]), 5)

    def test_rectangular_matrix(self):
        self.assertEqual(weakest_strong_link([[3, 1],
                                              [2, 4]]), 2)
        self.assertEqual(weakest_strong_link([[10, 20],
                                              [30, 5]]), -1)

    def test_no_weakest_strong_link(self):
        self.assertEqual(weakest_strong_link([[9, 8],
                                              [7, 6]]), -1)

    def test_large_matrix(self):
        self.assertEqual(weakest_strong_link([[1, 2, 3], [0, 5, 1], [4, 6, 7]]), 4)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(weakest_strong_link([[-1, -2], [-3, -4]]), -1)

    def test_equal_values(self):
        self.assertEqual(weakest_strong_link([[2, 2], [2, 2]]), 2)


if __name__ == '__main__':
    unittest.main()
