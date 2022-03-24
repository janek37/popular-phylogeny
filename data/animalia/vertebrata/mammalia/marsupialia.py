from clade import Clade, Family, Genus, Infraclass, Order, Species, Suborder, Superorder
from constants import EN, PL

D_VIRGINIANA = Species(
    name="Didelphis virginiana",
    local_names={
        EN: "possum, North Americam opossum, Virginia opossum",
        PL: "opos północny, dydelf wirginijski",
    },
)
O_RUFUS = Species(
    name="Osphranter rufus", local_names={EN: "red kangaroo", PL: "kangur rudy"}
)
P_CINEREUS = Species(
    name="Phascolarctos cinereus", local_names={EN: "koala", PL: "koala australijski"}
)
V_URSINUS = Species(
    name="Vombatus ursinus", local_names={EN: "common vombat", PL: "wombat tasmański"}
)
S_HARRISII = Species(
    name="Sarcophilus harrisii",
    local_names={EN: "Tasmanian devil", PL: "diabeł tasmański"},
)
T_CYNOCEPHALUS = Species(
    name="Thylacinus cynocephalus",
    local_names={
        EN: "Tasmanian tiger, Tasmanian wolf, thylacine",
        PL: "wilk workowaty, wilkowór tasmański",
    },
    extinct=True,
)
P_GUNNII = Species(
    name="Perameles gunnii",
    local_names={EN: "eastern barred bandicoot", PL: "jamraj pręgowany"},
    known_for=[{EN: "Crash Bandicoot"}],
)

DIDELPHIS = Genus(name="Didelphis", children=[D_VIRGINIANA])
OSPHRANTER = Genus(name="Osphranter", children=[O_RUFUS])
PHASCOLARCTOS = Genus(name="Phascolarctos", children=[P_CINEREUS])
VOMBATUS = Genus(name="Vombatus", children=[V_URSINUS])
SARCOPHILUS = Genus(name="Sarcophilus", children=[S_HARRISII])
THYLACINUS = Genus(name="Thylacinus", children=[T_CYNOCEPHALUS])
PERAMELES = Genus(name="Perameles", children=[P_GUNNII])

DIDELPHIDAE = Family(name="Didelphidae", children=[DIDELPHIS])
MACROPODIDAE = Family(name="Macropodidae", children=[OSPHRANTER])
PHASCOLARCTIDAE = Family(name="Phascolarctidae", children=[PHASCOLARCTOS])
VOMBATIDAE = Family(name="Vombatidae", children=[VOMBATUS])
DASYURIDAE = Family(name="Dasyuridae", children=[SARCOPHILUS])
THYLACINIDAE = Family(name="Thylacinidae", children=[THYLACINUS])
PERAMELIDAE = Family(name="Peramelidae", children=[PERAMELES])

MACROPODIFORMES = Suborder(name="Macropodiformes", children=[MACROPODIDAE])
VOMBATIFORMES = Suborder(name="Vombatiformes", children=[PHASCOLARCTIDAE, VOMBATIDAE])

DIDELPHIMORPHIA = Order(name="Didelphimorphia", children=[DIDELPHIDAE])
DIPROTODONTIA = Order(name="Diprotodontia", children=[MACROPODIFORMES, VOMBATIFORMES])
DASYUROMORPHIA = Order(name="Dasyuromorphia", children=[DASYURIDAE, THYLACINIDAE])
PERAMELEMORPHIA = Order(name="Peramelemorphia", children=[PERAMELIDAE])

POLYPROTODONTIA = Clade(
    name="Polyprotodontia", children=[DASYUROMORPHIA, PERAMELEMORPHIA]
)

AUSTRALIDELPHIA = Superorder(
    name="Australidelphia", children=[DIPROTODONTIA, POLYPROTODONTIA]
)

MARSUPIALIA = Infraclass(
    name="Marsupialia", children=[DIDELPHIMORPHIA, AUSTRALIDELPHIA]
)
