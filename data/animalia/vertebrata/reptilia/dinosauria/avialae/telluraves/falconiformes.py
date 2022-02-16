from clade import Family, Genus, Order, Species
from constants import EN, PL

F_PEREGRINUS = Species(
    name="Falco peregrinus", local_names={EN: "peregrine falcon", PL: "sokół wędrowny"}
)
F_TINNUNCULUS = Species(
    name="Falco tinnunculus",
    local_names={EN: "common kestrel, European kestrel", PL: "pustułka zwyczajna"},
)
F_SPARVERIUS = Species(
    name="Falco sparverius",
    local_names={EN: "American kestrel, sparrow hawk", PL: "pustułka amerykańska"},
)
C_PLANCUS = Species(
    name="Caracara plancus",
    local_names={EN: "crested caracara", PL: "karakara czubata"},
)

# unresolved
FALCO = Genus(name="Falco", children=[F_PEREGRINUS, F_TINNUNCULUS, F_SPARVERIUS])
CARACARA = Genus(name="Caracara", children=[C_PLANCUS])

FALCONIDAE = Family(name="Falconidae", children=[FALCO, CARACARA])

FALCONIFORMES = Order(name="Falconiformes", children=[FALCONIDAE])
