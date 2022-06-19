from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

C_NILOTICUS = Species(
    name="Crocodylus niloticus",
    local_names={EN: "Nile crocodile", PL: "krokodyl nilowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crocodylus_niloticus_MNHN.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Crocodylus_niloticus_MNHN.jpg",
        author="Muséum national d'histoire naturelle",
        license=License.CC0,
    ),
)
C_POROSUS = Species(
    name="Crocodylus porosus",
    local_names={EN: "saltwater crocodile", PL: "krokodyl różańcowy"},
    known_for=[{EN: "the largest living reptile"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Saltwater_Crocodile_(Crocodylus_porosus)_(10106331165).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bc/Saltwater_Crocodile_%28Crocodylus_porosus%29_%2810106331165%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
A_MISSISSIPPIENSIS = Species(
    name="Alligator mississippiensis",
    local_names={
        EN: "American alligator, common alligator",
        PL: "aligator amerykański",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:American_Alligator_(Alligator_mississippiensis)_Chambers_Co._Texas._photo_W._L._Farr.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/25/American_Alligator_%28Alligator_mississippiensis%29_Chambers_Co._Texas._photo_W._L._Farr.jpg",
        author="Wilafa",
        license=License.CC_BY_SA_4_0,
    ),
)
A_SINENSIS = Species(
    name="Alligator sinensis",
    local_names={EN: "Chinese alligator", PL: "aligator chiński"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:China-Alligator.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/China-Alligator.jpg",
        author="Stolz, Gary M.",
        license=License.FWS,
    ),
)
G_GANGETICUS = Species(
    name="Gavialis gangeticus",
    local_names={EN: "gharial, gavial", PL: "gawial gangesowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gavialis_gangeticus_(Gharial).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Gavialis_gangeticus_%28Gharial%29.png",
        author="Unknown",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_CROCODILUS = Species(
    name="Caiman crocodilus",
    local_names={
        EN: "spectacled caiman, white caiman, common caiman",
        PL: "kajman krokodylowy, kajman okularowy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Caiman_crocodilus_llanos_white_background.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Caiman_crocodilus_llanos_white_background.JPG",
        author="Berrucomons",
        license=License.CC_BY_SA_3_0,
    ),
)

CROCODYLUS = Genus(name="Crocodylus", children=[C_NILOTICUS, C_POROSUS])
ALLIGATOR = Genus(name="Alligator", children=[A_MISSISSIPPIENSIS, A_SINENSIS])
GAVIALIS = Genus(name="Gavialis", children=[G_GANGETICUS])
CAIMAN = Genus(name="Caiman", children=[C_CROCODILUS])

CROCODYLIDAE = Family(name="Crocodylidae", children=[CROCODYLUS])
ALLIGATORIDAE = Family(name="Alligatoridae", children=[ALLIGATOR, CAIMAN])
GAVIALIDAE = Family(name="Gavialidae", children=[GAVIALIS])

LONGINOSTRES = Clade(name="Longinostres", children=[CROCODYLIDAE, GAVIALIDAE])

CROCODILIA = Order(name="Crocodilia", children=[LONGINOSTRES, ALLIGATORIDAE])
