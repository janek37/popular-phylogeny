from clade import Clade, Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL

from .selachimorpha import SELACHIMORPHA

C_MONSTROSA = Species(
    name="Chimaera monstrosa",
    local_names={EN: "rabbit fish, rat fish", PL: "chimera pospolita, przeraza"},
)
D_BATIS = Species(
    name="Dipturus batis",
    local_names={EN: "common skate, blue skate", PL: "raja gładka, płaszczka naga"},
)
B_BREVICAUDATA = Species(
    name="Bathytoshia brevicaudata",
    local_names={EN: "short-tail stingray, smooth stingray"},
    known_for=[
        {EN: "death of Steve Irwin"},
        {EN: "the largest stingray in the world", PL: "największa ogończa świata"},
    ],
)
P_PRISTIS = Species(
    name="Pristis pristis",
    local_names={
        EN: "common sawfish, largetooth sawfish",
        PL: "ryba piła, piła zwyczajna",
    },
)
M_BIROSTRIS = Species(
    name="Mobula birostris",
    local_names={EN: "giant oceanic manta ray", PL: "manta, diabeł morski"},
    known_for=[{EN: "the largest ray", PL: "największa płaszczka"}],
)

CHIMAERA = Genus(name="Chimaera", children=[C_MONSTROSA])
DIPTURUS = Genus(name="Dipturus", children=[D_BATIS])
BATHYTOSHIA = Genus(name="Bathytoshia", children=[B_BREVICAUDATA])
PRISTIS = Genus(name="Pristis", children=[P_PRISTIS])
MOBULA = Genus(name="Mobula", children=[M_BIROSTRIS])

CHIMAERIDAE = Family(name="Chimaeridae", children=[CHIMAERA])
RAJIDAE = Family(name="Rajidae", children=[DIPTURUS])
DASYATIDAE = Family(name="Dasyatidae", children=[BATHYTOSHIA])
PRISTIDAE = Family(name="Pristidae", children=[PRISTIS])
MOBULIDAE = Family(name="Mobulidae", children=[MOBULA])

CHIMAERIFORMES = Order(name="Chimaeriformes", children=[CHIMAERIDAE])
RAJIFORMES = Order(name="Rajiformes", children=[RAJIDAE])
MYLIOBATIFORMES = Order(name="Myliobatiformes", children=[DASYATIDAE, MOBULIDAE])
RHINOPRISTIFORMES = Order(name="Rhinopristiformes", children=[PRISTIDAE])

BATOIDEA_A = Clade(children=[RAJIFORMES, MYLIOBATIFORMES])
BATOIDEA = Superorder(name="Batoidea", children=[BATOIDEA_A, RHINOPRISTIFORMES])

ELASMOBRANCHII = Subclass(name="Elasmobranchii", children=[SELACHIMORPHA, BATOIDEA])

CHONDRICHTHYES = Class(name="Chondrichthyes", children=[CHIMAERIFORMES, ELASMOBRANCHII])
