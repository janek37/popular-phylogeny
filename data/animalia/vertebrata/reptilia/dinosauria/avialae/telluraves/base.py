from clade import Clade

from .accipitrimorphae import ACCIPITRIMORPHAE
from .coraciimorphae import CORACIIMORPHAE
from .falconiformes import FALCONIFORMES
from .psittaciformes import PSITTACIFORMES
from .strigiformes import STRIGIFORMES

PSITTACOPASSERAE = Clade(name="Psittacopasserae", children=[PSITTACIFORMES])

AUSTRALAVES = Clade(name="Australaves", children=[FALCONIFORMES, PSITTACOPASSERAE])

TELLURAVES = Clade(
    name="Telluraves",
    children=[ACCIPITRIMORPHAE, STRIGIFORMES, CORACIIMORPHAE, AUSTRALAVES],
)
