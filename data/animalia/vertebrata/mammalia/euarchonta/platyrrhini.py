from clade import Clade, Family, Genus, Parvorder, Species
from constants import EN, PL

C_JACCHUS = Species(
    name="Callithrix jacchus",
    local_names={EN: "common marmoset", PL: "marmozeta zwyczajna, uistiti białoucha"},
)
S_IMPERATOR = Species(
    name="Saguinus imperator",
    local_names={EN: "emperor tamarin", PL: "tamaryna cesarska"},
)
L_ROSALIA = Species(
    name="Leontopithecus rosalia",
    local_names={EN: "golden lion tamarin", PL: "marmozeta lwia"},
)
A_GUARIBA = Species(
    name="Alouatta guariba", local_names={EN: "brown howler", PL: "wyjec brązowy"}
)
A_GEOFFROYI = Species(
    name="Ateles geoffroyi",
    local_names={EN: "Geoffroy's spider monkey", PL: "czepiak czarnoręki"},
)
S_APELLA = Species(
    name="Sapajus apella", local_names={EN: "tufted capuchin", PL: "kapucynka czubata"}
)

CALLITHRIX = Genus(name="Callithrix", children=[C_JACCHUS])
SAGUINUS = Genus(name="Saguinus", children=[S_IMPERATOR])
LEONTOPITHECUS = Genus(name="Leontopithecus", children=[L_ROSALIA])
ALOUATTA = Genus(name="Alouatta", children=[A_GUARIBA])
ATELES = Genus(name="Ateles", children=[A_GEOFFROYI])
SAPAJUS = Genus(name="Sapajus", children=[S_APELLA])

# https://www.researchgate.net/publication/259499744_Evolutionary_genetics_and_implications_of_small_size_and_twinning_in_callitrichine_primates
CALLITRICHIDAE_A = Clade(children=[CALLITHRIX, LEONTOPITHECUS])

CALLITRICHIDAE = Family(name="Callitrichidae", children=[CALLITRICHIDAE_A, SAGUINUS])
ATELIDAE = Family(name="Atelidae", children=[ALOUATTA, ATELES])
CEBIDAE = Family(name="Cebidae", children=[SAPAJUS])

# https://www.researchgate.net/publication/259499744_Evolutionary_genetics_and_implications_of_small_size_and_twinning_in_callitrichine_primates
PLATYRRHINI_A = Clade(children=[CALLITRICHIDAE, CEBIDAE])

PLATYRRHINI = Parvorder(name="Platyrrhini", children=[PLATYRRHINI_A, ATELIDAE])
