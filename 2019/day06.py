import unittest
import queue


class BreadthFirstSearchOrbits:
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._distance = {}
        self._marked = {}

        self._run_bfs(graph, source)

    def _run_bfs(self, graph, source):

        q = queue.Queue()
        self._distance[source] = 0
        self._marked[source] = True
        q.put(source)
        while not q.empty():
            node = q.get()
            for adj in graph.adj(node):
                if adj not in self._marked:
                    self._distance[adj] = self._distance[node] + 1
                    q.put(adj)

    def total_orbits(self):
        total = 0
        for node in self._graph:
            total += self._distance.get(node, 0)
        return total


class Graph:

    @staticmethod
    def graph_from_input_stream(instream):
        graph = Graph()
        for row in instream:
            source, target = row.strip().split(")")
            graph.add_edge(source, target)
        return graph

    def __init__(self):
        self._nodes = set()
        self._adj = {}  # dict of sets
        self._E = 0  # number of edges

    def add_edge(self, source, target):
        if source in self._adj:
            self._adj[source].append(target)
        else:
            self._adj[source] = [target]

        self._nodes.add(source)
        self._nodes.add(target)
        self._E += 1

    def num_edges(self):
        return self._E

    def num_nodes(self):
        return len(self._nodes)

    def adj(self, node):
        return self._adj.get(node, [])

    def __iter__(self):
        for node in self._nodes:
            yield node


class TestDay06(unittest.TestCase):

    def test_total_orbits(self):

        input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

        graph = Graph.graph_from_input_stream(input)

        self.assertEqual(11, graph.num_edges())
        self.assertEqual(12, graph.num_nodes())
        self.assertEqual(['C', 'G'], graph.adj('B'))

        bfs = BreadthFirstSearchOrbits(graph, 'COM')
        self.assertEqual(42, bfs.total_orbits())


if __name__ == '__main__':
    with open('inputs/input_day06.in') as file:
        graph = Graph.graph_from_input_stream(file)
        part_1_result = BreadthFirstSearchOrbits(graph, 'COM').total_orbits()
        print("Part 1: ", part_1_result)
