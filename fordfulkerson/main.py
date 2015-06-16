from adjacencylist import AdjacencyList
from fulkersonedge import FulkersonEdge
from breadthfirstsearch import *

__author__ = 'bolek_000'


def define_edges():
    edges = AdjacencyList()

    data = [[0, 1, 10],
            [0, 2, 7],
            [1, 3, 8],
            [1, 4, 4],
            [2, 4, 8],
            [2, 5, 7],
            [3, 4, 7],
            [3, 6, 2],
            [4, 6, 8],
            [4, 8, 1],
            [5, 4, 2],
            [5, 8, 3],
            [6, 7, 2],
            [6, 9, 1],
            [7, 9, 9],
            [7, 10, 1],
            [8, 7, 3],
            [8, 10, 7],
            [9, 11, 4],
            [9, 12, 10],
            [10, 12, 1],
            [10, 13, 5],
            [11, 14, 4],
            [12, 11, 1],
            [12, 14, 8],
            [12, 13, 5],
            [13, 14, 5]]

    for e in data:
        edges.add_edge(e)

    return edges


def main():
    adj_list = define_edges()
    # worker = Worker(adj_list)

    max_flow = 0

    """
    :var path : list[int]
    """
    # adj_list.hide_edge(Edge(0, 1))
    # adj_list.hide_edge(Edge(0,2))

    iteration = 0
    while True:
        path = bfs_paths(adj_list.get_routes(), 0, adj_list.last_node)

        # Augmenting path not found
        if path is None:
            print('No augmenting paths found (iteration {})'.format(iteration))
            break

        """
        :type edges : list[FulkersonEdge]
        """
        edges = []

        # Get first edge from path
        edge = adj_list.get_edge_by_ids(path[0], path[1])

        # Save found edge for speedup
        edges.append(edge)

        # Define initial min_flow
        min_flow = edge.augmenting_flow

        # Save number of elements for speedup
        elements = len(path)-1

        # Find min flow on path
        for i in xrange(elements):
            node_start = path[i]
            node_end = path[i+1]

            edge = adj_list.get_edge_by_ids(node_start, node_end)
            edges.append(edge)

            flow = edge.augmenting_flow
            if flow < min_flow:
                min_flow = edge.augmenting_flow

        # Add actual min_flow to value of maximum flow
        max_flow += min_flow

        print('Path {} with flow {}, actual max flow is {}'.format(path, min_flow, max_flow))

        # subtract minimum flow from all residual flows
        for edge in edges:
            assert isinstance(edge, FulkersonEdge)
            edge.augmenting_flow -= min_flow
            edge.residual_flow += min_flow

            if edge.augmenting_flow <= 0:
                edge.is_available = False

        iteration += 1

    print('Found max flow: {}'.format(max_flow))


if __name__ == "__main__":
    main()
