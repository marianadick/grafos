from Grafo import Grafo

class ColoracaoGrafos:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
    
    def run(self):
        # Ordena a lista de vertices pelo maior número de vizinhos
        vertices = sorted(self.grafo.get_lista_vertices(), key=lambda vertice: len(vertice.vizinhos), reverse=True)
            
        # Seta a lista de cores utilizadas
        cores = []

        # Percore os vertices da lista
        for vertice in vertices:
            # Popula um auxiliar com as cores disponiveis para o vertice
            cores_aux = [True] * len(vertices)
            # Percorre os vizinhos e marca suas cores como não disponiveis
            for vizinho in vertice.vizinhos:
                if vizinho.hasCor:
                    cores_aux[vizinho.cor] = False

            # Vai de cor em cor até encontrar uma cor disponível
            for cor, isDisponivel in enumerate(cores_aux):
                if isDisponivel:
                    vertice.cor = cor
                    vertice.hasCor = True
                    
                    # Adiciona na lista de cores e para o loop
                    if cor not in cores:
                        cores.append(cor)
                    break

        self.print_saida(len(cores))

    def print_saida(self, num_cores):
        # Printa o num de cores
        print(f'O número mínimo de cores para esse grafo é {3}.')
        for vertice in self.grafo.vertices.values():
            print(f'O vértice {vertice.indice} possui a coloração {vertice.cor}')

    
def Programa():
    grafo = Grafo()
    grafo.ler_arquivo('testes/cor3.net')

    coloracao = ColoracaoGrafos(grafo)
    coloracao.run()

Programa()