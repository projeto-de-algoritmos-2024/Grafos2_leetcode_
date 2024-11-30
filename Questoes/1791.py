#1791. Find Center of Star Graph

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """  
        flat_edges = [item for sublist in edges for item in sublist]
        from collections import Counter
        counts = Counter(flat_edges)
        most_common_element = counts.most_common(1)[0][0] 
        return most_common_element

# foi de primeira