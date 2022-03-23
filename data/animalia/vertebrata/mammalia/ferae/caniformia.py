from clade import Clade, Infraorder, Suborder, Superfamily

from .canidae import CANIDAE
from .musteloidea import MUSTELOIDEA
from .pinnipedia import PINNIPEDIA
from .ursidae import URSIDAE

CYNOIDEA = Superfamily(name="Cynoidea", children=[CANIDAE])

MUSTELIDA = Clade(name="Mustelida", children=[PINNIPEDIA, MUSTELOIDEA])

ARCTOIDEA = Infraorder(name="Arctoidea", children=[URSIDAE, MUSTELIDA])

CANIFORMIA = Suborder(name="Caniformia", children=[CYNOIDEA, ARCTOIDEA])
