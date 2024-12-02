class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(n):
            if n not in visited:
                visited[n] = Node(n.val)
                for neighbor in n.neighbors:
                    dfs(neighbor)
        
        dfs(node)
        return visited[node]
