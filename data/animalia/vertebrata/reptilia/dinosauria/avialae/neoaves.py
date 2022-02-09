from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .columbiformes import COLUMBIFORMES

P_RUBER = Species(
    name="Phoenicopterus ruber",
    local_names={EN: "American flamingo", PL: "flaming karmazynowy"},
)
P_CRISTATUS = Species(
    name="Podiceps cristatus",
    local_names={EN: "great-crested grabe", PL: "perkoz dwuczuby"},
)

PHOENICOPTERUS = Genus(name="Phoenicopterus", children=[P_RUBER])
PODICEPS = Genus(name="Podiceps", children=[P_CRISTATUS])

PHOENICOPTERIDAE = Family(name="Phoenicopteridae", children=[PHOENICOPTERUS])
PODICIPEDIDAE = Family(name="Podicipedidae", children=[PODICEPS])

PHOENICOPTERIFORMES = Order(name="Phoenicopteriformes", children=[PHOENICOPTERIDAE])
PODICIPEDIFORMES = Order(name="Podicipediformes", children=[PODICIPEDIDAE])

MIRANDORNITHES = Clade(
    name="Mirandornithes", children=[PHOENICOPTERIFORMES, PODICIPEDIFORMES]
)

NEOAVES = Clade(name="Neoaves", children=[MIRANDORNITHES, COLUMBIFORMES])
