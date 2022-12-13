from queue import Queue

from Grafo import Grafo


class HopCroftKarp:

    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.x = []
        self.y = []
        self.encontra_conjuntos()  # testado funcionando

    def encontra_conjuntos(self):
        '''Verifica bipartição do gráfico e separa os conjuntos, pois o algoritmo é para grafos bipartidos.'''

        vertices = self.grafo.vertices  # dict
        lista = list()
        lista.append(vertices[1])

        while lista != []:
            vertice = lista.pop()
            vizinho_em_x = False
            vizinho_em_y = False
            for v in vertice.vizinhos:
                if v in self.x:
                    vizinho_em_x = True  # Possui vizinho em x, logo não pode ser x
                if v in self.y:
                    vizinho_em_y = True  # Possui vizinho em y, logo não pode ser y
                if (v not in lista) and (v not in self.x) and (v not in self.y):
                    lista.append(v)  # Não analisado, analisar
            if (not vizinho_em_x) and (not vizinho_em_y):
                self.x.append(vertice)
            elif vizinho_em_x and vizinho_em_y:
                print('Grafo não bipartido.')
                exit(-1)
            elif vizinho_em_x:
                self.y.append(vertice)
            elif vizinho_em_y:
                self.x.append(vertice)

    def bfs(self, mates: list, D: list):
        q = Queue()

        for x in self.x:
            if mates[x.indice] == None:
                D[x.indice] = 0
                q.put(x)
            else:
                D[x.indice] = float('inf')

        D['null'] = float('inf')

        while q.empty() == False:
            x = q.get()
            if D[x.indice] < D['null']:
                for y in x.vizinhos:
                    if mates[y.indice] == None:
                        if D['null'] == float('inf'):
                            D['null'] = D[x.indice] + 1
                    elif D[mates[y.indice].indice] == float('inf'):
                        D[mates[y.indice].indice] = D[x.indice] + 1
                        q.put(mates[y.indice])

        return D['null'] != float('inf')

    def dfs(self, mates: list, x, D: list):

        if x != None:
            for y in x.vizinhos:
                if mates[y.indice] == None:
                    if D['null'] == (D[x.indice] + 1):
                        if self.dfs(mates, mates[y.indice], D):
                            # mates[y.indice] = x
                            mates[x.indice] = y
                            return True

                elif D[mates[y.indice]] == (D[x.indice] + 1):
                    if self.dfs(mates, mates[y.indice], D):
                        mates[y.indice] = x
                        mates[x.indice] = y
                        return True
                # else?
        D[x] = float('inf')
        return False

    def run(self):
        D = {}
        mates = {}  # É pra ser um dict de vários mate = vertice
        for i in range(1, self.grafo.qtd_vertices() + 1):
            D[i] = float('inf')
            mates[i] = None

        m = 0  # tamanho do emparelhamento
        while self.bfs(mates, D) == True:
            for x in self.x:
                if mates[x.indice] == None:
                    if self.dfs(mates, x, D) == True:
                        m += 1

        self.print_saida(m, mates)

    def print_saida(self, m, mates):
        print(f'Emparelhamento máximo: {m}')
        for k, v in mates.items():
            if v != None:
                print(f'{k} <-> {v.indice}')


def Programa():
    grafo = Grafo()
    grafo.ler_arquivo('testes/pequeno.net')
    HopCroftKarp(grafo).run()


Programa()
