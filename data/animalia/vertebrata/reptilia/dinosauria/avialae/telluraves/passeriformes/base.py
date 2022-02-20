from clade import Infraorder, Order, Suborder

from .corvides import CORVIDES
from .sylviida import SYLVIIDA

PASSERIDES = Infraorder(name="Passerides", children=[SYLVIIDA])

PASSERI = Suborder(name="Passeri", children=[CORVIDES, PASSERIDES])

PASSERIFORMES = Order(name="Passeriformes", children=[PASSERI])
