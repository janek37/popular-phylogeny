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

# region CHARACIFORMES
P_INNESI = Species(
    name="Paracheirodon innesi",
    local_names={EN: "neon tetra", PL: "bystrzyk neonowy, neon Innesa"},
)
P_NATTERERI = Species(
    name="Pygocentrus nattereri",
    local_names={
        EN: "red-bellied piranha, red piranha",
        PL: "pirania czarnoogonowa, pirania czerwona, pirania Natterera",
    },
)

PARACHEIRODON = Genus(name="Paracheirodon", children=[P_INNESI])
PYGOCENTRUS = Genus(name="Pygocentrus", children=[P_NATTERERI])

CHARACIDAE = Family(name="Characidae", children=[PARACHEIRODON])
SERRASALMIDAE = Family(name="Serrasalmidae", children=[PYGOCENTRUS])

CHARACIFORMES = Order(name="Characiformes", children=[CHARACIDAE, SERRASALMIDAE])
# endregion CHARACIFORMES

OSTARIOPHYSI = Superorder(name="Ostariophysi", children=[CYPRINIFORMES, CHARACIFORMES])

OTOCEPHALA = Cohort(name="Otocephala", children=[CLUPEIFORMES, OSTARIOPHYSI])
