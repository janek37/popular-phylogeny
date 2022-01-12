from clade import Family, Genus, Order, Species, Subfamily, Superorder
from constants import EN, LA, PL

E_LUCIUS = Species(
    name="Esox lucius", local_names={EN: "northern pike", PL: "szczupak pospolity"}
)
S_SALAR = Species(
    name="Salmo salar",
    local_names={
        EN: "Atlantic salmon",
        PL: "łosoś pospolity, łosoś atlantycki, łosoś szlachetny",
    },
)
S_TRUTTA = Species(
    name="Salmo trutta",
    local_names={EN: "brown trout"},
    known_for=[
        {
            LA: "Salmo trutta trutta",
            EN: "sea trout",
            PL: "troć wędrowna, troć atlantycka",
        },
        {LA: "Salmo trutta fario", EN: "river trout", PL: "pstrąg potokowy"},
        {LA: "Salmo trutta lacustris", EN: "lake trout", PL: "troć jeziorowa"},
    ],
)
O_MYKISS = Species(
    name="Oncorhynchus mykiss",
    local_names={EN: "rainbow trout", PL: "tęczak, pstrąg tęczowy"},
)
C_ALBULA = Species(
    name="Coregonus albula",
    local_names={EN: "vendace, European cisco", PL: "sielawa europejska"},
)
C_ARTEDI = Species(
    name="Coregonus artedi",
    local_names={EN: "cisco, tullibee", PL: "sielawa amerykańska"},
)

ESOX = Genus(name="Esox", children=[E_LUCIUS])
SALMO = Genus(name="Salmo", children=[S_SALAR, S_TRUTTA])
ONCORHYNCHUS = Genus(name="Oncorhynchus", children=[O_MYKISS])
COREGONUS = Genus(name="Coregonus", children=[C_ALBULA, C_ARTEDI])

SALMONINAE = Subfamily(name="Salmoninae", children=[SALMO, ONCORHYNCHUS])
COREGONINAE = Subfamily(name="Coregoninae", children=[COREGONUS])

ESOCIDAE = Family(name="Esocidae", children=[ESOX])
SALMONIDAE = Family(name="Salmonidae", children=[SALMONINAE, COREGONINAE])

ESOCIFORMES = Order(name="Esociformes", children=[ESOCIDAE])
SALMONIFORMES = Order(name="Salmoniformes", children=[SALMONIDAE])

PROTACANTHOPTERYGII = Superorder(
    name="Protacanthopterygii", children=[ESOCIFORMES, SALMONIFORMES]
)
