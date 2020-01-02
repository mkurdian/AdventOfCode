import unittest
from day04 import two_adjacent_digits_same, never_decrease, two_adjacent_digits_same_2, repeated_digit_counts


class TestDay04(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(two_adjacent_digits_same(111111))
        self.assertFalse(two_adjacent_digits_same(123456))
        self.assertTrue(two_adjacent_digits_same(3241125))

        self.assertTrue(never_decrease(123456))
        self.assertFalse(never_decrease(654321))
        self.assertFalse(never_decrease(223450))

    def test_part02(self):
        self.assertTrue(two_adjacent_digits_same_2(112233))

    def test_group_repeated_digits(self):
        self.assertEqual(repeated_digit_counts([1]), [1])
        self.assertEqual(repeated_digit_counts([1, 1]), [2])
        self.assertEqual(repeated_digit_counts([1, 1, 1]), [3])
        self.assertEqual(repeated_digit_counts([1, 2, 2]), [1, 2])
        self.assertEqual(repeated_digit_counts([1, 2]), [1, 1])
        self.assertEqual(repeated_digit_counts([1, 2]), [1, 1])
        self.assertEqual(repeated_digit_counts([1, 2, 3]), [1, 1, 1])
        self.assertEqual(repeated_digit_counts([1, 2, 3, 3]), [1, 1, 2])
