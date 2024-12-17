import unittest
from unittest import TestCase

import solution

test_string = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


test_string_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            "4,6,3,5,6,3,5,2,1,0",
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string_2.split("\n"), 2)

        self.assertEqual(
            "117440",
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
