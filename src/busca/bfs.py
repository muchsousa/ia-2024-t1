"""Implementação da busca em profundidade."""

from collections import deque

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def purge(self):
        self.items = [] 

    def __str__(self):
        return '({})'.format(self.items)


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    count_visited = 0
    total_length = 0.0
    path = []

    queue = Queue()
    queue.enqueue(start)

    visited = {}
    for vertice in graph.getVertices():
        visited[vertice] = 0

    while not queue.is_empty():
        u = queue.dequeue()

        count_visited = count_visited + 1
        total_length = total_length # add cost here
        path.append(u)

        if (u == goal):
            return (count_visited, total_length, path)

        neighbors = graph.getNeighbors(u)

        for neighbor in neighbors.keys():
            if (visited[neighbor] == 0):
                visited[neighbor] = 1 # visited
                queue.enqueue(neighbor)

    return None


