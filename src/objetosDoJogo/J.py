from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idJ

class J(PecaBase):

    def __init__(self):
        formas = [
            [
                [0, 0  , idJ, 0],
                [0, 0  , idJ, 0],
                [0, 0  , idJ, 0],
                [0, idJ, idJ, 0],
            ],
            [
                [0  , 0  , 0  , 0  ],
                [idJ, 0  , 0  , 0  ],
                [idJ, idJ, idJ, idJ],
                [0  , 0  , 0  , 0  ],
            ],
            [
                [0, idJ, idJ, 0],
                [0, idJ, 0  , 0],
                [0, idJ, 0  , 0],
                [0, idJ, 0  , 0],
            ],
            [
                [0  , 0  , 0  , 0  ],
                [idJ, idJ, idJ, idJ],
                [0  , 0  , 0  , idJ],
                [0  , 0  , 0  , 0  ],
            ]
        ]
        super.__init__(idJ, formas, [4, 4])