from clade import Clade, Family, Genus, Order, Species, Superfamily
from constants import EN, PL

L_DIMIDIATUS = Species(
    name="Labroides dimidiatus",
    local_names={
        EN: "bluestreak cleaner wrasse",
        PL: "wargatek czyściciel, wargatek sanitarnik",
    },
    known_for=[{EN: "Oscar from Shark Tale"}],
)
S_VITREUS = Species(
    name="Sander vitreus", local_names={EN: "walleye", PL: "sandacz amerykański"}
)
S_LUCIOPERCA = Species(
    name="Sander lucioperca",
    local_names={EN: "zander, sander, pikeperch", PL: "sandacz pospolity"},
)
P_FLUVIATILIS = Species(
    name="Perca fluviatilis",
    local_names={EN: "common perch, European perch", PL: "okoń pospolity"},
)
P_VOLITANS = Species(
    name="Pterois volitans",
    local_names={EN: "red lionfish", PL: "skrzydlica pstra, ognica pstra"},
)
P_MARCIDUS = Species(
    name="Psychrolutes marcidus",
    local_names={EN: "smooth-head blobfish"},
    known_for=[{EN: "internet meme"}],
)
S_AURATA = Species(
    name="Sparus aurata", local_names={EN: "gilt-head bream", PL: "dorada"}
)
P_HEPATUS = Species(
    name="Paracanthurus hepatus",
    local_names={
        EN: "regal tang, palette surgeonfish, royal blue tang",
        PL: "chirurg, cyrulik, pokolec królewski",
    },
    known_for=[{EN: "Dory from Finding Nemo"}],
)
S_OCELLATUS = Species(
    name="Sciaenops ocellatus",
    local_names={
        EN: "red drum, redfish, channel/spottail bass, puppy drum",
        PL: "korwin czerwony, kulbak czerwony",
    },
)
P_DIACANTHUS = Species(
    name="Pygoplites diacanthus",
    local_names={EN: "royal angelfish", PL: "ustnik słoneczny"},
)
L_PISCATORIUS = Species(
    name="Lophius piscatorius",
    local_names={
        EN: "European angler or common monkfish",
        PL: "diabeł morski, żabnica nawęd",
    },
)
C_HOLBOELLI = Species(
    name="Ceratias holboelli",
    local_names={EN: "Krøyer's deep sea angler fish", PL: "matronica Holboella"},
)
M_MOLA = Species(
    name="Mola mola",
    local_names={EN: "ocean sunfish, common mola", PL: "mola, samogłów"},
)
T_RUBRIPES = Species(
    name="Takifugu rubripes",
    local_names={EN: "Japanese puffer, tiger puffer, torafugu"},
)
D_HYSTRIX = Species(
    name="Diodon hystrix",
    local_names={
        EN: "spotted porcupinefish, black-spotted porcupinefish",
        PL: "rybojeż, jeżoryb, najeżka, jeżówka, diodon jeżyk",
    },
)
M_SALMOIDES = Species(
    name="Micropterus salmoides",
    local_names={EN: "largemouth bass", PL: "bass wielkogębowy"},
)

LABROIDES = Genus(name="Labroides", children=[L_DIMIDIATUS])
SANDER = Genus(name="Sander", children=[S_VITREUS, S_LUCIOPERCA])
PERCA = Genus(name="Perca", children=[P_FLUVIATILIS])
PTEROIS = Genus(name="Pterois", children=[P_VOLITANS])
PSYCHROLUTES = Genus(name="Psychrolutes", children=[P_MARCIDUS])
SPARUS = Genus(name="Sparus", children=[S_AURATA])
PARACANTHURUS = Genus(name="Paracanthurus", children=[P_HEPATUS])
SCIAENOPS = Genus(name="Sciaenops", children=[S_OCELLATUS])
PYGOPLITES = Genus(name="Pygoplites", children=[P_DIACANTHUS])
LOPHIUS = Genus(name="Lophius", children=[L_PISCATORIUS])
CERATIAS = Genus(name="Ceratias", children=[C_HOLBOELLI])
MOLA = Genus(name="Mola", children=[M_MOLA])
TAKIFUGU = Genus(name="Takifugu", children=[T_RUBRIPES])
DIODON = Genus(name="Diodon", children=[D_HYSTRIX])
MICROPTERUS = Genus(name="Micropterus", children=[M_SALMOIDES])

LABRIDAE = Family(name="Labridae", children=[LABROIDES])
PERCIDAE = Family(name="Percidae", children=[SANDER, PERCA])
SCORPAENIDAE = Family(name="Scorpaenidae", children=[PTEROIS])
PSYCHROLUTIDAE = Family(name="Psychrolutidae", children=[PSYCHROLUTES])
SPARIDAE = Family(name="Sparidae", children=[SPARUS])
ACANTHURIDAE = Family(name="Acanthuridae", children=[PARACANTHURUS])
SCIAENIDAE = Family(name="Sciaenidae", children=[SCIAENOPS])
POMACANTHIDAE = Family(name="Pomacanthidae", children=[PYGOPLITES])
LOPHIIDAE = Family(name="Lophiidae", children=[LOPHIUS])
CERATIIDAE = Family(name="Ceratiidae", children=[CERATIAS])
MOLIDAE = Family(name="Molidae", children=[MOLA])
TETRAODONTIDAE = Family(name="Tetraodontidae", children=[TAKIFUGU])
DIODONTIDAE = Family(name="Diodontidae", children=[DIODON])
CENTRARCHIDAE = Family(name="Centrarchidae", children=[MICROPTERUS])

PERCOIDEA = Superfamily(name="Percoidea", children=[PERCIDAE, CENTRARCHIDAE])

# https://bmcecolevol.biomedcentral.com/articles/10.1186/s12862-017-0958-3
PERCIFORMES_A = Clade(children=[SCORPAENIDAE, PSYCHROLUTIDAE])

TETRAODONTIFORMES_A = Clade(children=[TETRAODONTIDAE, DIODONTIDAE])

LABRIFORMES = Order(name="Labriformes", children=[LABRIDAE])
PERCIFORMES = Order(name="Perciformes", children=[PERCOIDEA, PERCIFORMES_A])
SPARIFORMES = Order(name="Spariformes", children=[SPARIDAE])
ACANTHURIFORMES = Order(name="Acanthuriformes", children=[ACANTHURIDAE, SCIAENIDAE])
LOPHIIFORMES = Order(name="Lophiiformes", children=[LOPHIIDAE, CERATIIDAE])
TETRAODONTIFORMES = Order(
    name="Tetraodontiformes", children=[MOLIDAE, TETRAODONTIFORMES_A]
)

EUPERCARIA_A = Clade(children=[ACANTHURIFORMES, POMACANTHIDAE])
EUPERCARIA_B = Clade(children=[LOPHIIFORMES, TETRAODONTIFORMES])
EUPERCARIA_C = Clade(children=[SPARIFORMES, EUPERCARIA_B])
EUPERCARIA_D = Clade(children=[EUPERCARIA_C, EUPERCARIA_A])
EUPERCARIA_E = Clade(children=[PERCIFORMES, EUPERCARIA_D])
EUPERCARIA = Clade(name="Eupercaria", children=[LABRIFORMES, EUPERCARIA_E])
