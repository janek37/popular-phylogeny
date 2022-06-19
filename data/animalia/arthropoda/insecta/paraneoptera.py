from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, LA, PL
from image import Image, License

P_HUMANUS = Species(
    name="Pediculus humanus",
    local_names={PL: "wesz ludzka"},
    known_for=[
        {LA: "pediculus humanus humanus", EN: "body louse", PL: "wesz odzieżowa"},
        {LA: "pediculus humanus capitis", EN: "head louse", PL: "wesz głowowa"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nuttall_1917_f11.gif",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Nuttall_1917_f11.gif",
        author="Nuttall, George H. F. (1862-1937)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_PUBIS = Species(
    name="Pthirus pubis",
    local_names={EN: "crab louse, pubic louse", PL: "menda, wesz łonowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pthirus_inguinalis_adult.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Pthirus_inguinalis_adult.png",
        author="Servier Medical Art",
        license=License.CC_BY_2_0,
    ),
)
M_PERSICAE = Species(
    name="Myzus persicae",
    local_names={
        EN: "green peach aphid, greenfly",
        PL: "mszyca brzoskwiniowo-ziemniaczana",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myzus_persicae_75370975.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Myzus_persicae_75370975.jpg",
        author="Alexis",
        license=License.CC_BY_4_0,
    ),
)
P_POLONICA = Species(
    name="Porphyrophora polonica",
    local_names={EN: "Polish cochineal", PL: "czerwiec polski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Adult_Polish_cochineal.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Adult_Polish_cochineal.JPG",
        author="Unknown author",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
G_LACUSTRIS = Species(
    name="Gerris lacustris",
    local_names={EN: "common pond skater, common water strider", PL: "nartnik duży"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gerris_lacustris_07.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Gerris_lacustris_07.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
C_LECTULARIUS = Species(
    name="Cimex lectularius",
    local_names={EN: "common bed bug", PL: "pluskwa domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bed_bug,_Cimex_lectularius_(9627010587).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/35/Bed_bug%2C_Cimex_lectularius_%289627010587%29.jpg",
        author="AJC1 from UK",
        license=License.CC_BY_SA_2_0,
    ),
)
P_APTERUS = Species(
    name="Pyrrhocoris apterus",
    local_names={EN: "firebug", PL: "tramwajarz, kowal bezskrzydły"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pyrrhocoris_apterus_Piazzo_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Pyrrhocoris_apterus_Piazzo_01.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
P_PRASINA = Species(
    name="Palomena prasina",
    local_names={EN: "green shield bug", PL: "odorek zieleniak"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Palomena_prasina_Piazzo_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Palomena_prasina_Piazzo_01.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
P_RUFIPES = Species(
    name="Pentatoma rufipes",
    local_names={EN: "forest bug, red-legged shieldbug", PL: "tarczówka rudonoga"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pentatoma_rufipes-dkrb.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/Pentatoma_rufipes-dkrb.jpg",
        author="https://de.wikipedia.org/wiki/Benutzer:Drahkrub",
        license=License.CC_BY_3_0,
    ),
)
C_VIRIDIS = Species(
    name="Cicadella viridis",
    local_names={EN: "green leafhopper"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cicadella_viridis_(10.3897-BDJ.9.e65314)_Figure_1_b.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Cicadella_viridis_%2810.3897-BDJ.9.e65314%29_Figure_1_b.jpeg",
        author="Rui Andrade",
        license=License.CC_BY_4_0,
    ),
)
M_SEPTENDECIM = Species(
    name="Magicicada septendecim",
    local_names={EN: "Pharaoh cicada, 17-year locust", PL: "17-letnia cykada"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Magicicada_septendecim_female_(Brood_X)_-_journal.pone.0000892.g003A.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Magicicada_septendecim_female_%28Brood_X%29_-_journal.pone.0000892.g003A.png",
        author="Fontaine K, Cooley J, Simon C (2007)",
        license=License.CC_BY_2_5,
    ),
)

PEDICULUS = Genus(name="Pediculus", children=[P_HUMANUS])
PTHIRUS = Genus(name="Pthirus", children=[P_PUBIS])
MYZUS = Genus(name="Myzus", children=[M_PERSICAE])
PORPHYROPHORA = Genus(name="Porphyrophora", children=[P_POLONICA])
GERRIS = Genus(name="Gerris", children=[G_LACUSTRIS])
CIMEX = Genus(name="Cimex", children=[C_LECTULARIUS])
PYRRHOCORIS = Genus(name="Pyrrhocoris", children=[P_APTERUS])
PALOMENA = Genus(name="Palomena", children=[P_PRASINA])
PENTATOMA = Genus(name="Pentatoma", children=[P_RUFIPES])
CICADELLA = Genus(name="Cicadella", children=[C_VIRIDIS])
MAGICICADA = Genus(name="Magicicada", children=[M_SEPTENDECIM])

PEDICULIDAE = Family(name="Pediculidae", children=[PEDICULUS])
PTHIRIDAE = Family(name="Pthiridae", children=[PTHIRUS])
APHIDIDAE = Family(name="Aphididae", children=[MYZUS])
MARGARODIDAE = Family(name="Margarodidae", children=[PORPHYROPHORA])
GERRIDAE = Family(name="Gerridae", children=[GERRIS])
CIMICIDAE = Family(name="Cimicidae", children=[CIMEX])
PYRRHOCORIDAE = Family(name="Pyrrhocoridae", children=[PYRRHOCORIS])
PENTATOMIDAE = Family(name="Pentatomidae", children=[PALOMENA, PENTATOMA])
CICADELLIDAE = Family(name="Cicadellidae", children=[CICADELLA])
CICADIDAE = Family(name="Cicadidae", children=[MAGICICADA])

GERROMORPHA = Infraorder(name="Gerromorpha", children=[GERRIDAE])
CIMICOMORPHA = Infraorder(name="Cimicomorpha", children=[CIMICIDAE])
PENTATOMOMORPHA = Infraorder(
    name="Pentatomomorpha", children=[PYRRHOCORIDAE, PENTATOMIDAE]
)
CICADOMORPHA = Infraorder(name="Cicadomorpha", children=[CICADELLIDAE, CICADIDAE])

# https://www.researchgate.net/publication/227525359_Phylogeny_of_the_true_water_bugs_Nepomorpha_Hemiptera-Heteroptera_based_on_16S_and_28S_rDNA_and_morphology
HETEROPTERA_A = Clade(children=[CIMICOMORPHA, PENTATOMOMORPHA])

STERNORRHYNCHA = Suborder(name="Sternorrhyncha", children=[APHIDIDAE, MARGARODIDAE])
HETEROPTERA = Suborder(name="Heteroptera", children=[GERROMORPHA, HETEROPTERA_A])
AUCHENORRHYNCHA = Suborder(name="Auchenorrhyncha", children=[CICADOMORPHA])

HEMIPTERA_A = Clade(children=[HETEROPTERA, AUCHENORRHYNCHA])

PSOCODEA = Order(name="Psocodea", children=[PEDICULIDAE, PTHIRIDAE])
HEMIPTERA = Order(name="Hemiptera", children=[STERNORRHYNCHA, HEMIPTERA_A])

PARANEOPTERA = Clade(name="Paraneoptera", children=[PSOCODEA, HEMIPTERA])  # Superorder?
