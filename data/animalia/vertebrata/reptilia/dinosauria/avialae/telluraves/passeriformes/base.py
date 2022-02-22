from clade import Clade, Infraorder, Order, Suborder

from .corvides import CORVIDES
from .muscicapida import MUSCICAPIDA
from .passerida import PASSERIDA
from .sylviida import SYLVIIDA

PASSERIDES_A = Clade(children=[MUSCICAPIDA, PASSERIDA])

PASSERIDES = Infraorder(name="Passerides", children=[SYLVIIDA, PASSERIDES_A])

PASSERI = Suborder(name="Passeri", children=[CORVIDES, PASSERIDES])

PASSERIFORMES = Order(name="Passeriformes", children=[PASSERI])
