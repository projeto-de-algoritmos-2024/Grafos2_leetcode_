import math

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

    def shortestPath(self, node1, node2):
        dist = {node: math.inf for node in self.graph}
        dist[node1] = 0
        visited = set()

        for _ in range(len(self.graph)):
            # Encontrar o nó com a menor distância
            u = min((node for node in self.graph if node not in visited), key=lambda node: dist[node], default=None)
            if u is None or dist[u] == math.inf:
                break
            visited.add(u)

            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        return dist[node2] if dist[node2] != math.inf else -1
