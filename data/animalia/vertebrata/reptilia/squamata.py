from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Order,
    Species,
    Suborder,
    Superfamily,
)
from constants import EN, PL, URL
from image import Image, License

from .iguania import IGUANIA
from .serpentes import SERPENTES

P_LATICAUDA = Species(
    name="Phelsuma laticauda",
    local_names={
        EN: "gold dust day gecko",
        PL: "felsuma gruboogonowa, dniówka gruboogonowa",
    },
    known_for=[
        {
            EN: "GEICO mascot",
            URL: "https://geicocarinsurance.fandom.com/wiki/GEICO_Gecko",
        },
        {
            EN: "Gex video game series",
            URL: "https://en.wikipedia.org/wiki/Gex_(series)",
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phelsuma_l._laticauda.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Phelsuma_l._laticauda.jpg",
        author="Jurriaan Schulman",
        license=License.CC_BY_SA_3_0,
    ),
)
S_SCINCUS = Species(
    name="Scincus scincus",
    local_names={
        EN: "sandfish skink, common skink",
        PL: "ryba piaskowa, scynk aptekarski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apothekerskink01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2d/Apothekerskink01.jpg",
        author="Wilfried Berns",
        license=License.CC_BY_SA_2_0_DE,
    ),
)
L_AGILIS = Species(
    name="Lacerta agilis",
    local_names={EN: "sand lizard", PL: "jaszczurka zwinka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lacerta_agilis_2443.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Lacerta_agilis_2443.jpg",
        author="Karol Nicinski (Bzdykol)",
        license=License.CC_BY_2_0,
    ),
)
L_VIRIDIS = Species(
    name="Lacerta viridis",
    local_names={EN: "European green lizard", PL: "jaszczurka zielona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lacerta_viridis_-_male_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/87/Lacerta_viridis_-_male_01.JPG",
        author="Uoaei1",
        license=License.CC_BY_SA_4_0,
    ),
)
V_KOMODOENSIS = Species(
    name="Varanus komodoensis",
    local_names={
        EN: "Komodo dragon, Komodo monitor",
        PL: "smok z Komodo, waran z Komodo",
    },
    known_for=[{EN: "the largest living lizard"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Varanus_komodoensis.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Varanus_komodoensis.JPG",
        author="Dezidor",
        license=License.CC_BY_3_0,
    ),
)
V_GOULDII = Species(
    name="Varanus gouldii",
    local_names={
        EN: "sand goanna, Gould's monitor",
        PL: "waran piaskowy, waran Goulda",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Goulds_Sand_Goanna_SW_WA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Goulds_Sand_Goanna_SW_WA.jpg",
        author="Spikercs",
        license=License.CC_BY_SA_3_0,
    ),
)
A_FRAGILIS = Species(
    name="Anguis fragilis",
    local_names={EN: "slow worm, deaf adder", PL: "padalec zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Slow_Worm_(Anguis_fragilis)_(36258444582).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/Slow_Worm_%28Anguis_fragilis%29_%2836258444582%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
M_HOFFMANNII = Species(
    name="Mosasaurus hoffmannii",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mosasaurus_hoffmanni_life.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d0/Mosasaurus_hoffmanni_life.jpg",
        author="Jonagold2000",
        license=License.CC_BY_SA_4_0,
    ),
)

PHELSUMA = Genus(name="Phelsuma", children=[P_LATICAUDA])
SCINCUS = Genus(name="Scincus", children=[S_SCINCUS])
LACERTA = Genus(name="Lacerta", children=[L_AGILIS, L_VIRIDIS])
VARANUS = Genus(name="Varanus", children=[V_KOMODOENSIS, V_GOULDII])
ANGUIS = Genus(name="Anguis", children=[A_FRAGILIS])
MOSASAURUS = Genus(name="Mosasaurus", children=[M_HOFFMANNII])

GEKKONIDAE = Family(name="Gekkonidae", children=[PHELSUMA])
SCINCIDAE = Family(name="Scincidae", children=[SCINCUS])
LACERTIDAE = Family(name="Lacertidae", children=[LACERTA])
VARANIDAE = Family(name="Varanidae", children=[VARANUS])
ANGUIDAE = Family(name="Anguidae", children=[ANGUIS])
MOSASAURIDAE = Family(name="Mosasauridae", children=[MOSASAURUS])

MOSASAUROIDEA = Superfamily(name="Mosasauroidea", children=[MOSASAURIDAE])

GEKKOTA = Infraorder(name="Gekkota", children=[GEKKONIDAE])

ANGUIMORPHA = Suborder(name="Anguimorpha", children=[VARANIDAE, ANGUIDAE])

PYTHONOMORPHA = Clade(name="Pythonomorpha", children=[SERPENTES, MOSASAUROIDEA])

TOXICOFERA_A = Clade(children=[ANGUIMORPHA, IGUANIA])
TOXICOFERA = Clade(name="Toxicofera", children=[TOXICOFERA_A, PYTHONOMORPHA])

SQUAMATA_A = Clade(children=[LACERTIDAE, TOXICOFERA])
SQUAMATA_B = Clade(children=[SCINCIDAE, SQUAMATA_A])
SQUAMATA = Order(name="Squamata", children=[GEKKOTA, SQUAMATA_B])
