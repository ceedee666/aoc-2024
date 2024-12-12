import unittest
from unittest import TestCase

import solution

test_string = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            1930,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), 2)

        self.assertEqual(
            1206,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
