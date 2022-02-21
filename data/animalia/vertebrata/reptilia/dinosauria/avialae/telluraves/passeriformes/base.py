from clade import Infraorder, Order, Suborder

from .corvides import CORVIDES
from .muscicapida import MUSCICAPIDA
from .sylviida import SYLVIIDA

PASSERIDES = Infraorder(name="Passerides", children=[SYLVIIDA, MUSCICAPIDA])

PASSERI = Suborder(name="Passeri", children=[CORVIDES, PASSERIDES])

PASSERIFORMES = Order(name="Passeriformes", children=[PASSERI])
