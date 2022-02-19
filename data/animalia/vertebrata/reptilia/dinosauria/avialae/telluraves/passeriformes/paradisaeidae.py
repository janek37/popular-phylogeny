from clade import Clade, Family, Genus, Species
from constants import EN, PL

C_RESPUBLICA = Species(
    name="Cicinnurus respublica",
    local_names={EN: "Wilson's bird-of-paradise", PL: "latawiec krasnogrzbiety"},
)
C_REGIUS = Species(
    name="Cicinnurus regius",
    local_names={EN: "king bird-of-paradise", PL: "latawiec królewski"},
)
P_APODA = Species(
    name="Paradisaea apoda",
    local_names={EN: "greater bird-of-paradise", PL: "cudowronka wielka"},
)
P_MINOR = Species(
    name="Paradisaea minor",
    local_names={EN: "lesser bird-of-paradise", PL: "cudowronka mniejsza"},
)
P_RAGGIANA = Species(
    name="Paradisaea raggiana",
    local_names={EN: "Raggiana bird-of-paradise", PL: "cudowronka krasnopióra"},
)
P_RUBRA = Species(
    name="Paradisaea rubra",
    local_names={EN: "red bird-of-paradise", PL: "cudowronka czerwona"},
)
P_ALBERTI = Species(
    name="Pteridophora alberti",
    local_names={EN: "King of Saxony bird-of-paradise", PL: "wstęgogłów"},
)
P_RUDOLPHI = Species(
    name="Paradisornis rudolphi",
    local_names={EN: "blue bird-of-paradise", PL: "cudowronka błękitna"},
)
A_MAYERI = Species(
    name="Astrapia mayeri",
    local_names={EN: "ribbon-tailed astrapia", PL: "astrapia białosterna"},
)
L_SUPERBA = Species(
    name="Lophorina superba",
    local_names={
        EN: "greater lophorina, superb-bird-of-paradise",
        PL: "ozdobnik lirogłowy",
    },
)
L_VICTORIAE = Species(
    name="Lophorina victoriae",
    local_names={EN: "Victoria's riflebird", PL: "ozdobnik mały"},
)

# https://www.researchgate.net/publication/301538003_Can_the_Fisher-Lande_Process_Account_for_Birds_of_Paradise_and_Other_Sexual_Radiations
PARADISAEA_A = Clade(children=[P_APODA, P_RAGGIANA])
PARADISAEA_B = Clade(children=[PARADISAEA_A, P_MINOR])

CICINNURUS = Genus(name="Cicinnurus", children=[C_RESPUBLICA, C_REGIUS])
PARADISAEA = Genus(name="Paradisaea", children=[PARADISAEA_B, P_RUBRA])
PTERIDOPHORA = Genus(name="Pteridophora", children=[P_ALBERTI])
PARADISORNIS = Genus(name="Paradisornis", children=[P_RUDOLPHI])
ASTRAPIA = Genus(name="Astrapia", children=[A_MAYERI])
LOPHORINA = Genus(name="Lophorina", children=[L_SUPERBA, L_VICTORIAE])

PARADISAEIDAE_A = Clade(children=[PARADISAEA, PARADISORNIS])
PARADISAEIDAE_B = Clade(children=[PARADISAEIDAE_A, CICINNURUS])
PARADISAEIDAE_C = Clade(children=[PARADISAEIDAE_B, ASTRAPIA])
PARADISAEIDAE_D = Clade(children=[PARADISAEIDAE_C, LOPHORINA])

PARADISAEIDAE = Family(name="Paradisaeidae", children=[PARADISAEIDAE_D, PTERIDOPHORA])
