import unittest
from unittest import TestCase

import solution

test_string = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


test_string_2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            7036,
            r,
            "The result shoud be correct.",
        )

        r = solution.solve(test_string_2.split("\n"))

        self.assertEqual(
            11048,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), 2)

        self.assertEqual(
            45,
            r,
            "The result shoud be correct.",
        )

        r = solution.solve(test_string_2.split("\n"), 2)

        self.assertEqual(
            64,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
