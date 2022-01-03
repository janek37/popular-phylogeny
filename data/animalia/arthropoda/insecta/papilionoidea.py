from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN, PL

P_ICARUS = Species(
    name="Polyommatus icarus",
    local_names={EN: "common blue butterfly", PL: "modraszek ikar"},
)
P_MACHAON = Species(
    name="Papilio machaon",
    local_names={
        EN: "common yellow swallowtail, Old World swallowtail",
        PL: "paź królowej",
    },
)
P_GLAUCUS = Species(
    name="Papilio glaucus", local_names={EN: "eastern tiger swallowtail"}
)
P_BRASSICAE = Species(
    name="Pieris brassicae",
    local_names={EN: "large white, cabbage butterfly", PL: "bielinek kapustnik"},
)
G_RHAMNI = Species(
    name="Gonepteryx rhamni",
    local_names={EN: "common brimstone", PL: "latolistek cytrynek"},
)
A_IO = Species(
    name="Aglais io", local_names={EN: "peacock butterfly", PL: "rusałka pawik"}
)
V_ATALANTA = Species(
    name="Vanessa atalanta", local_names={EN: "red admiral", PL: "rusałka admirał"}
)
V_CARDUI = Species(
    name="Vanessa cardui",
    local_names={EN: "painted lady", PL: "rusałka osetnik"},
    known_for=[{EN: "the most widespread of all butterfly species"}],
)
D_PLEXIPPUS = Species(
    name="Danaus plexippus",
    local_names={EN: "monarch butterfly", PL: "monarch, monarcha, danaid wędrowny"},
)

POLYOMMATUS = Genus(name="Polyommatus", children=[P_ICARUS])
PAPILIO = Genus(name="Papilio", children=[P_MACHAON, P_GLAUCUS])
PIERIS = Genus(name="Pieris", children=[P_BRASSICAE])
GONEPTERYX = Genus(name="Gonepteryx", children=[G_RHAMNI])
AGLAIS = Genus(name="Aglais", children=[A_IO])
VANESSA = Genus(name="Vanessa", children=[V_ATALANTA, V_CARDUI])
DANAUS = Genus(name="Danaus", children=[D_PLEXIPPUS])

NYMPHAINE = Subfamily(name="Nymphalinae", children=[AGLAIS, VANESSA])
DANAINAE = Subfamily(name="Danainae", children=[DANAUS])

LYCAENIDAE = Family(name="Lycaenidae", children=[POLYOMMATUS])
PAPILIONIDAE = Family(name="Papilionidae", children=[PAPILIO])
PIERIDAE = Family(name="Pieridae", children=[PIERIS, GONEPTERYX])
NYMPHALIDAE = Family(name="Nymphalidae", children=[NYMPHAINE, DANAINAE])

# https://zookeys.pensoft.net/article/13097/zoom/fig/18/
PAPILIONOIDEA_A = Clade(children=[LYCAENIDAE, NYMPHALIDAE])
PAPILIONOIDEA_B = Clade(children=[PAPILIONOIDEA_A, PIERIDAE])

PAPILIONOIDEA = Superfamily(
    name="Papilionoidea", children=[PAPILIONOIDEA_B, PAPILIONIDAE]
)
