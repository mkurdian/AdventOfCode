import unittest
from io import StringIO
from unittest.mock import patch
from .computer import Computer
from .program import Program
from .instruction import get_modes


class Test(unittest.TestCase):

    def test_day02_solution(self):
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

