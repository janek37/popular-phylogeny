from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL
from image import Image, License

from .arachnida import ARACHNIDA
from .crustacea import CRUSTACEA
from .myriapoda import MYRIAPODA

P_DAVIDIS = Species(
    name="Paradoxides davidis",
    known_for=[{EN: "one of the largest trilobites"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paradoxides_davidis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/43/Paradoxides_davidis.jpg",
        author="Sam Gon III",
        license=License.ATTRIBUTION,
    ),
)
L_POLYPHEMUS = Species(
    name="Limulus polyphemus",
    local_names={EN: "Atlantic horseshoe crab", PL: "skrzypłocz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Atlantic_horseshoe_crab_(Limulus_polyphemus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/Atlantic_horseshoe_crab_%28Limulus_polyphemus%29.jpg",
        author="Kaldari",
        license=License.CC0,
    ),
)

PARADOXIDES = Genus(name="Paradoxides", children=[P_DAVIDIS])
LIMULUS = Genus(name="Limulus", children=[L_POLYPHEMUS])

PARADOXIDIDAE = Family(name="Paradoxididae", children=[PARADOXIDES])
LIMULIDAE = Family(name="Limulidae", children=[LIMULUS])

REDLICHIIDA = Order(name="Redlichiida", children=[PARADOXIDIDAE])
XIPHOSURA = Order(name="Xiphosura", children=[LIMULIDAE])

TRILOBITA = Class(name="Trilobita", children=[REDLICHIIDA])

CHELICERATA = Subphylum(name="Chelicerata", children=[XIPHOSURA, ARACHNIDA])

ARACHNOMORPHA = Clade(name="Arachnomorpha", children=[TRILOBITA, CHELICERATA])
MANDIBULATA = Clade(name="Mandibulata", children=[MYRIAPODA, CRUSTACEA])

ARTHROPODA = Phylum(
    name="Arthropoda",
    children=[ARACHNOMORPHA, MANDIBULATA],
    local_names={PL: "stawonogi"},
)
