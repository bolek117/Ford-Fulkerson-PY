__author__ = 'mwitas'


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)

        for e in path:
            if e in graph[vertex]:
                graph[vertex].remove(e)

        for next_point in graph[vertex]:
            if next_point == goal:
                path.append(next_point)
                return path
            else:
                queue.append((next_point, path + [next_point]))

    return None