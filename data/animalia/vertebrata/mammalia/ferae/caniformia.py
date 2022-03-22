from clade import Suborder, Superfamily

from .canidae import CANIDAE

CYNOIDEA = Superfamily(name="Cynoidea", children=[CANIDAE])

CANIFORMIA = Suborder(name="Caniformia", children=[CYNOIDEA])
