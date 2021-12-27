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
S_SIPYLUS = Species(
    name="Sipyloidea sipylus",
    local_names={EN: "pink winged stick insect", PL: "patyczak skrzydlaty"},
    known_for=[{EN: "the most widespread walking stick in the world"}],
)

FORFICULA = Genus(name="Forficula", children=[F_AURICULARIA])
MANTIS = Genus(name="Mantis", children=[M_RELIGIOSA])
SIPYLOIDEA = Genus(name="Sipyloidea", children=[S_SIPYLUS])

FORFICULIDAE = Family(name="Forficulidae", children=[FORFICULA])
MANTIDAE = Family(name="Mantidae", children=[MANTIS])
LONCHODIDAE = Family(name="Lonchodidae", children=[SIPYLOIDEA])

DERMAPTERA = Order(name="Dermaptera", children=[FORFICULIDAE])
MANTODEA = Order(name="Mantodea", children=[MANTIDAE])
PHASMATODEA = Order(name="Phasmatodea", children=[LONCHODIDAE])

DICTYOPTERA = Superorder(name="Dictyoptera", children=[MANTODEA, BLATTODEA])

POLYNEOPTERA_B = Clade(children=[DICTYOPTERA, PHASMATODEA])
POLYNEOPTERA_A = Clade(children=[ORTHOPTERA, POLYNEOPTERA_B])

POLYNEOPTERA = Cohort(
    name="Polyneoptera", children=[DERMAPTERA, POLYNEOPTERA_A]
)  # or Subdivision?
