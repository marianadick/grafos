from Grafo import Grafo

class GrafoDirigido(Grafo):
    def __init__(self, vertices={}, conexoes={}):
        super().__init__(vertices, conexoes) # Conexoes = arcos

    def ha_conexao(self, u, v):
        if ((u, v) in self.conexoes):
            return True
        return False
    
    def peso(self, u, v):
        if ((u, v) in self.conexoes):
            return self.conexoes[u, v].peso
        else:
            return 'Não há arco'