import unittest
from unittest import TestCase

import day_02

test_string = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


class Testing(TestCase):
    def test_part_1(self):
        r = day_02.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            2,
            r,
            "The result should be correct.",
        )

    def test_part_2(self):
        r = day_02.solve_part_2(test_string.split("\n"))

        self.assertEqual(
            4,
            r,
            "The result should be correct.",
        )


if __name__ == "__main__":
    unittest.main()
