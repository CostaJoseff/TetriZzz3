from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idI

class I(PecaBase):
    
    def __init__(self):
        formas = [
            [
                [0, idI, 0, 0],
                [0, idI, 0, 0],
                [0, idI, 0, 0],
                [0, idI, 0, 0]
            ],
            [
                [0  , 0  , 0  , 0  ],
                [idI, idI, idI, idI],
                [0  , 0  , 0  , 0  ],
                [0  , 0  , 0  , 0  ]
            ],
        ]
        super.__init__(idI, formas)