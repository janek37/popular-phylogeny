from clade import Clade, Class, Family, Genus, Infraphylum, Order, Species, Subphylum
from constants import EN, PL

from .actinopterygii import ACTINOPTERYGII
from .chondrichthyes import CHONDRICHTHYES

# region AGNATHA
M_GLUTINOSA = Species(
    name="Myxine glutinosa",
    local_names={EN: "Atlantic hagfish", PL: "śluzica pospolita"},
)
P_MARINUS = Species(
    name="Petromyzon marinus", local_names={EN: "sea lamprey", PL: "minóg morski"}
)

MYXINE = Genus(name="Myxine", children=[M_GLUTINOSA])
PETROMYZON = Genus(name="Petromyzon", children=[P_MARINUS])

MYXINIDAE = Family(name="Myxinidae", children=[MYXINE])
PETROMYZONTIDAE = Family(name="Petromyzontidae", children=[PETROMYZON])

MYXINIFORMES = Order(name="Myxiniformes", children=[MYXINIDAE])
PETROMYZONTIFORMES = Order(name="Petromyzontiformes", children=[PETROMYZONTIDAE])

MYXINI = Class(name="Myxini", children=[MYXINIFORMES])
HYPEROARTIA = Class(name="Hyperoartia", children=[PETROMYZONTIFORMES])

AGNATHA = Infraphylum(name="Agnatha", children=[MYXINI, HYPEROARTIA])
# endregion AGNATHA

EUTELEOSTOMI = Clade(name="Euteleostomi", children=[ACTINOPTERYGII])

GNATHOSTOMATA = Infraphylum(
    name="Gnathostomata", children=[CHONDRICHTHYES, EUTELEOSTOMI]
)

VERTEBRATA = Subphylum(name="Vertebrata", children=[AGNATHA, GNATHOSTOMATA])
