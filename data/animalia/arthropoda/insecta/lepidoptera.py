from clade import Clade, Family, Genus, Order, Species, Superfamily
from constants import EN, PL

from .papilionoidea import PAPILIONOIDEA

T_BISSELLIELLA = Species(
    name="Tineola bisselliella",
    local_names={EN: "common clothes moth", PL: "mól odzieżowy, mól włosienniczek"},
)
T_PELLIONELLA = Species(
    name="Tinea pellionella",
    local_names={EN: "case-bearing clothes moth", PL: "mól futrzany, mól kożusznik"},
)
H_PSEUDOSPRETELLA = Species(
    name="Hofmannophila pseudospretella",
    local_names={EN: "brown house moth", PL: "mól nasienniczek"},
)
P_INTERPUNCTELLA = Species(
    name="Plodia interpunctella",
    local_names={EN: "Indianmeal moth", PL: "mól spożywczy, omacnica spichrzanka"},
)
E_KUEHNIELLA = Species(
    name="Ephestia kuehniella",
    local_names={EN: "Mediterranean flour moth, mill moth", PL: "mklik mączny"},
)
N_PRONUBA = Species(
    name="Noctua pronuba",
    local_names={EN: "large yellow underwing", PL: "rolnica tasiemka"},
)
A_ATROPOS = Species(
    name="Acherontia atropos",
    local_names={EN: "African death's-head hawkmoth", PL: "zmierzchnica trupia główka"},
    known_for=[{EN: "The Silence of the Lambs"}],
)
B_MORI = Species(
    name="Bombyx mori", local_names={EN: "domestic silk worm", PL: "jedwabnik morwowy"}
)

TINEOLA = Genus(name="Tineola", children=[T_BISSELLIELLA])
TINEA = Genus(name="Tinea", children=[T_PELLIONELLA])
HOFMANNOPHILA = Genus(name="Hofmannophila", children=[H_PSEUDOSPRETELLA])
PLODIA = Genus(name="Plodia", children=[P_INTERPUNCTELLA])
EPHESTIA = Genus(name="Ephestia", children=[E_KUEHNIELLA])
NOCTUA = Genus(name="Noctua", children=[N_PRONUBA])
ACHERONTIA = Genus(name="Acherontia", children=[A_ATROPOS])
BOMBYX = Genus(name="Bombyx", children=[B_MORI])

TINEIDAE = Family(name="Tineidae", children=[TINEOLA, TINEA])
OECOPHORIDAE = Family(name="Oecophoridae", children=[HOFMANNOPHILA])
PYRALIDAE = Family(name="Pyralidae", children=[PLODIA, EPHESTIA])
NOCTUIDAE = Family(name="Noctuidae", children=[NOCTUA])
SPHINGIDAE = Family(name="Sphingidae", children=[ACHERONTIA])
BOMBYCIDAE = Family(name="Bombycidae", children=[BOMBYX])

PYRALOIDEA = Superfamily(name="Pyraloidea", children=[PYRALIDAE])
NOCTUOIDEA = Superfamily(name="Noctuoidea", children=[NOCTUIDAE])
BOMBYCOIDEA = Superfamily(name="Bombycoidea", children=[SPHINGIDAE, BOMBYCIDAE])

MACROHETEROCERA = Clade(name="Macroheterocera", children=[NOCTUOIDEA, BOMBYCOIDEA])
# unresolved, conflicting data
OBTECTOMERA = Clade(
    name="Obtectomera", children=[PYRALOIDEA, MACROHETEROCERA, PAPILIONOIDEA]
)
APODITRYSIA = Clade(name="Apoditrysia", children=[OECOPHORIDAE, OBTECTOMERA])

LEPIDOPTERA = Order(name="Lepidoptera", children=[TINEIDAE, APODITRYSIA])
