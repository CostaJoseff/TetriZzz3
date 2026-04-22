from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idL

class L(PecaBase):

    def __init__(self):
        formas = [
            [
                [0, idL, 0  ],
                [0, idL, 0  ],
                [0, idL, idL]
            ],
            [
                [0  , 0  , 0  ],
                [idL, idL, idL],
                [idL, 0  , 0  ],
            ],
            [
                [idL, idL, 0],
                [0  , idL, 0],
                [0  , idL, 0],
            ],
            [
                [0  , 0  , idL],
                [idL, idL, idL],
                [0  , 0  , 0  ],
            ]
        ]
        super().__init__(idL, formas, [3, 3])
        