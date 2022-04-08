from clade import Clade, Family, Genus, Infraorder, Parvorder, Species, Suborder
from constants import EN, PL

from .odontoceti import ODONTOCETI

H_AMPHIBIUS = Species(
    name="Hippopotamus amphibius",
    local_names={EN: "hippo, common hippopotamus", PL: "hipopotam nilowy"},
)
P_INACHUS = Species(name="Pakicetus inachus", extinct=True)
R_HARUDIENSIS = Species(name="Remingtonocetus harudiensis", extinct=True)
R_KASRANI = Species(name="Rodhocetus kasrani", extinct=True)
D_ATROX = Species(name="Dorudon atrox", extinct=True)
B_CETOIDES = Species(name="Basilosaurus cetoides", extinct=True)
B_MYSTICETUS = Species(
    name="Balaena mysticetus",
    local_names={
        EN: "bowhead whale, Greenland right whale",
        PL: "wieloryb grenlandzki, wal grenlandzki",
    },
)
E_GLACIALIS = Species(
    name="Eubalaena glacialis",
    local_names={EN: "North Atlantic right whale", PL: "waleń biskajski"},
)
B_MUSCULUS = Species(
    name="Balaenoptera musculus",
    local_names={EN: "blue whale", PL: "płetwal błękitny"},
    known_for=[{EN: "the largest animal known to have ever existed"}],
)
M_NOVAEANGLIAE = Species(
    name="Megaptera novaeangliae",
    local_names={EN: "humpback whale", PL: "humbak, długopłetwiec oceaniczny"},
)

HIPPOPOTAMUS = Genus(name="Hippopotamus", children=[H_AMPHIBIUS])
PAKICETUS = Genus(name="Pakicetus", children=[P_INACHUS])
REMINGTONOCETUS = Genus(name="Remingtonocetus", children=[R_HARUDIENSIS])
RODHOCETUS = Genus(name="Rodhocetus", children=[R_KASRANI])
DORUDON = Genus(name="Dorudon", children=[D_ATROX])
BASILOSAURUS = Genus(name="Basilosaurus", children=[B_CETOIDES])
BALAENA = Genus(name="Balaena", children=[B_MYSTICETUS])
EUBALAENA = Genus(name="Eubalaena", children=[E_GLACIALIS])
BALAENOPTERA = Genus(
    name="Balaenoptera", children=[B_MUSCULUS]
)  # currently polyphiletic :(
MEGAPTERA = Genus(name="Megaptera", children=[M_NOVAEANGLIAE])

HIPPOPOTAMIDAE = Family(name="Hippopotamidae", children=[HIPPOPOTAMUS])
PAKICETIDAE = Family(name="Pakicetidae", children=[PAKICETUS])
REMINGTONOCETIDAE = Family(name="Remingtonocetidae", children=[REMINGTONOCETUS])
PROTOCETIDAE = Family(name="Protocetidae", children=[RODHOCETUS])
BASILOSAURIDAE = Family(name="Basilosauridae", children=[DORUDON, BASILOSAURUS])
BALAENIDAE = Family(name="Balaenidae", children=[BALAENA, EUBALAENA])
BALAENOPTERIDAE = Family(name="Balaenopteridae", children=[BALAENOPTERA, MEGAPTERA])

MYSTICETI = Parvorder(name="Mysticeti", children=[BALAENIDAE, BALAENOPTERIDAE])

CETACEA_A = Clade(children=[MYSTICETI, ODONTOCETI])
CETACEA_B = Clade(children=[BASILOSAURIDAE, CETACEA_A])
CETACEA_C = Clade(children=[PROTOCETIDAE, CETACEA_B])
CETACEA_D = Clade(children=[REMINGTONOCETIDAE, CETACEA_C])

CETACEA = Infraorder(name="Cetacea", children=[PAKICETIDAE, CETACEA_D])

WHIPPOMORPHA = Suborder(name="Whippomorpha", children=[HIPPOPOTAMIDAE, CETACEA])
