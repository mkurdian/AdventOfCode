from .instruction import InstructionFactory


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
        self._instruction_pointer = instruction.execute(input)

    def update_program(self, intruction_pointer, value):
        """
        Update program at position given by instruction_pointer.
        """
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

        return InstructionFactory.instruction(opcode, args)

