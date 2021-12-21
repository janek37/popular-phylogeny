from clade import Cohort, Family, Genus, Order, Species
from constants import EN, PL

F_AURICULARIA = Species(
    name="Forficula auricularia",
    local_names={EN: "common earwig", PL: "skorek pospolity"},
)

FORFICULA = Genus(name="Forficula", children=[F_AURICULARIA])

FORFICULIDAE = Family(name="Forficulidae", children=[FORFICULA])

DERMAPTERA = Order(name="Dermaptera", children=[FORFICULIDAE])

POLYNEOPTERA = Cohort(name="Polyneoptera", children=[DERMAPTERA])  # or Subdivision?
