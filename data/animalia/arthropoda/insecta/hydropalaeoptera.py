from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder, Superorder
from constants import EN, PL

E_DANICA = Species(
    name="Ephemera danica",
    local_names={EN: "green drake mayfly", PL: "jętka duńska, jętka górska"},
)
M_PERMIANA = Species(
    name="Meganeuropsis permiana",
    local_names={EN: "griffinfly"},
    known_for=[{EN: "the largest prehistoric insect"}],
    extinct=True,
)
P_FLAVESCENS = Species(
    name="Pantala flavescens",
    local_names={EN: "globe skimmer, globe wanderer", PL: "nomadka żółtawa"},
)
E_CYATHIGERUM = Species(
    name="Enallagma cyathigerum",
    local_names={EN: "common blue damselfly", PL: "nimfa stawowa"},
)

EPHEMERA = Genus(name="Ephemera", children=[E_DANICA])
MEGANEUROPSIS = Genus(name="Meganeuropsis", children=[M_PERMIANA])
PANTALA = Genus(name="Pantala", children=[P_FLAVESCENS])
ENALLAGMA = Genus(name="Enallagma", children=[E_CYATHIGERUM])

EPHEMERIDAE = Family(name="Ephemeridae", children=[EPHEMERA])
MEGANEURIDAE = Family(name="Meganeuridae", children=[MEGANEUROPSIS])
LIBELLULIDAE = Family(name="Libellulidae", children=[PANTALA])
COENAGRIONIDAE = Family(name="Coenagrionidae", children=[ENALLAGMA])

ANISOPTERA = Infraorder(name="Anisoptera", children=[LIBELLULIDAE])

ZYGOPTERA = Suborder(name="Suborder", children=[COENAGRIONIDAE])

EPHEMEROPTERA = Order(name="Ephemeroptera", children=[EPHEMERIDAE])
MEGANISOPTERA = Order(name="Meganisoptera", children=[MEGANEURIDAE])
ODONATA = Order(name="Odonata", children=[ANISOPTERA, ZYGOPTERA])

ODONATOPTERA = Superorder(name="Euodonatoptera", children=[MEGANISOPTERA, ODONATA])

HYDROPALAEOPTERA = Clade(
    name="Hydropalaeoptera", children=[EPHEMEROPTERA, ODONATOPTERA]
)
