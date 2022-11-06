# -*- coding: utf-8 -*-


from GrafoDirigido import GrafoDirigido


class OrdenacaoTopologica:
    def __init__(self, grafo: GrafoDirigido):
        self.grafo = grafo
        self.ordenacao = []

    def run(self):
        self.ordenacao = self.algoritmo()
        self.print_saida(self.ordenacao)

    def algoritmo(self):
        c = {}
        t = {}
        f = {}
        numV = self.grafo.qtd_vertices()
        for v in range(1, numV+1):
            c[v] = False
            t[v] = float('inf')
            f[v] = float('inf')
        tempo = 0
        o = []

        for u in range(1, numV + 1):
            if c[u] == False:
                self.dfs_visit_ot(u, c, t, f, tempo, o)
        return o

    def dfs_visit_ot(self, v, c, t, f, tempo, o):
        c[v] = True
        tempo += 1
        t[v] = tempo
        objeto_v = self.grafo.vertices[v]

        for u in objeto_v.vizinhos_saintes:
            if c[u.indice] == False:
                self.dfs_visit_ot(u.indice, c, t, f, tempo, o)
        tempo += 1
        f[v] = tempo
        o.insert(0, objeto_v)

    def print_saida(self, o):
        rotulos = []
        for v in o:
            rotulos.append(v.rotulo)
        print(' → '.join(rotulos))


def Programa():
    nome_do_arquivo = input('Nome do arquivo na pasta: ')
    grafo = GrafoDirigido()

    try:
        grafo.ler_arquivo(nome_do_arquivo)
    except:
        print('Erro com nome de arquivo.')
        exit(-1)

    OrdenacaoTopologica(grafo).run()


Programa()
