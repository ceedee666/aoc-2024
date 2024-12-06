import unittest
from unittest import TestCase

import day_06

test_string = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


class Testing(TestCase):
    def test_part_1(self):
        r = day_06.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            41,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = day_06.solve_part_2(test_string.split("\n"))
        self.assertEqual(
            6,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
