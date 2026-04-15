from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idO

class O(PecaBase):

    def __init__(self):
        formas = [
            [idO, idO],
            [idO, idO]
        ]
        super.__init__(idO, formas)