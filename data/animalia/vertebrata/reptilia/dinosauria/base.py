from clade import Clade

from .ornithischia import ORNITHISCHIA

DINOSAURIA = Clade(name="Dinosauria", children=[ORNITHISCHIA])
