class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = {}
        for i in range(n):
            self.graph[i] = []
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]):
        u, v, w = edge
        self.graph[u].append((v, w))

    def getGraph(self):
        return self.graph
