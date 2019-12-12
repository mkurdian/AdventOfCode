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

    def execute(self, instruction, input = None):
        """
        Executes a given instruction according to the
        value of the optcode.
        """
        optcode = instruction['optcode']
        output = instruction['output']
        
        values = list(map(self._program.__getitem__, instruction['inputs']))

        if optcode == 1:
            self._program[output] = reduce(lambda a, b: a + b, values)
        elif optcode == 2:
            self._program[output] = reduce(lambda a, b: a * b, values)
        elif optcode == 3:
            self._program[output] = input
        elif optcode == 4:
            print(self._program[output])
        else:
            raise Exception("Unrecognised optcode.")

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
        optcode = int(str(self.program[self.index])[-2:])

        if optcode == 99:
            raise StopIteration()

        instruction_size = self.instruction_size[optcode]
        
        inputs = self.program[self.index + 1 : self.index + instruction_size - 1]
        output = self.program[self.index + instruction_size - 1]

        self.index += instruction_size

        return {
            "optcode": optcode,
            "inputs": inputs,
            "output": output
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


if __name__ == '__main__':

    # Read input
    with open('inputs/input_day05.in') as file:
        source_code = file.readline()
