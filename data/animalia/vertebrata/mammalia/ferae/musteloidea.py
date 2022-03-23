from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN, PL

M_MEPHITIS = Species(
    name="Mephitis mephitis", local_names={EN: "striped skunk", PL: "skunks zwyczajny"}
)
A_FULGENS = Species(
    name="Ailurus fulgens",
    local_names={EN: "red panda, lesser panda", PL: "panda mała, pandka ruda"},
)
P_LOTOR = Species(
    name="Procyon lotor", local_names={EN: "common raccoon", PL: "szop pracz"}
)
M_CAPENSIS = Species(
    name="Mellivora capensis",
    local_names={EN: "honey badger, ratel", PL: "miodożer, ratel miodożerny"},
    known_for=[{EN: "one of the toughest animals"}],
)
M_MELES = Species(
    name="Meles meles", local_names={EN: "European badger", PL: "borsuk europejski"}
)
M_FOINA = Species(
    name="Martes foina", local_names={EN: "beech marten", PL: "kuna domowa"}
)
G_GULO = Species(
    name="Gulo gulo",
    local_names={EN: "wolverine", PL: "rosomak tundrowy"},
    known_for=[{EN: "Marvel's Wolverine"}],
)
M_FURO = Species(name="Mustela furo", local_names={EN: "ferret", PL: "fretka domowa"})
M_ERMINEA = Species(
    name="Mustela erminea",
    local_names={EN: "stoat, Eurasian ermine", PL: "gronostaj europejski"},
)
M_NIVALIS = Species(
    name="Mustela nivalis",
    local_names={
        EN: "least weasel, small weasel, common weasel",
        PL: "łasica pospolita",
    },
)
M_PUTORIUS = Species(
    name="Mustela putorius",
    local_names={EN: "European polecat", PL: "tchórz zwyczajny"},
)
M_LUTREOLA = Species(
    name="Mustela lutreola", local_names={EN: "European mink", PL: "norka europejska"}
)
L_LUTRA = Species(
    name="Lutra lutra",
    local_names={EN: "European otter, common otter", PL: "wydra europejska"},
)

MUSTELA_A = Clade(children=[M_FURO, M_PUTORIUS])
MUSTELA_B = Clade(children=[M_LUTREOLA, MUSTELA_A])
MUSTELA_C = Clade(children=[M_NIVALIS, MUSTELA_B])

MEPHITIS = Genus(name="Mephitis", children=[M_MEPHITIS])
AILURUS = Genus(name="Ailurus", children=[A_FULGENS])
PROCYON = Genus(name="Procyon", children=[P_LOTOR])
MELLIVORA = Genus(name="Mellivora", children=[M_CAPENSIS])
MELES = Genus(name="Meles", children=[M_MELES])
MARTES = Genus(name="Martes", children=[M_FOINA])
GULO = Genus(name="Gulo", children=[G_GULO])
MUSTELA = Genus(name="Mustela", children=[M_ERMINEA, MUSTELA_C])
LUTRA = Genus(name="Lutra", children=[L_LUTRA])

MELLIVORINAE = Subfamily(name="Mellivorinae", children=[MELLIVORA])
MELINAE = Subfamily(name="Melinae", children=[MELES])
GULONINAE = Subfamily(name="Guloninae", children=[MARTES, GULO])
MUSTELINAE = Subfamily(name="Mustelinae", children=[MUSTELA])
LUTRINAE = Subfamily(name="Lutrinae", children=[LUTRA])

MUSTELIDAE_A = Clade(children=[MUSTELINAE, LUTRINAE])
MUSTELIDAE_B = Clade(children=[GULONINAE, MUSTELIDAE_A])
MUSTELIDAE_C = Clade(children=[MELINAE, MUSTELIDAE_B])

MEPHITIDAE = Family(name="Mephitidae", children=[MEPHITIS])
AILURIDAE = Family(name="Ailuridae", children=[AILURUS])
PROCYONIDAE = Family(name="Procyonidae", children=[PROCYON])
MUSTELIDAE = Family(name="Mustelidae", children=[MELLIVORINAE, MUSTELIDAE_C])

MUSTELOIDEA_A = Clade(children=[PROCYONIDAE, MUSTELIDAE])
MUSTELOIDEA_B = Clade(children=[AILURIDAE, MUSTELOIDEA_A])

MUSTELOIDEA = Superfamily(name="Musteloidea", children=[MEPHITIDAE, MUSTELOIDEA_B])
