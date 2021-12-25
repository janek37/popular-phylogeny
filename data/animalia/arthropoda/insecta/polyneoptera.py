from clade import Clade, Cohort, Family, Genus, Order, Species, Superorder
from constants import EN, PL

from .blattodea import BLATTODEA
from .orthoptera import ORTHOPTERA

F_AURICULARIA = Species(
    name="Forficula auricularia",
    local_names={EN: "common earwig", PL: "skorek pospolity"},
)
M_RELIGIOSA = Species(
    name="Mantis religiosa",
    local_names={EN: "praying mantis, European mantis", PL: "modliszka zwyczajna"},
)

FORFICULA = Genus(name="Forficula", children=[F_AURICULARIA])
MANTIS = Genus(name="Mantis", children=[M_RELIGIOSA])

FORFICULIDAE = Family(name="Forficulidae", children=[FORFICULA])
MANTIDAE = Family(name="Mantidae", children=[MANTIS])

DERMAPTERA = Order(name="Dermaptera", children=[FORFICULIDAE])
MANTODEA = Order(name="Mantodea", children=[MANTIDAE])

DICTYOPTERA = Superorder(name="Dictyoptera", children=[MANTODEA, BLATTODEA])

POLYNEOPTERA_A = Clade(children=[ORTHOPTERA, DICTYOPTERA])

POLYNEOPTERA = Cohort(
    name="Polyneoptera", children=[DERMAPTERA, POLYNEOPTERA_A]
)  # or Subdivision?
