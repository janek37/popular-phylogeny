from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

C_NILOTICUS = Species(
    name="Crocodylus niloticus",
    local_names={EN: "Nile crocodile", PL: "krokodyl nilowy"},
)
C_POROSUS = Species(
    name="Crocodylus porosus",
    local_names={EN: "saltwater crocodile", PL: "krokodyl różańcowy"},
    known_for=[{EN: "the largest living reptile"}],
)
A_MISSISSIPPIENSIS = Species(
    name="Alligator mississippiensis",
    local_names={
        EN: "American alligator, common alligator",
        PL: "aligator amerykański",
    },
)
A_SINENSIS = Species(
    name="Alligator sinensis",
    local_names={EN: "Chinese alligator", PL: "aligator chiński"},
)
G_GANGETICUS = Species(
    name="Gavialis gangeticus",
    local_names={EN: "gharial, gavial", PL: "gawial gangesowy"},
)
C_CROCODILUS = Species(
    name="Caiman crocodilus",
    local_names={
        EN: "spectacled caiman, white caiman, common caiman",
        PL: "kajman krokodylowy, kajman okularowy",
    },
)

CROCODYLUS = Genus(name="Crocodylus", children=[C_NILOTICUS, C_POROSUS])
ALLIGATOR = Genus(name="Alligator", children=[A_MISSISSIPPIENSIS, A_SINENSIS])
GAVIALIS = Genus(name="Gavialis", children=[G_GANGETICUS])
CAIMAN = Genus(name="Caiman", children=[C_CROCODILUS])

CROCODYLIDAE = Family(name="Crocodylidae", children=[CROCODYLUS])
ALLIGATORIDAE = Family(name="Alligatoridae", children=[ALLIGATOR, CAIMAN])
GAVIALIDAE = Family(name="Gavialidae", children=[GAVIALIS])

LONGINOSTRES = Clade(name="Longinostres", children=[CROCODYLIDAE, GAVIALIDAE])

CROCODILIA = Order(name="Crocodilia", children=[LONGINOSTRES, ALLIGATORIDAE])
