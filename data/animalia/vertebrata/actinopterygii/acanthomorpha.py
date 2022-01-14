from clade import Clade, Family, Genus, Order, Species, Superorder
from constants import EN, PL

L_GUTTATUS = Species(
    name="Lampris guttatus",
    local_names={
        EN: "opah, cravo, moonfish, kingfish, Jerusalem haddock",
        PL: "ryba księżycowa, strojnik",
    },
)
R_GLESNE = Species(
    name="Regalecus glesne",
    local_names={EN: "giant oarfish, king of herrings", PL: "wstęgor królewski"},
    known_for=[
        {EN: "the longest bony fish in the world (up to at least 8 m)"},
        {EN: "probable source of sea serpent sightings"},
    ],
)
Z_FABER = Species(
    name="Zeus faber",
    local_names={EN: "John Dory, St Pierre, Peter's fish", PL: "paszczak, piotrosz"},
)
G_MORHUA = Species(
    name="Gadus morhua", local_names={EN: "Atlantic cod", PL: "dorsz atlantycki"}
)
G_CHALCOGRAMMUS = Species(
    name="Gadus chalcogrammus",
    local_names={EN: "Alaska pollock, walleye pollock", PL: "mintaj"},
)
M_AEGLEFINUS = Species(
    name="Melanogrammus aeglefinus",
    local_names={EN: "haddock", PL: "wątłusz srebrzysty, plamiak"},
)
M_MERLUCCIUS = Species(
    name="Merluccius merluccius",
    local_names={EN: "European hake", PL: "morszczuk zwyczajny"},
)

LAMPRIS = Genus(name="Lampris", children=[L_GUTTATUS])
REGALECUS = Genus(name="Regalecus", children=[R_GLESNE])
ZEUS = Genus(name="Zeus", children=[Z_FABER])
GADUS = Genus(name="Gadus", children=[G_MORHUA, G_CHALCOGRAMMUS])
MELANOGRAMMUS = Genus(name="Melanogrammus", children=[M_AEGLEFINUS])
MERLUCCIUS = Genus(name="Merluccius", children=[M_MERLUCCIUS])

LAMPRIDAE = Family(name="Lampridae", children=[LAMPRIS])
REGALECIDAE = Family(name="Regalecidae", children=[REGALECUS])
ZEIDAE = Family(name="Zeidae", children=[ZEUS])
GADIDAE = Family(name="Gadidae", children=[GADUS, MELANOGRAMMUS])
MERLUCCIIDAE = Family(name="Merlucciidae", children=[MERLUCCIUS])

LAMPRIFORMES = Order(name="Lampriformes", children=[LAMPRIDAE, REGALECIDAE])
ZEIFORMES = Order(name="Zeiformes", children=[ZEIDAE])
GADIFORMES = Order(name="Gadiformes", children=[GADIDAE, MERLUCCIIDAE])

LAMPRIPTERYGII = Superorder(name="Lampripterygii", children=[LAMPRIFORMES])
PARACANTHOPTERYGII = Superorder(
    name="Paracanthopterygii", children=[ZEIFORMES, GADIFORMES]
)

ACANTHOMORPHA = Clade(
    name="Acanthomorpha", children=[LAMPRIPTERYGII, PARACANTHOPTERYGII]
)
