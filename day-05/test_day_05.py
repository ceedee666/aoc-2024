import unittest
from unittest import TestCase

import day_05

test_string = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


class Testing(TestCase):
    def test_part_1(self):
        r = day_05.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            142,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
