class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        clone = Node(node.val)
        clone.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        
        return clone
