from clade import Clade

from .accipitrimorphae import ACCIPITRIMORPHAE
from .strigiformes import STRIGIFORMES

TELLURAVES = Clade(name="Telluraves", children=[ACCIPITRIMORPHAE, STRIGIFORMES])
