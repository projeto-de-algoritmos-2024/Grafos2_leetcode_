from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph: dict = {}, passingFees: list = []):
      self.graph = graph  # A dictionary for the adjacency list
      self.passingFees = passingFees  # Lista de passing fees para cada cidade

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

    def shortest_distances_by_fees(self, source: str):
      # Inicializa as distâncias com infinito e o custo dos vértices com infinito
      costs = {node: float("inf") for node in self.graph}
      costs[source] = self.passingFees[source]  # O custo inicial é o custo do vértice de origem

      # Inicializa os caminhos com listas vazias
      paths = {node: [] for node in self.graph}
      paths[source] = [source]

      # Inicializa a fila de prioridade (min-heap) com o custo de origem
      pq = [(self.passingFees[source], source)]  # (custo, nó)
      heapify(pq)

      # Criar um conjunto para manter os nós visitados
      visited = set()

      while pq:
          current_cost, current_node = heappop(pq)

          if current_node in visited:
              continue  # Pula nós já visitados
          visited.add(current_node)

          for neighbor in self.graph[current_node].keys():
              # Cálculo do custo total (acumulado de passing fees)
              tentative_cost = current_cost + self.passingFees[neighbor]

              if tentative_cost < costs[neighbor]:
                  costs[neighbor] = tentative_cost
                  paths[neighbor] = paths[current_node] + [neighbor]
                  heappush(pq, (tentative_cost, neighbor))

      return costs, paths

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        #djikstra porém vai adicionar mais os valores dos vértices