from clade import Infraorder, Suborder, Superfamily

from .canidae import CANIDAE
from .pinnipedia import PINNIPEDIA
from .ursidae import URSIDAE

CYNOIDEA = Superfamily(name="Cynoidea", children=[CANIDAE])

ARCTOIDEA = Infraorder(name="Arctoidea", children=[URSIDAE, PINNIPEDIA])

CANIFORMIA = Suborder(name="Caniformia", children=[CYNOIDEA, ARCTOIDEA])
