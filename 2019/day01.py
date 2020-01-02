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


def corrected_fuel_for_mass(mass):
    """
    Mass of fuel corrected for fuels own mass.
    """
    result = 0
    fuel = mass

    while fuel >= 0:
        fuel = fuel_for_mass(fuel)
        if fuel <= 0:
            fuel = 0
            break
        result += fuel

    return result


if __name__ == '__main__':
    with open('inputs/input_day01.in') as file:
        part_1_result = sum_func(fuel_for_mass, file)
        print("Part 1: ", part_1_result)

    with open('inputs/input_day01.in') as file:
        part_2_result = sum_func(corrected_fuel_for_mass, file)
        print("Part 2: ", part_2_result)
