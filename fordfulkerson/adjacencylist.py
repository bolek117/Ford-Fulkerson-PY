__author__ = 'bolek_000'

from fulkersonedge import FulkersonEdge


class AdjacencyList:
    """
    Adjacency list class
    :type lst: list[FulkersonEdge]
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

    def add_edge(self, data_row):
        """

        :param data_row: list[int]
        """
        self.lst.append(FulkersonEdge(data_row[0], data_row[1], data_row[2]))
        self.edges_count += 1

        if data_row[0] not in self.known_nodes:
            self.known_nodes.append(data_row[0])
            self.nodes_count += 1

        self.last_node = data_row[1]

    def hide_edge(self, edge):
        """

        :param edge: FulkersonEdge
        """
        for e in self.lst:
            if e == edge:
                e.is_available = False
                return True

        return False

    def hide_edge_by_ids(self, start_node, end_node):
        """

        :param start_node: int
        :param end_node: int
        :return: bool
        """

        edge = self.get_edge_by_ids(start_node, end_node)
        if edge is not None:
            edge.is_available = False
            return True
        else:
            return False

    def get_edge_by_ids(self, start_node, end_node):
        """

        :param start_node: int
        :param end_node: int
        :return: FulkersonEdge
        """
        for e in self.lst:
            if e.start_node == start_node and e.end_node == end_node:
                return e

        return None

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

