from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Order,
    Species,
    Subclass,
    Subphylum,
    Superorder,
)
from constants import EN, PL
from image import Image, License

from .insecta import INSECTA
from .malacostraca import MALACOSTRACA

P_POLLICIPES = Species(
    name="Pollicipes pollicipes",
    local_names={EN: "goose neck barnacle"},
    known_for=[{EN: "one of the most popular edible barnacles"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pollicipes_pollicipes_transparent_background.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Pollicipes_pollicipes_transparent_background.png",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
A_IMPROVISUS = Species(
    name="Amphibalanus improvisus",
    local_names={EN: "bay barnacle", PL: "pąkla niespodziewana"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Balanus_improvisus_on_Mya_arenaria_shell.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/47/Balanus_improvisus_on_Mya_arenaria_shell.jpg",
        author="Andrew Butko",
        license=License.CC_BY_SA_3_0,
    ),
)
D_PULEX = Species(
    name="Daphnia pulex",
    local_names={PL: "rozwielitka pchłowata"},
    known_for=[{EN: "the most common species of water flea"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Daphnia_pulex.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Daphnia_pulex.png",
        author="Paul Hebert",
        license=License.CC_BY_2_5,
    ),
)

POLLICIPES = Genus(name="Pollicipes", children=[P_POLLICIPES])
AMPHIBALANUS = Genus(name="Amphibalanus", children=[A_IMPROVISUS])
DAPHNIA = Genus(name="Daphnia", children=[D_PULEX])

POLLICIPEDIDAE = Family(name="Pollicipedidae", children=[POLLICIPES])
BALANIDAE = Family(name="Balanidae", children=[AMPHIBALANUS])
DAPHNIIDAE = Family(name="Daphniidae", children=[DAPHNIA])

POLLICIPEDOMORPHA = Order(name="Pollicipedomorpha", children=[POLLICIPEDIDAE])
BALANOMORPHA = Order(name="Balanomorpha", children=[BALANIDAE])
ANOMOPODA = Order(name="Anomopoda", children=[DAPHNIIDAE])

THORACICALCAREA = Superorder(
    name="Thoracicalcarea", children=[POLLICIPEDOMORPHA, BALANOMORPHA]
)

CIRRIPEDIA = Subclass(name="Cirripedia", children=[THORACICALCAREA])

THECOSTRACA = Class(name="Thecostraca", children=[CIRRIPEDIA])
BRANCHIOPODA = Class(name="Branchiopoda", children=[ANOMOPODA])

HEXAPODA = Clade(name="Hexapoda", children=[INSECTA])

MULTICRUSTACEA = Clade(name="Multicrustacea", children=[THECOSTRACA, MALACOSTRACA])
ALLOTRIOCARIDA = Clade(name="Allotriocarida", children=[BRANCHIOPODA, HEXAPODA])

CRUSTACEA = Subphylum(name="Crustacea", children=[MULTICRUSTACEA, ALLOTRIOCARIDA])
