import unittest
from unittest import TestCase

import solution

test_string = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            6,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), 2)

        self.assertEqual(
            16,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
