import unittest
from unittest import TestCase

import solution

test_string = """1
10
100
2024"""

test_string_2 = """1
2
3
2024"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(["123"], steps=10)

        self.assertEqual(
            5908254,
            r,
            "The result shoud be correct.",
        )

        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            37327623,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string_2.split("\n"), part=2)

        self.assertEqual(
            23,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
