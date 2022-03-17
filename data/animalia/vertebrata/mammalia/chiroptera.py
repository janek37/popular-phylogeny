from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, PL

P_VAMPYRUS = Species(
    name="Pteropus vampyrus",
    local_names={
        EN: "large flying fox, large fruit bat",
        PL: "pies latający, rudawka malajska",
    },
)
D_ROTUNDUS = Species(
    name="Desmodus rotundus",
    local_names={EN: "common vampire bat", PL: "wampir zwyczajny"},
)
P_PIPISTRELLUS = Species(
    name="Pipistrellus pipistrellus",
    local_names={EN: "common pipistrelle", PL: "karlik malutki"},
)
M_LUCIFUGUS = Species(
    name="Myotis lucifugus", local_names={EN: "little brown bat", PL: "nocek myszouchy"}
)
P_AURITUS = Species(
    name="Plecotus auritus",
    local_names={
        EN: "brown long-eared bat, common long-eared bat",
        PL: "gacek wielkouch, gacek brunatny",
    },
)

PTEROPUS = Genus(name="Pteropus", children=[P_VAMPYRUS])
DESMODUS = Genus(name="Desmodus", children=[D_ROTUNDUS])
PIPISTRELLUS = Genus(name="Pipistrellus", children=[P_PIPISTRELLUS])
MYOTIS = Genus(name="Myotis", children=[M_LUCIFUGUS])
PLECOTUS = Genus(name="Plecotus", children=[P_AURITUS])

VESPERTILIONINAE = Subfamily(name="Vespertilioninae", children=[PIPISTRELLUS, PLECOTUS])
MYOTINAE = Subfamily(name="Myotinae", children=[MYOTIS])

PTEROPODIDAE = Family(name="Pteropodidae", children=[PTEROPUS])
PHYLLOSTOMIDAE = Family(name="Phyllostomidae", children=[DESMODUS])
VESPERTILIONIDAE = Family(
    name="Vespertilionidae", children=[VESPERTILIONINAE, MYOTINAE]
)

CHIROPTERA_A = Clade(children=[PHYLLOSTOMIDAE, VESPERTILIONIDAE])

CHIROPTERA = Order(name="Chiroptera", children=[PTEROPODIDAE, CHIROPTERA_A])
