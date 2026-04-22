class MemoriaConsequencial:

    def __init__(self):
        # {
        #     "consequencia": [
        #         {
        #            "causa": [[]] <- tabuleiro,
        #            "acao": 0.5 <- valor predito pelo modelo
        #         }
        #     ]
        # }
        self.jsonDataset = {}

    def obterCausa(self, consequenciaAlvo) -> dict:
        return self.jsonDataset.get(consequenciaAlvo, {})
    
    def obterConseguencias(self, causaAlvo) -> list:
        consequencias = set()
        for consequencia, causas in self.jsonDataset.items():
            for causaAcao in causas:
                if causaAcao["causa"] == causaAlvo:
                    consequencias.add(consequencia)
        
        return consequencias
    
    def salvar(self, causa, acao, consequencia):
        novoDado = {
            "causa": causa,
            "acao": acao
        }
        if self.jsonDataset.get(consequencia):
            if novoDado in self.jsonDataset[consequencia]:
                return
            self.jsonDataset[consequencia].append(novoDado)

        else:
            self.jsonDataset[consequencia] = [novoDado]

    def dadosParaTreino(self) -> list[list]:
        dataset = [[]] # [[causa, consequencia]]
        for consequencia, causas in self.jsonDataset.items():
            for causaAcao in causas:
                dataset.append([causaAcao["causa"], consequencia])

        return dataset
        