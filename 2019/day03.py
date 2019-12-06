import unittest

def manhatten(point_1, point_2 = (0,0)):
    """
    Returns the manhatten distance between two points
    that are represented as tuples.
    """
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

class Panel:
    """
    A panel
    """
    def __init__(self, wire_1, wire_2):
        self._wires = [wire_1, wire_2]

    def _find_crossings(self):
        """
        Returns the set intersection of the wire positions on the grid.
        """
        crossings = []
        wire_set = set(self._wires[0])
        for point in self._wires[1]:
            if point in wire_set:
                crossings.append(point)

        return crossings


    def distance(self):
        """
        Returns the manhatten distance to the intersection point
        that is closest to the central port.
        """
        return min(map(manhatten, self._find_crossings()))

class Wire:
    """
    Representation of a wire as a collection of points that it occupies
    on the panel grid.
    """
    def __init__(self, wire):
        self._x = 0
        self._y = 0
        self._points = []

        instructions = wire.split(',')
        for instruction in instructions:
            direction = instruction[0]
            moves = int(instruction[1:])

            if direction == 'U':
                self._add_points(moves, lambda: self._increment_y(1))
            elif direction == 'D':
                self._add_points(moves, lambda: self._increment_y(-1))
            elif direction == 'L':
                self._add_points(moves, lambda: self._increment_x(-1))
            elif direction == 'R':
                self._add_points(moves, lambda: self._increment_x(1))
            else:
                raise ValueError("Unrecognised direction code")

    def _add_points(self, moves, increment):
        for i in range(1, moves + 1):
            increment()
            self._points.append((self._x, self._y))

    def _increment_x(self, value):
        self._x += value

    def _increment_y(self, value):
        self._y += value

    def __iter__(self):
        for point in self._points:
            yield point    


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


if __name__ == '__main__':
    with open('inputs/input_day03.in') as file:
        lines = file.readlines()

    wire_1 = Wire(lines[0])
    wire_2 = Wire(lines[1])
    panel = Panel(wire_1, wire_2)
    print("Part 1: ", panel.distance())