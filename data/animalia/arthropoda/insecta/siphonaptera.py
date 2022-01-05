from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

C_CANIS = Species(
    name="Ctenocephalides canis", local_names={EN: "dog flea", PL: "pchła psia"}
)
C_FELIS = Species(
    name="Ctenocephalides felis", local_names={EN: "cat flea", PL: "pchła kocia"}
)
P_IRRITANS = Species(
    name="Pulex irritans", local_names={EN: "human flea", PL: "pchła ludzka"}
)
X_CHEOPIS = Species(
    name="Xenopsylla cheopis",
    local_names={EN: "oriental rat flea", PL: "pchła szczurza"},
    known_for=[{EN: "a primary vector of bubonic plague"}],
)

CTENOCEPHALIDES = Genus(name="Ctenocephalides", children=[C_CANIS, C_FELIS])
PULEX = Genus(name="Pulex", children=[P_IRRITANS])
XENOPSYLLA = Genus(name="Xenopsylla", children=[X_CHEOPIS])

# https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1096-0031.2008.00211.x
PULICIDAE_A = Clade(children=[CTENOCEPHALIDES, PULEX])

PULICIDAE = Family(name="Pulicidae", children=[PULICIDAE_A, XENOPSYLLA])

SIPHONAPTERA = Order(name="Siphonaptera", children=[PULICIDAE])
