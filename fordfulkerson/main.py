from fordfulkerson.adjacencylist import *
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
            [6, 9, 9],
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
    edges = define_edges()
    path = bfs_paths(edges.get_routes(), 0, edges.last_node)
    pass



if __name__ == "__main__":
    main()
