from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
    Subphylum,
    Superphylum,
)
from constants import EN, PL

from .cnidaria import CNIDARIA
from .echinodermata import ECHINODERMATA
from .protostomia import PROTOSTOMIA
from .vertebrata import VERTEBRATA

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

# region TUNICATA
C_INTESTINALIS = Genus(
    name="Ciona intestinalis", local_names={EN: "vase tunicate", PL: "przejrzystka"}
)
CIONA = Genus(name="Ciona", children=[C_INTESTINALIS])
CIONIDAE = Family(name="Cionidae", children=[CIONA])
ENTEROGONA = Order(name="Enterogona", children=[CIONIDAE])
ASCIDIACEA = Class(name="Ascidiacea", children=[ENTEROGONA])
TUNICATA = Subphylum(name="Tunicata", children=[ASCIDIACEA])
# endregion TUNICATA

CHORDATA = Phylum(name="Chordata", children=[TUNICATA, VERTEBRATA])

DEUTEROSTOMIA = Superphylum(name="Deuterostomia", children=[ECHINODERMATA, CHORDATA])

NEPHROZOA = Clade(name="Nephrozoa", children=[PROTOSTOMIA, DEUTEROSTOMIA])
PARAHOXOZOA = Clade(name="ParaHoxozoa", children=[CNIDARIA, NEPHROZOA])

ANIMALIA = Kingdom(name="Animalia", children=[PORIFERA, PARAHOXOZOA])
