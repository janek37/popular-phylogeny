from clade import (
    Class,
    Family,
    Genus,
    Order,
    Species,
    Subclass,
    Subfamily,
    Suborder,
    Superfamily,
    Superorder,
    Tribe,
)
from constants import EN, PL

# region HETEROBRANCHIA
H_POMATIA = Species(
    name="Helix pomatia", local_names={EN: "Roman snail", PL: "ślimak winniczek"}
)
C_ASPERSUM = Species(
    name="Cornu aspersum", local_names={EN: "garden snail", PL: "ślimak szary"}
)
L_MAXIMUS = Species(
    name="Limax maximus",
    local_names={EN: "great grey slug, leopard slug", PL: "pomrów wielki"},
)
L_FULICA = Species(
    name="Lissachatina fulica",
    local_names={EN: "giant African snail"},
    known_for=[
        {EN: "one of the largest land snails"},
        {EN: "most invasive snail species"},
        {EN: "giant pet snail"},
    ],
)
E_CHLOROTICA = Species(
    name="Elysia chlorotica",
    local_names={EN: "eastern emerald elysia"},
    known_for=[{EN: "photosynthetic leaf-like sea slug"}],
)

HELIX = Genus(name="Helix", children=[H_POMATIA])
CORNU = Genus(name="Cornu", children=[C_ASPERSUM])
LIMAX = Genus(name="Limax", children=[L_MAXIMUS])
LISSACHATINA = Genus(name="Lissachatina", children=[L_FULICA])
ELYSIA = Genus(name="Elysia", children=[E_CHLOROTICA])

HELICININI = Tribe(name="Helicinini", children=[HELIX])
OTALINI = Tribe(name="Otalini", children=[CORNU])

HELICINAE = Subfamily(name="Helicinae", children=[HELICININI, OTALINI])

HELICIDAE = Family(name="Helicidae", children=[HELICINAE])
LIMACIDAE = Family(name="Limacidae", children=[LIMAX])
ACHATINIDAE = Family(name="Achatinidae", children=[LISSACHATINA])
PLAKOBRANCHIDAE = Family(name="Plakobranchidae", children=[ELYSIA])

HELICOIDEA = Superfamily(name="Helicoidea", children=[HELICIDAE])
LIMACOIDEA = Superfamily(name="Limacoidea", children=[LIMACIDAE])
ACHATINOIDEA = Superfamily(name="Achatinoidea", children=[ACHATINIDAE])
PLAKOBRANCHOIDEA = Superfamily(name="Plakobranchoidea", children=[PLAKOBRANCHIDAE])

HELICINA = Suborder(name="Helicina", children=[HELICOIDEA, LIMACOIDEA])
ACHATININA = Suborder(name="Achatinina", children=[ACHATINOIDEA])

STYLOMMATOPHORA = Order(name="Stylommatophora", children=[HELICINA, ACHATININA])

EUPULMONATA = Superorder(name="Eupulmonata", children=[STYLOMMATOPHORA])
SACOGLOSSA = Superorder(name="Sacoglossa", children=[PLAKOBRANCHOIDEA])

HETEROBRANCHIA = Subclass(name="Heterobranchia", children=[STYLOMMATOPHORA, SACOGLOSSA])
# endregion HETEROBRANCHIA

# region CAENOGASTROPODA
C_TIGRIS = Species(
    name="Cypraea tigris", local_names={EN: "tiger cowrie", PL: "porcelanka tygrysia"}
)
A_GIGAS = Species(
    name="Aliger gigas", local_names={EN: "queen conch", PL: "skrzydelnik wielki"}
)

CYPRAEA = Genus(name="Cypraea", children=[C_TIGRIS])
ALIGER = Genus(name="Aliger", children=[A_GIGAS])

CYPRAEIDAE = Family(name="Cypraeidae", children=[CYPRAEA])
STROMBIDAE = Family(name="Strombidae", children=[ALIGER])

CYPRAEOIDEA = Superfamily(name="Cypraeoidea", children=[CYPRAEIDAE])
STROMBOIDEA = Superfamily(name="Stromboidea", children=[STROMBIDAE])

LITTORINIMORPHA = Order(name="Littorinimorpha", children=[CYPRAEOIDEA, STROMBOIDEA])

CAENOGASTROPODA = Subclass(name="Caenogastropoda", children=[LITTORINIMORPHA])
# endregion

GASTROPODA = Class(name="Gastropoda", children=[HETEROBRANCHIA, CAENOGASTROPODA])
