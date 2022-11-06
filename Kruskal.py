from Grafo import Grafo


class Kruskal():

    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo

    def run(self):
        a = self.find_minimal_tree()
        self.print_saida(a)

    def find_minimal_tree(self):
        A = []
        S = {}
        for v in self.grafo.vertices.keys():
            S[v] = [v]
        e = []
        for x in self.grafo.conexoes.values():
            e.append((x.a.indice, x.b.indice, x.peso))
        e.sort(key=lambda item: item[2])
        for v in e:
            if (S[v[0]] != S[v[1]]):
                A.append((v[0], v[1]))
                X = S[v[0]] + S[v[1]]
                for y in X:
                    S[y] = X
        return A

    def print_saida(self, a):
        peso = 0
        for x in a:
            peso += self.grafo.conexoes[(x[0], x[1])].peso
        print(peso)
        for x in range(len(a)-1):
            print(f'{a[x][0]}-{a[x][1]}, ', end= '')
        print(f'{a[len(a)-1][0]}-{a[len(a)-1][1]}')


def Programa():
    nome_do_arquivo = input()
    grafo = Grafo()

    try:
        grafo.ler_arquivo(nome_do_arquivo)
    except:
        print('Erro com nome de arquivo.')
        exit(-1)

    Kruskal(grafo).run()


Programa()