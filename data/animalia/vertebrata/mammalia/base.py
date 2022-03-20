from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Grandorder,
    Infraclass,
    Magnorder,
    Order,
    Species,
    Subclass,
    Superorder,
)
from constants import EN, PL

from .afrotheria import AFROTHERIA
from .chiroptera import CHIROPTERA
from .euarchonta import EUARCHONTA
from .eulipotyphla import EULIPOTYPHLA
from .ferae import FERAE
from .glires import GLIRES
from .marsupialia import MARSUPIALIA
from .ungulata import UNGULATA
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

# Grandorder inside Superorder, but what can I do
FERUNGULATA = Grandorder(name="Ferungulata", children=[UNGULATA, FERAE])

SCROTIPHERA = Clade(name="Scrotiphera", children=[CHIROPTERA, FERUNGULATA])

EUARCHONTOGLIRES = Superorder(name="Euarchontoglires", children=[GLIRES, EUARCHONTA])
LAURASIATHERIA = Superorder(name="Laurasiatheria", children=[EULIPOTYPHLA, SCROTIPHERA])

BOREOEUTHERIA = Magnorder(
    name="Boreoeutheria", children=[EUARCHONTOGLIRES, LAURASIATHERIA]
)

# not certain; it's possible that Afrotheria, Xenarthra and Boreoeutheria
# diverged three ways nearly the same time (trifurcation)
ATLANTOGENATA = Clade(name="Atlantogenata", children=[AFROTHERIA, XENARTHRA])

PLACENTALIA = Infraclass(name="Placentalia", children=[ATLANTOGENATA, BOREOEUTHERIA])

THERIA = Subclass(name="Theria", children=[MARSUPIALIA, PLACENTALIA])

MAMMALIA = Class(name="Mammalia", children=[MONOTREMATA, THERIA])
