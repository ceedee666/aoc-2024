import unittest
from unittest import TestCase

import solution

test_string = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(
            test_string.split("\n"), width=7, height=7, steps=12, end=6 + 1j * 6
        )

        self.assertEqual(
            22,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve_2(
            test_string.split("\n"), width=7, height=7, steps=12, end=6 + 1j * 6
        )

        self.assertEqual(
            (6, 1),
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
