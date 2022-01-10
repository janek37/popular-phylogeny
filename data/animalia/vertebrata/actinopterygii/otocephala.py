from clade import Cohort, Family, Genus, Order, Species, Subfamily, Superorder
from constants import EN, PL

from .cypriniformes import CYPRINIFORMES

# region CLUPEIFORMES
C_HARENGUS = Species(
    name="Clupea harengus",
    local_names={
        EN: "Atlantic herring",
        PL: "śledź pospolity, śledź atlantycki, śledź oceaniczny",
    },
)
S_PILCHARDUS = Species(
    name="Sardina pilchardus",
    local_names={EN: "European pilchard", PL: "sardynka europejska"},
    known_for=[{EN: "sardines"}],
)
S_SPRATTUS = Species(
    name="Sprattus sprattus",
    local_names={EN: "European sprat", PL: "szprot, sardynka norweska"},
)
E_ENCRASICOLUS = Species(
    name="Engraulis encrasicolus",
    local_names={EN: "European anchovy", PL: "sardela europejska"},
    known_for=[{EN: "traditional pizza topping"}],
)

CLUPEA = Genus(name="Clupea", children=[C_HARENGUS])
SARDINA = Genus(name="Sardina", children=[S_PILCHARDUS])
SPRATTUS = Genus(name="Sprattus", children=[S_SPRATTUS])
ENGRAULIS = Genus(name="Engraulis", children=[E_ENCRASICOLUS])

CLUPEINAE = Subfamily(name="Clupeinae", children=[CLUPEA, SPRATTUS])
ALOSINAE = Subfamily(name="Alosinae", children=[SARDINA])

CLUPEIDAE = Family(name="Clupeidae", children=[CLUPEINAE, ALOSINAE])
ENGRAULIDAE = Family(name="Engraulidae", children=[ENGRAULIS])

CLUPEIFORMES = Order(name="Clupeiformes", children=[CLUPEIDAE, ENGRAULIDAE])
# endregion CLUPEIFORMES

OSTARIOPHYSI = Superorder(name="Ostariophysi", children=[CYPRINIFORMES])

OTOCEPHALA = Cohort(name="Otocephala", children=[CLUPEIFORMES, OSTARIOPHYSI])
