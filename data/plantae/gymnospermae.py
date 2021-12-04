from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subfamily
from constants import EN, PL

A_ALBA = Species(
    name="Abies alba", local_names={EN: "silver fir", PL: "jodła pospolita"}
)
P_SILVESTRIS = Species(
    name="Pinus sylvestris",
    local_names={EN: "European red pine", PL: "sosna zwyczajna"},
)
P_ABIES = Species(
    name="Picea abies", local_names={EN: "European spruce", PL: "świerk pospolity"}
)
L_DECIDUA = Species(
    name="Larix decidua", local_names={EN: "European larch", PL: "modrzew europejski"}
)
C_LIBANI = Species(
    name="Cedrus libani", local_names={EN: "Lebanese cedar", PL: "cedr libański"}
)
C_SEMPERVIRENS = Species(
    name="Cupressus sempervirens",
    local_names={EN: "Mediterranean cypress", PL: "cyprys wiecznie zielony"},
)
T_OCCIDENTALIS = Species(
    name="Thuja occidentalis",
    local_names={EN: "northen white cedar", PL: "tuja, żywotnik zachodni"},
)
J_COMMUNIS = Species(
    name="Juniperus communis",
    local_names={PL: "jałowiec pospolity", EN: "common juniper"},
)
S_GIGANTEUM = Species(
    name="Sequoiadendron giganteum",
    local_names={PL: "sekwoja olbrzymia, mamutowiec olbrzymi", EN: "giant sequoia"},
    known_for=[{EN: "the most massive trees on Earth"}],
)
T_BACCATA = Species(
    name="Taxus baccata", local_names={PL: "cis pospolity", EN: "common yew"}
)
G_BILOBA = Species(
    name="Ginkgo biloba", local_names={PL: "miłorząb dwuklapowy", EN: "ginkgo"}
)

ABIES = Genus(name="Abies", children=[A_ALBA])
PINUS = Genus(name="Pinus", children=[P_SILVESTRIS])
PICEA = Genus(name="Picea", children=[P_ABIES])
LARIX = Genus(name="Larix", children=[L_DECIDUA])
CEDRUS = Genus(name="Cedrus", children=[C_LIBANI])
CUPRESSUS = Genus(name="Cupressus", children=[C_SEMPERVIRENS])
THUJA = Genus(name="Thuja", children=[T_OCCIDENTALIS])
JUNIPERUS = Genus(name="Juniperus", children=[J_COMMUNIS])
SEQUOIADENDRON = Genus(name="Sequoiadendron", children=[S_GIGANTEUM])
TAXUS = Genus(name="Taxus", children=[T_BACCATA])
GINKGO = Genus(name="Ginkgo", children=[G_BILOBA])

PINUS_PICEA = Clade(children=[PINUS, PICEA])

PINACEAE_A = Clade(children=[PINUS_PICEA, LARIX])

ABIETOIDEAE = Clade(name="Abietoideae", children=[ABIES, CEDRUS])

CUPRESSUS_JUNIPERUS = Clade(children=[CUPRESSUS, JUNIPERUS])

CUPRESSOIDEAE = Subfamily(name="Cupressoideae", children=[CUPRESSUS_JUNIPERUS, THUJA])

PINACEAE = Family(name="Pinaceae", children=[ABIETOIDEAE, PINACEAE_A])
CUPRESSACEAE = Family(name="Cupressaceae", children=[CUPRESSOIDEAE, SEQUOIADENDRON])
TAXACEAE = Family(name="Taxaceae", children=[TAXUS])
GINKGOACEAE = Family(name="Ginkgoaceae", children=[GINKGO])

CUPRESSALES = Clade(
    name="Cupressales", children=[CUPRESSACEAE, TAXACEAE]
)  # former Order

PINALES = Order(name="Pinales", children=[PINACEAE, CUPRESSALES])
GINKGOALES = Order(name="Ginkgoales", children=[GINKGOACEAE])

PINOPSIDA = Class(name="Pinopsida", children=[PINALES])
GINKGOOPSIDA = Class(name="Ginkgoopsida", children=[GINKGOALES])

PINOPHYTA = Phylum(name="Pinophyta", children=[PINOPSIDA])
GINKGOPHYTA = Phylum(name="Ginkgophyta", children=[GINKGOOPSIDA])

GYMNOSPERMAE = Clade(name="Gymnospermae", children=[PINOPHYTA, GINKGOPHYTA])
