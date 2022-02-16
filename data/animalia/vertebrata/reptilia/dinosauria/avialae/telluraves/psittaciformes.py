from clade import Family, Genus, Order, Species, Subfamily, Superfamily, Tribe
from constants import EN, PL

A_MACAO = Species(
    name="Ara macao",
    local_names={EN: "scarlet macaw", PL: "ara czerwona, ara żółtoskrzydła"},
)
A_ARARAUNA = Species(
    name="Ara ararauna", local_names={EN: "blue-and-yellow macaw", PL: "ara ararauna"}
)
C_SPIXII = Species(
    name="Cyanopsitta spixii",
    local_names={EN: "Spix's macaw, little blue macaw", PL: "ara modra"},
)
P_ERITHACUS = Species(
    name="Psittacus erithacus", local_names={EN: "Congo grey parrot", PL: "żako"}
)
M_UNDULATUS = Species(
    name="Melopsittacus undulatus",
    local_names={EN: "budgerigar, common parakeet", PL: "papużka falista"},
)
A_ROSEICOLLIS = Species(
    name="Agapornis roseicollis",
    local_names={EN: "rosy-faced lovebird", PL: "nierozłączka czerwonoczelna"},
)
C_GALERITA = Species(
    name="Cacatua galerita",
    local_names={EN: "sulphur-crested cockatoo", PL: "kakadu żółtoczuba"},
)

ARA = Genus(name="Ara", children=[A_MACAO, A_ARARAUNA])
CYANOPSITTA = Genus(name="Cyanopsitta", children=[C_SPIXII])
PSITTACUS = Genus(name="Psittacus", children=[P_ERITHACUS])
MELOPSITTACUS = Genus(name="Melopsittacus", children=[M_UNDULATUS])
AGAPORNIS = Genus(name="Agapornis", children=[A_ROSEICOLLIS])
CACATUA = Genus(name="Cacatua", children=[C_GALERITA])

ARINI = Tribe(name="Arini", children=[ARA, CYANOPSITTA])
PSITTACINI = Tribe(name="Psittacini", children=[PSITTACUS])

ARINAE = Subfamily(name="Arinae", children=[ARINI])
PSITTACINAE = Subfamily(name="Psittacinae", children=[PSITTACINI])

PSITTACIDAE = Family(name="Psittacidae", children=[ARINAE, PSITTACINAE])
PSITTACULIDAE = Family(name="Psittaculidae", children=[MELOPSITTACUS, AGAPORNIS])
CACATUIDAE = Family(name="Cacatuidae", children=[CACATUA])

PSITTACOIDEA = Superfamily(name="Psittacoidea", children=[PSITTACIDAE, PSITTACULIDAE])
CACATUOIDEA = Superfamily(name="Cacatuoidea", children=[CACATUIDAE])

PSITTACIFORMES = Order(name="Psittaciformes", children=[PSITTACOIDEA, CACATUOIDEA])
