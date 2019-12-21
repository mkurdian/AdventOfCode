import unittest
from functools import reduce
from abc import ABC, abstractmethod
from io import StringIO
from unittest.mock import patch


class Program:
    """
    A computer program
    """
    def __init__(self, source_code):
        self._program = list(map(int, source_code.split(',')))
        self._instruction_pointer = 0

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
        self._instruction_pointer = instruction.execute(self, input)

    def update_program(self, intruction_pointer, value):
        self._program[intruction_pointer] = value

    def __iter__(self):
        return ProgramIterator(self)

    def __str__(self):
        return ",".join(map(str, self._program))

    @property
    def instruction_pointer(self):
        return self._instruction_pointer

    @property
    def current_value(self):
        return self._program[self._instruction_pointer]


class ProgramIterator:
    """
    An iterator to be only used by the Program class
    """
    def __init__(self, program):
        self.program = program

    def __iter__(self):
        return self

    def __next__(self):
        opcode = int(str(self.program.current_value)[-2:])

        if opcode == 99:
            raise StopIteration()

        args = {
            'program': self.program
        }

        if opcode == 1:
            return Instruction1(args)
        elif opcode == 2:
            return Instruction2(args)
        elif opcode == 3:
            return Instruction3(args)
        elif opcode == 4:
            return Instruction4(args)
        elif opcode == 5:
            return Instruction5(args)
        elif opcode == 6:
            return Instruction6(args)
        elif opcode == 7:
            return Instruction7(args)
        elif opcode == 8:
            return Instruction8(args)
        else:
            raise ValueError("Unrecognised opcode")


class Instruction(ABC):

    def __init__(self, args):
        self.program = args.get('program', None)

    @abstractmethod
    def execute(self, input=None):
        pass

    @property
    def instruction_pointer(self):
        return self.program.instruction_pointer

    def value(self, start, stop=None):
        if stop:
            return self.program._program[start:stop]
        return self.program._program[start]

    def set_instruction_pointer(self, value):
        self.program._instruction_pointer = value

    def update_program(self, instruction_pointer, value):
        self.program.update_program(instruction_pointer, value)


class Instruction1(Instruction):

    def execute(self, program, input=None):
        instruction_size = 4
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))

        params = parameters[:-1]
        output = parameters[-1]
        values = []
        for index, value in enumerate(params):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")

        self.update_program(output, reduce(lambda a, b: a + b, values))
        return self.instruction_pointer + instruction_size


class Instruction2(Instruction):

    def execute(self, program, input=None):
        instruction_size = 4
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))

        params = parameters[:-1]
        output = parameters[-1]
        values = []
        for index, value in enumerate(params):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")

        self.update_program(output, reduce(lambda a, b: a * b, values))
        return self.instruction_pointer + instruction_size


class Instruction3(Instruction):

    def execute(self, program, input=None):
        instruction_size = 2
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        output = parameters[-1]
        self.update_program(output, input)
        return self.instruction_pointer + instruction_size


class Instruction4(Instruction):

    def execute(self, program, input=None):
        instruction_size = 2
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        output = parameters[-1]
        print("Diagnostic code: ", self.value(output))
        return self.instruction_pointer + instruction_size


class Instruction5(Instruction):

    def execute(self, program, input=None):
        instruction_size = 3
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))
        values = []
        for index, value in enumerate(parameters):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")
        param_1 = values[0]
        param_2 = values[1]
        if param_1 != 0:
            return param_2
        return self.instruction_pointer + instruction_size


class Instruction6(Instruction):

    def execute(self, program, input=None):
        instruction_size = 3
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))
        values = []
        for index, value in enumerate(parameters):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")
        param_1 = values[0]
        param_2 = values[1]
        if param_1 == 0:
            return param_2
        return self.instruction_pointer + instruction_size


class Instruction7(Instruction):

    def execute(self, program, input=None):
        instruction_size = 4
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))
        values = []
        for index, value in enumerate(parameters):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")

        param_1 = values[0]
        param_2 = values[1]
        param_3 = parameters[-1]

        if param_1 < param_2:
            self.update_program(param_3, 1)
        else:
            self.update_program(param_3, 0)

        return self.instruction_pointer + instruction_size


class Instruction8(Instruction):

    def execute(self, program, input=None):
        instruction_size = 4
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        modes = get_modes(self.value(self.instruction_pointer))
        values = []
        for index, value in enumerate(parameters):
            if modes[index] == 0:
                values.append(self.value(value))
            elif modes[index] == 1:
                values.append(value)
            else:
                raise ValueError("Unrecognised mode")

        param_1 = values[0]
        param_2 = values[1]
        param_3 = parameters[-1]

        if param_1 == param_2:
            self.update_program(param_3, 1)
        else:
            self.update_program(param_3, 0)

        return self.instruction_pointer + instruction_size


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

    def test_7_and_8(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,9,8,9,10,9,4,9,99,-1,8")
            Computer(program).run(diagnostic_id=8)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  1\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,9,8,9,10,9,4,9,99,-1,8")
            Computer(program).run(diagnostic_id=3)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  0\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,9,7,9,10,9,4,9,99,-1,8")
            Computer(program).run(diagnostic_id=3)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  1\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,9,7,9,10,9,4,9,99,-1,8")
            Computer(program).run(diagnostic_id=9)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  0\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,3,1108,-1,8,3,4,3,99")
            Computer(program).run(diagnostic_id=8)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  1\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,3,1108,-1,8,3,4,3,99")
            Computer(program).run(diagnostic_id=9)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  0\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,3,1107,-1,8,3,4,3,99")
            Computer(program).run(diagnostic_id=3)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  1\n")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,3,1107,-1,8,3,4,3,99")
            Computer(program).run(diagnostic_id=9)
            self.assertEqual(mock_stdout.getvalue(), "Diagnostic code:  0\n")

    def test_jump(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
            Computer(program).run(diagnostic_id=0)
            self.assertEqual("Diagnostic code:  0\n", mock_stdout.getvalue())

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
            Computer(program).run(diagnostic_id=4)
            self.assertEqual("Diagnostic code:  1\n", mock_stdout.getvalue())

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            program = Program("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
            Computer(program).run(diagnostic_id=0)
            self.assertEqual("Diagnostic code:  0\n", mock_stdout.getvalue())


if __name__ == '__main__':

    # Read input
    with open('inputs/input_day05.in') as file:
        source_code = file.readline()

    program = Program(source_code)
    Computer(program).run(diagnostic_id=1)

    program = Program(source_code)
    Computer(program).run(diagnostic_id=5)
