from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Tribe
from constants import EN, PL

N_VIVERRINUS = Species(
    name="Nyctereutes viverrinus",
    local_names={EN: "Japanese raccoon dog, tanuki", PL: "jenot wiwerowaty"},
)
N_PROCYONOIDES = Species(
    name="Nyctereutes procyonoides",
    local_names={
        EN: "common raccoon dog, Chinese/Asian raccoon dog",
        PL: "tanuki, lis japoński, jenot azjatycki",
    },
)
V_ZERDA = Species(
    name="Vulpes zerda",
    local_names={EN: "fennec fox", PL: "lis pustynny, fenek pustynny"},
)
V_LAGOPUS = Species(
    name="Vulpes lagopus",
    local_names={
        EN: "Arctic fox, white fox, polar fox, snow fox",
        PL: "piesiec, lis polarny",
    },
)
V_VULPES = Species(
    name="Vulpes vulpes", local_names={EN: "red fox", PL: "lis pospolity, lis rudy"}
)
C_BRACHYURUS = Species(
    name="Chrysocyon brachyurus",
    local_names={EN: "maned wolf", PL: "wilk grzywiasty, pampasowiec grzywiasty"},
)
L_PICTUS = Species(
    name="Lycaon pictus", local_names={EN: "African wild dog", PL: "likaon pstry"}
)
C_AUREUS = Species(
    name="Canis aureus", local_names={EN: "golden jackal", PL: "szakal złocisty"}
)
C_LATRANS = Species(
    name="Canis latrans",
    local_names={EN: "coyote", PL: "wilk preriowy, kojot preriowy"},
)
C_LUPUS = Species(name="Canis lupus", local_names={EN: "grey wolf", PL: "wilk szary"})
C_FAMILIARIS = Species(
    name="Canis familiaris", local_names={EN: "domestic dog", PL: "pies domowy"}
)

VULPES_A = Clade(children=[V_LAGOPUS, V_VULPES])

CANINA_A = Clade(children=[C_LUPUS, C_FAMILIARIS])
CANINA_B = Clade(children=[C_LATRANS, CANINA_A])

NYCTEREUTES = Genus(name="Nyctereutes", children=[N_VIVERRINUS, N_PROCYONOIDES])
VULPES = Genus(name="Vulpes", children=[V_ZERDA, VULPES_A])
CHRYSOCYON = Genus(name="Chrysocyon", children=[C_BRACHYURUS])
LYCAON = Genus(name="Lycaon", children=[L_PICTUS])
CANIS = Genus(name="Canis", children=[C_AUREUS, CANINA_B])

CERDOCYONINA = Subtribe(name="Cerdocyonina", children=[CHRYSOCYON])
CANINA = Subtribe(name="Canina", children=[LYCAON, CANIS])

VULPINI = Tribe(name="Vulpini", children=[NYCTEREUTES, VULPES])
CANINI = Tribe(name="Canini", children=[CERDOCYONINA, CANINA])

CANINAE = Subfamily(name="Caninae", children=[VULPINI, CANINI])

CANIDAE = Family(name="Canidae", children=[CANINAE])
