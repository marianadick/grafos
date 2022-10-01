from queue import Queue
from Grafo import Grafo
from collections import defaultdict


class Buscas():
    def __init__(self, grafo: Grafo, indice_vertice: int):
        self.grafo = grafo
        self.vertice_s = self.grafo.vertices[indice_vertice]

    def run(self):
        d, _ = self.busca_em_largura()
        self.print_saida(d)

    def busca_em_largura(self):

        visitados = {}  # vértices visitados
        distancias = {}  # distâncias até encontrar cada vertice
        antecessores = {}  # antecessores aos vértices

        # Configuração de vertíces
        for i in range(1, self.grafo.qtd_vertices() + 1):
            visitados[i] = False
            distancias[i] = float('inf')
            antecessores[i] = None

        # Configurando vértice de origem
        visitados[self.vertice_s.indice] = True
        distancias[self.vertice_s.indice] = 0

        # Preparando fila de visitas
        fila = Queue()
        fila.put(self.vertice_s)  # Enqueue

        # Propagação das visitas
        while fila.empty() == False:
            u = fila.get()  # Dequeue -> retorna um vértice
            for v in u.vizinhos:
                if visitados[v.indice] == False:
                    visitados[v.indice] = True
                    distancias[v.indice] = distancias[u.indice] + 1
                    antecessores[v.indice] = u
                    fila.put(v)

        return distancias, antecessores

    def print_saida(self, d):
        # Ordenando lista de distância por níveis
        res = defaultdict(list)
        for key, val in sorted(d.items()):
            res[val].append(key)
        res = dict(res)

        # Print de cada nível com formatação
        for i in range(len(res.keys())):
            list_str = str(res[i]).replace(
                ' ', '').replace('[', '').replace(']', '')
            print(f'{i}: {list_str}')


def Programa():
    nome_do_arquivo, indice_vertice = input().split()
    grafo = Grafo()

    try:
        grafo.ler_arquivo(nome_do_arquivo)
    except:
        print('Erro com nome de arquivo.')
        exit(-1)

    try:
        indice_vertice = int(indice_vertice)
    except:
        print('Erro no índice do vértice.')
        exit(-1)

    if grafo.qtd_vertices() >= indice_vertice > 0:
        Buscas(grafo, indice_vertice).run()
    else:
        print(
            f'Vértice inválido. Número deve ser de 1 a {grafo.qtd_vertices()}.')


Programa()
