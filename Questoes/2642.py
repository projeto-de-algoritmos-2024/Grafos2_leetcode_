import math  # Importa a biblioteca para usar "math.inf", que representa o infinito.

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        # Inicializa o grafo como um dicionário onde cada nó é uma chave
        # e os valores são listas de tuplas (destino, peso).
        self.graph = {}
        for i in range(n):
            self.graph[i] = []  # Inicializa cada nó com uma lista vazia para suas arestas.
        for edge in edges:
            self.addEdge(edge)  # Adiciona as arestas fornecidas ao grafo.

    def addEdge(self, edge: list[int]):
        # Extrai os valores da aresta: nó de origem (u), nó de destino (v), e peso (w).
        u, v, w = edge
        # Adiciona a aresta ao grafo no nó de origem (u), apontando para o nó de destino (v) com peso (w).
        self.graph[u].append((v, w))

    def shortestPath(self, node1, node2):
        # Inicializa o dicionário de distâncias com infinito para todos os nós.
        dist = {node: math.inf for node in self.graph}
        # A distância do nó inicial para ele mesmo é zero.
        dist[node1] = 0
        visited = set()  # Conjunto para rastrear os nós já visitados.

        for _ in range(len(self.graph)):  # Itera até que todos os nós tenham sido processados.
            # Encontra o nó não visitado com a menor distância conhecida.
            u = min((node for node in self.graph if node not in visited), 
                    key=lambda node: dist[node], 
                    default=None)
            
            # Se nenhum nó não visitado restante ou todas as distâncias forem infinitas, encerra o loop.
            if u is None or dist[u] == math.inf:
                break
            
            visited.add(u)  # Marca o nó atual como visitado.

            # Atualiza as distâncias para os vizinhos do nó atual.
            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:  # Se uma distância menor é encontrada...
                    dist[v] = dist[u] + weight  # Atualiza a distância do vizinho.

        # Retorna a menor distância para o nó de destino ou -1 se não houver caminho.
        return dist[node2] if dist[node2] != math.inf else -1
