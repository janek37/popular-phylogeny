from clade import Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL

from .decapoda import DECAPODA

O_SCYLLARUS = Species(
    name="Odontodactylus scyllarus",
    local_names={EN: "peacock mantis shrimp", PL: "rawka błazen"},
)
E_SUPERBA = Species(
    name="Euphausia superba",
    local_names={EN: "Antarctic krill", PL: "kryl antarktyczny"},
)
B_GIGANTEUS = Species(
    name="Bathynomus giganteus",
    local_names={EN: "giant isopod"},
    known_for=[{EN: "the largest peracarid", PL: "największy torborak"}],
)
O_ASELLUS = Species(
    name="Oniscus asellus", local_names={EN: "common woodlouse", PL: "stonoga murowa"}
)

ODONTODACTYLUS = Genus(name="Odontodactylus", children=[O_SCYLLARUS])
EUPHASIA = Genus(name="Euphasia", children=[E_SUPERBA])
BATHYNOMUS = Genus(name="Bathynomus", children=[B_GIGANTEUS])
ONISCUS = Genus(name="Oniscus", children=[O_ASELLUS])

ODONTODACTYLIDAE = Family(name="Odontodactylidae", children=[ODONTODACTYLUS])
EUPHAUSIIDAE = Family(name="Euphausiidae", children=[EUPHASIA])
CIROLANIDAE = Family(name="Cirolanidae", children=[BATHYNOMUS])
ONISCIDAE = Family(name="Oniscidae", children=[ONISCUS])

STOMATOPODA = Order(name="Stomatopoda", children=[ODONTODACTYLIDAE])
EUPHAUSIACEA = Order(name="Euphausiacea", children=[EUPHAUSIIDAE])
ISOPODA = Order(name="Isopoda", children=[CIROLANIDAE, ONISCIDAE])

EUCARIDA = Superorder(name="Eucarida", children=[EUPHAUSIACEA, DECAPODA])
PERACARIDA = Superorder(name="Peracarida", children=[ISOPODA])

HOPLOCARIDA = Subclass(name="Hoplocarida", children=[STOMATOPODA])
EUMALACOSTRACA = Subclass(name="Eumalacostraca", children=[EUCARIDA, PERACARIDA])

MALACOSTRACA = Class(name="Malacostraca", children=[HOPLOCARIDA, EUMALACOSTRACA])
