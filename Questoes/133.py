class Solution:
    def cloneGraph(self, node):
        # Se o nó inicial for None, o grafo está vazio. Retorna None.
        if not node:
            return None
        
        # Dicionário para mapear cada nó original ao seu clone correspondente.
        visited = {}
        
        # Função auxiliar para realizar busca em profundidade (DFS).
        def dfs(n):
            # Caso o nó já tenha sido clonado, retorna o clone diretamente.
            if n in visited:
                return visited[n]
            
            # Cria um clone do nó atual com o mesmo valor, mas sem vizinhos inicialmente.
            clone = Node(n.val)
            
            # Adiciona o clone ao dicionário de nós visitados.
            visited[n] = clone
            
            # Percorre todos os vizinhos do nó original.
            for neighbor in n.neighbors:
                # Adiciona o clone de cada vizinho à lista de vizinhos do nó clonado.
                clone.neighbors.append(dfs(neighbor))
            
            # Retorna o clone do nó atual.
            return clone
        
        # Inicia o processo de clonagem a partir do nó inicial.
        return dfs(node)
