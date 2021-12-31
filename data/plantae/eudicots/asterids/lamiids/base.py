from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL

from .lamiales import LAMIALES
from .solanales import SOLANALES

M_SYLVATICA = Species(
    name="Myosotis sylvatica",
    local_names={EN: "forget-me-not", PL: "niezapominajka leśna"},
)
S_OFFICINALE = Species(
    name="Symphytum officinale",
    local_names={EN: "common comfrey", PL: "żywokost lekarski"},
)
B_OFFICINALIS = Species(
    name="Borago officinalis",
    local_names={EN: "borage, starflower", PL: "ogórecznik lekarski"},
)
C_ARABICA = Species(
    name="Coffea arabica", local_names={EN: "Arabian coffee", PL: "kawa arabska"}
)
C_CANEPHORA = Species(
    name="Coffea canephora",
    local_names={EN: "robusta coffee", PL: "robusta, kawa kongijska"},
)
C_OFFICINALIS = Species(
    name="Cinchona officinalis",
    local_names={PL: "chinowiec lekarski"},
    known_for=[{PL: "chinina", EN: "quinine"}],
)
S_NUX_VOMICA = Species(
    name="Strychnos nux-vomica",
    local_names={PL: "kulczyba wronie oko", EN: "strychnine tree"},
    known_for=[{EN: "strychnine", PL: "strychnina"}],
)

MYOSOTIS = Genus(name="Myosotis", children=[M_SYLVATICA])
SYMPHYTUM = Genus(name="Symphytum", children=[S_OFFICINALE])
BORAGO = Genus(name="Borago", children=[B_OFFICINALIS])
COFFEA = Genus(name="Coffea", children=[C_ARABICA, C_CANEPHORA])
CINCHONA = Genus(name="Cinchona", children=[C_OFFICINALIS])
STRYCHNOS = Genus(name="Strychnos", children=[S_NUX_VOMICA])

ERITRICHIEAE = Tribe(name="Eritrichieae", children=[MYOSOTIS])
BORAGINEAE = Tribe(name="Boragineae", children=[SYMPHYTUM, BORAGO])

BORAGINACEAE = Family(name="Boraginaceae", children=[ERITRICHIEAE, BORAGINEAE])
RUBIACEAE = Family(name="Rubiaceae", children=[COFFEA, CINCHONA])
LOGANIACEAE = Family(name="Loganiaceae", children=[STRYCHNOS])

BORAGINALES = Order(name="Boraginales", children=[BORAGINACEAE])
GENTIANALES = Order(name="Gentianales", children=[RUBIACEAE, LOGANIACEAE])

# Boraginales and Lamiales may be sisters, but the evidence is weak so far
LAMIIDS = Clade(
    name="lamiids", children=[BORAGINALES, GENTIANALES, LAMIALES, SOLANALES]
)
