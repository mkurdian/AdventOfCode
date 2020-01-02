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
