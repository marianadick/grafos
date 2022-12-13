from queue import Queue

from Grafo import Grafo


class HopCroftKarp:
    
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.x = {}
        self.y = {}
        
    def encontra_conjuntos(self):
        pass
    
    def bfs(self, mate, x, D):
        q = Queue()
        
        for x in self.x:
            if mate[x.indice] == None:
                D[x.indice] = 0
                q.put(x)
            else:
                D[x.indice] = float('inf')
                
        D_null = float('inf')
        
        while q.empty() == False:
            x = q.get()
            if D[x.indice] < D_null:
                for y in x.vizinhos():
                    if D[mate[1].indice] == float('inf'):
                        D[mate[1].indice] = D[x.indice] + 1
                        q.put(mate[1])
                        
        return D_null != float('inf')
    
    def dfs(self, mate, ):
        pass
    
    def run(self):
        D_v = {}
        mate_v = {}
        for i in range(1, self.grafo.qtd_vertices() + 1):
            D_v[i] = float('inf')
            mate_v[i] = None
        
        m = 0 # tamanho do emparelhamento
        while self.bfs(mate_v, D_v) == True:
            for x in self.grafo.vertices():
                if self.dfs(mate_v, x, D_v) == True:
                    m += 1
        return (m, mate_v)
            
        
        
            