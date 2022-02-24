from clade import Class, Family, Genus, Order, Species
from constants import EN, PL

from .marsupialia import MARSUPIALIA

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

MAMMALIA = Class(name="Mammalia", children=[MONOTREMATA, MARSUPIALIA])
