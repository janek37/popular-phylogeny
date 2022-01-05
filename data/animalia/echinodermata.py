from clade import Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL

A_RUBENS = Species(
    name="Asterias rubens",
    local_names={EN: "common starfish", PL: "rozgwiazda czerwona"},
)
E_ESCULENTUS = Species(
    name="Echinus esculentus",
    local_names={
        EN: "common sea urchin, European edible sea urchin",
        PL: "jeżowiec jadalny",
    },
)
E_PARMA = Species(
    name="Echinarachnius parma",
    local_names={EN: "common sand dollar", PL: "dolar piaskowy"},
)
P_REGALIS = Species(
    name="Parastichopus regalis",
    local_names={EN: "royal sea cucumber", PL: "trepang królewski"},
)
C_MINIATA = Species(
    name="Cucumaria miniata",
    local_names={EN: "orange/red sea cucumber", PL: "ogórczak japoński"},
)

ASTERIAS = Genus(name="Asterias", children=[A_RUBENS])
ECHINUS = Genus(name="Echinus", children=[E_ESCULENTUS])
ECHINARACHNIUS = Genus(name="Echinarachnius", children=[E_PARMA])
PARASTICHOPUS = Genus(name="Parastichopus", children=[P_REGALIS])
CUCUMARIA = Genus(name="Cucumaria", children=[C_MINIATA])

ASTERIIDAE = Family(name="Asteriidae", children=[ASTERIAS])
ECHINIDAE = Family(name="Echinidae", children=[ECHINUS])
ECHINARACHNIIDAE = Family(name="Echinarachniidae", children=[ECHINARACHNIUS])
STICHOPODIDAE = Family(name="Stichopodidae", children=[PARASTICHOPUS])
CUCUMARIIDAE = Family(name="Cucumariidae", children=[CUCUMARIA])

FORCIPULATIDA = Order(name="Forcipulatida", children=[ASTERIIDAE])
CAMARODONTA = Order(name="Camarodonta", children=[ECHINIDAE])
CLYPEASTEROIDA = Order(name="Clypeasteroida", children=[ECHINARACHNIIDAE])
SYNALLACTIDA = Order(name="Synallactida", children=[STICHOPODIDAE])
DENDROCHIROTIDA = Order(name="Dendrochirotida", children=[CUCUMARIIDAE])

ASTEROIDEA = Class(name="Asteroidea", children=[FORCIPULATIDA])
ECHINOIDEA = Class(name="Echinoidea", children=[CAMARODONTA, CLYPEASTEROIDA])
HOLOTHUROIDEA = Class(name="Holothuroidea", children=[SYNALLACTIDA, DENDROCHIROTIDA])

ECHINOZOA = Subphylum(name="Echinozoa", children=[ECHINOIDEA, HOLOTHUROIDEA])

ECHINODERMATA = Phylum(name="Echinodermata", children=[ASTEROIDEA, ECHINOZOA])
