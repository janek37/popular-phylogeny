from clade import Clade, Family, Genus, Order, Species, Superfamily
from constants import EN, PL
from image import Image, License

from .papilionoidea import PAPILIONOIDEA

T_BISSELLIELLA = Species(
    name="Tineola bisselliella",
    local_names={EN: "common clothes moth", PL: "mól odzieżowy, mól włosienniczek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tineola_bisselliella_Piazzo_04.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Tineola_bisselliella_Piazzo_04.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
T_PELLIONELLA = Species(
    name="Tinea pellionella",
    local_names={EN: "case-bearing clothes moth", PL: "mól futrzany, mól kożusznik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:12.027_BF240_Case-bearing_Clothes_Moth,_Tinea_pellionella_(2454551537).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/12.027_BF240_Case-bearing_Clothes_Moth%2C_Tinea_pellionella_%282454551537%29.jpg",
        author="Patrick Clement from West Midlands, England",
        license=License.CC_BY_2_0,
    ),
)
H_PSEUDOSPRETELLA = Species(
    name="Hofmannophila pseudospretella",
    local_names={EN: "brown house moth", PL: "mól nasienniczek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hofmannophila_pseudospretella_(9247368924).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Hofmannophila_pseudospretella_%289247368924%29.jpg",
        author="Donald Hobern from Copenhagen, Denmark",
        license=License.CC_BY_2_0,
    ),
)
P_INTERPUNCTELLA = Species(
    name="Plodia interpunctella",
    local_names={EN: "Indianmeal moth", PL: "mól spożywczy, omacnica spichrzanka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Indianmeal_moth_2009.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Indianmeal_moth_2009.jpg",
        author="Kaldari",
        license=License.CC0,
    ),
)
E_KUEHNIELLA = Species(
    name="Ephestia kuehniella",
    local_names={EN: "Mediterranean flour moth, mill moth", PL: "mklik mączny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:-_6020_%E2%80%93_Ephestia_kuehniella_%E2%80%93_Mediterranean_Flour_Moth_(9984047955).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/-_6020_%E2%80%93_Ephestia_kuehniella_%E2%80%93_Mediterranean_Flour_Moth_%289984047955%29.jpg",
        author="Andy Reago & Chrissy McClarren",
        license=License.CC_BY_2_0,
    ),
)
N_PRONUBA = Species(
    name="Noctua pronuba",
    local_names={EN: "large yellow underwing", PL: "rolnica tasiemka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Noctua_pronuba_(Large_yellow_underwing),_Arnhem,_the_Netherlands.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Noctua_pronuba_%28Large_yellow_underwing%29%2C_Arnhem%2C_the_Netherlands.jpg",
        author="Bj.schoenmakers",
        license=License.CC0,
    ),
)
A_ATROPOS = Species(
    name="Acherontia atropos",
    local_names={EN: "African death's-head hawkmoth", PL: "zmierzchnica trupia główka"},
    known_for=[{EN: "The Silence of the Lambs"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acherontia_Atropos.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cc/Acherontia_Atropos.jpg",
        author="Luca Losito at Italian Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
B_MORI = Species(
    name="Bombyx mori",
    local_names={EN: "domestic silk worm", PL: "jedwabnik morwowy"},
    known_for=[{EN: "silk", PL: "jedwab"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bombyx_mori_4521.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/99/Bombyx_mori_4521.jpg",
        author="Amada44",
        license=License.CC_BY_SA_3_0,
    ),
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
