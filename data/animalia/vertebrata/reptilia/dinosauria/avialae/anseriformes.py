from clade import Family, Genus, Order, Species, Subfamily
from constants import EN, LA, PL

A_PLATYRHYNCHOS = Species(
    name="Anas platyrhynchos",
    local_names={EN: "mallard", PL: "kaczka krzyżówka"},
    known_for=[
        {LA: "Anas platyrhynchos domesticus", EN: "domestic duck", PL: "kaczka domowa"}
    ],
)
A_RUBRIPES = Species(
    name="Anas rubripes",
    local_names={EN: "American black duck", PL: "brązówka"},
    known_for=[{EN: "Daffy Duck"}],
)
A_GALERICULATA = Species(
    name="Aix galericulata", local_names={EN: "mandarin duck", PL: "kaczka mandarynka"}
)
A_ANSER = Species(
    name="Anser anser", local_names={EN: "greylag goose", PL: "gęś gęgawa"}
)
C_OLOR = Species(name="Cygnus olor", local_names={EN: "mute swan", PL: "łabędź niemy"})

ANAS = Genus(name="Anas", children=[A_PLATYRHYNCHOS, A_RUBRIPES])
AIX = Genus(name="Aix", children=[A_GALERICULATA])
ANSER = Genus(name="Anser", children=[A_ANSER])
CYGNUS = Genus(name="Cygnus", children=[C_OLOR])

ANATINAE = Subfamily(name="Anatinae", children=[ANAS, AIX])
ANSERINAE = Subfamily(name="Anserinae", children=[ANSER, CYGNUS])

ANATIDAE = Family(name="Anatidae", children=[ANATINAE, ANSERINAE])

ANSERIFORMES = Order(name="Anseriformes", children=[ANATIDAE])
