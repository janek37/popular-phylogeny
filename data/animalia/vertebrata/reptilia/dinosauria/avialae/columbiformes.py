from clade import Family, Genus, Order, Species, Subfamily
from constants import EN, PL
from image import Image, License

C_LIVIA = Species(
    name="Columba livia",
    local_names={EN: "rock dove, rock pigeon, common pigeon", PL: "gołąb skalny"},
    known_for=[
        {EN: "domestic pigeon"},
        {EN: "homing pigeon", PL: "gołąb pocztowy"},
        {EN: "ciy pigeon, feral pigeon", PL: "gołąb miejski"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Feral_pigeon_2022_03_18_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f9/Feral_pigeon_2022_03_18_01.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)
R_CUCULLATUS = Species(
    name="Raphus cucullatus",
    local_names={EN: "dodo", PL: "dront dodo"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Didus_cucullatus_white_background.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Didus_cucullatus_white_background.jpg",
        author="Frederick William Frohawk (16 July 1861 - 10 December 1946), an English zoological artist",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_DECAOCTO = Species(
    name="Streptopelia decaocto",
    local_names={EN: "Eurasian collared dove", PL: "synogarlica turecka, sierpówka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Streptopelia_decaocto_-_Eurasian_Collared_Dove_05.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/35/Streptopelia_decaocto_-_Eurasian_Collared_Dove_05.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
S_TURTUR = Species(
    name="Streptopelia turtur",
    local_names={EN: "European turtle dove", PL: "turkawka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Streptopelia_turtur_in_an_English_zoo_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6b/Streptopelia_turtur_in_an_English_zoo_%28cropped%29.jpg",
        author="Kev Chapman",
        license=License.CC_BY_2_0,
    ),
)

COLUMBA = Genus(name="Columba", children=[C_LIVIA])
RAPHUS = Genus(name="Raphus", children=[R_CUCULLATUS])
STREPTOPELIA = Genus(name="Streptopelia", children=[S_DECAOCTO, S_TURTUR])

COLUMBINAE = Subfamily(name="Columbinae", children=[COLUMBA, STREPTOPELIA])
RAPHINAE = Subfamily(name="Raphinae", children=[RAPHUS])

COLUMBIDAE = Family(name="Columbidae", children=[COLUMBINAE, RAPHINAE])

COLUMBIFORMES = Order(name="Columbiformes", children=[COLUMBIDAE])
