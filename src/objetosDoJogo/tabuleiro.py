from objetosDoJogo.pecas import listaDePecas
from objetosDoJogo.base import PecaBase
from exceptions import ChegouNaBase
import random as rd

class Tabuleiro:

    def __init__(self):
        self.largura = 10
        self.altura = 25
        self.alturaLimite = 5
        self.pecaAtual: PecaBase = rd.choice(listaDePecas)
        self.matriz = self.produzirMatriz()
        self.posicaoAtual = [self.largura//4, 0]

    def produzirMatriz(self):
        matriz = []
        linha = [0 for i in range(self.largura)]
        for i in range(self.altura):
            matriz.append(linha.copy())
        
        return matriz
    
    def posicionarPeca(self):
        