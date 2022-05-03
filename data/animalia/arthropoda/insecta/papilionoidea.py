from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN, PL
from image import Image, License

P_ICARUS = Species(
    name="Polyommatus icarus",
    local_names={EN: "common blue butterfly", PL: "modraszek ikar"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hauhechel-Bl%C3%A4uling,_Polyommatus_icarus_Paarung_3.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f4/Hauhechel-Bl%C3%A4uling%2C_Polyommatus_icarus_Paarung_3.JPG",
        author="Böhringer Friedrich",
        license=License.CC_BY_SA_2_5,
    ),
)
P_MACHAON = Species(
    name="Papilio machaon",
    local_names={
        EN: "common yellow swallowtail, Old World swallowtail",
        PL: "paź królowej",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Papilio_machaon_Mitterbach_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/26/Papilio_machaon_Mitterbach_01.jpg",
        author="Uoaei1",
        license=License.CC_BY_SA_4_0,
    ),
)
P_GLAUCUS = Species(
    name="Papilio glaucus",
    local_names={EN: "eastern tiger swallowtail"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eastern_Tiger_Swallowtail_(Papilio_glaucus)_2019.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Eastern_Tiger_Swallowtail_%28Papilio_glaucus%29_2019.jpg",
        author="Kaldari",
        license=License.CC0,
    ),
)
P_BRASSICAE = Species(
    name="Pieris brassicae",
    local_names={EN: "large white, cabbage butterfly", PL: "bielinek kapustnik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pieris_brassicae_auf_Centaurea_jacea_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0a/Pieris_brassicae_auf_Centaurea_jacea_01.jpg",
        author="Uoaei1",
        license=License.CC_BY_SA_4_0,
    ),
)
G_RHAMNI = Species(
    name="Gonepteryx rhamni",
    local_names={EN: "common brimstone", PL: "latolistek cytrynek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gonepteryx_rhamni_Ledro.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/Gonepteryx_rhamni_Ledro.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
A_IO = Species(
    name="Aglais io",
    local_names={EN: "peacock butterfly", PL: "rusałka pawik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aglais_io_Mitterbach_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Aglais_io_Mitterbach_01.jpg",
        author="Uoaei1",
        license=License.CC_BY_SA_4_0,
    ),
)
V_ATALANTA = Species(
    name="Vanessa atalanta",
    local_names={EN: "red admiral", PL: "rusałka admirał"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vanessa_atalanta_-_Red_admiral_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5c/Vanessa_atalanta_-_Red_admiral_01.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
V_CARDUI = Species(
    name="Vanessa cardui",
    local_names={EN: "painted lady", PL: "rusałka osetnik"},
    known_for=[{EN: "the most widespread of all butterfly species"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vanessa_cardui_197.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1e/Vanessa_cardui_197.jpg",
        author="Anna N Chapman",
        license=License.CC0,
    ),
)
D_PLEXIPPUS = Species(
    name="Danaus plexippus",
    local_names={EN: "monarch butterfly", PL: "monarch, monarcha, danaid wędrowny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Danaus_plexippus_megalippe.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/23/Danaus_plexippus_megalippe.jpg",
        author="NaturaLista.co user: juan_carlos_caicedo_hernandez",
        license=License.CC_BY_4_0,
    ),
)

POLYOMMATUS = Genus(name="Polyommatus", children=[P_ICARUS])
PAPILIO = Genus(name="Papilio", children=[P_MACHAON, P_GLAUCUS])
PIERIS = Genus(name="Pieris", children=[P_BRASSICAE])
GONEPTERYX = Genus(name="Gonepteryx", children=[G_RHAMNI])
AGLAIS = Genus(name="Aglais", children=[A_IO])
VANESSA = Genus(name="Vanessa", children=[V_ATALANTA, V_CARDUI])
DANAUS = Genus(name="Danaus", children=[D_PLEXIPPUS])

NYMPHALINAE = Subfamily(name="Nymphalinae", children=[AGLAIS, VANESSA])
DANAINAE = Subfamily(name="Danainae", children=[DANAUS])

LYCAENIDAE = Family(name="Lycaenidae", children=[POLYOMMATUS])
PAPILIONIDAE = Family(name="Papilionidae", children=[PAPILIO])
PIERIDAE = Family(name="Pieridae", children=[PIERIS, GONEPTERYX])
NYMPHALIDAE = Family(name="Nymphalidae", children=[NYMPHALINAE, DANAINAE])

# https://zookeys.pensoft.net/article/13097/zoom/fig/18/
PAPILIONOIDEA_A = Clade(children=[LYCAENIDAE, NYMPHALIDAE])
PAPILIONOIDEA_B = Clade(children=[PAPILIONOIDEA_A, PIERIDAE])

PAPILIONOIDEA = Superfamily(
    name="Papilionoidea", children=[PAPILIONOIDEA_B, PAPILIONIDAE]
)
