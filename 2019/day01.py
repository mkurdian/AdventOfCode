import unittest


def fuel_for_mass(mass):
    """
    Mass of fuel for given mass.
    """
    return (mass // 3) - 2


def sum_func(func, stream):
    """
    Map stream with func and sum up the result.
    """
    return sum(map(func, map(int, stream)))


class TestDay01(unittest.TestCase):

    def test_fuel_for_mass(self):
        self.assertEqual(fuel_for_mass(12), 2)
        self.assertEqual(fuel_for_mass(14), 2)
        self.assertEqual(fuel_for_mass(1969), 654)
        self.assertEqual(fuel_for_mass(100756), 33583)

    def test_sum_func(self):
        module_masses = [12, 14, 1969, 100756]
        self.assertEqual(sum_func(fuel_for_mass, module_masses[:1]), 2)
        self.assertEqual(sum_func(fuel_for_mass, module_masses[:2]), 2 + 2)
        self.assertEqual(
            sum_func(fuel_for_mass, module_masses[:3]), 2 + 2 + 654)
        self.assertEqual(
            sum_func(fuel_for_mass, module_masses), 2 + 2 + 654 + 33583)

    def test_sum_func_string(self):
        module_masses = ['12', '14', '1969', '100756']
        self.assertEqual(
            sum_func(fuel_for_mass, module_masses), 2 + 2 + 654 + 33583)


if __name__ == '__main__':
    with open('inputs/input_day01.in') as file:
        part_1_result = sum_func(fuel_for_mass, file)
        print("Part 1: ", part_1_result)
