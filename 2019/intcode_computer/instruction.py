from functools import reduce
from abc import ABC, abstractmethod


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


class InstructionFactory:
    @classmethod
    def instruction(cls, opcode, args):
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

    def execute(self, input=None):
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

    def execute(self, input=None):
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

    def execute(self, input=None):
        instruction_size = 2
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        output = parameters[-1]
        self.update_program(output, input)
        return self.instruction_pointer + instruction_size


class Instruction4(Instruction):

    def execute(self, input=None):
        instruction_size = 2
        parameters = self.value(self.instruction_pointer + 1, self.instruction_pointer + instruction_size)
        output = parameters[-1]
        print("Diagnostic code: ", self.value(output))
        return self.instruction_pointer + instruction_size


class Instruction5(Instruction):

    def execute(self, input=None):
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

    def execute(self, input=None):
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

    def execute(self, input=None):
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

    def execute(self, input=None):
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
