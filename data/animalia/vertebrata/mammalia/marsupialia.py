from clade import Clade, Family, Genus, Infraclass, Order, Species, Suborder, Superorder
from constants import EN, PL
from image import Image, License

D_VIRGINIANA = Species(
    name="Didelphis virginiana",
    local_names={
        EN: "possum, North Americam opossum, Virginia opossum",
        PL: "opos północny, dydelf wirginijski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Opossum_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/27/Opossum_2.jpg",
        author="Cody Pope",
        license=License.CC_BY_SA_2_5,
    ),
)
O_RUFUS = Species(
    name="Osphranter rufus",
    local_names={EN: "red kangaroo", PL: "kangur rudy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:RedRoo.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/RedRoo.JPG",
        author="Rileypie",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
P_CINEREUS = Species(
    name="Phascolarctos cinereus",
    local_names={EN: "koala", PL: "koala australijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Koala_climbing_tree.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/Koala_climbing_tree.jpg",
        author="Diliff",
        license=License.CC_BY_SA_3_0,
    ),
)
V_URSINUS = Species(
    name="Vombatus ursinus",
    local_names={EN: "common vombat", PL: "wombat tasmański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vombatus_ursinus_-Maria_Island_National_Park.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg",
        author="JJ Harrison (jjharrison89@facebook.com)",
        license=License.CC_BY_SA_3_0,
    ),
)
S_HARRISII = Species(
    name="Sarcophilus harrisii",
    local_names={EN: "Tasmanian devil", PL: "diabeł tasmański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sarcophilus_harrisii_Gould.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Sarcophilus_harrisii_Gould.jpg",
        author="John Gould",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_CYNOCEPHALUS = Species(
    name="Thylacinus cynocephalus",
    local_names={
        EN: "Tasmanian tiger, Tasmanian wolf, thylacine",
        PL: "wilk workowaty, wilkowór tasmański",
    },
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Thylacinus_cynocephalus_white_background.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/26/Thylacinus_cynocephalus_white_background.jpg",
        author="Biodiversity Heritage Library",
        license=License.CC_BY_2_0,
    ),
)
P_GUNNII = Species(
    name="Perameles gunnii",
    local_names={EN: "eastern barred bandicoot", PL: "jamraj pręgowany"},
    known_for=[{EN: "Crash Bandicoot"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Perameles_gunnii_-_Gould.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/10/Perameles_gunnii_-_Gould.jpg",
        author="John Gould",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
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
