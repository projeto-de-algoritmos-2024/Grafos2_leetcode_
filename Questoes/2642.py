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

    def bfs(self, node1, node2):
        visited = set()
        queue = [(node1, 0)]  
        while queue:
            current, dist = queue.pop(0)
            if current == node2:
                return dist
            visited.add(current)
            for neighbor, weight in self.graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + weight))
        return -1

    def shortestPath(self, node1, node2):
        return self.bfs(node1, node2)
