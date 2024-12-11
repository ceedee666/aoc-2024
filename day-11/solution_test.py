import unittest
from unittest import TestCase

import solution

test_string = """125 17"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"), 6)

        self.assertEqual(
            22,
            r,
            "The result shoud be correct.",
        )

        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            55312,
            r,
            "The result shoud be correct.",
        )

    def test_part_1_wo_recursion(self):
        r = solution.solve(test_string.split("\n"), 6, False)

        self.assertEqual(
            22,
            r,
            "The result shoud be correct.",
        )

        r = solution.solve(data=test_string.split("\n"), recursive=False)

        self.assertEqual(
            55312,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
