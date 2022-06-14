from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Superfamily, Tribe
from constants import EN, PL
from image import Image, License

H_LAR = Species(
    name="Hylobates lar",
    local_names={EN: "lar gibbon", PL: "gibon białoręki, gibbon białoręki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hylobates-lar-02-Chiang-Mai.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Hylobates-lar-02-Chiang-Mai.jpg",
        author="Ladislav Král",
        license=License.CC_BY_SA_3_0,
    ),
)
P_PYGMAEUS = Species(
    name="Pongo pygmaeus",
    local_names={EN: "Bornean orangutan", PL: "orangutan borneański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:How_to_peel_a_banana_with_your_foot_(26443349170).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/How_to_peel_a_banana_with_your_foot_%2826443349170%29.jpg",
        author="Thomas Quine",
        license=License.CC_BY_2_0,
    ),
)
G_BLACKI = Species(
    name="Gigantopithecus blacki",
    known_for=[{EN: "speculated species of yeti, bigfoot etc."}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gigantopithecus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Gigantopithecus.png",
        author="Concavenator",
        license=License.CC_BY_SA_4_0,
    ),
)
G_GORILLA = Species(
    name="Gorilla gorilla",
    local_names={EN: "western gorilla", PL: "goryl nizinny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:3972_image2_western_gorilla_MWatson.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/3972_image2_western_gorilla_MWatson.jpg",
        author="Lavgcom",
        license=License.CC_BY_SA_3_0,
    ),
)
P_TROGLODYTES = Species(
    name="Pan troglodytes",
    local_names={EN: "chimpanzee", PL: "szympans zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pan_troglodytes_-_Serengeti-Park_Hodenhagen_14.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/Pan_troglodytes_-_Serengeti-Park_Hodenhagen_14.jpg",
        author="Frank Schwichtenberg",
        license=License.CC_BY_SA_4_0,
    ),
)
P_PANISCUS = Species(
    name="Pan paniscus",
    local_names={EN: "bonobo", PL: "bonobo, szympans karłowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pan_paniscus12.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Pan_paniscus12.jpg",
        author="Pierre Fidenci",
        license=License.CC_BY_SA_2_5,
    ),
)
A_AFARENSIS = Species(
    name="Australopithecus afarensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Australopithecus_afarensis_(%E2%80%9ELucy)_Rekonstruktion.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Australopithecus_afarensis_%28%E2%80%9ELucy%29_Rekonstruktion.jpg",
        author="Neanderthal-Museum, Mettmann",
        license=License.CC_BY_SA_4_0,
    ),
)
H_HABILIS = Species(
    name="Homo habilis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Homo_habilis_-_forensic_facial_reconstruction.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Homo_habilis_-_forensic_facial_reconstruction.png",
        author="Cicero Moraes",
        license=License.CC_BY_SA_4_0,
    ),
)
H_ERECTUS = Species(
    name="Homo erectus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Homo_erectus_Steveoc_86.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Homo_erectus_Steveoc_86.jpg",
        author="Steveoc 86",
        license=License.CC_BY_SA_3_0,
    ),
)
H_NEANDERTHALENSIS = Species(
    name="Homo neanderthalensis",
    local_names={EN: "Neanderthal", PL: "neandertalczyk, człowiek neandertalski"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Le_Moustier_(white_background).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/87/Le_Moustier_%28white_background%29.jpg",
        author="Charles R. Knight",
        license=License.PUBLIC_DOMAIN,
    ),
)
H_SAPIENS = Species(
    name="Homo sapiens",
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Akha_cropped_hires.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Akha_cropped_hires.JPG",
        author="Weltenbummler84",
        license=License.CC_BY_SA_2_0_DE,
    ),
)

HOMO_A = Clade(children=[H_NEANDERTHALENSIS, H_SAPIENS])
HOMO_B = Clade(children=[H_ERECTUS, HOMO_A])

HYLOBATES = Genus(name="Hylobates", children=[H_LAR])
PONGO = Genus(name="Pongo", children=[P_PYGMAEUS])
GIGANTOPITHECUS = Genus(name="Gigantopithecus", children=[G_BLACKI])
GORILLA = Genus(name="Gorilla", children=[G_GORILLA])
PAN = Genus(name="Pan", children=[P_TROGLODYTES, P_PANISCUS])
HOMO = Genus(name="Homo", children=[H_HABILIS, HOMO_B])
AUSTRALOPITHECUS = Genus(
    name="Australopithecus", children=[A_AFARENSIS, HOMO]
)  # anomaly

PANINA = Subtribe(name="Panina", children=[PAN])
HOMININA = Subtribe(name="Hominina", children=[AUSTRALOPITHECUS])

GORILLINI = Tribe(name="Gorillini", children=[GORILLA])
HOMININI = Tribe(name="Hominini", children=[PANINA, HOMININA])

PONGINAE = Subfamily(name="Ponginae", children=[PONGO, GIGANTOPITHECUS])
HOMININAE = Subfamily(name="Homininae", children=[GORILLINI, HOMININI])

HYLOBATIDAE = Family(name="Hylobatidae", children=[HYLOBATES])
HOMINIDAE = Family(name="Hominidae", children=[PONGINAE, HOMININAE])

HOMINOIDEA = Superfamily(name="Hominoidea", children=[HYLOBATIDAE, HOMINIDAE])
