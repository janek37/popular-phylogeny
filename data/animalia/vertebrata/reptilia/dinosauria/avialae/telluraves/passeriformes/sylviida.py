from clade import Clade, Family, Genus, Parvorder, Species
from constants import EN, PL

P_MAJOR = Species(
    name="Parus major",
    local_names={EN: "great tit", PL: "sikora bogatka, bogatka zwyczajna"},
)
C_CAERULEUS = Species(
    name="Cyanistes caeruleus",
    local_names={EN: "Eurasian blue tit", PL: "sikora modra, modraszka zwyczajna"},
)
P_ATER = Species(
    name="Periparus ater", local_names={EN: "coal tit", PL: "sikora sosnówka, sosnówka"}
)
P_PALUSTRIS = Species(
    name="Poecile palustris", local_names={EN: "marsh tit", PL: "sikora uboga"}
)
L_CRISTATUS = Species(
    name="Lophophanes cristatus",
    local_names={
        EN: "European crested tit",
        PL: "sikora czubatka, czubatka europejska",
    },
)
B_BICOLOR = Species(
    name="Baeolophus bicolor",
    local_names={EN: "tufted titmouse", PL: "sikora dwubarwna"},
)
R_PENDULINUS = Species(
    name="Remiz pendulinus",
    local_names={EN: "Eurasian penduline tit", PL: "remiz zwyczajny"},
)
A_ARVENSIS = Species(
    name="Alauda arvensis",
    local_names={EN: "Eurasian skylark", PL: "skowronek zwyczajny"},
)
E_ALPESTRIS = Species(
    name="Eremophila alpestris",
    local_names={EN: "horned lark, shore lark", PL: "górniczek zwyczajny"},
)
G_CRISTATA = Species(
    name="Galerida cristata",
    local_names={EN: "crested lark", PL: "pośmieciuszka, dzierlatka zwyczajna"},
)
H_RUSTICA = Species(
    name="Hirundo rustica",
    local_names={EN: "barn swallow, European swallow", PL: "jaskółka dymówka, dymówka"},
)
P_SPILODERA = Species(
    name="Petrochelidon spilodera",
    local_names={
        EN: "African swallow, South African cliff swallow",
        PL: "jaskółka towarzyska",
    },
    known_for=[{EN: "carrying coconuts"}],
)
D_URBICUM = Species(
    name="Delichon urbicum",
    local_names={EN: "common house martin", PL: "jaskółka oknówka, oknówka zwyczajna"},
)
A_CAUDATUS = Species(
    name="Aegithalos caudatus",
    local_names={EN: "long-tailed tit, long-tailed bushtit", PL: "raniuszek zwyczajny"},
)

PARUS = Genus(name="Parus", children=[P_MAJOR])
CYANISTES = Genus(name="Cyanistes", children=[C_CAERULEUS])
PERIPARUS = Genus(name="Periparus", children=[P_ATER])
POECILE = Genus(name="Poecile", children=[P_PALUSTRIS])
LOPHOPHANES = Genus(name="Lophophanes", children=[L_CRISTATUS])
BAEOLOPHUS = Genus(name="Baeolophus", children=[B_BICOLOR])
REMIZ = Genus(name="Remiz", children=[R_PENDULINUS])
ALAUDA = Genus(name="Alauda", children=[A_ARVENSIS])
EREMOPHILA = Genus(name="Eremophila", children=[E_ALPESTRIS])
GALERIDA = Genus(name="Galerida", children=[G_CRISTATA])
HIRUNDO = Genus(name="Hirundo", children=[H_RUSTICA])
PETROCHELIDON = Genus(name="Petrochelidon", children=[P_SPILODERA])
DELICHON = Genus(name="Delichon", children=[D_URBICUM])
AEGITHALOS = Genus(name="Aegithalos", children=[A_CAUDATUS])

PARIDAE_A = Clade(children=[PARUS, CYANISTES])
PARIDAE_B = Clade(children=[POECILE, LOPHOPHANES])
PARIDAE_C = Clade(children=[PARIDAE_B, BAEOLOPHUS])
PARIDAE_D = Clade(children=[PERIPARUS, PARIDAE_C])

# https://www.researchgate.net/publication/241692441_Multilocus_phylogeny_of_the_avian_family_Alaudidae_larks_reveals_complex_morphological_evolution_non-monophyletic_genera_and_hidden_species_diversity
ALAUDIDAE_A = Clade(children=[ALAUDA, GALERIDA])

# https://www.sciencedirect.com/science/article/abs/pii/S1055790304003501
# https://ars.els-cdn.com/content/image/1-s2.0-S1055790304003501-gr1.jpg
HIRUNDINIDAE_A = Clade(children=[PETROCHELIDON, DELICHON])

PARIDAE = Family(name="Paridae", children=[PARIDAE_A, PARIDAE_D])
REMIZIDAE = Family(name="Remizidae", children=[REMIZ])
ALAUDIDAE = Family(name="Alaudidae", children=[ALAUDIDAE_A, EREMOPHILA])
HIRUNDINIDAE = Family(name="Hirundinidae", children=[HIRUNDO, HIRUNDINIDAE_A])
AEGITHALIDAE = Family(name="Aegithalidae", children=[AEGITHALOS])

SYLVIIDA_A = Clade(children=[PARIDAE, REMIZIDAE])
SYLVIIDA_B = Clade(children=[HIRUNDINIDAE, AEGITHALIDAE])
SYLVIIDA_C = Clade(children=[ALAUDIDAE, SYLVIIDA_B])

SYLVIIDA = Parvorder(name="Sylviida", children=[SYLVIIDA_A, SYLVIIDA_C])
