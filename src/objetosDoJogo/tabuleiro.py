from nucleoDoJogo.mecanismos import MecanismoGrafico, MecanismoControlador
from objetosDoJogo.idList import idPecaPosicionada, idVazio
from objetosDoJogo.pecas import listaDePecas
from objetosDoJogo.variaveisDoJogo import *
from objetosDoJogo.base import PecaBase
import objetosDoJogo.pontuacoes as pts
from exceptions import *
import random as rd

class Tabuleiro:

    def __init__(self):
        self.largura = larguraDoTabuleiro
        self.altura = alturaDoTabuleiro
        self.alturaLimite = limiteParaDerrota
        self.matriz = self.produzirMatriz()

        self.mecanismoGrafico = MecanismoGrafico()
        self.mecanismoGrafico.desenharMatrizInteira(self.matriz)
        self.mecanismoGrafico.update()

        self.mecanismoControlador = MecanismoControlador()

        self.pecaAtual: PecaBase
        self.sortearNovaPeca()

        self.pontos = 0
        self.recompensaRecebida = 0

    def produzirMatriz(self):
        matriz = []
        linha = [0 for i in range(self.largura)]
        linha.insert(0, idPecaPosicionada)
        linha.append(idPecaPosicionada)
        for i in range(self.altura):
            matriz.append(linha.copy())
        
        return matriz

    def executarAcao(self):
        self.mecanismoControlador.capturarEventos()
        inputs = self.mecanismoControlador.capturarTeclasPressionadas()

        if inputs["w"]:
            self.rotacionarPeca()
        if inputs["a"]:
            self.moverPecaParaEsquerda()
        if inputs["s"]:
            self.moverPecaParaBaixo()
        if inputs["d"]:
            self.moverPecaParaDireita()
        self.mecanismoGrafico.clock.tick(10)

        if inputs["spc"]:
            self.descerAteColidir()
            self.mecanismoGrafico.clock.tick(5)


    def sortearNovaPeca(self):
        self.pecaAtual = rd.choice(listaDePecas)()
        self.posicaoAtual = [0, self.largura//4] # y, x
        self.posicionarPeca()
        self.mecanismoGrafico.update()

    def setValorPecaPosicionada(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(self.pecaAtual.shape[0]):
            for x in range(self.pecaAtual.shape[1]):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if pertenceAPeca:
                    self.setValorNoTabuleiro(x, y, idPecaPosicionada)

    def verificarDerrota(self):
        for y in range(self.alturaLimite):
            for x in range(1, self.largura-1):
                if self.getValorDoTabuleiro(x, y, relativoAPeca=False) == idPecaPosicionada:
                    self.recompensaRecebida = pts.derrota
                    raise PerdeuOJogo()

    def swap(self, y):
        for linha in range(y, 0, -1):
            self.matriz[linha] = self.matriz[linha - 1]

    # Existe uma forma muito mais otimizada de efetuar esse processo
    # Lembrar de otimizar esse trexo no futuro (se necessário)
    def verificarLinhasCompletas(self):
        multiplicador = 1
        bonus = 1.25
        renderizarNovamente = False
        for y in range(self.altura):
            if idVazio not in self.matriz[y]:
                renderizarNovamente = True
                self.recompensaRecebida = pts.linhaCompleta * multiplicador
                multiplicador *= bonus
                self.pontos += self.recompensaRecebida
                self.swap(y)

        if renderizarNovamente:
            self.mecanismoGrafico.desenharMatrizInteira(self.matriz)
        

    def verificacoesPecaPosicionada(self):
        self.setValorPecaPosicionada()
        self.verificarLinhasCompletas()
        self.verificarDerrota()
        self.sortearNovaPeca()
    
    def descerAteColidir(self):
        self.removerPeca()

        self.posicaoAtual[0] += 1
        linhasDescidas = 0
        while self.ehPossivelAdicionar():
            linhasDescidas += 1
            self.posicaoAtual[0] += 1
        
        self.posicaoAtual[0] -= 1
        self.posicionarPeca()

        self.recompensaRecebida = pts.pecaPosicionada + (pts.pecaPosicionada * linhasDescidas + .5)
        self.pontos += self.recompensaRecebida

        self.verificacoesPecaPosicionada()


    def moverPecaParaBaixo(self):
        yAtual = self.posicaoAtual[0]
        proxY = yAtual+1
        
        self.posicaoAtual[0] = proxY
        if self.ehPossivelAdicionar():
            self.posicaoAtual[0] = yAtual
            self.removerPeca()

            self.posicaoAtual[0] = proxY
            self.posicionarPeca()

            self.mecanismoGrafico.update()

        else:
            self.posicaoAtual[0] = yAtual
            self.recompensaRecebida = pts.pecaPosicionada
            self.pontos += self.recompensaRecebida

            self.verificacoesPecaPosicionada()
        
        return True

    def moverLateral(self, esquerda=True):
        xAtual = self.posicaoAtual[1]
        proxX = xAtual + (- 1 if esquerda else 1)
        
        self.posicaoAtual[1] = proxX
        if self.ehPossivelAdicionar():
            self.posicaoAtual[1] = xAtual
            self.removerPeca()

            self.posicaoAtual[1] = proxX
            self.posicionarPeca()

            self.mecanismoGrafico.update()

            return True
        else:
            self.recompensaRecebida = pts.colidiu
            self.pontos += self.recompensaRecebida

            self.posicaoAtual[1] = xAtual
            return False

    def moverPecaParaEsquerda(self):
        return self.moverLateral()

    def moverPecaParaDireita(self):
        return self.moverLateral(esquerda=False)

    def rotacionarPeca(self):
        self.pecaAtual.rotacionar()

        if self.posicaoAtual[0] + self.pecaAtual.shape[0] >= self.altura or self.posicaoAtual[1] == 0 or self.posicaoAtual[1] + self.pecaAtual.shape[1] > self.largura+2:
            self.pecaAtual.rotacionar(horario=False)
            
            self.recompensaRecebida = pts.colidiu
            self.pontos += self.recompensaRecebida

            return False
        
        if self.ehPossivelAdicionar():
            self.pecaAtual.rotacionar(horario=False)
            self.removerPeca()

            self.pecaAtual.rotacionar()
            self.posicionarPeca()

            self.mecanismoGrafico.update()

            return True
        else:
            self.recompensaRecebida = pts.colidiu
            self.pontos += self.recompensaRecebida

            self.pecaAtual.rotacionar(horario=False)
            return False

    def removerPeca(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(self.pecaAtual.shape[0]):
            for x in range(self.pecaAtual.shape[1]):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if pertenceAPeca:
                    self.setValorNoTabuleiro(x, y, idVazio)

    def posicionarPeca(self):
        formaAlvo = self.pecaAtual.getForma()

        for y in range(self.pecaAtual.shape[0]):
            for x in range(self.pecaAtual.shape[1]):
                pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                if pertenceAPeca:
                    self.setValorNoTabuleiro(x, y, self.pecaAtual.id)

    def setValorNoTabuleiro(self, x, y, valor):
        y = y+self.posicaoAtual[0]
        x = x+self.posicaoAtual[1]

        self.matriz[y][x] = valor
        self.mecanismoGrafico.desenhar(x, y, valor)

    def getValorDaPeca(self, x, y, formaAlvo):
        try:
            return formaAlvo[y][x]
        except:
            ""
    
    def getValorDoTabuleiro(self, x, y, relativoAPeca=True):
        if relativoAPeca:
            return self.matriz[y+self.posicaoAtual[0]][x+self.posicaoAtual[1]]
        else:
            return self.matriz[y][x]

    def ehPossivelAdicionar(self):
        formaAlvo = self.pecaAtual.getForma()

        try: 
            for y in range(self.pecaAtual.shape[0]):
                for x in range(self.pecaAtual.shape[1]):
                    pertenceAPeca = self.getValorDaPeca(x, y, formaAlvo) != 0
                    if not pertenceAPeca:
                        continue

                    ehEspacoValido = self.getValorDoTabuleiro(x, y) != idPecaPosicionada
                    if not ehEspacoValido:
                        return False
                    
            return True
        except:
            return False