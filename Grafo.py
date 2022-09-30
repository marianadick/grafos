from Vertice import Vertice
from Aresta import Aresta

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}

    def qtd_vertices(self):  
        return len(self.vertices.keys())

    def qtd_arestas(self):
        return len(self.arestas.keys())

    def grau(self, index):
        return self.vertices[index].grau

    def rotulo(self, index):
        return self.vertices[index].rotulo

    def vizinhos(self, index):
        return self.vertices[index].vizinhos

    def ha_aresta(self, a, b):
        if (self.arestas[a, b]):
            return True
        return False
    
    def peso(self, a, b):
        return self.arestas[a, b]
        

    def ler_arquivo(self, arquivo):   
        ref_arquivo = open(arquivo, 'r').read().split('\n')
        lendo_arestas = False
        
        for linha in ref_arquivo:
            if (linha == ''):
                continue

            elif ("*vertices" in linha):
                continue

            elif ("*edges" in linha):
                lendo_arestas = True
                continue

            elif (not lendo_arestas):
                val = linha.split(' ')

                index = int(val[0])
                rotulo = val[1]
                vertice = Vertice(rotulo)
                self.vertices[index] = vertice

            else:
                val = linha.split(' ')

                a = self.vertices[int(val[0])]
                b = self.vertices[int(val[1])]
                peso = float(val[2])
                aresta = Aresta(a, b, peso)

                self.arestas[a, b] = aresta
                a.vizinhos.append(b)
                a.grau += 1
                b.vizinhos.append(a)
                b.grau += 1

grafo = Grafo()
grafo.ler_arquivo('cor3.net')