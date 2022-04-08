from clade import Clade, Family, Genus, Order, Species, Subfamily, Superfamily
from constants import EN, PL

C_CARPIO = Species(name="Cyprinus carpio", local_names={EN: "common carp", PL: "karp"})
C_RUBROFUSCUS = Species(
    name="Cyprinus rubrofuscus",
    local_names={EN: "Amur carp", PL: "karp amurski"},
    known_for=[{EN: "koi", PL: "koi carp"}],
)
C_CARASSIUS = Species(
    name="Carassius carassius", local_names={EN: "Crucian carp", PL: "karaś pospolity"}
)
C_AURATUS = Species(
    name="Carassius auratus",
    local_names={EN: "goldfish", PL: "karaś chiński"},
    known_for=[{PL: "złota rybka"}],
)
R_RUTILUS = Species(
    name="Rutilus rutilus",
    local_names={EN: "common roach", PL: "płotka, płoć"},
    known_for=[{EN: "the witcher Geralt's mare"}, {PL: "klacz wiedźmina Geralta"}],
)
A_ALBURNUS = Species(
    name="Alburnus alburnus", local_names={EN: "common bleak", PL: "ukleja pospolita"}
)
S_CEPHALUS = Species(
    name="Squalius cephalus", local_names={EN: "common chub, European chub", PL: "kleń"}
)
A_BRAMA = Species(name="Abramis brama", local_names={EN: "common bream", PL: "leszcz"})
P_PHOXINUS = Species(
    name="Phoxinus phoxinus", local_names={EN: "common minnow", PL: "strzebla potokowa"}
)
B_BARBUS = Species(
    name="Barbus barbus", local_names={EN: "common barbel", PL: "brzana pospolita"}
)
P_TITTEYA = Species(
    name="Puntius titteya", local_names={EN: "cherry barb", PL: "brzanka wysmukła"}
)
T_TINCA = Species(name="Tinca tinca", local_names={EN: "tench, doctor fish", PL: "lin"})
G_GOBIO = Species(
    name="Gobio gobio", local_names={EN: "gudgeon", PL: "kiełb pospolity"}
)
C_MACRACANTHUS = Species(
    name="Chromobotia macracanthus",
    local_names={EN: "clown loach, tiger botia", PL: "bocja wspaniała"},
)
M_FOSSILIS = Species(
    name="Misgurnus fossilis", local_names={EN: "weatherfish", PL: "piskorz"}
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
