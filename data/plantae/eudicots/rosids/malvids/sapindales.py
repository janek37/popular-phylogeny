from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, PL

C_HABESSINICA = Species(
    name="Commiphora habessinica",
    local_names={EN: "Abyssinian myrrh", PL: "balsamowiec mirra"},
    known_for=[{EN: "myrrh", PL: "mirra"}],
)
A_OCCIDENTALE = Species(
    name="Anacardium occidentale",
    local_names={EN: "cashew", PL: "nerkowiec, nanercz zachodni"},
)
M_INDICA = Species(
    name="Mangifera indica", local_names={EN: "mango", PL: "mango indyjskie"}
)
S_MOLLE = Species(
    name="Schinus molle",
    local_names={EN: "Peruvian pepper tree", PL: "schinus peruwiański"},
    known_for=[{EN: "pink peppercorn", PL: "pieprz czerwony"}],
)
P_VERA = Species(
    name="Pistacia vera", local_names={EN: "pistacchio", PL: "pistacja właściwa"}
)
T_RADICANS = Species(
    name="Toxicodendron radicans",
    local_names={EN: "(eastern) poison ivy", PL: "trujący bluszcz, sumak pnący"},
)
A_HIPPOCASTANUM = Species(
    name="Aesculus hippocastanum",
    local_names={EN: "horse chestnut", PL: "kasztanowiec pospolity"},
)
A_PSEUDOPLATANUS = Species(
    name="Acer pseudoplatanus", local_names={EN: "sycamore", PL: "klon jawor"}
)
A_PLATANOIDES = Species(
    name="Acer platanoides", local_names={EN: "Norway maple", PL: "klon zwyczajny"}
)
A_SACCHARUM = Species(
    name="Acer saccharum",
    local_names={EN: "sugar mapple", PL: "klon cukrowy"},
    known_for=[{EN: "maple syrup", PL: "syrop klonowy"}],
)
L_CHINENSIS = Species(
    name="Litchi chinensis", local_names={EN: "lychee", PL: "liczi chińskie"}
)
P_CUPANA = Species(
    name="Paullinia cupana", local_names={EN: "guaraná", PL: "paulinia guarana"}
)
C_SINENSIS = Species(
    name="Citrus × sinensis", local_names={EN: "sweet orange", PL: "pomarańcza chińska"}
)
C_LIMON = Species(
    name="Citrus limon", local_names={EN: "lemon", PL: "cytryna zwyczajna"}
)
C_PARADISI = Species(
    name="Citrus × paradisi", local_names={EN: "grapefruit", PL: "grejpfrut"}
)
C_MAXIMA = Species(
    name="Citrus maxima", local_names={EN: "pomelo", PL: "pomelo, pomarańcza olbrzymia"}
)
C_AURANTIIFOLIA = Species(
    name="Citrus × aurantiifolia",
    local_names={EN: "key lime", PL: "limonka, limetka, lima"},
)
C_RETICULATA = Species(
    name="Citrus reticulata", local_names={EN: "mandarin orange", PL: "mandarynka"}
)
C_TANGERINA = Species(
    name="Citrus x tangerina", local_names={EN: "tangerine", PL: "mandarynka"}
)
C_CLEMENTINA = Species(
    name="Citrus × clementina", local_names={EN: "clementine", PL: "klementynka"}
)
C_JAPONICA = Species(name="Citrus japonica", local_names={EN: "kumquat", PL: "kumkwat"})
Z_BUNGEANUM = Species(
    name="Zanthoxylum bungeanum",
    local_names={
        EN: "Sichuan/Szechuan pepper",
        PL: "pieprz syczuanski, żółtodrzew Bungego",
    },
    known_for=[{EN: "Szechuan sauce"}],
)

ACER_SECTION_ACER = Clade(
    name="Acer sect. Acer", children=[A_PSEUDOPLATANUS, A_SACCHARUM]
)  # Section

CORE_CITRUSES = Clade(
    children=[
        C_SINENSIS,
        C_LIMON,
        C_PARADISI,
        C_MAXIMA,
        C_AURANTIIFOLIA,
        C_RETICULATA,
        C_TANGERINA,
        C_CLEMENTINA,
        C_JAPONICA,
    ]
)

COMMIPHORA = Genus(name="Commiphora", children=[C_HABESSINICA])
ANACARDIUM = Genus(name="Anacardium", children=[A_OCCIDENTALE])
MANGIFERA = Genus(name="Mangifera", children=[M_INDICA])
SCHINUS = Genus(name="Schinus", children=[S_MOLLE])
PISTACIA = Genus(name="Pistacia", children=[P_VERA])
TOXICODENDRON = Genus(name="Toxicodendron", children=[T_RADICANS])
AESCULUS = Genus(name="Aesculus", children=[A_HIPPOCASTANUM])
ACER = Genus(name="Acer", children=[ACER_SECTION_ACER, A_PLATANOIDES])
LITCHI = Genus(name="Litchi", children=[L_CHINENSIS])
PAULINIA = Genus(name="Paulinia", children=[P_CUPANA])
CITRUS = Genus(name="Citrus", children=[CORE_CITRUSES, C_JAPONICA])
ZANTHOXYLUM = Genus(name="Zanthoxylum", children=[Z_BUNGEANUM])

# https://www.researchgate.net/publication/323561612_Anacardiaceae_Phylogeny_Poster_2018
ANACORDIOIDEAE_A = Clade(children=[ANACARDIUM, MANGIFERA])
ANACORDIOIDEAE_B = Clade(children=[TOXICODENDRON, PISTACIA])
ANACORDIOIDEAE_C = Clade(children=[ANACORDIOIDEAE_B, SCHINUS])

ANACARDIOIDEAE = Subfamily(
    name="Anacardioideae", children=[ANACORDIOIDEAE_A, ANACORDIOIDEAE_C]
)
HIPPOCASTANOIDEAE = Subfamily(name="Hippocastanoideae", children=[AESCULUS, ACER])
SAPINDOIDEAE = Subfamily(name="Sapindoideae", children=[LITCHI, PAULINIA])
AURANTIOIDEAE = Subfamily(name="Aurantioideae", children=[CITRUS])
ZANTHOXYLOIDEAE = Subfamily(name="Zanthoxyloideae", children=[ZANTHOXYLUM])

BURSERACEAE = Family(name="Burseraceae", children=[COMMIPHORA])
ANACARDIACEAE = Family(name="Anacardiaceae", children=[ANACARDIOIDEAE])
SAPINDACEAE = Family(name="Sapindaceae", children=[HIPPOCASTANOIDEAE, SAPINDOIDEAE])
RUTACEAE = Family(name="Rutaceae", children=[AURANTIOIDEAE, ZANTHOXYLOIDEAE])

# https://www.researchgate.net/publication/311503129_An_Expanded_Nuclear_Phylogenomic_PCR_Toolkit_for_Sapindales
SAPINDALES_A = Clade(children=[BURSERACEAE, ANACARDIACEAE])
SAPINDALES_B = Clade(children=[SAPINDACEAE, RUTACEAE])

SAPINDALES = Order(name="Sapindales", children=[SAPINDALES_A, SAPINDALES_B])
