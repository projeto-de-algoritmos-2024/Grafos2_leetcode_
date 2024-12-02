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

    def dfs(self, node, target, visited, path):
        if node == target:
            return path
        visited.add(node)
        for neighbor, _ in self.graph[node]:
            if neighbor not in visited:
                new_path = self.dfs(neighbor, target, visited, path + [neighbor])
                if new_path:
                    return new_path
        return []

    def shortestPath(self, node1, node2):
        return self.dfs(node1, node2, set(), [node1])
