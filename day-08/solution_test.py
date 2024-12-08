import unittest
from unittest import TestCase

import solution

test_string = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            9,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), True)

        self.assertEqual(
            34,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
