from clade import Clade

from .accipitrimorphae import ACCIPITRIMORPHAE
from .coraciimorphae import CORACIIMORPHAE
from .strigiformes import STRIGIFORMES

TELLURAVES = Clade(
    name="Telluraves", children=[ACCIPITRIMORPHAE, STRIGIFORMES, CORACIIMORPHAE]
)
