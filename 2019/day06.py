import queue


class BreadthFirstSearchOrbits:
    def __init__(self, graph, source):
        self._graph = graph
        self._source = source
        self._distance = {}
        self._marked = {}
        self._prev = {}

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
                    self._prev[adj] = node

    def _get_lowest_common_ancestor(self, start, end):
        path_to_start = self._get_path(start)
        path_to_end = self._get_path(end)
        for node in path_to_start:
            if node in path_to_end:
                return node
        return self._source

    def _get_path(self, node):
        n = node
        result = [n]
        while n != self._source:
            n = self._prev[n]
            result.append(n)
        return result

    def total_orbits(self):
        total = 0
        for node in self._graph:
            total += self._distance.get(node, 0)
        return total

    def orbital_transfers(self, start, end):
        common_ancestor = self._get_lowest_common_ancestor(start, end)
        return self._distance[start] + self._distance[end] - 2 * self._distance[common_ancestor]


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


if __name__ == '__main__':
    with open('inputs/input_day06.in') as file:
        graph = Graph.graph_from_input_stream(file)
        bfs = BreadthFirstSearchOrbits(graph, 'COM')

        part_1_result = bfs.total_orbits()
        print("Part 1: ", part_1_result)

        part_2_result = bfs.orbital_transfers('YOU', 'SAN') - 2  # Don't want to count hop from YOU and to SAN.
        print("Part 2: ", part_2_result)
