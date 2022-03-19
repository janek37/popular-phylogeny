from clade import Clade, Family, Genus, Parvorder, Species, Subfamily, Superfamily
from constants import EN, PL

P_MACROCEPHALUS = Species(
    name="Physeter macrocephalus",
    local_names={EN: "sperm whale, cachalot", PL: "kaszalot spermacetowy"},
    known_for=[{EN: "Moby Dick"}],
)
P_PHOCOENA = Species(
    name="Phocoena phocoena",
    local_names={EN: "harbour porpoise", PL: "morświn zwyczajny"},
)
D_LEUCAS = Species(
    name="Delphinapterus leucas",
    local_names={EN: "beluga whale, white whale", PL: "wal biały, białucha arktyczna"},
)
M_MONOCEROS = Species(
    name="Monodon monoceros", local_names={EN: "narwhal", PL: "narwal jednozębny"}
)
O_ORCA = Species(
    name="Orcinus orca", local_names={EN: "orca, killer whale", PL: "orka oceaniczna"}
)
D_DELPHIS = Species(
    name="Delphinus delphis", local_names={EN: "common dolphin", PL: "delfin zwyczajny"}
)
T_TRUNCATUS = Species(
    name="Tursiops truncatus",
    local_names={
        EN: "common bottlenose dolphin",
        PL: "delfin butlonosy, butlonos zwyczajny",
    },
)

PHYSETER = Genus(name="Physeter", children=[P_MACROCEPHALUS])
PHOCOENA = Genus(name="Phocoena", children=[P_PHOCOENA])
DELPHINAPTERUS = Genus(name="Delphinapterus", children=[D_LEUCAS])
MONODON = Genus(name="Monodon", children=[M_MONOCEROS])
ORCINUS = Genus(name="Orcinus", children=[O_ORCA])
DELPHINUS = Genus(name="Delphinus", children=[D_DELPHIS])
TURSIOPS = Genus(name="Tursiops", children=[T_TRUNCATUS])

ORCININAE = Subfamily(name="Orcininae", children=[ORCINUS])
DELPHININAE = Subfamily(name="Delphininae", children=[DELPHINUS, TURSIOPS])

PHYSETERIDAE = Family(name="Physeteridae", children=[PHYSETER])
PHOCOENIDAE = Family(name="Phocoenidae", children=[PHOCOENA])
MONODONTIDAE = Family(name="Monodontidae", children=[DELPHINAPTERUS, MONODON])
DELPHINIDAE = Family(name="Delphinidae", children=[ORCININAE, DELPHININAE])

DELPHINOIDEA_A = Clade(children=[PHOCOENIDAE, MONODONTIDAE])

PHYSETEROIDEA = Superfamily(name="Physeteroidea", children=[PHYSETERIDAE])
DELPHINOIDEA = Superfamily(name="Delphinoidea", children=[DELPHINOIDEA_A, DELPHINIDAE])

ODONTOCETI = Parvorder(name="Odontoceti", children=[PHYSETEROIDEA, DELPHINOIDEA])
