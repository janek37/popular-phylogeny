from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL

from .iguania import IGUANIA

P_LATICAUDA = Species(
    name="Phelsuma laticauda",
    local_names={
        EN: "gold dust day gecko",
        PL: "felsuma gruboogonowa, dniówka gruboogonowa",
    },
    known_for=[{EN: "GEICO mascot"}, {EN: "Gex video game series"}],
)
S_SCINCUS = Species(
    name="Scincus scincus",
    local_names={
        EN: "sandfish skink, common skink",
        PL: "ryba piaskowa, scynk aptekarski",
    },
)
L_AGILIS = Species(
    name="Lacerta agilis", local_names={EN: "sand lizard", PL: "jaszczurka zwinka"}
)
V_KOMODOENSIS = Species(
    name="Varanus komodoensis",
    local_names={
        EN: "Komodo dragon, Komodo monitor",
        PL: "smok z Komodo, waran z Komodo",
    },
    known_for=[{EN: "the largest living lizard"}],
)
V_GOULDII = Species(
    name="Varanus gouldii",
    local_names={
        EN: "sand goanna, Gould's monitor",
        PL: "waran piaskowy, waran Goulda",
    },
)
A_FRAGILIS = Species(
    name="Anguis fragilis",
    local_names={EN: "slow worm, deaf adder", PL: "padalec zwyczajny"},
)

PHELSUMA = Genus(name="Phelsuma", children=[P_LATICAUDA])
SCINCUS = Genus(name="Scincus", children=[S_SCINCUS])
LACERTA = Genus(name="Lacerta", children=[L_AGILIS])
VARANUS = Genus(name="Varanus", children=[V_KOMODOENSIS, V_GOULDII])
ANGUIS = Genus(name="Anguis", children=[A_FRAGILIS])

GEKKONIDAE = Family(name="Gekkonidae", children=[PHELSUMA])
SCINCIDAE = Family(name="Scincidae", children=[SCINCUS])
LACERTIDAE = Family(name="Lacertidae", children=[LACERTA])
VARANIDAE = Family(name="Varanidae", children=[VARANUS])
ANGUIDAE = Family(name="Anguidae", children=[ANGUIS])

GEKKOTA = Infraorder(name="Gekkota", children=[GEKKONIDAE])

ANGUIMORPHA = Suborder(name="Anguimorpha", children=[VARANIDAE, ANGUIDAE])

TOXICOFERA = Clade(name="Toxicofera", children=[ANGUIMORPHA, IGUANIA])

SQUAMATA_A = Clade(children=[LACERTIDAE, TOXICOFERA])
SQUAMATA_B = Clade(children=[SCINCIDAE, SQUAMATA_A])
SQUAMATA = Order(name="Squamata", children=[GEKKOTA, SQUAMATA_B])
