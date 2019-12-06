import unittest

def two_adjacent_digits_same(number):
    """
    Returns true if number contains two adjacent digits
    that are the same.
    """
    digits = separate_digits(number)

    i = 0
    while i < len(digits) - 1:
        if digits[i] == digits[i+1]:
            return True
        i += 1
    return False

def separate_digits(number):
    """
    Separate the digits of the number and returns
    them as a list.
    """
    result = []
    while number != 0:
        result.append(number % 10)
        number = number // 10
    result.reverse()
    return result

def never_decrease(number):
    """
    Returns true if digits in the number are non-decreasing.
    """
    digits = separate_digits(number)

    i = 0
    while i < len(digits) - 1:
        if digits[i] > digits[i+1]:
            return False
        i += 1
    return True

class TestDay04(unittest.TestCase):
    
    def test_solution(self):
        self.assertTrue(two_adjacent_digits_same(111111))
        self.assertFalse(two_adjacent_digits_same(123456))
        self.assertTrue(two_adjacent_digits_same(3241125))

        self.assertTrue(never_decrease(123456))
        self.assertFalse(never_decrease(654321))
        self.assertFalse(never_decrease(223450))


if __name__ == '__main__':
    input = '246540-787419'
    start, end = map(int, input.split('-'))
    count = 0
    for password in range(start, end + 1):
        if two_adjacent_digits_same(password) and never_decrease(password):
          count += 1
    print("Part 01: ", count)