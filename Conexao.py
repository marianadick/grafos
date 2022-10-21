# Classe utilizada para representação de arestas e arcos

class Conexao:
    def __init__(self, a, b, peso):
        self.a = a #Objeto vertice
        self.b = b #Objeto vertice
        self.peso = peso