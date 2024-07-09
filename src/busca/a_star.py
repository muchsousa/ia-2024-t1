"""Implementação do algoritmo A*."""

import sys

def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""

    count_visited = 1
    total_length = 0.0
    path = []


    length = len(graph)

    distances = {}
    visited = {}
    for v in graph.get_vertices():
        visited[v] = 0
        distances[v] = sys.maxsize

    distances[start] = 0

    for _ in range(length - 1):
        min_dist = sys.maxsize
        u = None
        for i in range(length - 1):
            if (visited[i] == 0 and distances[i] <= min_dist):
                min_dist = distances[i]
                u = i

        if u is None:
            break

        visited[u] = 1  # visited
        count_visited = count_visited + 1

        for v in range(length - 1):
            if graph.adj[u][v] != 0 and visited[v] == 0:

                alt = distances[u] + graph.adj[u][v]
                if alt < distances[v]:
                    distances[v] = alt

                    count_visited = count_visited + 1
                    path.append(v)

                if (v == goal):
                    return (count_visited, total_length, path)

    return (0, 0.0, [])