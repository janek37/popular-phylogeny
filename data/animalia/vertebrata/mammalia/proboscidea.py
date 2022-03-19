from clade import (
    Clade,
    Family,
    Genus,
    Order,
    Species,
    Subfamily,
    Suborder,
    Subtribe,
    Superfamily,
    Tribe,
)
from constants import EN, PL

M_LYONSI = Species(name="Moeritherium lyonsi", extinct=True)
B_GRAVE = Species(name="Barytherium grave", extinct=True)
P_GRANGERI = Species(name="Platybelodon grangeri", extinct=True)
D_GIGANTEUM = Species(name="Deinotherium giganteum", extinct=True)
P_BEADNELLI = Species(name="Palaeomastodon beadnelli", extinct=True)
M_AMERICANUM = Species(
    name="Mammut americanum",
    local_names={EN: "American mastodon", PL: "mastodont amerykański"},
    extinct=True,
)
S_ZDANSKYI = Species(name="Stegodon zdanskyi", extinct=True)
S_SYRTICUS = Species(name="Stegotetrabelodon syrticus", extinct=True)
L_AFRICANA = Species(
    name="Loxodonta africana",
    local_names={
        EN: "African bush elephant, African savanna elephant",
        PL: "słoń afrykański",
    },
)
P_ANTIQUUS = Species(
    name="Palaeoloxodon antiquus",
    local_names={EN: "straight-tusked elephant", PL: "słoń leśny"},
    extinct=True,
)
P_FALCONERI = Species(
    name="Palaeoloxodon falconeri",
    local_names={EN: "Maltese pygmy elephant, Sicilian dwarf elephant"},
    known_for=[
        {EN: "possible source of the cyclops myth"},
        {EN: "Mr. Tusks from Dinosaur Comics"},
    ],
    extinct=True,
)
M_PRIMIGENIUS = Species(
    name="Mammuthus primigenius",
    local_names={EN: "woolly mammoth", PL: "mamut włochaty"},
    extinct=True,
)
E_MAXIMUS = Species(
    name="Elephas maximus", local_names={EN: "Asian elephant", PL: "słoń indyjski"}
)

MOERITHERIUM = Genus(name="Moeritherium", children=[M_LYONSI])
BARYTHERIUM = Genus(name="Barytherium", children=[B_GRAVE])
PLATYBELODON = Genus(name="Platybelodon", children=[P_GRANGERI])
DEINOTHERIUM = Genus(name="Deinotherium", children=[D_GIGANTEUM])
PALAEOMASTODON = Genus(name="Palaeomastodon", children=[P_BEADNELLI])
MAMMUT = Genus(name="Mammut", children=[M_AMERICANUM])
STEGODON = Genus(name="Stegodon", children=[S_ZDANSKYI])
STEGOTETRABELODON = Genus(name="Stegotetrabelodon", children=[S_SYRTICUS])
LOXODONTA = Genus(name="Loxodonta", children=[L_AFRICANA])
PALAEOLOXODON = Genus(name="Palaeoloxodon", children=[P_ANTIQUUS, P_FALCONERI])
MAMMUTHUS = Genus(name="Mammuthus", children=[M_PRIMIGENIUS])
ELEPHAS = Genus(name="Elephas", children=[E_MAXIMUS])

ELEPHANTINA = Subtribe(name="Elephantina", children=[MAMMUTHUS, ELEPHAS])

ELEPHANTINI = Tribe(name="Elephantini", children=[ELEPHANTINA, PALAEOLOXODON])

ELEPHANTINAE = Subfamily(name="Elephantinae", children=[LOXODONTA, ELEPHANTINI])

MOERITHERIIDAE = Family(name="Moeritheriidae", children=[MOERITHERIUM])
BARYTHERIIDAE = Family(name="Barytheriidae", children=[BARYTHERIUM])
AMEBELODONTIDAE = Family(name="Amebelodontidae", children=[PLATYBELODON])
DEINOTHERIIDAE = Family(name="Deinotheriidae", children=[DEINOTHERIUM])
PALAEOMASTODONTIDAE = Family(name="Palaeomastodontidae", children=[PALAEOMASTODON])
MAMMUTIDAE = Family(name="Mammutidae", children=[MAMMUT])
STEGODONTIDAE = Family(name="Stegodontidae", children=[STEGODON])
ELEPHANTIDAE = Family(name="Elephantidae", children=[ELEPHANTINAE, STEGOTETRABELODON])

ELEPHANTOIDEA = Superfamily(
    name="Elephantoidea", children=[ELEPHANTIDAE, STEGODONTIDAE]
)

ELEPHANTIDA = Clade(name="Elephantida", children=[ELEPHANTOIDEA, AMEBELODONTIDAE])

ELEPHANTIMORPHA = Clade(name="Elephantimorpha", children=[ELEPHANTIDA, MAMMUTIDAE])

PLESIELEPHANTIFORMES = Suborder(
    name="Plesielephantiformes", children=[BARYTHERIIDAE, DEINOTHERIIDAE]
)
ELEPHANTIFORMES = Suborder(
    name="Elephantiformes", children=[ELEPHANTIMORPHA, PALAEOMASTODONTIDAE]
)

# https://en.wikipedia.org/wiki/Elephant#Evolution_and_extinct_relatives
PROBOSCIDEA_A = Clade(children=[ELEPHANTIFORMES, PLESIELEPHANTIFORMES])

PROBOSCIDEA = Order(name="Proboscidea", children=[PROBOSCIDEA_A, MOERITHERIIDAE])
