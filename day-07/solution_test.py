import unittest
from unittest import TestCase

import solution

test_string = """aaaa
bbbb
cccc
dddd"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            1,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
