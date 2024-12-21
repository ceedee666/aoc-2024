import unittest
from unittest import TestCase

import solution

test_string = """029A
980A
179A
456A
379A"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"))

        self.assertEqual(
            126384,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
