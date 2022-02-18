from clade import Order, Suborder

from .corvides import CORVIDES

PASSERI = Suborder(name="Passeri", children=[CORVIDES])

PASSERIFORMES = Order(name="Passeriformes", children=[PASSERI])
