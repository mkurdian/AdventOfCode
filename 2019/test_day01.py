import unittest
from day01 import fuel_for_mass, sum_func, corrected_fuel_for_mass


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

    def test_corrected_fuel_for_mass(self):
        self.assertEqual(corrected_fuel_for_mass(5), 0)
        self.assertEqual(corrected_fuel_for_mass(21), 5)
        self.assertEqual(corrected_fuel_for_mass(70), 21 + 5)
        self.assertEqual(corrected_fuel_for_mass(216), 70 + 21 + 5)
        self.assertEqual(corrected_fuel_for_mass(1969), 966)
        self.assertEqual(corrected_fuel_for_mass(100756), 50346)
