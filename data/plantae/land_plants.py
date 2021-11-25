from clade import Clade, Class, Family, Genus, Order, Phylum, Species
from constants import EN, PL

from .angiospermae import ANGIOSPERMAE
from .gymnospermae import GYMNOSPERMAE

P_COMMUNE = Species(
    name="Polytrichum commune",
    local_names={EN: "common haircap moss", PL: "płonnik pospolity"},
    known_for=[{EN: "one of the most common mosses"}],
)
L_GLAUCUM = Species(
    name="Leucobryum glaucum",
    local_names={EN: "pin cusion moss", PL: "bielistka siwa"},
    known_for=[{EN: "one of the most common mosses"}],
)
P_AQUILINUM = Species(
    name="Pteridium aquilinum",
    local_names={EN: "common bracken, eagle fern", PL: "orlica pospolita"},
    known_for=[{EN: "one of the most common ferns"}],
)
A_AUSTRALIS = Species(name="Alsophila australis", local_names={EN: "rough tree fern"})
M_QUADRIFOLIA = Species(
    name="Marsilea quadrifolia",
    local_names={EN: "four leaf clover", PL: "marsylia czterolistna"},
)

POLYTRICHUM = Genus(name="Polytrichum", children=[P_COMMUNE])
LEUCOBRYUM = Genus(name="Leucobryum", children=[L_GLAUCUM])
PTERIDIUM = Genus(name="Pteridium", children=[P_AQUILINUM])
ALSOPHILA = Genus(name="Alsophila", children=[A_AUSTRALIS])
MARSILEA = Genus(name="Marsilea", children=[M_QUADRIFOLIA])

POLYTRICHACEAE = Family(name="Polytrichaceae", children=[POLYTRICHUM])
LEUCOBRYACEAE = Family(name="Leucobryaceae", children=[LEUCOBRYUM])
DENNSTAEDTIACEAE = Family(name="Dennstaedtiaceae", children=[PTERIDIUM])
CYATHEACEAE = Family(name="Cyatheaceae", children=[ALSOPHILA])
MARSILEACEAE = Family(name="Marsileaceae", children=[MARSILEA])

POLYTRICHALES = Order(name="Polytrichales", children=[POLYTRICHACEAE])
DICRANALES = Order(name="Dicranales", children=[LEUCOBRYACEAE])
POLYPODIALES = Order(name="Polypodiales", children=[DENNSTAEDTIACEAE])
CYATHEALES = Order(name="Cyatheales", children=[CYATHEACEAE])
SALVINIALES = Order(name="Salviniales", children=[MARSILEACEAE])

POLYPODIALES_CYATHEALES = Clade(children=[POLYPODIALES, CYATHEALES])

POLYTRICHOPSIDA = Class(name="Polytrichopsida", children=[POLYTRICHALES])
BRYOPSIDA = Class(name="Bryopsida", children=[DICRANALES])
POLYPODIOPSIDA = Class(
    name="Polypodiopsida", children=[POLYPODIALES_CYATHEALES, SALVINIALES]
)

BRYOPHYTA = Phylum(name="Bryophyta", children=[POLYTRICHOPSIDA, BRYOPSIDA])
POLYPODIOPHYTA = Phylum(name="Polypodiophyta", children=[POLYPODIOPSIDA])

SPERMATOPHYTES = Clade(name="Spermatophyta", children=[GYMNOSPERMAE, ANGIOSPERMAE])
TRACHEOPHYTES = Clade(name="Tracheophytes", children=[POLYPODIOPHYTA, SPERMATOPHYTES])

EMBRYOPHYTA = Clade(name="Embryophyta", children=[BRYOPHYTA, TRACHEOPHYTES])
