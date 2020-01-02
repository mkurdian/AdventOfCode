from intcode_computer import Program, Computer


if __name__ == '__main__':

    # Read input
    with open('inputs/input_day02.in') as file:
        source_code = file.readline()
    
    # Part 1: Restore and run program
    program = Program(source_code)
    program.restore(12, 2)
    print("Part1: ", Computer(program).run())

    # Part 2: Search for noun and verb that computes to 19690720
    for noun in range(100):
        for verb in range(100):
            program = Program(source_code)
            program.restore(noun, verb)
            if Computer(program).run() == 19690720:
                print("Part2: ", 100 * noun + verb)
                break
