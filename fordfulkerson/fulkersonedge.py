__author__ = 'mwitas'

from graph import Edge


class FulkersonEdge(Edge):
    """
    :type residual_flow: int
    :type augmenting_flow: int
    """

    def __init__(self, start_node, end_node, distance=0, augmenting_flow=-1, residual_flow=0):
        Edge.__init__(self, start_node, end_node)

        self.residual_flow = residual_flow
        self.distance = distance
        if augmenting_flow >= 0:
            self.augmenting_flow = augmenting_flow
        else:
            self.augmenting_flow = distance


# class Worker:
#     """
#     :type edges :
#     """
#     def __init__(self, edges):
#         self.edges = edges
#         pass