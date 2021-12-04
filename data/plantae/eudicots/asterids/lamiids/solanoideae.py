from clade import Clade, Genus, Species, Subfamily, Subgenus, Tribe
from constants import EN, PL

M_OFFICINARUM = Species(
    name="Mandragora officinarum",
    local_names={EN: "mandrake", PL: "mandragora lekarska"},
)
D_STRAMONIUM = Species(
    name="Datura stramonium",
    local_names={EN: "thorn apple, jimsonweed", PL: "bieluń dziędzierzawa"},
)
A_BELLADONNA = Species(
    name="Atropa belladonna",
    local_names={EN: "belladonna, deadly nightshade", PL: "pokrzyk wilcza jagoda"},
)
S_LYCOPERSICUM = Species(
    name="Solanum lycopersicum", local_names={EN: "tomato", PL: "pomidor zwyczajny"}
)
S_TUBEROSUM = Species(
    name="Solanum tuberosum", local_names={EN: "potato", PL: "kartofel, ziemniak"}
)
S_MELONGENA = Species(
    name="Solanum melongena",
    local_names={EN: "eggplant, aubergine", PL: "bakłażan, oberżyna, psianka podłużna"},
)
C_ANNUUM = Species(
    name="Capsicum annuum",
    local_names={PL: "papryka roczna"},
    known_for=[
        {EN: "bell pepper", PL: "papryka słodka"},
        {EN: "chili pepper", PL: "papryka chili"},
        {EN: "jalapeño"},
        {EN: "cayenne pepper", PL: "pieprz cayenne"},
    ],
)
C_FRUTESCENS = Species(
    name="Capsicum frutescens",
    local_names={PL: "papryka owocowa"},
    known_for=[{EN: "piri piri"}, {EN: "Tabasco"}],
)
C_CHINENSE = Species(
    name="Capsicum chinense",
    local_names={EN: "habanero-type pepper", PL: "papryka habanero"},
    known_for=[{EN: "the hottest peppers"}],
)

SOLANUM_SENSU_STRICTO = Subgenus(
    name="Solanum sensu stricto", children=[S_LYCOPERSICUM, S_TUBEROSUM]
)
SOLANUM_SUBGENUS_LEPTOSTEMONUM = Subgenus(
    name="Solanum subg. Leptostemonum", children=[S_MELONGENA]
)

CAPSICUM_A = Clade(children=[C_FRUTESCENS, C_CHINENSE])

MANDRAGORA = Genus(name="Mandragora", children=[M_OFFICINARUM])
DATURA = Genus(name="Datura", children=[D_STRAMONIUM])
ATROPA = Genus(name="Atropa", children=[A_BELLADONNA])
SOLANUM = Genus(
    name="Solanum", children=[SOLANUM_SENSU_STRICTO, SOLANUM_SUBGENUS_LEPTOSTEMONUM]
)
CAPSICUM = Genus(name="Capsicum", children=[C_ANNUUM, CAPSICUM_A])

MANDRAGOREAE = Tribe(name="Mandragoreae", children=[MANDRAGORA])
DATUREAE = Tribe(name="Datureae", children=[DATURA])
HYOSCYAMEAE = Tribe(name="Hyoscyameae", children=[ATROPA])
SOLANEAE = Tribe(name="Solaneae", children=[SOLANUM])
CAPSICEAE = Tribe(name="Capsiceae", children=[CAPSICUM])

# https://www.researchgate.net/publication/257251395_Discovery_of_novel_plastid_phenylalanine_trnF_pseudogenes_defines_a_distinctive_clade_in_Solanaceae
PSEUDOSOLANOIDS_A = Clade(children=[SOLANEAE, CAPSICEAE])
PSEUDOSOLANOIDS = Clade(children=[DATUREAE, PSEUDOSOLANOIDS_A])
SOLANOIDEAE_A = Clade(children=[MANDRAGOREAE, PSEUDOSOLANOIDS])

SOLANOIDEAE = Subfamily(name="Solanoideae", children=[SOLANOIDEAE_A, HYOSCYAMEAE])
