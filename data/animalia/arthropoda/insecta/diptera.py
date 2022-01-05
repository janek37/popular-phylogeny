from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Order,
    Species,
    Subfamily,
    Suborder,
    Superfamily,
)
from constants import EN, PL

S_ERYTHROCEPHALUM = Species(
    name="Simulium erythrocephalum",
    known_for=[
        {EN: "one of many species of black flies", PL: "jeden z wielu gatunków meszek"}
    ],
)
A_VEXANS = Species(
    name="Aedes vexans",
    local_names={EN: "inland floodwater mosquito", PL: "doskwier pastwiskowy"},
    known_for=[{EN: "one of the most common mosquitos"}],
)
A_GAMBIAE = Species(
    name="Anopheles gambiae",
    known_for=[
        {
            EN: "one of the main malaria vectors in sub-Saharan Africa",
            PL: (
                "gatunek widliszka; "
                "jeden z głównych roznosicieli malarii w Afryce Subsaharyjskiej"
            ),
        }
    ],
)
T_RUTILUS = Species(
    name="Toxorhynchites rutilus",
    local_names={EN: "elephant mosquito, treehole predatory mosquito"},
    known_for=[{EN: "Jurassic Park"}],
)
P_NEARCTICA = Species(
    name="Plecia nearctica", local_names={EN: "lovebug, honeymoon fly"}
)
T_OLERACEA = Species(
    name="Tipula oleracea",
    local_names={EN: "marsh crane fly", PL: "komarnica warzywna, koziułka warzywna"},
)
H_PLUVIALIS = Species(
    name="Haematopota pluvialis",
    local_names={EN: "common horse fly", PL: "mucha końska, jusznica deszczowa"},
)
T_BOVINUS = Species(
    name="Tabanus bovinus", local_names={EN: "pale giant horse-fly", PL: "bąk bydlęcy"}
)
S_RIBESII = Species(
    name="Syrphus ribesii", local_names={EN: "common hoverfly", PL: "bzyg pospolity"}
)
D_MELANOGASTER = Species(
    name="Drosophila melanogaster",
    local_names={EN: "fruit fly", PL: "muszka owocowa, wywilżna karłowata"},
)
G_MORSITANS = Species(
    name="Glossina morsitans",
    local_names={EN: "tsetse fly", PL: "mucha tsetse"},
    known_for=[{EN: "African sleeping sickness", PL: "śpiączka afrykańska"}],
)
M_DOMESTICA = Species(
    name="Musca domestica", local_names={EN: "house fly", PL: "mucha domowa"}
)
L_SERICATA = Species(
    name="Lucilia sericata",
    local_names={EN: "common green bottle fly", PL: "mucha zielona"},
)
S_AFRICA = Species(
    name="Sarcophaga africa",
    known_for=[{EN: "the best known common flesh fly species"}],
)
H_BOVIS = Species(
    name="Hypoderma bovis", local_names={EN: "ox warble fly", PL: "giez bydlęcy duży"}
)

SIMULIUM = Genus(name="Simulium", children=[S_ERYTHROCEPHALUM])
AEDES = Genus(name="Aedes", children=[A_VEXANS])
ANOPHELES = Genus(name="Anopheles", children=[A_GAMBIAE])
TOXORHYNCHITES = Genus(name="Toxorhynchites", children=[T_RUTILUS])
PLECIA = Genus(name="Plecia", children=[P_NEARCTICA])
TIPULA = Genus(name="Tipula", children=[T_OLERACEA])
HAEMATOPOTA = Genus(name="Haematopota", children=[H_PLUVIALIS])
TABANUS = Genus(name="Tabanus", children=[T_BOVINUS])
SYRPHUS = Genus(name="Syrphus", children=[S_RIBESII])
DROSOPHILA = Genus(name="Drosophila", children=[D_MELANOGASTER])
GLOSSINA = Genus(name="Glossina", children=[G_MORSITANS])
MUSCA = Genus(name="Musca", children=[M_DOMESTICA])
LUCILLA = Genus(name="Lucilla", children=[L_SERICATA])
SARCOPHAGA = Genus(name="Sarcophaga", children=[S_AFRICA])
HYPODERMA = Genus(name="Hypoderma", children=[H_BOVIS])

CULCINAE = Subfamily(name="Culcinae", children=[AEDES, TOXORHYNCHITES])
ANOPHELINAE = Subfamily(name="Anophelinae", children=[ANOPHELES])

SIMULIIDAE = Family(name="Simuliidae", children=[SIMULIUM])
CULICIDAE = Family(name="Culicidae", children=[CULCINAE, ANOPHELINAE])
BIBIONIDAE = Family(name="Bibionidae", children=[PLECIA])
TIPULIDAE = Family(name="Tipulidae", children=[TIPULA])
TABANIDAE = Family(name="Tabanidae", children=[HAEMATOPOTA, TABANUS])
SYRPHIDAE = Family(name="Syrphidae", children=[SYRPHUS])
DROSOPHILIDAE = Family(name="Drosophilidae", children=[DROSOPHILA])
GLOSSINIDAE = Family(name="Glossinidae", children=[GLOSSINA])
MUSCIDAE = Family(name="Muscidae", children=[MUSCA])
CALLIPHORIDAE = Family(name="Calliphoridae", children=[LUCILLA])
SARCOPHAGIDAE = Family(name="Sarcophagidae", children=[SARCOPHAGA])
OESTRIDAE = Family(name="Oestridae", children=[HYPODERMA])

MUSCOIDEA = Superfamily(name="Muscoidea", children=[MUSCIDAE])
# unresolved
OESTROIDEA = Superfamily(
    name="Oestroidea", children=[CALLIPHORIDAE, SARCOPHAGIDAE, OESTRIDAE]
)

CALYPTRATAE_A = Clade(children=[MUSCOIDEA, OESTROIDEA])

ACALYPTRATAE = Clade(name="Acalyptratae", children=[DROSOPHILIDAE])  # Subsection
CALYPTRATAE = Clade(
    name="Calyptratae", children=[GLOSSINIDAE, CALYPTRATAE_A]
)  # Subsection

SCHIZOPHORA = Clade(name="Schizophora", children=[ACALYPTRATAE, CALYPTRATAE])  # Section

CULICOMORPHA = Infraorder(name="Culicomorpha", children=[SIMULIIDAE, CULICIDAE])
BIBIONOMORPHA = Infraorder(name="Bibionomorpha", children=[BIBIONIDAE])
MUSCOMORPHA = Infraorder(name="Muscomorpha", children=[SYRPHIDAE, SCHIZOPHORA])

BRACHYCERA = Suborder(name="Brachycera", children=[TABANIDAE, MUSCOMORPHA])

DIPTERA_B = Clade(children=[TIPULIDAE, BRACHYCERA])
DIPTERA_A = Clade(children=[BIBIONOMORPHA, DIPTERA_B])

DIPTERA = Order(name="Diptera", children=[CULICOMORPHA, DIPTERA_A])
