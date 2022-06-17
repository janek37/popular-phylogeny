from clade import Clade, Family, Genus, Infraorder, Parvorder, Species, Suborder
from constants import EN, PL
from image import Image, License

from .odontoceti import ODONTOCETI

H_AMPHIBIUS = Species(
    name="Hippopotamus amphibius",
    local_names={EN: "hippo, common hippopotamus", PL: "hipopotam nilowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hippopotamus-2780699_1280.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/43/Hippopotamus-2780699_1280.png",
        author="Capri23auto",
        license=License.CC0,
    ),
)
P_INACHUS = Species(
    name="Pakicetus inachus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pakicetus_inachus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Pakicetus_inachus.jpg",
        author="Zerosmany",
        license=License.CC_BY_SA_4_0,
    ),
)
R_HARUDIENSIS = Species(
    name="Remingtonocetus harudiensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Remingtonocetus_BW.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Remingtonocetus_BW.jpg",
        author="Nobu Tamura (http://spinops.blogspot.com)",
        license=License.CC_BY_3_0,
    ),
)
R_KASRANI = Species(
    name="Rodhocetus kasrani",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhodocetus_BW.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Rhodocetus_BW.jpg",
        author="Nobu Tamura",
        license=License.CC_BY_3_0,
    ),
)
D_ATROX = Species(
    name="Dorudon atrox",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dorudon_BW.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Dorudon_BW.jpg",
        author="Nobu Tamura",
        license=License.CC_BY_3_0,
    ),
)
B_CETOIDES = Species(
    name="Basilosaurus cetoides",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Basilosaurus1DB.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Basilosaurus1DB.jpg",
        author="Dmitry Bogdanov",
        license=License.CC_BY_3_0,
    ),
)
B_MYSTICETUS = Species(
    name="Balaena mysticetus",
    local_names={
        EN: "bowhead whale, Greenland right whale",
        PL: "wieloryb grenlandzki, wal grenlandzki",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bowhead-Whale1_(16273933365).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0c/Bowhead-Whale1_%2816273933365%29.jpg",
        author="Bering Land Bridge National Preserve",
        license=License.CC_BY_SA_2_0,
    ),
)
E_GLACIALIS = Species(
    name="Eubalaena glacialis",
    local_names={EN: "North Atlantic right whale", PL: "waleń biskajski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eubalaena_glacialis_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f9/Eubalaena_glacialis_NOAA.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
)
B_MUSCULUS = Species(
    name="Balaenoptera musculus",
    local_names={EN: "blue whale", PL: "płetwal błękitny"},
    known_for=[{EN: "the largest animal known to have ever existed"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Balaenoptera_musculus_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/97/Balaenoptera_musculus_NOAA.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
)
M_NOVAEANGLIAE = Species(
    name="Megaptera novaeangliae",
    local_names={EN: "humpback whale", PL: "humbak, długopłetwiec oceaniczny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Megaptera_novaeangliae_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Megaptera_novaeangliae_NOAA.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
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
