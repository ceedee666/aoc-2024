import unittest
from unittest import TestCase

import day_01

test_string = """3   4
4   3
2   5
1   3
3   9
3   3"""


class Testing(TestCase):
    def test_part_1(self):
        r = day_01.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            11,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = day_01.solve_part_2(test_string.split("\n"))

        self.assertEqual(
            31,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
