from heapq import heapify, heappop, heappush

class Graph:
  def __init__(self, graph: dict = {}):
    self.graph = graph  # A dictionary for the adjacency list

  def add_edge(self, node1, node2, weight):
    # Adiciona node1 ao grafo, se necessário
    if node1 not in self.graph:
        self.graph[node1] = {}
    # Adiciona node2 ao grafo, mesmo que não tenha arestas saindo dele
    if node2 not in self.graph:
        self.graph[node2] = {}
    # Adiciona a aresta de node1 para node2
    self.graph[node1][node2] = weight

  def add_edges_from_list(self, edges):
    for edge in edges:
      self.add_edge(edge[0], edge[1], edge[2]) 

  def shortest_distances(self, source: str):
    # Initialize the values of all nodes with infinity
    distances = {node: float("inf") for node in self.graph}
    distances[source] = 0  # Set the source value to 0

    # Initialize a priority queue
    pq = [(0, source)]
    heapify(pq)

    # Create a set to hold visited nodes
    visited = set()
    while pq:  # While the priority queue isn't empty
      current_distance, current_node = heappop(
          pq
      )  # Get the node with the min distance

      if current_node in visited:
          continue  # Skip already visited nodes
      visited.add(current_node)  # Else, add the node to visited set

      for neighbor, weight in self.graph[current_node].items():
        # Calculate the distance from current_node to the neighbor
        tentative_distance = current_distance + weight
        if tentative_distance < distances[neighbor]:
          distances[neighbor] = tentative_distance
          heappush(pq, (tentative_distance, neighbor))

    return distances


class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        #djikstra porém vai adicionar mais os valores dos vértices