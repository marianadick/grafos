from Vertice import Vertice
from Conexao import Conexao

''' As buscas são realizadas através dos indices. '''


class Grafo:
    def __init__(self, vertices={}, conexoes={}):
        self.vertices = vertices  # {index: objeto Vertice}
        self.conexoes = conexoes  # {(indice a, indice b): objeto Conexao}

    def get_lista_vertices(self):
        return list(self.vertices.values())
    
    def qtd_vertices(self):
        return len(self.vertices.keys())

    def qtd_conexoes(self):
        return len(self.conexoes.keys())

    def grau(self, v):
        return self.vertices[v].grau

    def rotulo(self, v):
        return self.vertices[v].rotulo

    def vizinhos(self, v):
        return self.vertices[v].vizinhos

    def ha_conexao(self, u, v):
        if ((u, v) in self.conexoes or (v, u) in self.conexoes):
            return True
        return False

    def peso(self, u, v):
        if ((u, v) in self.conexoes):
            return self.conexoes[u, v].peso
        elif ((v, u) in self.conexoes):
            return self.conexoes[v, u].peso
        else:
            return 'Não há aresta'

    def ler_arquivo(self, arquivo):
        ref_arquivo = open(arquivo, 'r').read().split('\n')
        lendo_conexoes = False

        for linha in ref_arquivo:
            if (linha == ''):
                continue

            elif ("*vertices" in linha):
                continue

            elif ("*edges" in linha or "*arcs" in linha):
                lendo_conexoes = True
                continue

            elif (not lendo_conexoes):
                val = linha.split(' ')

                indice = int(val[0])

                if '"' in val[1]:
                    last_word = len(val) - 1
                    val[1] = val[1].replace('"', '')
                    val[last_word] = val[last_word].replace('"', '')
                    rotulo = ' '.join(val[1:last_word+1])

                else:
                    rotulo = val[1]

                vertice = Vertice(indice, rotulo)
                self.vertices[indice] = vertice

            else:
                val = linha.split(' ')

                a = self.vertices[int(val[0])]
                b = self.vertices[int(val[1])]
                peso = float(val[2])

                conexao = Conexao(a, b, peso)
                self.conexoes[a.indice, b.indice] = conexao

                a.vizinhos.append(b)
                a.grau += 1
                b.vizinhos.append(a)
                b.grau += 1

                # Importante para dirigidos
                a.vizinhos_saintes.append(b)
                b.vizinhos_entrantes.append(a)
