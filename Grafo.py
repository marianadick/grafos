from Vertice import Vertice
from Aresta import Aresta

''' As buscas são realizadas através dos indices. '''
class Grafo:
    def __init__(self):
        self.vertices = {} #{index: objeto Vertice}
        self.arestas = {} #{(indice a, indice b): objeto Aresta}

    def qtd_vertices(self):  
        return len(self.vertices.keys())

    def qtd_arestas(self):
        return len(self.arestas.keys())

    def grau(self, v):
        return self.vertices[v].grau

    def rotulo(self, v):
        return self.vertices[v].rotulo

    def vizinhos(self, v):
        return self.vertices[v].vizinhos

    def ha_aresta(self, u, v):
        if ((u, v) in self.arestas or (v, u) in self.arestas):
            return True
        return False
    
    def peso(self, u, v):
        if (u, v) in self.arestas:
            return self.arestas[u, v].peso
        elif (v, u) in self.arestas:
            return self.arestas[v, u].peso
        else:
            return 'Não há aresta'

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

                indice = int(val[0])
                rotulo = val[1]

                vertice = Vertice(indice, rotulo)
                self.vertices[indice] = vertice

            else:
                val = linha.split(' ')

                a = self.vertices[int(val[0])]
                b = self.vertices[int(val[1])]
                peso = float(val[2])

                aresta = Aresta(a, b, peso)
                self.arestas[a.indice, b.indice] = aresta
                
                a.vizinhos.append(b)
                a.grau += 1
                b.vizinhos.append(a)
                b.grau += 1

#grafo = Grafo()
#grafo.ler_arquivo('cor3.net')
