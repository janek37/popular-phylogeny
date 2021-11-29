from clade import Family, Genus, Order, Species
from constants import EN, PL

from .asteraceae import ASTERACEAE

C_MEDIUM = Species(
    name="Campanula medium",
    local_names={EN: "Canterbury bells", PL: "dzwonek ogrodowy"},
)
C_RAPUNCULUS = Species(
    name="Campanula rapunculus",
    local_names={EN: "rampion bellflower", PL: "dzwonek rapunkuł"},
    known_for=[{EN: "Rapunzel"}],
)

CAMPANULA = Genus(name="Campanula", children=[C_MEDIUM, C_RAPUNCULUS])

CAMPANULACEAE = Family(name="Campanulaceae", children=[CAMPANULA])

ASTERALES = Order(name="Asterales", children=[CAMPANULACEAE, ASTERACEAE])
