from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idZ

class Z(PecaBase):

    def __init__(self):
        formas = [
            [
                [idZ, idZ, 0  ],
                [0  , idZ, idZ],
                [0  , 0  , 0  ]
            ],
            [
                [0, 0  , idZ],
                [0, idZ, idZ],
                [0, idZ, 0  ]
            ],
        ]
        super.__init__(idZ, formas, [3, 3])