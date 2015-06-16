__author__ = 'bolek_000'

from graph import Edge


class AdjacencyList:
    """
    Adjacency list class
    :type lst: list[Edge]
    :type known_nodes : list[int]
    :type nodes_count: int
    :type edges_count: int
    """

    known_nodes = []
    nodes_count = 0
    edges_count = 0
    last_node = 0

    def __init__(self):
        self.lst = []

    def get_neighbours(self, node, only_available=True):
        """

        :param node: int
        :return list[Edge]
        """
        result = []
        for edge in self.lst:
            is_start = edge.start_node == node
            if (is_start or edge.is_available) and (is_start or not only_available):
                result.append(edge)

        return result

    def add_edge(self, data_row):
        """

        :param data_row: list[int]
        """
        self.lst.append(Edge(data_row[0], data_row[1], data_row[2]))
        self.edges_count += 1

        if data_row[0] not in self.known_nodes:
            self.known_nodes.append(data_row[0])
            self.nodes_count += 1

        self.last_node = data_row[1]

    def hide_edge(self, edge):
        """

        :param edge: Edge
        """
        for e in self.lst:
            if e == edge:
                e.is_available = False
                return True

        return False

    def hide_edge_by_id(self, start_node, end_node):
        """

        :param start_node: int
        :param end_node: int
        :return: bool
        """

        for e in self.lst:
            if e.start_node == start_node and e.end_node == end_node:
                e.is_available = False
                return True

        return False

    def get_routes(self):
        """
        :var sets : list[list[int]]
        :var graph : Set[Set[int]]
        :return:
        """

        sets = [[] for i in range(self.nodes_count + 1)]

        for e in self.lst:
            if e.is_available:
                sets[e.end_node].append(e.start_node)
                sets[e.start_node].append(e.end_node)

        return sets

