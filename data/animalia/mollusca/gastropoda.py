from clade import (
    Clade,
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
C_KUROSHIMAE = Species(
    name="Costasiella kuroshimae",
    local_names={EN: "leaf slug, leaf sheep", PL: "morska owieczka"},
    known_for=[{EN: "photosyntetic sheep-like sea slug"}],
)
G_ATLANTICUS = Species(
    name="Glaucus atlanticus", local_names={EN: "blue sea dragon", PL: "niebieski smok"}
)
C_ELISABETHINA = Species(
    name="Chromodoris elisabethina",
    known_for={EN: "one of more recognisable nudibranchs"},
)

HELIX = Genus(name="Helix", children=[H_POMATIA])
CORNU = Genus(name="Cornu", children=[C_ASPERSUM])
LIMAX = Genus(name="Limax", children=[L_MAXIMUS])
LISSACHATINA = Genus(name="Lissachatina", children=[L_FULICA])
ELYSIA = Genus(name="Elysia", children=[E_CHLOROTICA])
COSTASIELLA = Genus(name="Costasiella", children=[C_KUROSHIMAE])
GLAUCUS = Genus(name="Glaucus", children=[G_ATLANTICUS])
CHROMODORIS = Genus(name="Chromodoris", children=[C_ELISABETHINA])

HELICININI = Tribe(name="Helicinini", children=[HELIX])
OTALINI = Tribe(name="Otalini", children=[CORNU])

HELICINAE = Subfamily(name="Helicinae", children=[HELICININI, OTALINI])

HELICIDAE = Family(name="Helicidae", children=[HELICINAE])
LIMACIDAE = Family(name="Limacidae", children=[LIMAX])
ACHATINIDAE = Family(name="Achatinidae", children=[LISSACHATINA])
PLAKOBRANCHIDAE = Family(name="Plakobranchidae", children=[ELYSIA])
COSTASIELLIDAE = Family(name="Costasiellidae", children=[COSTASIELLA])
GLAUCIDAE = Family(name="Glaucidae", children=[GLAUCUS])
CHROMODORIDIDAE = Family(name="Chromodorididae", children=[CHROMODORIS])

HELICOIDEA = Superfamily(name="Helicoidea", children=[HELICIDAE])
LIMACOIDEA = Superfamily(name="Limacoidea", children=[LIMACIDAE])
ACHATINOIDEA = Superfamily(name="Achatinoidea", children=[ACHATINIDAE])
PLAKOBRANCHOIDEA = Superfamily(name="Plakobranchoidea", children=[PLAKOBRANCHIDAE])
LIMAPONTIOIDEA = Superfamily(name="Limapontioidea", children=[COSTASIELLIDAE])
AEOLIDIOIDEA = Superfamily(name="Aeolidioidea", children=[GLAUCIDAE])
DORIDOIDEA = Superfamily(name="Doridoidea", children=[CHROMODORIDIDAE])

HELICINA = Suborder(name="Helicina", children=[HELICOIDEA, LIMACOIDEA])
ACHATININA = Suborder(name="Achatinina", children=[ACHATINOIDEA])
CLADOBRANCHIA = Suborder(name="Cladobranchia", children=[AEOLIDIOIDEA])
DORIDINA = Suborder(name="Doridina", children=[DORIDOIDEA])

STYLOMMATOPHORA = Order(name="Stylommatophora", children=[HELICINA, ACHATININA])
NUDIBRANCHIA = Order(name="Nudibranchia", children=[CLADOBRANCHIA, DORIDINA])

EUPULMONATA = Superorder(name="Eupulmonata", children=[STYLOMMATOPHORA])
SACOGLOSSA = Superorder(name="Sacoglossa", children=[PLAKOBRANCHOIDEA, LIMAPONTIOIDEA])
NUDIPLEURA = Superorder(name="Nudipleura", children=[NUDIBRANCHIA])

PANPULMONATA = Clade(
    name="Panpulmonata", children=[EUPULMONATA, SACOGLOSSA]
)  # Subcohort

HETEROBRANCHIA = Subclass(name="Heterobranchia", children=[PANPULMONATA, NUDIPLEURA])
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

P_VULGATA = Species(
    name="Patella vulgata", local_names={EN: "common limpet", PL: "czaszołka pospolita"}
)

PATELLA = Genus(name="Patella", children=[P_VULGATA])

PATELLIDAE = Family(name="Patellidae", children=[PATELLA])

PATELLOGASTROPODA = Subclass(name="Patellogastropoda", children=[PATELLIDAE])

GASTROPODA_A = Clade(children=[HETEROBRANCHIA, CAENOGASTROPODA])

GASTROPODA = Class(name="Gastropoda", children=[GASTROPODA_A, PATELLOGASTROPODA])