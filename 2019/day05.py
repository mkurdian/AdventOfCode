import unittest
from functools import reduce


class Program:
    """
    A computer program
    """
    def __init__(self, source_code):
        self._program = list(map(int, source_code.split(',')))
        self._instruction_size = {1: 4, 2: 4, 3: 2, 4: 2}

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

    def execute(self, instruction, input=None):
        """
        Executes a given instruction according to the
        value of the opcode.
        """
        opcode = instruction['opcode']
        output = instruction['output']
        modes = instruction['modes']

        values = []
        for index, value in enumerate(instruction['inputs']):
            if modes[index] == 0:
                values.append(self._program[value])
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")

        if opcode == 1:
            self._program[output] = reduce(lambda a, b: a + b, values)
        elif opcode == 2:
            self._program[output] = reduce(lambda a, b: a * b, values)
        elif opcode == 3:
            self._program[output] = input
        elif opcode == 4:
            print("Diagnostic code: ", self._program[output])
        else:
            raise Exception("Unrecognised opcode.")

    def __iter__(self):
        return ProgramIterator(self._program, self._instruction_size)

    def __str__(self):
        return ",".join(map(str, self._program))


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
        opcode = int(str(self.program[self.index])[-2:])

        if opcode == 99:
            raise StopIteration()

        instruction_size = self.instruction_size[opcode]
        
        inputs = self.program[self.index + 1: self.index + instruction_size - 1]
        output = self.program[self.index + instruction_size - 1]
        modes = get_modes(self.program[self.index])

        self.index += instruction_size

        return {
            "opcode": opcode,
            "inputs": inputs,
            "output": output,
            "modes": modes
        }


class Computer:
    """
    A computer to execute the program.
    """
    def __init__(self, program):
        self._program = program

    def run(self, diagnostic_id = None):
        for instruction in self._program:
            self._program.execute(instruction, diagnostic_id)
        return self._program.result()


def get_modes(code):
    """
    Get the mode codes as list from the given code.
    """
    mode_code = code // 100  # remove opcode
    result = [0, 0, 0]

    if mode_code < 10:
        result[0] = mode_code
        return result
    elif mode_code < 100:
        digits = split_digits(mode_code)[::-1]
        result[0] = digits[0]
        result[1] = digits[1]
        return result
    elif mode_code < 1000:
        return split_digits(mode_code)[::-1]


def split_digits(number):
    """
    Split the digits of the number into a list of integers.
    """
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    return digits[::-1]


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

    def test_day05_solution(self):
        program = Program('3,0,4,0,99')
        self.assertEqual(Computer(program).run(diagnostic_id=123), 123)

        program = Program('1002,4,3,4,33')
        instruction = next(iter(program))
        program.execute(instruction)
        self.assertEqual(str(program), '1002,4,3,4,99')

    def test_get_modes(self):
        self.assertEqual(get_modes(3), [0, 0, 0])

        self.assertEqual(get_modes(103), [1, 0, 0])

        self.assertEqual(get_modes(1103), [1, 1, 0])

        self.assertEqual(get_modes(11103), [1, 1, 1])

        self.assertEqual(get_modes(10103), [1, 0, 1])

        self.assertEqual(get_modes(11003), [0, 1, 1])

        self.assertEqual(get_modes(1002), [0, 1, 0])


if __name__ == '__main__':

    # Read input
    with open('inputs/input_day05.in') as file:
        source_code = file.readline()

    program = Program(source_code)
    Computer(program).run(diagnostic_id=1)
