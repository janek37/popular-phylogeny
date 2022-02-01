from clade import Clade, Family, Genus, Order, Species, Suborder, Superfamily
from constants import EN, LA, PL

T_SCRIPTA = Species(
    name="Trachemys scripta",
    local_names={EN: "pond turtle", PL: "żółw ozdobny"},
    known_for=[
        {
            LA: "Trachemys scripta elegans",
            EN: "red-eared slider",
            PL: "żółw czerwonolicy",
        }
    ],
)
C_VANDENBURGHI = Species(
    name="Chelonoidis vandenburghi",
    local_names={EN: "Alcedo giant tortoise"},
    known_for=[
        {
            EN: "one of the most numerous species of Galápagos tortoise",
            PL: "jeden z najliczniejszych gatunków żółwi słoniowych",
        }
    ],
)
L_OLIVACEA = Species(
    name="Lepidochelys olivacea",
    local_names={EN: "Olive ridley sea turtle", PL: "żółw oliwkowy"},
    known_for=[{EN: "the most common sea turtle"}],
)

C_NIGER = Clade(
    name="Chelonoidis niger complex",
    local_names={EN: "Galápagos tortoise", PL: "żółw z Galapagos, żółw słoniowy"},
    children=[C_VANDENBURGHI],
)  # Species complex

TRACHEMYS = Genus(name="Trachemys", children=[T_SCRIPTA])
CHELONOIDIS = Genus(name="Chelonoidis", children=[C_NIGER])
LEPIDOCHELYS = Genus(name="Lepidochelys", children=[L_OLIVACEA])

EMYDIDAE = Family(name="Emydidae", children=[TRACHEMYS])
TESTUDINIDAE = Family(name="Testudinidae", children=[CHELONOIDIS])
CHELONIIDAE = Family(name="Cheloniidae", children=[LEPIDOCHELYS])

TESTUDINOIDEA = Superfamily(name="Testudinoidea", children=[EMYDIDAE, TESTUDINIDAE])
CHELONIOIDEA = Superfamily(name="Chelonioidea", children=[CHELONIIDAE])

CRYPTODIRA = Suborder(name="Cryptodira", children=[TESTUDINOIDEA, CHELONIOIDEA])

TESTUDINES = Order(name="Testudines", children=[CRYPTODIRA])
