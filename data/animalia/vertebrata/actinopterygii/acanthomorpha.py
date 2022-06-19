from clade import Clade, Family, Genus, Order, Species, Superorder
from constants import EN, PL
from image import Image, License

from .percomorpha import PERCOMORPHA

L_GUTTATUS = Species(
    name="Lampris guttatus",
    local_names={
        EN: "opah, cravo, moonfish, kingfish, Jerusalem haddock",
        PL: "ryba księżycowa, strojnik",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lampridae_-_Lampris_guttatus.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/Lampridae_-_Lampris_guttatus.JPG",
        author="Hectonichus",
        license=License.CC_BY_SA_3_0,
    ),
)
R_GLESNE = Species(
    name="Regalecus glesne",
    local_names={EN: "giant oarfish, king of herrings", PL: "wstęgor królewski"},
    known_for=[
        {EN: "the longest bony fish in the world (up to at least 8 m)"},
        {EN: "probable source of sea serpent sightings"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Regalecus_glesne_Mexico.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Regalecus_glesne_Mexico.jpg",
        author="Katia Cao",
        license=License.CC_BY_3_0,
    ),
)
Z_FABER = Species(
    name="Zeus faber",
    local_names={EN: "John Dory, St Pierre, Peter's fish", PL: "paszczak, piotrosz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zeus.faber.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Zeus.faber.jpg",
        author="de:Benutzer:Kleines.Opossum",
        license=License.CC_BY_SA_3_0,
    ),
)
G_MORHUA = Species(
    name="Gadus morhua",
    local_names={EN: "Atlantic cod", PL: "dorsz atlantycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gadus_morhua_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Gadus_morhua_Gervais.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
G_CHALCOGRAMMUS = Species(
    name="Gadus chalcogrammus",
    local_names={EN: "Alaska pollock, walleye pollock", PL: "mintaj"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Theragra_chalcogramma.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Theragra_chalcogramma.png",
        author="Unknown",
        license=License.NOAA,
    ),
)
M_AEGLEFINUS = Species(
    name="Melanogrammus aeglefinus",
    local_names={EN: "haddock", PL: "wątłusz srebrzysty, plamiak"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Melanogrammus_aeglefinus1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Melanogrammus_aeglefinus1.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
M_MERLUCCIUS = Species(
    name="Merluccius merluccius",
    local_names={EN: "European hake", PL: "morszczuk zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Merluccius_merluccius.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/Merluccius_merluccius.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
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

ACANTHOMORPHA_A = Clade(children=[LAMPRIPTERYGII, PARACANTHOPTERYGII])

ACANTHOMORPHA = Clade(name="Acanthomorpha", children=[ACANTHOMORPHA_A, PERCOMORPHA])
