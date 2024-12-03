import unittest
from unittest import TestCase

import day_03

test_string = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


class Testing(TestCase):
    def test_part_1(self):
        r = day_03.solve_part_1(test_string)

        self.assertEqual(
            161,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = day_03.solve_part_2(test_string)

        self.assertEqual(
            48,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
