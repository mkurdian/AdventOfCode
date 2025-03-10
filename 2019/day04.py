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


def repeated_digit_counts(digits):
    """
    List of counts of repeated digit sequences.
    """
    result = []

    i, j = 0, 0
    while i < len(digits):
        while j < len(digits) and digits[j] == digits[i]:
            j += 1
        result.append(j-i)
        i = j
    return result


def two_adjacent_digits_same_2(number):
    """
    Determine if there are two adjacent matching digits
    and that they are not part of a larger group of matching digits
    """
    digits = separate_digits(number)
    digit_counts = repeated_digit_counts(digits)
    return any(map(lambda x: x==2, digit_counts))


if __name__ == '__main__':
    input_data = '246540-787419'
    start, end = map(int, input_data.split('-'))

    count = 0
    for password in range(start, end + 1):
        if two_adjacent_digits_same(password) and never_decrease(password):
          count += 1
    print("Part 01: ", count)

    count = 0
    for password in range(start, end + 1):
        if two_adjacent_digits_same_2(password) and never_decrease(password):
          count += 1
    print("Part 02: ", count)
