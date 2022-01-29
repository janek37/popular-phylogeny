from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily
from constants import EN, PL

P_MOLURUS = Species(
    name="Python molurus",
    local_names={EN: "Indian python", PL: "pyton tygrysi"},
    known_for=[{EN: "Kaa from The Jungle Book"}],
)
P_REGIUS = Species(
    name="Python regius",
    local_names={EN: "ball python, royal python", PL: "pyton królewski"},
    known_for=[{EN: "most common pet snake"}],
)
B_CONSTRICTOR = Species(
    name="Boa constrictor", local_names={EN: "boa constrictor", PL: "boa dusiciel"}
)
E_MURINUS = Species(
    name="Eunectes murinus", local_names={EN: "green anaconda", PL: "anakonda zielona"}
)
E_NOTAEUS = Species(
    name="Eunectes notaeus", local_names={EN: "yellow anaconda", PL: "anakonda żółta"}
)
V_BERUS = Species(
    name="Vipera berus",
    local_names={
        EN: "black adder, common European adder/viper",
        PL: "żmija zygzakowata",
    },
)
C_VIRIDIS = Species(
    name="Crotalus viridis",
    local_names={EN: "prairie rattlesnake", PL: "grzechotnik preriowy"},
)
P_GUTTATUS = Species(
    name="Pantherophis guttatus",
    local_names={EN: "corn snake", PL: "wąż zbożowy"},
    known_for=[{EN: "second most common pet snake"}],
)
Z_LONGISSIMUS = Species(
    name="Zamenis longissimus",
    local_names={EN: "Aesculapian snake", PL: "wąż Eskulapa"},
    known_for=[{EN: "Rod of Asclepius", PL: "laska Eskulapa"}],
)
N_NATRIX = Species(
    name="Natrix natrix",
    local_names={EN: "grass snake, rigged snake", PL: "zaskroniec zwyczajny"},
)
N_NAJA = Species(
    name="Naja naja",
    local_names={EN: "Indian cobra, spectacled cobra", PL: "okularnik, kobra indyjska"},
)
M_FULVIUS = Species(
    name="Micrurus fulvius",
    local_names={
        EN: "eastern coral snake, common coral snake",
        PL: "wąż koralowy arlekin, koralówka arlekin",
    },
)
O_HANNAH = Species(
    name="Ophiophagus hannah",
    local_names={EN: "king cobra", PL: "kobra królewska"},
    known_for=[{EN: "the longest venomous snake"}],
)
D_POLYLEPIS = Species(
    name="Dendroaspis polylepis", local_names={EN: "black mamba", PL: "mamba czarna"}
)

PYTHON = Genus(name="Python", children=[P_MOLURUS, P_REGIUS])
BOA = Genus(name="Boa", children=[B_CONSTRICTOR])
EUNECTES = Genus(name="Eunectes", children=[E_MURINUS, E_NOTAEUS])
VIPERA = Genus(name="Vipera", children=[V_BERUS])
CROTALUS = Genus(name="Crotalus", children=[C_VIRIDIS])
PANTHEROPHIS = Genus(name="Pantherophis", children=[P_GUTTATUS])
ZAMENIS = Genus(name="Zamenis", children=[Z_LONGISSIMUS])
NATRIX = Genus(name="Natrix", children=[N_NATRIX])
NAJA = Genus(name="Naja", children=[N_NAJA])
MICRURUS = Genus(name="Micrurus", children=[M_FULVIUS])
OPHIOPHAGUS = Genus(name="Ophiophagus", children=[O_HANNAH])
DENDROASPIS = Genus(name="Dendroaspis", children=[D_POLYLEPIS])

COLUBRINAE = Subfamily(name="Colubrinae", children=[PANTHEROPHIS, ZAMENIS])
NATRICINAE = Subfamily(name="Natricinae", children=[NATRIX])

PYTHONIDAE = Family(name="Pythonidae", children=[PYTHON])
BOIDAE = Family(name="Boidae", children=[BOA, EUNECTES])
VIPERIDAE = Family(name="Viperidae", children=[VIPERA, CROTALUS])
COLUBRIDAE = Family(name="Colubridae", children=[COLUBRINAE, NATRICINAE])
# unresolved for now
ELAPIDAE = Family(name="Elapidae", children=[NAJA, MICRURUS, OPHIOPHAGUS, DENDROASPIS])

PROTEROGLYPHA = Clade(name="Proteroglypha", children=[COLUBRIDAE, ELAPIDAE])

BOOIDEA = Superfamily(name="Booidea", children=[PYTHONIDAE, BOIDAE])
COLUBROIDEA = Superfamily(name="Colubroidea", children=[VIPERIDAE, PROTEROGLYPHA])

SERPENTES = Suborder(name="Serpentes", children=[BOOIDEA, COLUBROIDEA])
