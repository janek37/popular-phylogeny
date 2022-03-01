from clade import Family, Genus, Order, Species, Suborder, Superorder
from constants import EN, PL

D_NOVEMCINCTUS = Species(
    name="Dasypus novemcinctus",
    local_names={
        EN: "nine-banded armadillo",
        PL: "pancernik długoogonowy, pancernik dziewięciopaskowy",
    },
)
M_TRIDACTYLA = Species(
    name="Myrmecophaga tridactyla",
    local_names={EN: "giant anteater, ant bear", PL: "mrówkojad wielki"},
)
M_AMERICANUM = Species(
    name="Megatherium americanum",
    local_names={EN: "giant ground sloth, megathere"},
    known_for=[{EN: "one of the largest land mammals"}],
    extinct=True,
)
B_VARIEGATUS = Species(
    name="Bradypus variegatus",
    local_names={EN: "brown-throated sloth", PL: "leniwiec pstry"},
)

DASYPUS = Genus(name="Dasypus", children=[D_NOVEMCINCTUS])
MYRMECOPHAGA = Genus(name="Myrmecophaga", children=[M_TRIDACTYLA])
MEGATHERIUM = Genus(name="Megatherium", children=[M_AMERICANUM])
BRADYPUS = Genus(name="Bradypus", children=[B_VARIEGATUS])

DASYPODIDAE = Family(name="Dasypodidae", children=[DASYPUS])
MYRMECOPHAGIDAE = Family(name="Myrmecophagidae", children=[MYRMECOPHAGA])
MEGATHERIIDAE = Family(name="Megatheriidae", children=[MEGATHERIUM])
BRADYPODIDAE = Family(name="Bradypodidae", children=[BRADYPUS])

VERMILINGUA = Suborder(name="Vermilingua", children=[MYRMECOPHAGIDAE])
FOLIVORA = Suborder(name="Folivora", children=[MEGATHERIIDAE, BRADYPODIDAE])

CINGULATA = Order(name="Cingulata", children=[DASYPODIDAE])
PILOSA = Order(name="Pilosa", children=[VERMILINGUA, FOLIVORA])

XENARTHRA = Superorder(name="Xenarthra", children=[CINGULATA, PILOSA])
