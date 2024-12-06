import unittest
from unittest import TestCase

import solution

test_string = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            18,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve_part_2(test_string.split("\n"))

        self.assertEqual(
            9,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
