from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL

P_MONODON = Species(
    name="Penaeus monodon",
    local_names={EN: "giant tiger prawn", PL: "krewetka tygrysia"},
)
L_VANNAMEI = Species(
    name="Litopenaeus vannamei",
    local_names={EN: "Pacific white shrimp, King prawn", PL: "krewetka biała"},
)
S_HISPIDUS = Species(
    name="Stenopus hispidus",
    local_names={
        EN: "coral banded shrimp, banded cleaner shrimp",
        PL: "krewetka boksująca",
    },
)
P_BOREALIS = Species(
    name="Pandalus borealis",
    local_names={EN: "northern shrimp, pink shrimp", PL: "krewetka północna"},
)
H_GAMMARUS = Species(
    name="Homarus gammarus",
    local_names={EN: "European lobster", PL: "homar europejski"},
)
N_NORVEGICUS = Species(
    name="Nephrops norvegicus",
    local_names={EN: "Norway lobster, Dublin Bay prawn", PL: "homarzec"},
)
P_ELEPHAS = Species(
    name="Palinurus elephas", local_names={EN: "European spiny lobster", PL: "langusta"}
)
A_ASTACUS = Species(
    name="Astacus astacus",
    local_names={EN: "European crayfish", PL: "rak rzeczny, rak szlachetny"},
)
P_BERNHARDUS = Species(
    name="Pagurus bernhardus",
    local_names={EN: "common hermit crab", PL: "pustelnik bernardyn"},
)
C_PAGURUS = Species(
    name="Cancer pagurus", local_names={EN: "edible/brown crab", PL: "krab kieszeniec"}
)
M_MERCENARIA = Species(
    name="Menippe mercenaria", local_names={EN: "Florida stone crab"}
)
C_SAPIDUS = Species(
    name="Callinectes sapidus",
    local_names={EN: "Atlantic blue crab", PL: "krab błękitny, kalinek błękitny"},
)
B_LATRO = Species(
    name="Birgus latro",
    local_names={
        EN: "coconut crab, robber crab, palm thief",
        PL: "krab kokosowy, krab palmowy",
    },
    known_for=[{EN: "the largest terrestrial arthropod"}, {EN: "Tamatoa from Moana"}],
)

PENAEUS = Genus(name="Penaeus", children=[P_MONODON])
LITOPENAEUS = Genus(name="Litopenaeus", children=[L_VANNAMEI])
STENOPUS = Genus(name="Stenopus", children=[S_HISPIDUS])
PANDALUS = Genus(name="Pandalus", children=[P_BOREALIS])
HOMARUS = Genus(name="Homarus", children=[H_GAMMARUS])
NEPHROPS = Genus(name="Nephrops", children=[N_NORVEGICUS])
PAULINURUS = Genus(name="Paulinurus", children=[P_ELEPHAS])
ASTACUS = Genus(name="Astacus", children=[A_ASTACUS])
PAGURUS = Genus(name="Pagurus", children=[P_BERNHARDUS])
CANCER = Genus(name="Cancer", children=[C_PAGURUS])
MENIPPE = Genus(name="Menippe", children=[M_MERCENARIA])
CALLINECTES = Genus(name="Callinectes", children=[C_SAPIDUS])
BIRGUS = Genus(name="Birgus", children=[B_LATRO])

PENAEIDAE = Family(name="Penaeidae", children=[PENAEUS, LITOPENAEUS])
STENOPODIDAE = Family(name="Stenopodidae", children=[STENOPUS])
PANDALIDAE = Family(name="Pandalidae", children=[PANDALUS])
NEPHROPIDAE = Family(name="Nephropidae", children=[HOMARUS, NEPHROPS])
PALINURIDAE = Family(name="Palinuridae", children=[PAULINURUS])
ASTACIDAE = Family(name="Astacidae", children=[ASTACUS])
PAGURIDAE = Family(name="Paguridae", children=[PAGURUS])
CANCRIDAE = Family(name="Cancridae", children=[CANCER])
PORTUNIDAE = Family(name="Portunidae", children=[CALLINECTES])
COENOBITIDAE = Family(name="Coenobitidae", children=[BIRGUS])

HETEROTREMATA_A = Clade(
    children=[MENIPPE, PORTUNIDAE]
)  # Menippidae is not monophyletic
HETEROTREMATA = Clade(
    name="Heterotremata", children=[CANCRIDAE, HETEROTREMATA_A]
)  # Subsection

EUBRACHYURA = Clade(name="Eubrachyura", children=[HETEROTREMATA])  # Section

STENOPODIDEA = Infraorder(name="Stenopodidea", children=[STENOPODIDAE])
CARIDEA = Infraorder(name="Caridea", children=[PANDALIDAE])
ASTACIDEA = Infraorder(name="Astacidea", children=[NEPHROPIDAE, ASTACIDAE])
ACHELATA = Infraorder(name="Achelata", children=[PALINURIDAE])
ANOMURA = Infraorder(name="Anomura", children=[PAGURIDAE, COENOBITIDAE])
BRACHYURA = Infraorder(name="Brachyura", children=[EUBRACHYURA])

PLEOCYEMATA_A = Clade(children=[STENOPODIDEA, CARIDEA])
REPTANTIA_A = Clade(children=[ASTACIDEA, ACHELATA])
REPTANTIA_B = Clade(children=[ANOMURA, BRACHYURA])
REPTANTIA = Clade(name="Reptantia", children=[REPTANTIA_A, REPTANTIA_B])

DENDROBRANCHIATA = Suborder(name="Dendrobranchiata", children=[PENAEIDAE])
PLEOCYEMATA = Suborder(name="Pleocyemata", children=[PLEOCYEMATA_A, REPTANTIA])

DECAPODA = Order(name="Decapoda", children=[DENDROBRANCHIATA, PLEOCYEMATA])
