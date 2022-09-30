class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.vizinhos = [] #Lista de objetos vertice
        self.grau = 0
