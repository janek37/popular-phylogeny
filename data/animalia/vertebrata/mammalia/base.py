from clade import Clade, Class, Family, Genus, Infraclass, Order, Species, Subclass
from constants import EN, PL

from .afrotheria import AFROTHERIA
from .marsupialia import MARSUPIALIA
from .xenarthra import XENARTHRA

O_ANATINUS = Species(
    name="Ornithorhynchus anatinus",
    local_names={EN: "platypus", PL: "dziobak australijski"},
)
T_ACULEATUS = Species(
    name="Tachyglossus aculeatus",
    local_names={EN: "short-beaked echidna", PL: "kolczatka australijska"},
)

ORNITHORHYNCHUS = Genus(name="Ornithorhynchus", children=[O_ANATINUS])
TACHYGLOSSUS = Genus(name="Tachyglossus", children=[T_ACULEATUS])

ORNITHORHYNCHIDAE = Family(name="Ornithorhynchidae", children=[ORNITHORHYNCHUS])
TACHYGLOSSIDAE = Family(name="Tachyglossidae", children=[TACHYGLOSSUS])

MONOTREMATA = Order(name="Monotremata", children=[ORNITHORHYNCHIDAE, TACHYGLOSSIDAE])

# not certain; it's possible that Afrotheria, Xenarthra and Boreoeutheria
# diverged three ways nearly the same time (trifurcation)
ATLANTOGENATA = Clade(name="Atlantogenata", children=[AFROTHERIA, XENARTHRA])

PLACENTALIA = Infraclass(name="Placentalia", children=[ATLANTOGENATA])

THERIA = Subclass(name="Theria", children=[MARSUPIALIA, PLACENTALIA])

MAMMALIA = Class(name="Mammalia", children=[MONOTREMATA, THERIA])
