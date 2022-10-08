from Grafo import Grafo


class FloydWarshall():
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def run(self):
        adj = self.cria_matriz_adjacencias()
        dist = self.algoritmo(adj)
        self.print_saida(dist)

    def cria_matriz_adjacencias(self):
        adj = {}
        numV = self.grafo.qtd_vertices()
        for u in range(1, numV+1):
            linha = {}
            for v in range(1, numV+1):
                if u == v:
                    linha[v] = 0
                elif self.grafo.ha_aresta(u, v):
                    linha[v] = self.grafo.peso(u, v)
                else:
                    linha[v] = float('inf')
            adj[u] = linha
        return adj

    def algoritmo(self, adj: dict):
        d = adj.copy()
        numV = self.grafo.qtd_vertices()
        for k in range(1, numV + 1):
            for u in range(1, numV + 1):
                for v in range(1, numV + 1):
                    d[u][v] = min(d[u][v], d[u][k] + d[k][v])
        return d

    def print_saida(self, d: list):
        numV = self.grafo.qtd_vertices()
        for vertice in range(1, numV + 1):
            aux = []
            for v in range(1, numV + 1):
                numero = d[vertice][v]
                if (numero - int(numero)) == 0:  # Checo se há casas decimais
                    aux.append(int(numero))  # Formatação
                else:
                    aux.append(numero)
            list_str = str(aux).replace(
                ' ', '').replace('[', '').replace(']', '')
            print(f'{vertice}:{list_str}')


def Programa():
    nome_do_arquivo = input()
    grafo = Grafo()

    try:
        grafo.ler_arquivo(nome_do_arquivo)
    except:
        print('Erro com nome de arquivo.')
        exit(-1)

    FloydWarshall(grafo).run()


Programa()
