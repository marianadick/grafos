from Grafo import Grafo


class CicloEuleriano:


    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo

    def run(self):
        e, c = self.hierholzer()
        self.print_saida(e, c)

    def hierholzer(self):
        C = {}  # Arestas visitadas
        vertices = list(self.grafo.vertices.values())
        arestas = list(self.grafo.arestas.values())

        for x in arestas:
            C[(x.a.indice, x.b.indice)] = False

        v = vertices[0].indice
        r, ciclo = self.buscarSubcicloEuleriano(v, C)    
        if r == False:
            return False, None
        
        else:
            if False in C.values():
                return False, None
            else:
                return True, ciclo

    def buscarSubcicloEuleriano(self, v, C):
        ciclo = [v]
        t = v
        
        while True:

            if not False in C.values():
                return False, None
            else:
                nao_visitados = [k for k, i in C.items() if i == False and (k[0]==v or k[1]==v)]
                usado = v
                v = nao_visitados[0][0]
                u = nao_visitados[0][1]
                C[(v, u)] = True
                v = u if u != usado else v
                ciclo.append(v)

            if v == t:
                break

        vertices_no_ciclo = [self.grafo.vertices[x] for x in ciclo]
        vizinhos_abertos = []

        

        for x in vertices_no_ciclo:
            for y in x.vizinhos:
                if (x.indice, y.indice) in C:
                    if C[(x.indice, y.indice)] == False:
                        vizinhos_abertos.append(x)

                elif (y.indice, x.indice) in C:
                    if C[(y.indice, x.indice)] == False:
                        vizinhos_abertos.append(x)

        if not vizinhos_abertos:
            return True, ciclo

        for x in vizinhos_abertos:
            r, ciclo_2 = self.buscarSubcicloEuleriano(x.indice, C)

            if r == False:
                return False, None

            for x in ciclo:
                if x == ciclo_2[0]:
                    index = ciclo.index(x)
                    ciclo[index+1:index+1] = ciclo_2
                    ciclo.pop(index)
                    break

            return True, ciclo

    def print_saida(self, e, c):
        if e == True:
            print('1')
            for x in range(len(c)-1):
                print(f'{c[x]},', end='')
            print(c[-1])
        else:
            print('0')


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
        CicloEuleriano(grafo).run()
    else:
        print(
            f'Vértice inválido. Número deve ser de 1 a {grafo.qtd_vertices()}.')


Programa()