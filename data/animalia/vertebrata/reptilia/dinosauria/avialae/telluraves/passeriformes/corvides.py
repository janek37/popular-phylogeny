from clade import Clade, Family, Genus, Infraorder, Species, Subfamily, Superfamily
from constants import EN, PL

from .paradisaeidae import PARADISAEIDAE

C_CORAX = Species(
    name="Corvus corax",
    local_names={
        EN: "common raven, western raven, northen raven",
        PL: "kruk zwyczajny",
    },
)
C_CORNIX = Species(
    name="Corvus cornix", local_names={EN: "hooded crow", PL: "wrona siwa"}
)
C_CORONE = Species(
    name="Corvus corone",
    local_names={EN: "carrion crow", PL: "wrona czarna, wroniec, czarnowron"},
)
C_BRACHYRHYNCHOS = Species(
    name="Corvus brachyrhynchos",
    local_names={EN: "American crow", PL: "wrona amerykańska"},
)
C_FRUGILEGUS = Species(name="Corvus frugilegus", local_names={EN: "rook", PL: "gawron"})
C_MONEDULA = Species(
    name="Coloeus monedula", local_names={EN: "western jackdaw", PL: "kawka zwyczajna"}
)
G_GLANDARIUS = Species(
    name="Garrulus glandarius", local_names={EN: "Eursasian jay", PL: "sójka zwyczajna"}
)
P_PICA = Species(
    name="Pica pica",
    local_names={EN: "Eurasian magpie, common magpie", PL: "sroka zwyczajna"},
)
C_CRISTATA = Species(
    name="Cyanocitta cristata", local_names={EN: "blue jay", PL: "modrosójka błękitna"}
)
O_ORIOLUS = Species(
    name="Oriolus oriolus",
    local_names={EN: "Eurasian golden oriole", PL: "wilga zwyczajna"},
)

# https://bmcecolevol.biomedcentral.com/articles/10.1186/1471-2148-12-72
CORVUS_A = Clade(children=[C_CORAX, C_FRUGILEGUS])
CORVUS_B = Clade(children=[C_CORNIX, C_CORONE])  # sometimes considered subspecies
CORVUS_C = Clade(children=[CORVUS_B, C_BRACHYRHYNCHOS])

CORVUS = Genus(name="Corvus", children=[CORVUS_A, CORVUS_C])
COLOEUS = Genus(name="Coloeus", children=[C_MONEDULA])
GARRULUS = Genus(name="Garrulus", children=[G_GLANDARIUS])
PICA = Genus(name="Pica", children=[P_PICA])
CYANOCITTA = Genus(name="Cyanocitta", children=[C_CRISTATA])
ORIOLUS = Genus(name="Oriolus", children=[O_ORIOLUS])

CORVINAE_A = Clade(children=[CORVUS, COLOEUS])
CORVINAE_B = Clade(children=[GARRULUS, PICA])

CORVINAE = Subfamily(name="Corvinae", children=[CORVINAE_A, CORVINAE_B])
CYANOCORACINAE = Subfamily(name="Cyanocoracinae", children=[CYANOCITTA])

CORVIDAE = Family(name="Corvidae", children=[CORVINAE, CYANOCORACINAE])
ORIOLIDAE = Family(name="Oriolidae", children=[ORIOLUS])

CORVOIDEA = Superfamily(name="Corvoidea", children=[CORVIDAE, PARADISAEIDAE])
ORIOLOIDEA = Subfamily(name="Orioloidea", children=[ORIOLIDAE])

CORVIDES = Infraorder(name="Corvides", children=[CORVOIDEA, ORIOLOIDEA])
