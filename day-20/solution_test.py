import unittest
from unittest import TestCase

import solution

test_string = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"), minimal_saves=2, cheat_time=2)

        self.assertEqual(
            44,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), minimal_saves=50, cheat_time=20)

        self.assertEqual(
            285,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
