from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, PL

D_LEUCOTOS = Species(
    name="Dendrocopos leucotos",
    local_names={EN: "white-backed woodpecker", PL: "dzięcioł białogrzbiety"},
)
D_MARTIUS = Species(
    name="Dryocopus martius",
    local_names={EN: "black woodpecker", PL: "dzięcioł czarny"},
)
D_PILEATUS = Species(
    name="Dryocopus pileatus",
    local_names={EN: "pileated woodpecker", PL: "dzięcioł smugoszyi"},
    known_for=[{EN: "Woody Woodpecker"}],
)
M_FORMICIVORUS = Species(
    name="Melanerpes formicivorus",
    local_names={EN: "acorn woodpecker", PL: "dzięciur żołędziowy"},
    known_for=[
        {EN: "trypohobia-triggering granary trees"},
        {EN: "probable inspiration for Woody Woodpecker's signature laugh"},
    ],
)
D_PUBESCENS = Species(
    name="Dryobates pubescens",
    local_names={EN: "downy woodpecker", PL: "dzięcioł kosmaty"},
)
P_VIRIDIS = Species(
    name="Picus viridis",
    local_names={EN: "European green woodpecker", PL: "dzięcioł zielony"},
)
R_TOCO = Species(
    name="Ramphastos toco",
    local_names={
        EN: "toco toucan, common toucan, giant toucan",
        PL: "tukan toko, tukan wielki",
    },
)

DENDROCOPOS = Genus(name="Dendrocopos", children=[D_LEUCOTOS])
DRYOCOPUS = Genus(name="Dryocopus", children=[D_MARTIUS, D_PILEATUS])
MELANERPES = Genus(name="Melanerpes", children=[M_FORMICIVORUS])
DRYOBATES = Genus(name="Dryobates", children=[D_PUBESCENS])
PICUS = Genus(name="Picus", children=[P_VIRIDIS])
RAMPHASTOS = Genus(name="Ramphastos", children=[R_TOCO])

# https://en.wikipedia.org/wiki/Picinae
MELANERPINI_A = Clade(children=[DENDROCOPOS, DRYOBATES])

MELANERPINI = Tribe(name="Melanerpini", children=[MELANERPINI_A, MELANERPES])
PICINI = Tribe(name="Picini", children=[DRYOCOPUS, PICUS])

PICINAE = Subfamily(name="Picinae", children=[MELANERPINI, PICINI])

PICIDAE = Family(name="Picidae", children=[PICINAE])
RAMPHASTIDAE = Family(name="Ramphastidae", children=[RAMPHASTOS])

PICIFORMES = Order(name="Piciformes", children=[PICIDAE, RAMPHASTIDAE])
