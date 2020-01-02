from intcode_computer import Program, Computer


if __name__ == '__main__':

    # Read input
    with open('inputs/input_day05.in') as file:
        source_code = file.readline()

    # Part 1
    program = Program(source_code)
    Computer(program).run(diagnostic_id=1)

    # Part 2
    program = Program(source_code)
    Computer(program).run(diagnostic_id=5)
