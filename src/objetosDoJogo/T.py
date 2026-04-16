from objetosDoJogo.base import PecaBase
from objetosDoJogo.idList import idT

class T(PecaBase):
    formas = [
        [
            [0  , idT, 0  ],
            [idT, idT, idT],
            [0  , 0  , 0  ]
        ],
        [
            [0, idT, 0  ],
            [0, idT, idT],
            [0, idT, 0  ]
        ],
        [
            [0  , 0  , 0  ],
            [idT, idT, idT],
            [0  , idT, 0  ]
        ],
        [
            [0  , idT, 0],
            [idT, idT, 0],
            [0  , idT, 0]
        ],
    ]
    super.__init__(idT, formas, [3, 3])