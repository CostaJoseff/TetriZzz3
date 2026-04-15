import random as rd

class PecaBase:

    def __init__(self, id_, formas):
        self.id: float = id_
        self.formas: list = formas
        self.rotacaoAtual: int = 0

    def rotacionar(self):
        self.rotacaoAtual = (self.rotacaoAtual + 1) % len(self.formas)

    def getForma(self):
        return self.formas[self.rotacaoAtual]
    
    def rotacaoAleatoria(self):
        self.rotacaoAtual = rd.randint(0, len(self.formas)-1)