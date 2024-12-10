import unittest
from unittest import TestCase

import solution

test_string = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            36,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), False)

        self.assertEqual(
            81,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
