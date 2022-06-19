from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Order,
    Phylum,
    Species,
    Subclass,
    Superphylum,
)
from constants import EN, PL
from image import Image, License

from .arthropoda import ARTHROPODA
from .mollusca import MOLLUSCA

# region PLATYHELIMNTES
F_HEPATICA = Species(
    name="Fasciola hepatica",
    local_names={EN: "common liver fluke", PL: "motylica wątrobowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fasciola_hepatica.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Fasciola_hepatica.JPG",
        author="Flukeman",
        license=License.CC_BY_SA_3_0,
    ),
)
T_SAGINATA = Species(
    name="Taenia saginata",
    local_names={EN: "beef tapeworm", PL: "tasiemiec nieuzbrojony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Taenia_saginata_adult_5260_lores.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e2/Taenia_saginata_adult_5260_lores.jpg",
        author="Centers for Disease Control and Prevention",
        license=License.CDC,
    ),
)
T_SOLIUM = Species(
    name="Taenia solium",
    local_names={EN: "pork tapeworm", PL: "tasiemiec uzbrojony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Taenia_solium.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Taenia_solium.jpg",
        author="Unknown author",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

FASCIOLA = Genus(name="Fasciola", children=[F_HEPATICA])
TAENIA = Genus(name="Taenia", children=[T_SAGINATA, T_SOLIUM])

FASCIOLIDAE = Family(name="Fasciolidae", children=[FASCIOLA])
TAENIIDAE = Family(name="Taeniidae", children=[TAENIA])

PLAGIORCHIIDA = Order(name="Plagiorchiida", children=[FASCIOLIDAE])
CYCLOPHYLLIDEA = Order(name="Cyclophyllidea", children=[TAENIIDAE])

DIGENEA = Subclass(name="Digenea", children=[PLAGIORCHIIDA])

TREMATODA = Class(name="Trematoda", children=[DIGENEA])  # not sure about class

CESTODA = Class(name="Cestoda", children=[CYCLOPHYLLIDEA])

PLATYHELMINTHES = Phylum(name="Platyhelminthes", children=[TREMATODA, CESTODA])
# endregion PLATYHELIMNTES

# region ANNELIDA
L_TERRESTRIS = Species(
    name="Lumbricus terrestris",
    local_names={EN: "common earthworm", PL: "dżdżownica ziemna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lumbricus_terrestris_R.H_(3).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Lumbricus_terrestris_R.H_%283%29.JPG",
        author="Rob Hille",
        license=License.CC_BY_SA_3_0,
    ),
)
H_MEDICINALIS = Species(
    name="Hirudo medicinalis",
    local_names={EN: "European medicinal leech", PL: "pijawka lekarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sv%C3%B8mmende_blodigle.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/Sv%C3%B8mmende_blodigle.JPG",
        author="Karl Ragnar Gjertsen",
        license=License.CC_BY_SA_3_0,
    ),
)

LUMBRICUS = Genus(name="Lumbricus", children=[L_TERRESTRIS])
HIRUDO = Genus(name="Hirudo", children=[H_MEDICINALIS])

LUMBRICIDAE = Family(name="Lumbricidae", children=[LUMBRICUS])
HIRUDINIDAE = Family(name="Hirudinidae", children=[HIRUDO])

OPISTHOPORA = Order(name="Opisthopora", children=[LUMBRICIDAE])
ARHYNCHOBDELLIDA = Order(name="Arhynchobdellida", children=[HIRUDINIDAE])

CITELLATA = Class(name="Citellata", children=[OPISTHOPORA, ARHYNCHOBDELLIDA])

ANNELIDA = Phylum(name="Annelida", children=[CITELLATA])
# endregion ANNELIDA

# region NEMATODA
A_LUMBRICOIDES = Species(
    name="Ascaris lumbricoides",
    local_names={EN: "large roundworm", PL: "glista ludzka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ascaris_lumbricoides.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7e/Ascaris_lumbricoides.jpeg",
        author="Centers for Disease Control and Prevention",
        license=License.CDC,
    ),
)
E_VERMICULARIS = Species(
    name="Enterobius vermicularis",
    local_names={EN: "pinworm, threadworm", PL: "owsik ludzki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Enterobius_vermicularis_(YPM_IZ_093289).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Enterobius_vermicularis_%28YPM_IZ_093289%29.jpeg",
        author="Daniel J. Drew",
        license=License.CC0,
    ),
)
O_VOLVULUS = Species(
    name="Onchocerca volvulus",
    known_for=[{EN: "river blindness", PL: "ślepota rzeczna"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Onchocerca_volvulus_mf1_DPDx.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Onchocerca_volvulus_mf1_DPDx.JPG",
        author="Centers for Disease Control and Prevention",
        license=License.CDC,
    ),
)

ASCARIS = Genus(name="Ascaris", children=[A_LUMBRICOIDES])
ENTEROBIUS = Genus(name="Enterobius", children=[E_VERMICULARIS])
ONCHOCERCA = Genus(name="Onchocerca", children=[O_VOLVULUS])

ASCARIDIDAE = Family(name="Ascarididae", children=[ASCARIS])
OXYURIDAE = Family(name="Oxyuridae", children=[ENTEROBIUS])
ONCHOCERCIDAE = Family(name="Onchocercidae", children=[ONCHOCERCA])

ASCARIDIDA = Order(name="Ascaridida", children=[ASCARIDIDAE])
RHABDITIDA = Order(name="Rhabditida", children=[OXYURIDAE, ONCHOCERCIDAE])

CHROMADOREA = Class(name="Chromadorea", children=[ASCARIDIDA, RHABDITIDA])

NEMATODA = Phylum(name="Nematoda", children=[CHROMADOREA])
# endregion NEMATODA

# region TARDIGRADA
M_TARDIGRADUM = Species(
    name="Milnesium tardigradum",
    known_for=[{EN: "cosmopolitan tardigrade", PL: "kosmpolityczny niesporczak"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:SEM_image_of_Milnesium_tardigradum_in_active_state_-_journal.pone.0045682.g001-2.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/SEM_image_of_Milnesium_tardigradum_in_active_state_-_journal.pone.0045682.g001-2.png",
        author="Schokraie E, Warnken U, Hotz-Wagenblatt A, Grohme MA, Hengherr S, et al. (2012)",
        license=License.CC_BY_2_5,
    ),
)
MILNESIUM = Genus(name="Milnesium", children=[M_TARDIGRADUM])
MILNESIIDAE = Family(name="Milnesiidae", children=[MILNESIUM])
APOCHELA = Order(name="Apochela", children=[MILNESIIDAE])
EUTARDIGRADA = Class(name="Eutardigrada", children=[APOCHELA])
TARDIGRADA = Phylum(name="Tardigrada", children=[EUTARDIGRADA])
# endregion TARDIGRADA

# region ROTIFERA
H_ROSA = Species(
    name="Habrotrocha rosa",
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Habrotrocha_rosa_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Habrotrocha_rosa_1.jpg",
        author="Rkitko",
        license=License.CC_BY_SA_3_0,
    ),
)
HABROTROCHA = Genus(name="Habrotrocha", children=[H_ROSA])
HABROTROCHIDAE = Family(name="Habrotrochidae", children=[HABROTROCHA])
BDELLOIDA = Order(name="Bdelloida", children=[HABROTROCHIDAE])
BDELLOIDEA = Class(name="Bdelloidea", children=[BDELLOIDA])
ROTIFERA = Phylum(name="Rotifera", children=[BDELLOIDEA])
# endregion ROTIFERA

PANARTHROPODA = Clade(name="Panarthropoda", children=[TARDIGRADA, ARTHROPODA])

LOPHOTROCHOZOA = Superphylum(name="Lophotrochozoa", children=[ANNELIDA, MOLLUSCA])

ECDYSOZOA = Superphylum(name="Ecdysozoa", children=[NEMATODA, PANARTHROPODA])

PLATYTROCHOZOA = Clade(
    name="Platytrochozoa", children=[PLATYHELMINTHES, LOPHOTROCHOZOA]
)

SPIRALIA = Clade(name="Spiralia", children=[PLATYTROCHOZOA, ROTIFERA])

PROTOSTOMIA = Class(
    name="Protostomia",
    children=[SPIRALIA, ECDYSOZOA],
    local_names={PL: "pierwouste"},
)
