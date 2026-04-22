from nucleoDoJogo.variaveisDeInterface import *
from objetosDoJogo.variaveisDoJogo import *
from objetosDoJogo.idList import *
import pygame, sys

class MecanismoGrafico:

    def __init__(self):
        self.alturaDaJanela = alturaDaJanela
        self.larguraDaJanela = larguraDaJanela

        self.alturaDoTabuleiro = alturaDoTabuleiro
        self.larguraDoTabuleiro = larguraDoTabuleiro+2

        self.alturaDoBloco = self.alturaDaJanela // self.alturaDoTabuleiro
        self.larguraDoBloco = self.larguraDaJanela // self.larguraDoTabuleiro

        self.clock = pygame.time.Clock()
        self.janela = self.criarJanela()
        self.fonte = pygame.font.SysFont("Pixeled", 30)

        bloco = pygame.image.load("src/bloco.jpg").convert()
        bloco = pygame.transform.scale(bloco, (self.larguraDoBloco, self.alturaDoBloco))

        parede = pygame.image.load("src/parede.jpg").convert()
        parede = pygame.transform.scale(parede, (self.larguraDoBloco, self.alturaDoBloco))
        
        vazio = pygame.image.load("src/vazio.jpg").convert()
        vazio = pygame.transform.scale(vazio, (self.larguraDoBloco, self.alturaDoBloco))

        self.texturaL            = bloco.copy()
        self.texturaJ            = bloco.copy()
        self.texturaS            = bloco.copy()
        self.texturaO            = bloco.copy()
        self.texturaZ            = bloco.copy()
        self.texturaT            = bloco.copy()
        self.texturaI            = bloco.copy()
        self.texturaVazio        = vazio.copy()
        self.texturaPosicionada = parede.copy()
        
        self.texturaJ.fill([255, 0  , 198], special_flags=pygame.BLEND_MULT)
        self.texturaL.fill([255, 31 , 62 ], special_flags=pygame.BLEND_MULT)
        self.texturaS.fill([124, 255, 255], special_flags=pygame.BLEND_MULT)
        self.texturaO.fill([255, 255, 255], special_flags=pygame.BLEND_MULT)
        self.texturaZ.fill([62 , 58 , 228], special_flags=pygame.BLEND_MULT)
        self.texturaT.fill([147, 35 , 206], special_flags=pygame.BLEND_MULT)
        self.texturaI.fill([255, 136, 43 ], special_flags=pygame.BLEND_MULT)
        self.texturaVazio.fill([20, 20, 20], special_flags=pygame.BLEND_MULT)
        self.texturaPosicionada.fill([50, 50, 50], special_flags=pygame.BLEND_MULT)

    def criarJanela(self):
        pygame.init()
        # info = pygame.display.Info()
        pygame.display.set_caption("TetriZzz 3!")
        janela = pygame.display.set_mode([self.larguraDaJanela, self.alturaDaJanela])
        return janela
    
    def getTextura(self, valor) -> pygame.Surface:
        if valor == idL:
            return self.texturaL
        elif valor == idJ:
            return self.texturaJ
        elif valor == idS:
            return self.texturaS
        elif valor == idZ:
            return self.texturaZ
        elif valor == idT:
            return self.texturaT
        elif valor == idO:
            return self.texturaO
        elif valor == idI:
            return self.texturaI
        elif valor == idVazio:
            return self.texturaVazio
        elif valor == idPecaPosicionada:
            return self.texturaPosicionada
        else:
            raise Exception("Peca não existe")

    def desenharLinhaLimite(self):
        pos1 = (0, limiteParaDerrota*self.alturaDoBloco)
        pos2 = (self.larguraDaJanela, limiteParaDerrota*self.alturaDoBloco)
        pygame.draw.line(self.janela, (255, 0, 0), pos1, pos2, 3)

    def desenharMatrizInteira(self, matriz):
        for y in range(len(matriz)):
            for x in range(len(matriz[0])):
                valor = matriz[y][x]
                self.desenhar(x, y, valor)

    def desenhar(self, x, y, valor):
        textura = self.getTextura(valor)
        xDaTela = x*self.larguraDoBloco
        yDaTela = y*self.alturaDoBloco
        self.janela.blit(textura, (xDaTela, yDaTela))

    def update(self):
        self.desenharLinhaLimite()
        pygame.display.update()

class MecanismoControlador:

    def capturarTeclasPressionadas(self):
        teclas = pygame.key.get_pressed()

        return {
            "w": teclas[pygame.K_w],
            "a": teclas[pygame.K_a],
            "s": teclas[pygame.K_s],
            "d": teclas[pygame.K_d],
            "spc": teclas[pygame.K_SPACE]
        }
    
    def quitEventCheck(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def capturarEventos(self):
        for event in pygame.event.get():
            self.quitEventCheck(event)
            if event.type == pygame.WINDOWFOCUSLOST:
                pause = True
                while pause:
                    for event in pygame.event.get():
                        self.quitEventCheck(event)
                        if event.type == pygame.WINDOWFOCUSGAINED:
                            pause = False
                            break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            self.quitEventCheck(event)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                pause = False
                                break
