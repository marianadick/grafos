'''Crie um programa que receba um grafo dirigido e n ao-ponderado como argumento. 
Ao final, imprima na tela as componentes fortemente conexas desse grafo.'''

from cmath import inf
from GrafoDirigido import GrafoDirigido

class ComponentesFortementeConexas:
    def __init__(self, grafo: GrafoDirigido):
        self.grafo = grafo
        self.componentes = []

    def run(self):
        F, A = self.DFS()
        self.grafo.transposicao()
        _, _, _, Ad = self.DFS_adaptado(F)
        print(Ad)
        for k, v in Ad.items():
            if v == None:
                self.componentes.append(self.encontrar_componentes(k,Ad))
        self.print_saida()

    def DFS(self):
        visitados = {}
        tempo_inicial = {}
        tempo_final = {}
        antecessores = {}
        
        for v in self.grafo.vertices.keys():
            visitados[v] = False
            tempo_inicial[v] = inf
            tempo_final[v] = inf        
            antecessores[v] = None

        tempo = 0

        for u in self.grafo.vertices.keys():
            if visitados[u] == False:
                self.DFS_visit(u, visitados, tempo_inicial, tempo_final, antecessores, tempo)
        
        return tempo_final, antecessores

    def DFS_adaptado(self, F):
        visitados = {}
        tempo_inicial = {}
        tempo_final = {}
        antecessores = {}
        
        for v in self.grafo.vertices.keys():
            visitados[v] = False
            tempo_inicial[v] = inf
            tempo_final[v] = inf        
            antecessores[v] = None

        tempo = 0
        F_ord = dict(sorted(F.items(), key=lambda item: item[1], reverse=True))
        vertices = []
        print(F_ord)
        
        for key in F_ord.keys():
            vertices.append(key)
           
        for v in vertices:
            if visitados[v] == False:
                self.DFS_visit(v, visitados, tempo_inicial, tempo_final, antecessores, tempo)
        
        return visitados, tempo_inicial, tempo_final, antecessores 
        

        
    def DFS_visit(self, v, visitados, tempo_inicial, tempo_final, antecessores, tempo):
        visitados[v] = True
        tempo += 1
        tempo_inicial[v] = tempo
        obj_v = self.grafo.vertices[v]
        
        for u in obj_v.vizinhos_saintes:
            if visitados[u.indice] == False:
                antecessores[u.indice] = v
                self.DFS_visit(u.indice, visitados, tempo_inicial, tempo_final, antecessores, tempo)
        
        tempo += 1
        tempo_final[v] = tempo
    
    def encontrar_componentes(self, r, antecessores):
        aux = []
        for k, v in antecessores.items():
            if v == r:
                aux.append(k)
            elif v in aux:
                aux.append(k)     
        return aux   
            


    def print_saida(self):
        for componente in self.componentes:
            print(', '.join(map(str, componente)))


def Programa(): 
    grafo = GrafoDirigido()
    grafo.ler_arquivo('cfc.net')

    cfc = ComponentesFortementeConexas(grafo)
    cfc.run()

Programa()
        

