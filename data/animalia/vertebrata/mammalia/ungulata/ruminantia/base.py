from clade import Clade, Family, Genus, Infraorder, Species, Suborder, Superfamily
from constants import EN, PL

from .aegodontia import AEGODONTIA
from .bovinae import BOVINAE
from .cervidae import CERVIDAE

T_JAVANICUS = Species(
    name="Tragulus javanicus",
    local_names={EN: "Java mouse-deer", PL: "kanczyl jawajski"},
    known_for=[{EN: "the smallest living hoofed mammal"}],
)
O_JOHNSTONI = Species(
    name="Okapia johnstoni", local_names={EN: "okapi", PL: "okapi leśne"}
)
G_GIRAFFA = Species(
    name="Giraffa giraffa",
    local_names={EN: "southern giraffe", PL: "żyrafa południowa"},
)
A_AMERICANA = Species(
    name="Antilocapra americana",
    local_names={EN: "pronghorn, American antelope", PL: "widłoróg amerykański"},
)

TRAGULUS = Genus(
    name="Tragulus",
    children=[T_JAVANICUS],
    local_names={EN: "mouse-deer", PL: "myszojeleń, kanczyl"},
)
OKAPIA = Genus(name="Okapia", children=[O_JOHNSTONI])
GIRAFFA = Genus(name="Giraffa", children=[G_GIRAFFA])
ANTILOCAPRA = Genus(name="Antilocapra", children=[A_AMERICANA])

TRAGULIDAE = Family(name="Tragulidae", children=[TRAGULUS])
GIRAFFIDAE = Family(name="Giraffidae", children=[OKAPIA, GIRAFFA])
ANTILOCAPRIDAE = Family(name="Antilocapridae", children=[ANTILOCAPRA])
BOVIDAE = Family(name="Bovidae", children=[BOVINAE, AEGODONTIA])

GIRAFFOIDEA = Superfamily(name="Giraffoidea", children=[GIRAFFIDAE, ANTILOCAPRIDAE])

PECORA_A = Clade(children=[CERVIDAE, BOVIDAE])

PECORA = Infraorder(name="Pecora", children=[GIRAFFOIDEA, PECORA_A])

RUMINANTIA = Suborder(name="Ruminantia", children=[TRAGULIDAE, PECORA])
