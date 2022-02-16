from clade import Clade

from .accipitrimorphae import ACCIPITRIMORPHAE
from .coraciimorphae import CORACIIMORPHAE
from .falconiformes import FALCONIFORMES
from .strigiformes import STRIGIFORMES

AUSTRALAVES = Clade(name="Australaves", children=[FALCONIFORMES])

TELLURAVES = Clade(
    name="Telluraves",
    children=[ACCIPITRIMORPHAE, STRIGIFORMES, CORACIIMORPHAE, AUSTRALAVES],
)
