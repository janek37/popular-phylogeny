from clade import Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL
from image import Image, License

from .decapoda import DECAPODA

O_SCYLLARUS = Species(
    name="Odontodactylus scyllarus",
    local_names={EN: "peacock mantis shrimp", PL: "rawka błazen"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Peacock_mantis_shrimp_(Odontodactylus_scyllarus)_(16245381575).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/61/Peacock_mantis_shrimp_%28Odontodactylus_scyllarus%29_%2816245381575%29.jpg",
        author="Rickard Zerpe",
        license=License.CC_BY_2_0,
    ),
)
E_SUPERBA = Species(
    name="Euphausia superba",
    local_names={EN: "Antarctic krill", PL: "kryl antarktyczny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Antarctic_krill_(Euphausia_superba).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Antarctic_krill_%28Euphausia_superba%29.jpg",
        author="Uwe Kils",
        license=License.CC_BY_SA_3_0,
    ),
)
O_ASELLUS = Species(
    name="Oniscus asellus",
    local_names={EN: "common woodlouse", PL: "stonoga murowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oniscus_asellus_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/97/Oniscus_asellus_01.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
T_SALTATOR = Species(
    name="Talitrus saltator",
    local_names={EN: "common sand hopper", PL: "zmieraczek plażowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Talitrus_saltator_2c.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f2/Talitrus_saltator_2c.jpg",
        author="Arnold Paul / edited by Waugsberg and Buchling",
        license=License.CC_BY_SA_2_0_DE,
    ),
)

ODONTODACTYLUS = Genus(name="Odontodactylus", children=[O_SCYLLARUS])
EUPHASIA = Genus(name="Euphasia", children=[E_SUPERBA])
ONISCUS = Genus(name="Oniscus", children=[O_ASELLUS])
TALITRUS = Genus(name="Talitrus", children=[T_SALTATOR])

ODONTODACTYLIDAE = Family(name="Odontodactylidae", children=[ODONTODACTYLUS])
EUPHAUSIIDAE = Family(name="Euphausiidae", children=[EUPHASIA])
ONISCIDAE = Family(name="Oniscidae", children=[ONISCUS])
TALITRIDAE = Family(name="Talitridae", children=[TALITRUS])

STOMATOPODA = Order(name="Stomatopoda", children=[ODONTODACTYLIDAE])
EUPHAUSIACEA = Order(name="Euphausiacea", children=[EUPHAUSIIDAE])
ISOPODA = Order(name="Isopoda", children=[ONISCIDAE])
AMPHIPODA = Order(name="Amphipoda", children=[TALITRIDAE])

EUCARIDA = Superorder(name="Eucarida", children=[EUPHAUSIACEA, DECAPODA])
PERACARIDA = Superorder(name="Peracarida", children=[ISOPODA, AMPHIPODA])

HOPLOCARIDA = Subclass(name="Hoplocarida", children=[STOMATOPODA])
EUMALACOSTRACA = Subclass(name="Eumalacostraca", children=[EUCARIDA, PERACARIDA])

MALACOSTRACA = Class(name="Malacostraca", children=[HOPLOCARIDA, EUMALACOSTRACA])
