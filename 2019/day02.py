import unittest


class Program:
    """
    A computer program
    """
    def __init__(self, source_code):
        self._program = list(map(int, source_code.split(',')))

    def result(self):
        """
        Returns the result of the executed program
        which will be at position 0.
        """
        return self._program[0]

    def restore(self, noun, verb):
        """
        Restore the first two inputs to the given
        noun and verb.
        """
        self._program[1] = noun
        self._program[2] = verb

    def execute(self, instruction):
        """
        Executes a given instruction according to the
        value of the optcode.
        """
        value_1 = self._program[instruction["input_1"]]
        value_2 = self._program[instruction["input_2"]]

        if instruction["optcode"] == 1:
            self._program[instruction["output"]] = value_1 + value_2
        elif instruction["optcode"] == 2:
            self._program[instruction["output"]] = value_1 * value_2
        else:
            raise Exception("Unrecognised optcode.")

    def __iter__(self):
        return ProgramIterator(self._program, 4)


class ProgramIterator:
    """
    An iterator to be only used by the Program class
    """
    def __init__(self, program, instruction_size):
        self.program = program
        self.index = 0
        self.instruction_size = instruction_size

    def __iter__(self):
        return self

    def __next__(self):
        optcode = self.program[self.index]
        if optcode == 99:
            raise StopIteration()
        
        input_1 = self.program[self.index + 1]
        input_2 = self.program[self.index + 2]
        output = self.program[self.index + 3]

        self.index += self.instruction_size

        return {
            "optcode": optcode,
            "input_1": input_1,
            "input_2": input_2,
            "output": output
        }


class Computer:
    """
    A computer to execute the program.
    """
    def __init__(self, program):
        self._program = program

    def run(self):
        for instruction in self._program:
            self._program.execute(instruction)
        return self._program.result()


class TestDay02(unittest.TestCase):

    def test_solution(self):
        program = Program('99')
        self.assertEqual(Computer(program).run(), 99)

        program = Program('1,0,0,0,99')
        self.assertEqual(Computer(program).run(), 2)

        program = Program('1,1,1,4,99,5,6,0,99')
        self.assertEqual(Computer(program).run(), 30)

        program = Program('1,9,10,3,2,3,11,0,99,30,40,50')
        self.assertEqual(Computer(program).run(), 3500)


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