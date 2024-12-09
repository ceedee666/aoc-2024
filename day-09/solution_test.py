import unittest
from unittest import TestCase

import solution

test_string = """2333133121414131402"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve_part_1(test_string)

        self.assertEqual(
            1928,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve_part_2(test_string)

        self.assertEqual(
            2858,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
