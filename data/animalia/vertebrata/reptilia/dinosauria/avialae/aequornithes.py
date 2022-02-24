from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .pelecaniformes import PELECANIFORMES

G_IMMER = Species(
    name="Gavia immer", local_names={EN: "common loon", PL: "nur lodowiec"}
)
D_EXULANS = Species(
    name="Diomedea exulans",
    local_names={EN: "wandering albatross, snowy albatross", PL: "albatros wędrowny"},
    known_for=[{EN: "the longest wingspan of all birds"}],
)
A_FORSTERI = Species(
    name="Aptenodytes forsteri",
    local_names={EN: "emperor penguin", PL: "pingwin cesarski"},
)
P_ADELIAE = Species(
    name="Pygoscelis adeliae",
    local_names={EN: "Adélie penguin", PL: "pingwin Adeli, pingwin białooki"},
    known_for=[{EN: "penguins from Madagascar franchise"}],
)
P_PAPUA = Species(
    name="Pygoscelis papua",
    local_names={EN: "Gentoo penguin", PL: "pingwin białobrewy"},
    known_for=[{EN: "Gentoo Linux"}],
)
C_CICONIA = Species(
    name="Ciconia ciconia", local_names={EN: "white stork", PL: "bocian biały"}
)
L_CRUMENIFER = Species(
    name="Leptoptilos crumenifer",
    local_names={EN: "marabou stork", PL: "marabut afrykański"},
)
M_BASSANUS = Species(
    name="Morus bassanus",
    local_names={EN: "northern gannet", PL: "głuptak biały, głuptak zwyczajny"},
)
S_LEUCOGASTER = Species(
    name="Sula leucogaster", local_names={EN: "brown booby", PL: "głuptak białobrzuchy"}
)
P_CARBO = Species(
    name="Phalacrocorax carbo",
    local_names={EN: "great cormorant", PL: "kormoran czarny, kormoran zwyczajny"},
)

GAVIA = Genus(name="Gavia", children=[G_IMMER])
DIOMEDEA = Genus(name="Diomedea", children=[D_EXULANS])
APTENODYTES = Genus(name="Aptenodytes", children=[A_FORSTERI])
PYGOSCELIS = Genus(name="Pygoscelis", children=[P_ADELIAE, P_PAPUA])
CICONIA = Genus(name="Ciconia", children=[C_CICONIA])
LEPTOPTILOS = Genus(name="Leptoptilos", children=[L_CRUMENIFER])
MORUS = Genus(name="Morus", children=[M_BASSANUS])
SULA = Genus(name="Sula", children=[S_LEUCOGASTER])
PHALACROCORAX = Genus(name="Phalacrocorax", children=[P_CARBO])

GAVIIDAE = Family(name="Gaviidae", children=[GAVIA])
DIOMEDEIDAE = Family(name="Diomedeidae", children=[DIOMEDEA])
SPHENISCIDAE = Family(name="Spheniscidae", children=[APTENODYTES, PYGOSCELIS])
CICONIIDAE = Family(name="Ciconiidae", children=[CICONIA, LEPTOPTILOS])
SULIDAE = Family(name="Sulidae", children=[MORUS, SULA])
PHALACROCORACIDAE = Family(name="Phalacrocoracidae", children=[PHALACROCORAX])

GAVIIFORMES = Order(name="Gaviiformes", children=[GAVIIDAE])
PROCELLARIIFORMES = Order(name="Procellariiformes", children=[DIOMEDEIDAE])
SPHENISCIFORMES = Order(name="Sphenisciformes", children=[SPHENISCIDAE])
CICONIIFORMES = Order(name="Ciconiiformes", children=[CICONIIDAE])
SULIFORMES = Order(name="Suliformes", children=[SULIDAE, PHALACROCORACIDAE])

PELECANIMORPHAE_A = Clade(children=[SULIFORMES, PELECANIFORMES])

AUSTRODYPTORNITHES = Clade(
    name="Austrodyptornithes", children=[PROCELLARIIFORMES, SPHENISCIFORMES]
)
PELECANIMORPHAE = Clade(
    name="Pelecanimorphae", children=[CICONIIFORMES, PELECANIMORPHAE_A]
)

FERAEQUORNITHES = Clade(
    name="Feraequornithes", children=[AUSTRODYPTORNITHES, PELECANIMORPHAE]
)

AEQUORNITHES = Clade(name="Aequornithes", children=[GAVIIFORMES, FERAEQUORNITHES])
