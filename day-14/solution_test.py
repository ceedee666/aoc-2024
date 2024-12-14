import unittest
from unittest import TestCase

import solution

test_string = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve(test_string.split("\n"), 7, 11)

        self.assertEqual(
            12,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
