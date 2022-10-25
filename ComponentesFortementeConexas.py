'''Crie um programa que receba um grafo dirigido e n ao-ponderado como argumento. 
Ao final, imprima na tela as componentes fortemente conexas desse grafo.'''

from cmath import inf
from itertools import count
from operator import truediv
from Grafo import Grafo
from GrafoDirigido import GrafoDirigido
from Buscas import Buscas

class ComponentesFortementeConexas:
    def __init__(self, grafo: GrafoDirigido):
        self.grafo = grafo
        self.componentes = []
        self.visitados = []

    def busca_em_largura(self, v):
        return Buscas(self.grafo, v).busca_em_largura()

    def print_saida(self):
        for componente in self.componentes:
            print(', '.join(map(str, componente)))

    def find_components(self, v=1):
        while (True):
            auxiliar = []
            distancia, _ = self.busca_em_largura(v)
            for d in distancia.keys():
                if d in self.visitados:
                    continue
                else:
                    if distancia[d] == inf:
                        self.find_components(d)
                    else:
                        auxiliar.append(d)
                        self.visitados.append(d)
            self.componentes.append(auxiliar)
            break

def Programa(): 
    grafo = GrafoDirigido()
    grafo.ler_arquivo('cfc.net')

    cfc = ComponentesFortementeConexas(grafo)
    cfc.find_components()
    cfc.print_saida()

Programa()
        

