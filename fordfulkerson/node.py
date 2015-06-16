__author__ = 'bolek_000'


class EdgesList:
    """
    :type edges : list[Edge]
    """
    edges = []

    def __init__(self):
        pass

    def add_edge(self, start, end, distance):
        if not self.node_exists(start, end):
            self.edges.append(Edge(start, end, distance))

    def node_exists(self, start, end):
        for e in self.edges:
            if e.is_equal(start, end):
                return True

        return False

    def get(self, i):
        return self.edges[i]

    def get_children(self, node):
        """

        :param node: Node
        :return: list[Node]
        """
        result = []
        for e in self.edges:
            if e.startNode is node:
                result.append(e)

        return result

    def get_parents(self, node):
        """

        :param node: Node
        :return: list[Node]
        """
        result = []
        for e in self.edges:
            if e.endNode is node:
                result.append(e)

        return result


class Edge:
    """
    :type start_node: Node
    :type end_node: Node
    :type id: int
    :type distance: int
    """

    # Static
    idI = 0

    def __init__(self, start_node, end_node, distance):
        """

        :param start_node: Node
        :param end_node: Node
        :param distance: int
        :return:
        """
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance

        self.id = self.idI
        self.idI += 1

    def is_equal(self, start, end):
        return start == self.start_node and end == self.end_node


class Node:
    nId = 0

    def __init__(self, nId):
        """
        Construct new graph node
        :param nId: int
        :return:
        """
        self.nId = nId