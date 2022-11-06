'''Crie um programa que receba um grafo dirigido e n ao-ponderado como argumento. 
Ao final, imprima na tela as componentes fortemente conexas desse grafo.'''

from cmath import inf
from GrafoDirigido import GrafoDirigido

class ComponentesFortementeConexas:
    def __init__(self, grafo: GrafoDirigido):
        self.grafo = grafo
        self.componentes = []

    def run(self):
        F = self.DFS()
        self.grafo.transposicao()
        At = self.DFS_adaptado(F)
        self.print_saida(At)

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
        
        return tempo_final

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
        
        F_ord = dict(sorted(F.items(), key=lambda item: item[0], reverse=True))
        vertices = list(F_ord.keys())
           
        for v in vertices:
            if visitados[v] == False:
                self.DFS_visit(v, visitados, tempo_inicial, tempo_final, antecessores, tempo)
        
        return antecessores 
        
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

    def print_saida(self, At):
        for k, v in At.items():
            if v == None:
                aux = []
                aux.append(k)
                aux.extend(self.print_recursiva(k, At, []))
                self.componentes.append(aux)
                
        for componente in self.componentes:
            print(', '.join(map(str, componente)))

                
    def print_recursiva(self, k, At, lista):
        for i, v in At.items():
            if k == v:
                lista.append(i)
                self.print_recursiva(i, At, lista)
        return lista                
        
def Programa(): 
    grafo = GrafoDirigido()
    grafo.ler_arquivo('cfc.net')

    cfc = ComponentesFortementeConexas(grafo)
    cfc.run()

Programa()
        

