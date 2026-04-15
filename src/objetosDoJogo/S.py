from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idS

class S(PecaBase):

    def __init__(self):
        formas = [
            [
                [0  , idS, idS],
                [idS, idS, 0  ],
                [0  , 0  , 0  ]
            ],
            [
                [0, idS, 0  ],
                [0, idS, idS],
                [0, 0  , idS]
            ],
        ]
        super.__init__(idS, formas)