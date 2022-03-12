from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Parvorder,
    Species,
    Suborder,
    Superfamily,
)
from constants import EN, PL

H_CRISTATA = Species(
    name="Hystrix cristata",
    local_names={EN: "crested porcupine", PL: "jeżozwierz afrykański"},
)
H_GLABER = Species(
    name="Heterocephalus glaber",
    local_names={EN: "naked mole-rat", PL: "golec piaskowy"},
)
E_DORSATUM = Species(
    name="Erethizon dorsatum",
    local_names={EN: "North American porcupine", PL: "urson amerykański"},
)
C_PORCELLUS = Species(
    name="Cavia porcellus",
    local_names={
        EN: "domestic guinea pig, domestic cavy",
        PL: "świnka morska, kawia domowa",
    },
)
H_HYDROCHAERIS = Species(
    name="Hydrochoerus hydrochaeris",
    local_names={EN: "greater capybara", PL: "kapibara wielka"},
)
C_LANIGERA = Species(
    name="Chinchilla lanigera",
    local_names={
        EN: "long-tailed chinchilla, coastal/common/lesser chinchilla",
        PL: "szynszyla mała",
    },
)
M_COYPUS = Species(
    name="Myocastor coypus", local_names={EN: "nutria, coypu", PL: "nutria amerykańska"}
)
O_DEGUS = Species(
    name="Octodon degus", local_names={EN: "common degu", PL: "koszatniczka pospolita"}
)

HYSTRIX = Genus(name="Hystrix", children=[H_CRISTATA])
HETEROCEPHALUS = Genus(name="Heterocephalus", children=[H_GLABER])
ERETHIZON = Genus(name="Erethizon", children=[E_DORSATUM])
CAVIA = Genus(name="Cavia", children=[C_PORCELLUS])
HYDROCHOERUS = Genus(name="Hydrochoerus", children=[H_HYDROCHAERIS])
CHINCHILLA = Genus(name="Chinchilla", children=[C_LANIGERA])
MYOCASTOR = Genus(name="Myocastor", children=[M_COYPUS])
OCTODON = Genus(name="Octodon", children=[O_DEGUS])

HYSTRICIDAE = Family(name="Hystricidae", children=[HYSTRIX])
HETEROCEPHALIDAE = Family(name="Heterocephalidae", children=[HETEROCEPHALUS])
ERETHIZONTIDAE = Family(name="Erethizontidae", children=[ERETHIZON])
CAVIIDAE = Family(name="Caviidae", children=[CAVIA, HYDROCHOERUS])
CHINCHILLIDAE = Family(name="Chinchillidae", children=[CHINCHILLA])
ECHIMYIDAE = Family(name="Echimyidae", children=[MYOCASTOR])
OCTODONTIDAE = Family(name="Octodontidae", children=[OCTODON])

CAVIOIDEA = Superfamily(name="Cavioidea", children=[ERETHIZONTIDAE, CAVIIDAE])
OCTODONTOIDEA = Superfamily(name="Octodontoidea", children=[ECHIMYIDAE, OCTODONTIDAE])

CAVIOMORPHA_A = Clade(children=[CHINCHILLIDAE, OCTODONTOIDEA])

PHIOMORPHA = Parvorder(name="Phiomorpha", children=[HYSTRICIDAE, HETEROCEPHALIDAE])
CAVIOMORPHA = Parvorder(name="Caviomorpha", children=[CAVIOIDEA, CAVIOMORPHA_A])

HYSTRICOGNATHI = Infraorder(name="Hystricognathi", children=[PHIOMORPHA, CAVIOMORPHA])

HYSTRICOMORPHA = Suborder(name="Hystricomorpha", children=[HYSTRICOGNATHI])
