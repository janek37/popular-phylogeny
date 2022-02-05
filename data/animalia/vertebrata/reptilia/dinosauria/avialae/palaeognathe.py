from clade import Clade, Family, Genus, Infraclass, Order, Species
from constants import EN, PL

S_CAMELUS = Species(
    name="Struthio camelus",
    local_names={EN: "common ostrich", PL: "struś czerwonoskóry"},
)
D_NOVAEZEALANDIAE = Species(
    name="Dinornis novaezealandiae", local_names={EN: "North Island giant moa"}
)
A_AUSTRALIS = Species(
    name="Apteryx australis",
    local_names={EN: "southern brown kiwi, tokoeka, common kiwi", PL: "kiwi brunatny"},
)
A_MAXIMUS = Species(
    name="Aepyornis maximus",
    local_names={
        EN: "giant elephant-bird",
        PL: "struś madagaskarski, epiornis, mamutak",
    },
    known_for=[{EN: "possible origin of the roc (rukh) myth"}],
)
C_CASUARIUS = Species(
    name="Casuarius casuarius",
    local_names={EN: "southern cassowary", PL: "kazuar hełmiasty"},
)
D_NOVAEHOLLANDIAE = Species(
    name="Dromaius novaehollandiae", local_names={EN: "emu", PL: "emu zwyczajne"}
)

STRUTHIO = Genus(name="Struthio", children=[S_CAMELUS])
DINORNIS = Genus(name="Dinornis", children=[D_NOVAEZEALANDIAE])
APTERYX = Genus(name="Apteryx", children=[A_AUSTRALIS])
AEPYORNIS = Genus(name="Aepyornis", children=[A_MAXIMUS])
CASUARIUS = Genus(name="Casuarius", children=[C_CASUARIUS])
DROMAIUS = Genus(name="Dromaius", children=[D_NOVAEHOLLANDIAE])

STRUTHIONIDAE = Family(name="Struthionidae", children=[STRUTHIO])
DINORNITHIDAE = Family(name="Dinornithidae", children=[DINORNIS])
APTERYGIDAE = Family(name="Apterygidae", children=[APTERYX])
AEPYORNITHIDAE = Family(name="Aepyornithidae", children=[AEPYORNIS])
CASUARIIDAE = Family(name="Casuariidae", children=[CASUARIUS, DROMAIUS])

STRUTHIONIFORMES = Order(name="Struthioniformes", children=[STRUTHIONIDAE])
DINORNITHIFORMES = Order(name="Dinornithiformes", children=[DINORNITHIDAE])
APTERYGIFORMES = Order(name="Apterygiformes", children=[APTERYGIDAE])
AEPYORNITHIFORMES = Order(name="Aepyornithiformes", children=[AEPYORNITHIDAE])
CASUARIIFORMES = Order(name="Casuariiformes", children=[CASUARIIDAE])

NOVAERATITAE_A = Clade(children=[APTERYGIFORMES, AEPYORNITHIFORMES])
NOVAERATITAE = Clade(name="Novaeratitae", children=[NOVAERATITAE_A, CASUARIIFORMES])

NOTOPALAEOGNATHAE = Clade(
    name="Notopalaeognathae", children=[DINORNITHIFORMES, NOVAERATITAE]
)

PALAEOGNATHAE = Infraclass(
    name="Palaeognathae", children=[STRUTHIONIFORMES, NOTOPALAEOGNATHAE]
)
