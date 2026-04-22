from IA.memoria import MemoriaConsequencial
from IA.util import *
from torch import nn

class GeneralizadorConsequencial(nn.Module):

    def __init__(self):

        self.memoria = MemoriaConsequencial()
        self.redeNeural = None
        self.epocasDeTreino = 1000
        self.plotarTreino = True

    def salvar(self, causa, acao, consequencia):
        self.memoria.salvar(causa, acao, consequencia)

    def treinarGeneralizacao(self):
        treinar(modelo, self.memoria.dadosParaTreino())