import unittest
from unittest import TestCase

import solution

test_string = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            3749,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve(test_string.split("\n"), True)

        self.assertEqual(
            11387,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
