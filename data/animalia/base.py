from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
    Superphylum,
)
from constants import EN

from .cnidaria import CNIDARIA
from .echinodermata import ECHINODERMATA
from .protostomia import PROTOSTOMIA

# region PORIFERA
A_FISTULARIS = Species(
    name="Aplysina fistularis",
    local_names={EN: "yellow sponge"},
    known_for=[{EN: "SpongeBob SquarePants"}],
)
APLYSINA = Genus(name="Aplysina", children=[A_FISTULARIS])
APLYSINIDAE = Family(name="Aplysinidae", children=[APLYSINA])
VERONGIDA = Order(name="Verongida", children=[APLYSINIDAE])
DEMOSPONGIAE = Class(name="Demospongiae", children=[VERONGIDA])
PORIFERA = Phylum(name="Porifera", children=[DEMOSPONGIAE])
# endregion PORIFERA

DEUTEROSTOMIA = Superphylum(name="Deuterostomia", children=[ECHINODERMATA])

NEPHROZOA = Clade(name="Nephrozoa", children=[PROTOSTOMIA, DEUTEROSTOMIA])
PARAHOXOZOA = Clade(name="ParaHoxozoa", children=[CNIDARIA, NEPHROZOA])

ANIMALIA = Kingdom(name="Animalia", children=[PORIFERA, PARAHOXOZOA])
