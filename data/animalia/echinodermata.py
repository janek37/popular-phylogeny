from clade import Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL
from image import Image, License

A_RUBENS = Species(
    name="Asterias rubens",
    local_names={EN: "common starfish", PL: "rozgwiazda czerwona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Asterias_rubens.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Asterias_rubens.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
E_ESCULENTUS = Species(
    name="Echinus esculentus",
    local_names={
        EN: "common sea urchin, European edible sea urchin",
        PL: "jeżowiec jadalny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Echinus_esculentus_Koster.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Echinus_esculentus_Koster.jpg",
        author="Bengt Littorin",
        license=License.CC_BY_2_0,
    ),
)
M_FRANCISCANUS = Species(
    name="Mesocentrotus franciscanus",
    local_names={EN: "red sea urchin", PL: "jeżowiec czerwony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Strongylocentrotus_franciscanus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2e/Strongylocentrotus_franciscanus.jpg",
        author="Taollan82, Kirt L. Onthank",
        license=License.CC_BY_3_0,
    ),
)
E_PARMA = Species(
    name="Echinarachnius parma",
    local_names={EN: "common sand dollar", PL: "dolar piaskowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Echinarachnius_parma%27_(YPM_IZ_069833).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Echinarachnius_parma%27_%28YPM_IZ_069833%29.jpg",
        author="Yale Peabody Museum of Natural History; photo by Eric A. Lazo-Wasem 2014",
        license=License.CC0,
    ),
)
P_REGALIS = Species(
    name="Parastichopus regalis",
    local_names={EN: "royal sea cucumber", PL: "trepang królewski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Parastichopus_regalis.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Parastichopus_regalis.JPG",
        author="FredD",
        license=License.CC_BY_SA_4_0,
    ),
)
C_MINIATA = Species(
    name="Cucumaria miniata",
    local_names={EN: "orange/red sea cucumber", PL: "ogórczak japoński"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cucumaria_miniata.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2b/Cucumaria_miniata.jpg",
        author="Jan Haaga",
        license=License.NOAA,
    ),
)

ASTERIAS = Genus(name="Asterias", children=[A_RUBENS])
ECHINUS = Genus(name="Echinus", children=[E_ESCULENTUS])
MESOCENTROTUS = Genus(name="Mesocentrotus", children=[M_FRANCISCANUS])
ECHINARACHNIUS = Genus(name="Echinarachnius", children=[E_PARMA])
PARASTICHOPUS = Genus(name="Parastichopus", children=[P_REGALIS])
CUCUMARIA = Genus(name="Cucumaria", children=[C_MINIATA])

ASTERIIDAE = Family(name="Asteriidae", children=[ASTERIAS])
ECHINIDAE = Family(name="Echinidae", children=[ECHINUS])
STRONGYLOCENTROTIDAE = Family(name="Strongylocentrotidae", children=[MESOCENTROTUS])
ECHINARACHNIIDAE = Family(name="Echinarachniidae", children=[ECHINARACHNIUS])
STICHOPODIDAE = Family(name="Stichopodidae", children=[PARASTICHOPUS])
CUCUMARIIDAE = Family(name="Cucumariidae", children=[CUCUMARIA])

FORCIPULATIDA = Order(name="Forcipulatida", children=[ASTERIIDAE])
CAMARODONTA = Order(name="Camarodonta", children=[ECHINIDAE, STRONGYLOCENTROTIDAE])
CLYPEASTEROIDA = Order(name="Clypeasteroida", children=[ECHINARACHNIIDAE])
SYNALLACTIDA = Order(name="Synallactida", children=[STICHOPODIDAE])
DENDROCHIROTIDA = Order(name="Dendrochirotida", children=[CUCUMARIIDAE])

ASTEROIDEA = Class(name="Asteroidea", children=[FORCIPULATIDA])
ECHINOIDEA = Class(name="Echinoidea", children=[CAMARODONTA, CLYPEASTEROIDA])
HOLOTHUROIDEA = Class(name="Holothuroidea", children=[SYNALLACTIDA, DENDROCHIROTIDA])

ECHINOZOA = Subphylum(name="Echinozoa", children=[ECHINOIDEA, HOLOTHUROIDEA])

ECHINODERMATA = Phylum(name="Echinodermata", children=[ASTEROIDEA, ECHINOZOA])
