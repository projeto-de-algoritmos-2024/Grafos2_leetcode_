from heapq import heappop, heappush

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        # Número de cidades
        n = len(passingFees)

        # Criar o grafo como lista de adjacências
        graph = {i: [] for i in range(n)}
        for x, y, time in edges:
            graph[x].append((y, time))
            graph[y].append((x, time))

        # Min-heap: (custo, tempo, cidade)
        pq = [(passingFees[0], 0, 0)]  # Inicia na cidade 0 com custo e tempo 0

        # Distância mínima para cada cidade com um determinado tempo
        min_time = {i: float('inf') for i in range(n)}
        min_time[0] = 0

        while pq:
            cost, time, city = heappop(pq)

            # Se chegou ao destino e está dentro do tempo, retorna o custo
            if city == n - 1 and time <= maxTime:
                return cost

            # Explorar vizinhos
            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time
                new_cost = cost + passingFees[neighbor]

                # Se o tempo for menor que o máximo permitido e melhora a solução, continua
                if new_time <= maxTime and new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heappush(pq, (new_cost, new_time, neighbor))

        # Se nenhum caminho válido foi encontrado, retorna -1
        return -1