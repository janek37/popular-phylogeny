from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Tribe
from constants import EN, PL

M_AVELLANARIUS = Species(
    name="Muscardinus avellanarius",
    local_names={EN: "hazel dormouse, common dormouse", PL: "orzesznica leszczynowa"},
    known_for=[{EN: "The Dormouse from Alice in Wonderland"}],
)
G_GLIS = Species(
    name="Glis glis",
    local_names={EN: "European edible dormouse", PL: "popielica szara"},
)
S_VULGARIS = Species(
    name="Sciurus vulgaris",
    local_names={EN: "red squirrel", PL: "wiewiórka ruda, wiewiórka pospolita"},
)
S_CAROLINENSIS = Species(
    name="Sciurus carolinensis",
    local_names={EN: "eastern gray squirrel", PL: "wiewiórka szara"},
)
G_VOLANS = Species(
    name="Glaucomys volans",
    local_names={EN: "southern flying squirrel", PL: "assapan południowy"},
)
P_VOLANS = Species(
    name="Pteromys volans",
    local_names={EN: "Siberian flying squirrel", PL: "polatucha syberyjska"},
)
M_MARMOTA = Species(
    name="Marmota marmota", local_names={EN: "alpine marmot", PL: "świstak alpejski"}
)
M_MONAX = Species(
    name="Marmota monax",
    local_names={EN: "groundhog, woodchuck", PL: "świszcz, świstak amerykański"},
)
T_STRIATUS = Species(
    name="Tamias striatus",
    local_names={EN: "eastern chipmunk", PL: "pręgowiec amerykański"},
)
C_LUDOVICIANUS = Species(
    name="Cynomys ludovicianus",
    local_names={
        EN: "black-tailed prairie dog",
        PL: "piesek preriowy, nieświszczuk czarnoogonowy",
    },
)
S_SUSLICUS = Species(
    name="Spermophilus suslicus",
    local_names={
        EN: "speckled ground squirrel, spotted souslik",
        PL: "suseł perełkowany",
    },
)

MUSCARDINUS = Genus(name="Muscardinus", children=[M_AVELLANARIUS])
GLIS = Genus(name="Glis", children=[G_GLIS])
SCIURUS = Genus(name="Sciurus", children=[S_VULGARIS, S_CAROLINENSIS])
GLAUCOMYS = Genus(name="Glaucomys", children=[G_VOLANS])
PTEROMYS = Genus(name="Pteromys", children=[P_VOLANS])
MARMOTA = Genus(name="Marmota", children=[M_MARMOTA, M_MONAX])
TAMIAS = Genus(name="Tamias", children=[T_STRIATUS])
CYNOMYS = Genus(name="Cynomys", children=[C_LUDOVICIANUS])
SPERMOPHILUS = Genus(name="Spermophilus", children=[S_SUSLICUS])

# https://www.researchgate.net/publication/327823215_Impacts_Of_Inference_Method_And_Dataset_Filtering_On_Phylogenomic_Resolution_In_A_Rapid_Radiation_of_Ground_Squirrels_Xerinae_Marmotini
MARMOTINI_A = Clade(children=[CYNOMYS, SPERMOPHILUS])
MARMOTINI_B = Clade(children=[MARMOTA, MARMOTINI_A])

SCIURINI = Tribe(name="Sciurini", children=[SCIURUS])
PTEROMYINI = Tribe(
    name="Pteromyini",
    children=[GLAUCOMYS, PTEROMYS],
    local_names={EN: "fyling squirrel", PL: "latające wiewiórki, polatuchy"},
)
MARMOTINI = Tribe(name="Marmotini", children=[MARMOTINI_B, TAMIAS])

SCIURINAE = Subfamily(name="Sciurinae", children=[SCIURINI, PTEROMYINI])
XERINAE = Subfamily(name="Xerinae", children=[MARMOTINI])

GLIRIDAE = Family(name="Gliridae", children=[MUSCARDINUS, GLIS])
SCIURIDAE = Family(name="Sciuridae", children=[SCIURINAE, XERINAE])

SCIUROMORPHA = Suborder(name="Sciuromorpha", children=[GLIRIDAE, SCIURIDAE])
