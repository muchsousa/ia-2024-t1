"""Implementação de uma estrutura de grafo."""

import sys

class Graph:
    def __init__(self, isDirect=False):
        self.vertices = {}
        self.adj = {}
        self.isDirect = isDirect

    def addVertex(self, vertex, data=None):
        self.vertices[vertex] = data
        self.adj[vertex] = {}

    def addEdge(self, from_vertex, to_vertex, cost=0.0):
        if (self.adj[from_vertex] is None):
            self.adj[from_vertex] = {}

        self.adj[from_vertex][to_vertex] = cost

        if not self.isDirect:
            self.adj[to_vertex][from_vertex] = cost

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))
    
    def getVertices(self):
        return self.vertices

    def getNeighbors(self, v):
        return self.adj[v]

# ----------------------------------------------------------------

def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""

    graph = Graph()
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())
        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph.addVertex(int(index), [latitude, longitude])
            
        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )
            graph.addEdge(int(from_vertex), int(to_vertex), float(cost))
    
    return graph
