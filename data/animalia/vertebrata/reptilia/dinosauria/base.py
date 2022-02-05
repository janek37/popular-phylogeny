from clade import Clade

from .ornithischia import ORNITHISCHIA
from .sauropoda import SAUROPODA
from .theropoda import THEROPODA

SAURISCHIA = Clade(name="Saurischia", children=[SAUROPODA, THEROPODA])

DINOSAURIA = Clade(name="Dinosauria", children=[ORNITHISCHIA, SAURISCHIA])
