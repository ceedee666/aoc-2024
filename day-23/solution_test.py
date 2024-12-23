import unittest
from unittest import TestCase

import solution

test_string = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


class Testing(TestCase):
    def test_part_1(self):
        r = solution.solve_1(test_string.split("\n"))

        self.assertEqual(
            7,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = solution.solve_2(test_string.split("\n"))

        self.assertEqual(
            "co,de,ka,ta",
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
