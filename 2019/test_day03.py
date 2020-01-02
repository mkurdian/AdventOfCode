import unittest
from day03 import Wire, Panel


class TestDay03(unittest.TestCase):

    def test_solution(self):
        wire_1 = Wire("R8,U5,L5,D3")
        wire_2 = Wire("U7,R6,D4,L4")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.distance(), 6)

        wire_1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        wire_2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.distance(), 159)

        wire_1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        wire_2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.distance(), 135)

    def test_solution_2(self):
        wire_1 = Wire("R8,U5,L5,D3")
        wire_2 = Wire("U7,R6,D4,L4")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.minimum_steps_to_crossing(), 30)

        wire_1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        wire_2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.minimum_steps_to_crossing(), 610)

        wire_1 = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        wire_2 = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        panel = Panel(wire_1, wire_2)
        self.assertEqual(panel.minimum_steps_to_crossing(), 410)
