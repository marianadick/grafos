from Grafo import Grafo


class Questao4:

    def __init__(self, grafo: Grafo, indice_vertice: int) -> None:
        self.grafo = grafo
        self.vertice_s = self.grafo.vertices[indice_vertice]

    def run(self):
        d, a = self.dijkstra()
        self.print_saida(d, a)

    def dijkstra(self):
        visitados = {}  # vértices visitados
        distancias = {}  # distâncias até encontrar cada vertice
        antecessores = {}  # antecessores aos vértices

        # Configuração de vertíces
        for i in range(1, self.grafo.qtd_vertices() + 1):
            visitados[i] = False
            distancias[i] = float('inf')
            antecessores[i] = None

        distancias[self.vertice_s.indice] = 0
        antecessores[self.vertice_s.indice] = self.vertice_s.indice

        while False in visitados.values():
            nao_visitados = {k: distancias[k] for k, v in visitados.items() if v == False}
            menor_valor = min(nao_visitados.values())
            key = [k for k, v in nao_visitados.items() if v == menor_valor][0]
            vertice_atual = [v for k, v in self.grafo.vertices.items() if v.indice == key][0]
            visitados[key] = True
            for x in vertice_atual.vizinhos:
                if visitados[x.indice] == False:
                    aresta = None
                    for y in self.grafo.arestas.keys():
                        if y == (vertice_atual.indice, x.indice):
                            aresta = self.grafo.arestas[(vertice_atual.indice, x.indice)]
                            break
                        elif y == (x.indice, vertice_atual.indice):
                            aresta = self.grafo.arestas[(x.indice, vertice_atual.indice)]
                            break
                    if distancias[x.indice] > (distancias[key] + aresta.peso):
                        distancias[x.indice] = (distancias[key] + aresta.peso)
                        antecessores[x.indice] = key

        return distancias, antecessores

    def print_saida(self, d, a):
        caminho = self.return_path(a)

        for i in caminho.keys():
            list_str = str(caminho[i]).replace(
                ' ', '').replace('[', '').replace(']', '')
            print(f'{i}: {list_str}; d={d[i]}')    

    def return_path(self, a):
        caminhos = {}

        for k in a.keys():
            caminhos[k] = [k]
            while True:
                antecessor = caminhos[k][0]
                if antecessor == self.vertice_s.indice:
                    break
                caminhos[k].insert(0, a[antecessor])
        
        return caminhos

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
        Questao4(grafo, indice_vertice).run()
    else:
        print(
            f'Vértice inválido. Número deve ser de 1 a {grafo.qtd_vertices()}.')


Programa()