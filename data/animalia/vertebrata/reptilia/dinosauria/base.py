from clade import Clade

from .ornithischia import ORNITHISCHIA
from .sauropoda import SAUROPODA

SAURISCHIA = Clade(name="Saurischia", children=[SAUROPODA])

DINOSAURIA = Clade(name="Dinosauria", children=[ORNITHISCHIA, SAURISCHIA])
