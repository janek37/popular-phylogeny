from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Infraphylum,
    Order,
    Species,
    Subclass,
    Subphylum,
    Superclass,
)
from constants import EN, PL

from .actinopterygii import ACTINOPTERYGII
from .amphibia import AMPHIBIA
from .chondrichthyes import CHONDRICHTHYES
from .reptilia import REPTILIA

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

# region SARCOPTERYGII
L_CHALUMNAE = Species(
    name="Latimeria chalumnae",
    local_names={EN: "West Indian Ocean coelacanth, gombessa", PL: "latimeria"},
)
N_FORSTERI = Species(
    name="Neoceratodus forsteri",
    local_names={
        EN: "Australian lungfish, Queensland lungfish, Burnett salmon, barramunda",
        PL: "barramunda, rogoząb australijski",
    },
)

LATIMERIA = Genus(name="Latimeria", children=[L_CHALUMNAE])
NEOCERATODUS = Genus(name="Neoceratodus", children=[N_FORSTERI])

LATIMERIIDAE = Family(name="Latimeriidae", children=[LATIMERIA])
NEOCERATODONTIDAE = Family(name="Neoceratodontidae", children=[NEOCERATODUS])

COELACANTHIFORMES = Order(name="Coelacanthiformes", children=[LATIMERIIDAE])
DIPNOI = Order(name="Dipnoi", children=[NEOCERATODONTIDAE])

ACTINISTIA = Subclass(name="Actinistia", children=[COELACANTHIFORMES])

SAUROPSIDA = Clade(name="Sauropsida", children=[REPTILIA])

AMNIOTA = Clade(name="Amniota", children=[SAUROPSIDA])

TETRAPODA = Superclass(name="Tetrapoda", children=[AMPHIBIA, AMNIOTA])

RHIPIDISTIA = Clade(name="Rhipidistia", children=[DIPNOI, TETRAPODA])

SARCOPTERYGII = Clade(name="Sarcopterygii", children=[ACTINISTIA, RHIPIDISTIA])
# endregion SARCOPTERYGII

EUTELEOSTOMI = Clade(name="Euteleostomi", children=[ACTINOPTERYGII, SARCOPTERYGII])

GNATHOSTOMATA = Infraphylum(
    name="Gnathostomata", children=[CHONDRICHTHYES, EUTELEOSTOMI]
)

VERTEBRATA = Subphylum(name="Vertebrata", children=[AGNATHA, GNATHOSTOMATA])
