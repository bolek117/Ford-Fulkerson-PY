__author__ = 'bolek_000'


class Edge:
    """
    :type start_node: int
    :type end_node: int
    :type distance: int
    :type is_available: bool
    """

    def __init__(self, start_node, end_node, distance=1):
        """
        :param start_node : int
        :param end_node : int
        :param distance : int
        """
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance
        self.is_available = True

    def __eq__(self, other):
        return isinstance(other, Edge) and other.start_node == self.start_node and other.end_node == self.end_node

    def __ne__(self, other):
        return not isinstance(other, Edge) or other.start_node != self.start_node or other.end_node != self.end_node


# class Node:
#     """
#     :type id: int
#     :type is_visited: bool
#     """
#
#     def __init__(self, identifier, is_visited=False):
#         """
#
#         :param id: int
#         :return:
#         """
#         self.id = identifier
#         self.is_visited = is_visited