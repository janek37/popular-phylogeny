from clade import Clade, Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL

O_VULGARIS = Species(
    name="Octopus vulgaris",
    local_names={EN: "common octopus", PL: "ośmiornica zwyczajna"},
)
G_UMBELLATA = Species(
    name="Grimpoteuthis umbellata",
    local_names={EN: "dumbo octopus"},
    known_for={EN: "swims using ear-like fins"},
)
V_INFERNALIS = Species(
    name="Vampyroteuthis infernalis",
    local_names={EN: "vampire squid", PL: "wampirnica, wampirzyca piekielna"},
)
L_VULGARIS = Species(
    name="Loligo vulgaris",
    local_names={EN: "European squid, common squid", PL: "kalmar pospolity"},
)
A_DUX = Species(
    name="Architeuthis dux",
    local_names={EN: "giant squid", PL: "kałamarnica olbrzymia"},
)
M_HAMILTONI = Species(
    name="Mesonychoteuthis hamiltoni",
    local_names={EN: "colossal squid", PL: "kałamarnica kolosalna"},
)
D_GIGAS = Species(
    name="Dosidicus gigas",
    local_names={EN: "Humboldt squid", PL: "kałamarnica Humboldta"},
)
S_OFFICINALIS = Species(
    name="Sepia officinalis",
    local_names={EN: "common cuttlefish", PL: "mątwa zwyczajna"},
)
N_POMPILIUS = Species(
    name="Nautilus pompilius",
    local_names={EN: "chambered nautilus, pearly nautilus", PL: "łodzik piękny"},
)
P_SEPPENRADENSIS = Species(
    name="Parapuzosia seppenradensis", known_for=[{EN: "the largest known ammonite"}]
)

OCTOPUS = Genus(name="Octopus", children=[O_VULGARIS])
GRIMPOTEUTHIS = Genus(name="Grimpoteuthis", children=[G_UMBELLATA])
VAMPYROTEUTHIS = Genus(name="Vampyroteuthis", children=[V_INFERNALIS])
LOLIGO = Genus(name="Loligo", children=[L_VULGARIS])
ARCHITEUTHIS = Genus(name="Architeuthis", children=[A_DUX])
MESONYCHOTEUTHIS = Genus("Mesonychoteuthis", children=[M_HAMILTONI])
DOSIDICUS = Genus(name="Dosidicus", children=[D_GIGAS])
SEPIA = Genus(name="Sepia", children=[S_OFFICINALIS])
NAUTILUS = Genus(name="Nautilus", children=[N_POMPILIUS])
PARAPUZOSIA = Genus(name="Parapuzosia", children=[P_SEPPENRADENSIS])

OCTOPODIDAE = Family(name="Octopodidae", children=[OCTOPUS])
OPISTHOTEUTHIDAE = Family(name="Opisthoteuthidae", children=[GRIMPOTEUTHIS])
VAMPYROTEUTHIDAE = Family(name="Vampyroteuthidae", children=[VAMPYROTEUTHIS])
LOLIGINIDAE = Family(name="Loliginidae", children=[LOLIGO])
ARCHITEUTHIDAE = Family(name="Architeuthidae", children=[ARCHITEUTHIS])
CRANCHIIDAE = Family(name="Cranchiidae", children=[MESONYCHOTEUTHIS])
OMMASTREPHIDAE = Family(name="Ommastrephidae", children=[DOSIDICUS])
SEPIIDAE = Family(name="Sepiidae", children=[SEPIA])
NAUTILIDAE = Family(name="Nautilidae", children=[NAUTILUS])
DESMOCERATIDAE = Family(name="Desmoceratidae", children=[PARAPUZOSIA])

OCTOPODA = Order(name="Octopoda", children=[OCTOPODIDAE, OPISTHOTEUTHIDAE])
VAMPYROMORPHIDA = Order(name="Vampyromorphida", children=[VAMPYROTEUTHIDAE])
MYOPSIDA = Order(name="Myopsida", children=[LOLIGINIDAE])
NAUTILIDA = Order(name="Nautilida", children=[NAUTILIDAE])
AMMONITIDA = Order(name="Ammonitida", children=[DESMOCERATIDAE])

DECAPODIFORMES_A = Clade(children=[ARCHITEUTHIDAE, CRANCHIIDAE])
DECAPODIFORMES_B = Clade(children=[DECAPODIFORMES_A, OMMASTREPHIDAE])
DECAPODIFORMES_C = Clade(children=[MYOPSIDA, SEPIIDAE])

OCTOPODIFORMES = Superorder(name="Octopodiformes", children=[OCTOPODA, VAMPYROMORPHIDA])
DECAPODIFORMES = Superorder(
    name="Decapodiformes", children=[DECAPODIFORMES_C, DECAPODIFORMES_B]
)

COLEOIDEA = Subclass(name="Coleoidea", children=[OCTOPODIFORMES, DECAPODIFORMES])
NAUTILOIDEA = Subclass(name="Nautiloidea", children=[NAUTILIDA])
AMMONOIDEA = Subclass(name="Ammonoidea", children=[AMMONITIDA])

# https://www.digitalatlasofancientlife.org/learn/mollusca/cephalopoda/ammonoidea/
CEPHALOPODA_A = Clade(children=[COLEOIDEA, AMMONOIDEA])

CEPHALOPODA = Class(name="Cephalopoda", children=[CEPHALOPODA_A, NAUTILOIDEA])
