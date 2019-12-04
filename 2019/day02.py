import unittest
from unittest.mock import Mock
from copy import copy

def process(func, program, index):
    index_a = program[index + 1] 
    index_b = program[index + 2] 
    result_index = program[index + 3] 
    result  = func(program[index_a], program[index_b])
    program[result_index] = result

def run_program(program):
    program_copy = copy(program)

    index = 0
    optcode = program_copy[index]

    while optcode != 99:
        if optcode == 1:
            # adds
            process(lambda a, b: a + b, program_copy, index)
        elif optcode == 2:
            # multiplies
            process(lambda a, b: a * b, program_copy, index)
        index += 4
        optcode = program_copy[index]

    return program_copy

def restore(program):
    program[1] = 12
    program[2] = 2


class TestDay02(unittest.TestCase):

    def test_run_program(self):
        self.assertEqual(run_program([99]), [99])
        self.assertEqual(run_program([1,0,0,0,99]), [2,0,0,0,99])
        self.assertEqual(run_program([2,3,0,3,99]), [2,3,0,6,99])
        self.assertEqual(run_program([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(run_program([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
        self.assertEqual(run_program([1,9,10,3,2,3,11,0,99,30,40,50]), [3500,9,10,70,2,3,11,0,99,30,40,50])

if __name__ == '__main__':
    with open('inputs/input_day02.in') as file:
        program = list(map(int, file.readline().split(',')))
        restore(program)
        print("Part 1: ", run_program(program)[0])