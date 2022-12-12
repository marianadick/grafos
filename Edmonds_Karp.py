from GrafoDirigido import GrafoDirigido
from Buscas import Buscas

class Edmonds_Karp:
    def __init__(self, grafo: GrafoDirigido, busca: Buscas):
        self.grafo = grafo
        self.busca = busca
        self.capacity_matrix = {}
    

    def Dfs(self, C, F, k, cp):
        tmp = cp
        if k == len(self.grafo.vertices) - 1:
            return cp
        f = 0
        for i in range(1, len(C)+1):
            if (((k.indice, self.grafo.vertices[i].indice) in self.grafo.conexoes )):
                if (F[(k.indice, self.grafo.vertices[i].indice)] < self.grafo.conexoes[(k.indice, self.grafo.vertices[i].indice)].peso):
                    f = self.Dfs(C, F, self.grafo.vertices[i], min(tmp, self.grafo.conexoes[(k.indice, self.grafo.vertices[i].indice)].peso - F[(k.indice, self.grafo.vertices[i].indice)]))
            if ((k.indice, self.grafo.vertices[i].indice) in F):
                F[(k.indice, self.grafo.vertices[i].indice)] = F[(k.indice, self.grafo.vertices[i].indice)] + f
                F[(self.grafo.vertices[i].indice, k.indice)] = F[(self.grafo.vertices[i].indice, k.indice)]  - f
            else:
                f = 0
            tmp = tmp - f
        return cp - tmp


    def run(self):
        n = len(self.grafo.conexoes)
        F = {}
        for x in self.grafo.conexoes.values():
            F[x.a.indice, x.b.indice] = 0
            F[x.b.indice, x.a.indice] = 0

        for i in range(n): # F is the flow matrix
            flow = 0
            while (True):
                distancia, antecessores =  self.busca.busca_em_largura()
                if distancia[self.grafo.vertices[len(self.grafo.vertices)].indice] == 0:
                    break
                flow = flow + self.Dfs(self.grafo.conexoes, F, self.grafo.vertices[1], 100000)

        self.print_saida(flow)

    def print_saida(self, fluxo):
        print(f'O número fluxo maximo é {fluxo}.')
    

    
def Programa():
    grafo = GrafoDirigido()
    grafo.ler_arquivo('testes/fluxo_maximo_aula.net')
    busca = Buscas(grafo)
    coloracao = Edmonds_Karp(grafo, busca)
    coloracao.run()

Programa()