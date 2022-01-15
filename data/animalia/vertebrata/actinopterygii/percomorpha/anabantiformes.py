from clade import Family, Genus, Order, Species
from constants import EN, PL

B_SPLENDENS = Species(
    name="Betta splendens",
    local_names={EN: "betta, Siamese fighting fish", PL: "bojownik wspaniały"},
)
O_GORAMY = Species(
    name="Osphronemus goramy", local_names={EN: "giant gouramy", PL: "gurami olbrzymi"}
)
H_TEMMINCKII = Species(
    name="Helostoma temminckii",
    local_names={EN: "kisser, kissing gouramy", PL: "całusek, gurami całujący"},
)

BETTA = Genus(name="Betta", children=[B_SPLENDENS])
OSPHRONEMUS = Genus(name="Osphronemus", children=[O_GORAMY])
HELOSTOMA = Genus(name="Helostoma", children=[H_TEMMINCKII])

OSPHRONEMIDAE = Family(name="Osphronemidae", children=[BETTA, OSPHRONEMUS])
HELOSTOMATIDAE = Family(name="Helostomatidae", children=[HELOSTOMA])

ANABANTIFORMES = Order(name="Anabantiformes", children=[OSPHRONEMIDAE, HELOSTOMATIDAE])
