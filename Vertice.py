class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.vizinhos = []  # Lista de objetos vertice
        self.vizinhos_entrantes = []  
        self.vizinhos_saintes = [] 
        self.grau = 0
