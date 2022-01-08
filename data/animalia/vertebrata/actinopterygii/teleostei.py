from clade import Family, Genus, Infraclass, Megacohort, Order, Species, Superorder
from constants import EN, PL

A_ANGUILLA = Species(
    name="Anguilla anguilla", local_names={EN: "European eel", PL: "węgorz europejski"}
)
M_HELENA = Species(
    name="Muraena helena",
    local_names={EN: "Mediterranean moray, Roman eel", PL: "murena śródziemnomorska"},
)
H_ALOSOIDES = Species(name="Hiodon alosoides", local_names={EN: "goldeye"})
A_GIGAS = Species(
    name="Arapaima gigas",
    local_names={EN: "arapaima, pirarucu", PL: "arapaima"},
    known_for=[{EN: "one of the largest freshwater fish"}],
)
G_PETERSII = Species(
    name="Gnathonemus petersii",
    local_names={EN: "Peters's elephantnose fish", PL: "trąbonos, mruk Petersa"},
)

ANGUILLA = Genus(name="Anguilla", children=[A_ANGUILLA])
MURAENA = Genus(name="Muraena", children=[M_HELENA])
HIODON = Genus(name="Hiodon", children=[H_ALOSOIDES])
ARAPAIMA = Genus(name="Arapaima", children=[A_GIGAS])
GNATHONEMUS = Genus(name="Gnathonemus", children=[G_PETERSII])

ANGUILLIDAE = Family(name="Anguillidae", children=[ANGUILLA])
MURAENIDAE = Family(name="Muraenidae", children=[MURAENA])
HIODONTIDAE = Family(name="Hiodontidae", children=[HIODON])
OSTEOGLOSSIDAE = Family(name="Osteoglossidae", children=[ARAPAIMA])
MORMYRIDAE = Family(name="Mormyridae", children=[GNATHONEMUS])

ANGUILLIFORMES = Order(name="Anguilliformes", children=[ANGUILLIDAE, MURAENIDAE])
HIODONTIFORMES = Order(name="Hiodontiformes", children=[HIODONTIDAE])
OSTEOGLOSSIFORMES = Order(
    name="Osteoglossiformes", children=[OSTEOGLOSSIDAE, MORMYRIDAE]
)

ELOPOMORPHA = Superorder(name="Elopomorpha", children=[ANGUILLIFORMES])
OSTEOGLOSSOMORPHA = Superorder(
    name="Osteoglossomorpha", children=[HIODONTIFORMES, OSTEOGLOSSIFORMES]
)

OSTEOGLOSSOCEPHALAI = Megacohort(
    name="Osteoglossocephalai", children=[OSTEOGLOSSOMORPHA]
)

TELEOSTEI = Infraclass(name="Teleostei", children=[ELOPOMORPHA, OSTEOGLOSSOCEPHALAI])
