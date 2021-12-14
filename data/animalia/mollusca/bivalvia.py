from clade import Class, Family, Genus, Order, Species, Subclass
from constants import EN, PL

M_MERCENARIA = Species(
    name="Mercenaria mercenaria", local_names={EN: "hard clam, quahog"}
)
S_SOLIDISSIMA = Species(
    name="Spisula solidissima", local_names={EN: "Atlantic surf clam"}
)
T_GIGAS = Species(
    name="Tridacna gigas",
    local_names={EN: "giant clam", PL: "przydacznia olbrzymia"},
    known_for=[{EN: "the largest living bivalve", PL: "największe żyjące małże"}],
)
C_EDULE = Species(
    name="Cerastoderma edule", local_names={EN: "common cockle", PL: "sercówka jadalna"}
)
O_EDULIS = Species(
    name="Ostrea edulis",
    local_names={EN: "European flat oyster", PL: "ostryga jadalna"},
)
M_GIGAS = Species(
    name="Magallana gigas", local_names={EN: "Pacific oyster", PL: "ostryżyca japońska"}
)
P_MAXIMUS = Species(
    name="Pecten maximus",
    local_names={EN: "great scallop, king scallop", PL: "przegrzebek zwyczajny"},
    known_for=[{EN: "Shell logo"}],
)
P_MARGARITIFERA = Species(
    name="Pinctada margaritifera",
    local_names={EN: "black-lip pearl oyster", PL: "perłopław indyjski"},
    known_for=[{EN: "pearl production"}],
)
M_EDULIS = Species(
    name="Mytilus edulis",
    local_names={EN: "blue mussel, common mussel", PL: "omułek jadalny"},
)

MERCENARIA = Genus(name="Mercenaria", children=[M_MERCENARIA])
SPISULA = Genus(name="Spisula", children=[S_SOLIDISSIMA])
TRIDACNA = Genus(name="Tridacna", children=[T_GIGAS])
CERASTODERMA = Genus(name="Cerastoderma", children=[C_EDULE])
OSTREA = Genus(name="Ostrea", children=[O_EDULIS])
MAGALLANA = Genus(name="Magallana", children=[M_GIGAS])
PECTEN = Genus(name="Pecten", children=[P_MAXIMUS])
PINCTADA = Genus(name="Pinctada", children=[P_MARGARITIFERA])
MYTILUS = Genus(name="Mytilus", children=[M_EDULIS])

VENERIDAE = Family(name="Veneridae", children=[MERCENARIA])
MACTRIDAE = Family(name="Mactridae", children=[SPISULA])
CARDIIDAE = Family(name="Cardiidae", children=[TRIDACNA, CERASTODERMA])
OSTREIDAE = Family(name="Ostreidae", children=[OSTREA, MAGALLANA])
PECTINIDAE = Family(name="Pectinidae", children=[PECTEN])
PTERIIDAE = Family(name="Pteriidae", children=[PINCTADA])
MYTILIDAE = Family(name="Mytilidae", children=[MYTILUS])

VENERIDA = Order(name="Venerida", children=[VENERIDAE, MACTRIDAE])
CARDIIDA = Order(name="Cardiida", children=[CARDIIDAE])
OSTREIDA = Order(name="Ostreida", children=[OSTREIDAE])
PECTINIDA = Order(name="Pectinida", children=[PECTINIDAE])
PTERIIDA = Order(name="Pteriida", children=[PTERIIDAE])
MYTILIDA = Order(name="Mytilida", children=[MYTILIDAE])

HETERODONTA = Subclass(name="Heterodonta", children=[VENERIDA, CARDIIDA])
# unresolved
PTERIOMORPHIA = Subclass(
    name="Pteriomorphia", children=[OSTREIDA, PECTINIDA, PTERIIDA, MYTILIDA]
)

BIVALVIA = Class(name="Bivalvia", children=[HETERODONTA, PTERIOMORPHIA])