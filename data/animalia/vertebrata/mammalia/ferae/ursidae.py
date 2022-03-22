from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, LA, PL

A_MELANOLEUCA = Species(
    name="Ailuropoda melanoleuca", local_names={EN: "giant panda", PL: "panda wielka"}
)
T_ORNATUS = Species(
    name="Tremarctos ornatus",
    local_names={
        EN: "spectacled bear, Andean bear",
        PL: "niedźwiedź andyjski, niedźwiedź okularowy, andoniedźwiedź okularowy",
    },
    known_for=[{EN: "Paddington Bear"}],
)
M_URSINUS = Species(
    name="Melursus ursinus",
    local_names={EN: "sloth bear", PL: "wargacz leniwy"},
    known_for=[{EN: "Baloo from The Jungle Book"}],
)
U_AMERICANUS = Species(
    name="Ursus americanus",
    local_names={
        EN: "American black bear",
        PL: "baribal, niedźwiedż amerykański, niedźwiedź czarny",
    },
    known_for=[{EN: "Winnipeg, inspiration for Winnie-the-Pooh"}],
)
U_THIBETANUS = Species(
    name="Ursus thibetanus",
    local_names={
        EN: "Asian black bear, moon bear",
        PL: "niedźwiedź księżycowy, niedźwiedź himalajski",
    },
)
U_SPELAEUS = Species(
    name="Ursus spelaeus",
    local_names={EN: "cave bear", PL: "niedźwiedź jaskiniowy"},
    extinct=True,
)
U_ARCTOS = Species(
    name="Ursus arctos",
    local_names={EN: "brown bear", PL: "niedźwiedź brunatny"},
    known_for=[
        {LA: "Ursus arctos horribilis", EN: "grizzly bear", PL: "niedźwiedź grizli"}
    ],
)
U_MARITIMUS = Species(
    name="Ursus maritimus", local_names={EN: "polar bear", PL: "niedźwiedź polarny"}
)

URSUS_A = Clade(children=[U_AMERICANUS, U_THIBETANUS])
URSUS_B = Clade(children=[U_ARCTOS, U_MARITIMUS])
# https://www.researchgate.net/publication/328232826_A_three-dimensional_analysis_of_tooth-root_morphology_in_living_bears_and_implications_for_feeding_behaviour_in_the_extinct_cave_bear
URSUS_C = Clade(children=[U_SPELAEUS, URSUS_B])

AILUROPODA = Genus(name="Ailuropoda", children=[A_MELANOLEUCA])
TREMARCTOS = Genus(name="Tremarctos", children=[T_ORNATUS])
MELURSUS = Genus(name="Melursus", children=[M_URSINUS])
URSUS = Genus(name="Ursus", children=[URSUS_A, URSUS_C])

AILUROPODINAE = Subfamily(name="Ailuropodinae", children=[AILUROPODA])
TREMARCTINAE = Subfamily(name="Tremarctinae", children=[TREMARCTOS])
URSINAE = Subfamily(name="Ursinae", children=[MELURSUS, URSUS])

URSIDAE_A = Clade(children=[TREMARCTINAE, URSINAE])
URSIDAE = Family(name="Ursidae", children=[AILUROPODINAE, URSIDAE_A])
