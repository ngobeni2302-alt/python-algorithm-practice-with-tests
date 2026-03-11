import unittest
import problems


class TestStreakProblems(unittest.TestCase):

# -------- WINNING STREAK STYLE TESTS --------

    def test_longest_heads_basic(self):
        self.assertEqual(problems.longest_heads(["H","T","H","H","H","T"]), 3)

    def test_longest_heads_all_heads(self):
        self.assertEqual(problems.longest_heads(["H","H","H","H"]), 4)

    def test_longest_heads_none(self):
        self.assertEqual(problems.longest_heads(["T","T","T"]), 0)

    def test_longest_heads_single(self):
        self.assertEqual(problems.longest_heads(["H"]), 1)

    def test_longest_heads_edge(self):
        self.assertEqual(problems.longest_heads(["T","H","H","T","H"]), 2)


    def test_longest_pass(self):
        self.assertEqual(problems.longest_pass(["P","P","F","P","P","P"]), 3)

    def test_longest_pass_fail_start(self):
        self.assertEqual(problems.longest_pass(["F","P","P"]), 2)

    def test_longest_pass_all_fail(self):
        self.assertEqual(problems.longest_pass(["F","F","F"]), 0)


    def test_longest_hot_days(self):
        self.assertEqual(
            problems.longest_hot_days(["H","H","N","H","H","H","N"]),
            3
        )

    def test_longest_hot_days_edge(self):
        self.assertEqual(
            problems.longest_hot_days(["N","H","N","H","H"]),
            2
        )


    def test_longest_positive(self):
        self.assertEqual(
            problems.longest_positive(["+","+","-","+","+","+"]),
            3
        )

    def test_longest_positive_all_gain(self):
        self.assertEqual(
            problems.longest_positive(["+","+","+","+"]),
            4
        )


    def test_longest_success(self):
        self.assertEqual(
            problems.longest_success(["S","S","F","S","S","S","F"]),
            3
        )

    def test_longest_success_none(self):
        self.assertEqual(
            problems.longest_success(["F","F","F"]),
            0
        )


if __name__ == "__main__":
    unittest.main()