"""Implementação da busca em profundidade."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    

def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""

    count_visited = 0
    total_length = 0.0
    path = []

    stack = Stack()
    stack.push(start)

    visited = {}
    for vertice in graph.getVertices():
        visited[vertice] = 0

    visited[start] = 1 # visited

    while not stack.is_empty():
        u = stack.pop()

        total_length = total_length # add cost here
        path.append(u)

        if (u == goal):
            return (count_visited, total_length, path)
        
        count_visited = count_visited + 1

        neighbors = graph.getNeighbors(u)

        for neighbor in neighbors.keys():
            if (visited[neighbor] == 0):

                if (neighbor == goal):
                    total_length = total_length # add cost here
                    path.append(neighbor)

                    return (count_visited, total_length, path)

                visited[neighbor] = 1 # visited
                stack.push(neighbor)

    return None

