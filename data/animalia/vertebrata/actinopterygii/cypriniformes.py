from clade import Clade, Family, Genus, Order, Species, Subfamily, Superfamily
from constants import EN, IMAGE, PL
from image import Image, License

C_CARPIO = Species(
    name="Cyprinus carpio",
    local_names={EN: "common carp", PL: "karp"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyprinus_carpio_GLERL_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/13/Cyprinus_carpio_GLERL_1.jpg",
        author="United States Great Lakes Environmental Research Laboratory (GLERL)",
        license=License.NOAA,
    ),
)
C_RUBROFUSCUS = Species(
    name="Cyprinus rubrofuscus",
    local_names={EN: "Amur carp", PL: "karp amurski"},
    known_for=[
        {
            EN: "koi",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Ojiya_Nishikigoi_no_Sato_ac_(3).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/10/Ojiya_Nishikigoi_no_Sato_ac_%283%29.jpg",
                author="Asturio Cantabrio",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyprinus_rubrofuscus_Bleeker.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Cyprinus_rubrofuscus_Bleeker.jpg",
        author="Published by Zoologische Mededelingen",
        license=License.CC_BY_3_0,
    ),
)
C_CARASSIUS = Species(
    name="Carassius carassius",
    local_names={EN: "Crucian carp", PL: "karaś pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CarassiusCarassius8.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/CarassiusCarassius8.JPG",
        author="Viridiflavus",
        license=License.CC_BY_SA_3_0,
    ),
)
C_AURATUS = Species(
    name="Carassius auratus",
    local_names={EN: "goldfish", PL: "karaś chiński"},
    known_for=[
        {
            PL: "złota rybka",
            IMAGE: Image(
                url="https://en.wikipedia.org/wiki/File:%E3%83%AF%E3%82%AD%E3%83%B320120701.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/%E3%83%AF%E3%82%AD%E3%83%B320120701.JPG",
                author="ぱたごん",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carassius_auratus6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Carassius_auratus6.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
R_RUTILUS = Species(
    name="Rutilus rutilus",
    local_names={EN: "common roach", PL: "płotka, płoć"},
    known_for=[{EN: "the witcher Geralt's mare"}, {PL: "klacz wiedźmina Geralta"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rutilus_rutilus_Prague_Vltava_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Rutilus_rutilus_Prague_Vltava_3.jpg",
        author="Karelj",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
A_ALBURNUS = Species(
    name="Alburnus alburnus",
    local_names={EN: "common bleak", PL: "ukleja pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Alburnus_alburnus_Hungary.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Alburnus_alburnus_Hungary.jpg",
        author="Harka, Akos",
        license=License.CC_BY_3_0,
    ),
)
S_CEPHALUS = Species(
    name="Squalius cephalus",
    local_names={EN: "common chub, European chub", PL: "kleń"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Squalius_cephalus_Prague_Vltava_1_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Squalius_cephalus_Prague_Vltava_1_%28cropped%29.jpg",
        author="Karelj",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
A_BRAMA = Species(
    name="Abramis brama",
    local_names={EN: "common bream", PL: "leszcz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Braxen,_Iduns_kokbok.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Braxen%2C_Iduns_kokbok.jpg",
        author="Elisabeth Östman",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_PHOXINUS = Species(
    name="Phoxinus phoxinus",
    local_names={EN: "common minnow", PL: "strzebla potokowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phoxinus_phoxinus_f%C3%BCrge_cselle.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Phoxinus_phoxinus_f%C3%BCrge_cselle.jpg",
        author="Zsoldos Márton",
        license=License.CC_BY_SA_3_0,
    ),
)
B_BARBUS = Species(
    name="Barbus barbus",
    local_names={EN: "common barbel", PL: "brzana pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Barbus_barbus1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Barbus_barbus1.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_TITTEYA = Species(
    name="Puntius titteya",
    local_names={EN: "cherry barb", PL: "brzanka wysmukła"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Puntius_titteya-cherry_barb.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3c/Puntius_titteya-cherry_barb.jpg",
        author="Uditha Thejan",
        license=License.CC_BY_SA_4_0,
    ),
)
T_TINCA = Species(
    name="Tinca tinca",
    local_names={EN: "tench, doctor fish", PL: "lin"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_35781_Tinca_vulgaris_--_Tinca.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/FMIB_35781_Tinca_vulgaris_--_Tinca.jpeg",
        author="Felice Supino",
        license=License.FMIB,
    ),
)
G_GOBIO = Species(
    name="Gobio gobio",
    local_names={EN: "gudgeon", PL: "kiełb pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gobio_gobio2_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1e/Gobio_gobio2_%28cropped%29.jpg",
        author="Gilles San Martin",
        license=License.CC_BY_SA_2_0,
    ),
)
C_MACRACANTHUS = Species(
    name="Chromobotia macracanthus",
    local_names={EN: "clown loach, tiger botia", PL: "bocja wspaniała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chromobotia_macracanthus_Bleeker.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Chromobotia_macracanthus_Bleeker.jpg",
        author="Published by Zoologische Mededelingen",
        license=License.CC_BY_3_0,
    ),
)
M_FOSSILIS = Species(
    name="Misgurnus fossilis",
    local_names={EN: "weatherfish", PL: "piskorz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Misgurnus_fossilis_2009_G1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Misgurnus_fossilis_2009_G1.jpg",
        author="George Chernilevsky",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)

CYPRINUS = Genus(name="Cyprinus", children=[C_CARPIO, C_RUBROFUSCUS])
CARASSIUS = Genus(name="Carassius", children=[C_CARASSIUS, C_AURATUS])
RUTILUS = Genus(name="Rutilus", children=[R_RUTILUS])
ALBURNUS = Genus(name="Alburnus", children=[A_ALBURNUS])
SQUALIUS = Genus(name="Squalius", children=[S_CEPHALUS])
ABRAMIS = Genus(name="Abramis", children=[A_BRAMA])
PHOXINUS = Genus(name="Phoxinus", children=[P_PHOXINUS])
BARBUS = Genus(name="Barbus", children=[B_BARBUS])
PUNTIUS = Genus(name="Puntius", children=[P_TITTEYA])
TINCA = Genus(name="Tinca", children=[T_TINCA])
GOBIO = Genus(name="Gobio", children=[G_GOBIO])
CHROMOBOTIA = Genus(name="Chromobotia", children=[C_MACRACANTHUS])
MISGURNUS = Genus(name="Misgurnus", children=[M_FOSSILIS])

CYPRININAE = Subfamily(name="Cyprininae", children=[CYPRINUS, CARASSIUS])
# unresolved, hard to find and conflicting data
LEUCISCINAE = Subfamily(
    name="Leuciscinae", children=[RUTILUS, ALBURNUS, SQUALIUS, ABRAMIS, PHOXINUS]
)
BARBINAE = Subfamily(name="Barbinae", children=[BARBUS, PUNTIUS])
TINCINAE = Subfamily(name="Tincinae", children=[TINCA])
GOBIONINAE = Subfamily(name="Gobioninae", children=[GOBIO])
COBITIDAE = Subfamily(name="Cobitidae", children=[MISGURNUS])

# https://www.researchgate.net/publication/13566245_Phylogenetic_relationships_of_Iberian_cyprinids_Systematic_and_biogeographical_implications
# but not sure
CYPRINIDAE_A = Clade(children=[CYPRININAE, BARBINAE])
CYPRINIDAE_B = Clade(children=[LEUCISCINAE, GOBIONINAE])
CYPRINIDAE_C = Clade(children=[CYPRINIDAE_B, TINCINAE])

CYPRINIDAE = Family(name="Cyprinidae", children=[CYPRINIDAE_A, CYPRINIDAE_C])
BOTIIDAE = Family(name="Botiidae", children=[CHROMOBOTIA])

COBITOIDEA = Superfamily(name="Cobitoidea", children=[BOTIIDAE, COBITIDAE])
CYPRINOIDEA = Superfamily(name="Cyprinoidea", children=[CYPRINIDAE])

CYPRINIFORMES = Order(name="Cypriniformes", children=[CYPRINOIDEA, COBITOIDEA])
