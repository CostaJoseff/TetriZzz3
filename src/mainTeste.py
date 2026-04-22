# from objetosDoJogo.tabuleiro import Tabuleiro
# import time


# while True:
#     tab = Tabuleiro()

#     try:
#         while True:
#             tab.executarAcao()
#     except KeyboardInterrupt:
#         exit()
#     except: ""


from IA.memoria import MemoriaConsequencial
from pprint import pprint as print

mem = MemoriaConsequencial()

while True:
    cons, acao, causa = input("SALVAR cons-acao-causa ").split("-")

    mem.salvar(causa, acao, cons)
    print(mem.jsonDataset)

    cons = input("GET CAUSA... cons ")
    print(mem.obterCausa(cons))

    causa = input("GET CONS... causa ")
    print(mem.obterConseguencias(causa))