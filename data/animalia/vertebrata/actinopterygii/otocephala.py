from clade import (
    Clade,
    Cohort,
    Family,
    Genus,
    Order,
    Species,
    Subcohort,
    Subfamily,
    Superorder,
)
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

# region SILURIPHYSAE
A_ALBIFRONS = Species(
    name="Apteronotus albifrons",
    local_names={EN: "black ghost knifefish", PL: "duch brazylijski"},
)
E_ELECTRICUS = Species(
    name="Electrophorus electricus",
    local_names={EN: "electric eel", PL: "węgorz elektryczny, strętwa"},
)
P_BOCOURTI = Species(
    name="Pangasius bocourti", local_names={EN: "basa, river cobbler", PL: "panga"}
)
S_GLANIS = Species(
    name="Silurus glanis",
    local_names={EN: "wels catfish, sheatfish", PL: "sum pospolity"},
)
A_NEBULOSUS = Species(
    name="Ameiurus nebulosus",
    local_names={EN: "brown bullhead", PL: "byczek, amerykański sumik karłowaty"},
)

APTERONOTUS = Genus(name="Apteronotus", children=[A_ALBIFRONS])
ELECTROPHORUS = Genus(name="Electrophorus", children=[E_ELECTRICUS])
PANGASIUS = Genus(name="Pangasius", children=[P_BOCOURTI])
SILURUS = Genus(name="Silurus", children=[S_GLANIS])
AMEIURUS = Genus(name="Ameiurus", children=[A_NEBULOSUS])

APTERONOTIDAE = Family(name="Apteronotidae", children=[APTERONOTUS])
GYMNOTIDAE = Family(name="Gymnotidae", children=[ELECTROPHORUS])
PANGASIIDAE = Family(name="Pangasiidae", children=[PANGASIUS])
SILURIDAE = Family(name="Siluridae", children=[SILURUS])
ICTALURIDAE = Family(name="Ictaluridae", children=[AMEIURUS])

SILURIFORMES_A = Clade(children=[PANGASIIDAE, ICTALURIDAE])

GYMNOTIFORMES = Order(name="Gymnotiformes", children=[APTERONOTIDAE, GYMNOTIDAE])
SILURIFORMES = Order(name="Siluriformes", children=[SILURIFORMES_A, SILURIDAE])

SILURIPHYSAE = Superorder(name="Siluriphysae", children=[GYMNOTIFORMES, SILURIFORMES])
# endregion SILURIPHYSAE

OSTARIOPHYSI_A = Clade(children=[CHARACIFORMES, SILURIPHYSAE])
OSTARIOPHYSI = Subcohort(name="Ostariophysi", children=[CYPRINIFORMES, OSTARIOPHYSI_A])

OTOCEPHALA = Cohort(name="Otocephala", children=[CLUPEIFORMES, OSTARIOPHYSI])
