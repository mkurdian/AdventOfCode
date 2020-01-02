import unittest
from day06 import Graph, BreadthFirstSearchOrbits


class TestDay06(unittest.TestCase):

    def test_total_orbits(self):

        input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

        graph = Graph.graph_from_input_stream(input)

        self.assertEqual(11, graph.num_edges())
        self.assertEqual(12, graph.num_nodes())
        self.assertEqual(['C', 'G'], graph.adj('B'))

        bfs = BreadthFirstSearchOrbits(graph, 'COM')
        self.assertEqual(42, bfs.total_orbits())

    def test_orbital_transfer(self):

        input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

        graph = Graph.graph_from_input_stream(input)
        bfs = BreadthFirstSearchOrbits(graph, 'COM')
        self.assertEqual(4, bfs.orbital_transfers('K', 'I'))
