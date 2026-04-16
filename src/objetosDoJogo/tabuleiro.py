from objetosDoJogo.idList import idPecaPosicionada, idVazio
from objetosDoJogo.pecas import listaDePecas
from objetosDoJogo.base import PecaBase
from exceptions import *
import random as rd

class Tabuleiro:

    def __init__(self):
        self.largura = 10
        self.altura = 25
        self.alturaLimite = 5
        self.pecaAtual: PecaBase = rd.choice(listaDePecas)
        self.matriz = self.produzirMatriz()
        self.posicaoAtual = [0, self.largura//4] # y, x

    def produzirMatriz(self):
        matriz = []
        linha = [0 for i in range(self.largura)]
        for i in range(self.altura):
            matriz.append(linha.copy())
        
        return matriz
    
    def moverPecaParaBaixo(self):
        yAtual = self.posicaoAtual[0]
        proxY = yAtual+1

        if proxY + self.pecaAtual.shape[0] >= self.altura:
            raise ChegouNaBase()

    def removerPeca(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(len(self.pecaAtual.shape[0])):
            for x in range(len(self.pecaAtual.shape[1])):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if pertenceAPeca:
                    self.setValorNoTabuleiro(x, y, idVazio)

    def posicionarPeca(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(len(self.pecaAtual.shape[0])):
            for x in range(len(self.pecaAtual.shape[1])):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if pertenceAPeca:
                    self.setValorNoTabuleiro(x, y, self.pecaAtual.id)

    def setValorNoTabuleiro(self, x, y, valor):
        self.matriz[y+self.posicaoAtual[0]][x+self.posicaoAtual[1]] = valor

    def getValorDaPeca(self, x, y, formaAlvo):
        return formaAlvo[y][x]
    
    def getValorDoTabuleiro(self, x, y):
        return self.matriz[y+self.posicaoAtual[0]][x+self.posicaoAtual[1]]

    def ehPossivelAdicionar(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(len(self.pecaAtual.shape[0])):
            for x in range(len(self.pecaAtual.shape[1])):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if not pertenceAPeca:
                    continue

                ehEspacoValido = self.getValorDoTabuleiro(x, y) != idPecaPosicionada
                if not ehEspacoValido:
                    return False
                
        return True