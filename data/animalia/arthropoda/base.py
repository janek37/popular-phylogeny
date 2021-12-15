from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL

from .arachnida import ARACHNIDA

P_DAVIDIS = Species(
    name="Paradoxides davidis", known_for=[{EN: "one of the largest trilobites"}]
)
L_POLYPHEMUS = Species(
    name="Limulus polyphemus",
    local_names={EN: "Atlantic horseshoe crab", PL: "skrzypłocz"},
)

PARADOXIDES = Genus(name="Paradoxides", children=[P_DAVIDIS])
LIMULUS = Genus(name="Limulus", children=[L_POLYPHEMUS])

PARADOXIDIDAE = Family(name="Paradoxididae", children=[PARADOXIDES])
LIMULIDAE = Family(name="Limulidae", children=[LIMULUS])

REDLICHIIDA = Order(name="Redlichiida", children=[PARADOXIDIDAE])
XIPHOSURA = Order(name="Xiphosura", children=[LIMULIDAE])

TRILOBITA = Class(name="Trilobita", children=[REDLICHIIDA])

CHELICERATA = Subphylum(name="Chelicerata", children=[XIPHOSURA, ARACHNIDA])

ARACHNOMORPHA = Clade(name="Arachnomorpha", children=[TRILOBITA, CHELICERATA])

ARTHROPODA = Phylum(
    name="Arthropoda", children=[ARACHNOMORPHA], local_names={PL: "stawonogi"}
)
