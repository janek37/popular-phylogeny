from clade import Clade, Family, Genus, Order, Species, Superorder
from constants import EN, PL

C_CARCHARIAS = Species(
    name="Carcharodon carcharias",
    local_names={EN: "great white shark", PL: "żarłacz biały, rekin ludojad"},
    known_for=[{EN: "Jaws"}],
)
S_ZYGAENA = Species(
    name="Sphyrna zygaena",
    local_names={EN: "smooth hammerhead", PL: "rekin młot, głowomłot pospolity"},
)
R_TYPUS = Species(
    name="Rhincodon typus",
    local_names={EN: "whale shark", PL: "rekin wielorybi"},
    known_for=[{EN: "the largest living nonmammalian vertebrate"}],
)
G_CUVIER = Species(
    name="Galeocerdo cuvier", local_names={EN: "tiger shark", PL: "żarłacz tygrysi"}
)
O_MEGALODON = Species(
    name="Otodus megalodon",
    local_names={EN: "megalodon"},
    known_for=[{EN: "giant extinct shark"}],
    extinct=True,
)
S_ACANTHIAS = Species(
    name="Squalus acanthias", local_names={EN: "spiny dogfish", PL: "koleń pospolity"}
)
S_SQUATINA = Species(
    name="Squatina squatina",
    local_names={EN: "angelshark, monkfish", PL: "raszpla zwyczajna"},
)

CARCHARODON = Genus(name="Carcharodon", children=[C_CARCHARIAS])
SPHYRNA = Genus(name="Sphyrna", children=[S_ZYGAENA])
RHINCODON = Genus(name="Rhincodon", children=[R_TYPUS])
GALEOCERDO = Genus(name="Galeocerdo", children=[G_CUVIER])
OTODUS = Genus(name="Otodus", children=[O_MEGALODON])
SQUALUS = Genus(name="Squalus", children=[S_ACANTHIAS])
SQUATINA = Genus(name="Squatina", children=[S_SQUATINA])

LAMNIDAE = Family(name="Lamnidae", children=[CARCHARODON])
SPHYRNIDAE = Family(name="Sphyrnidae", children=[SPHYRNA])
RHINCODONTIDAE = Family(name="Rhincodontidae", children=[RHINCODON])
CARCHARHINIDAE = Family(name="Carcharhinidae", children=[GALEOCERDO])
OTODONTIDAE = Family(name="Otodontidae", children=[OTODUS])
SQUALIDAE = Family(name="Squalidae", children=[SQUALUS])
SQUATINIDAE = Family(name="Squatinidae", children=[SQUATINA])

LAMNIFORMES = Order(name="Lamniformes", children=[LAMNIDAE, OTODONTIDAE])
CARCHARHINIFORMES = Order(
    name="Carcharhiniformes", children=[SPHYRNIDAE, CARCHARHINIDAE]
)
ORECTOLOBIFORMES = Order(name="Orectolobiformes", children=[RHINCODONTIDAE])
SQUALIFORMES = Order(name="Squaliformes", children=[SQUALIDAE])
SQUATINIFORMES = Order(name="Squatiniformes", children=[SQUATINIDAE])

SELACHIMORPHA_A = Clade(children=[LAMNIFORMES, CARCHARHINIFORMES])
SELACHIMORPHA_B = Clade(children=[SELACHIMORPHA_A, ORECTOLOBIFORMES])
SELACHIMORPHA_C = Clade(children=[SQUALIFORMES, SQUATINIFORMES])
SELACHIMORPHA = Superorder(
    name="Selachimorpha", children=[SELACHIMORPHA_B, SELACHIMORPHA_C]
)
