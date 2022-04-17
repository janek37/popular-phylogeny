from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
    Subphylum,
)
from constants import EN, PL

from .mushrooms import BASIDIOMYCOTA

S_CHARTARUM = Species(
    name="Stachybotrys chartarum", local_names={EN: "toxic black mold"}
)
A_ORYZAE = Species(
    name="Aspergillus oryzae", known_for=[{EN: "sake"}, {EN: "soy sauce"}, {EN: "miso"}]
)
P_CAMEMBERTI = Species(
    name="Penicillium camemberti", known_for=[{EN: "camembert"}, {EN: "brie"}]
)
P_CHRYSOGENUM = Species(name="Penicillium chrysogenum", known_for=[{EN: "penicilin"}])
P_DIGITATUM = Species(
    name="Penicillium digitatum",
    known_for=[
        {EN: "blue mold of citrus", PL: "niebieska zgnilizna owoców cytrusowych"}
    ],
)
P_EXPANSUM = Species(
    name="Penicillium expansum",
    known_for=[{EN: "blue mold of apples", PL: "mokra zgnilizna jabłek"}],
)
P_ROQUEFORTI = Species(name="Penicillium roqueforti", known_for=[{EN: "Roquefort"}])
S_CEREVISIAE = Species(
    name="Saccharomyces cerevisiae",
    known_for=[
        {EN: "ale", PL: "piwo górnej fermentacji"},
        {EN: "baker's yeast", PL: "drożdże piekarskie"},
    ],
)
S_PASTORIANUS = Species(
    name="Saccharomyces pastorianus",
    known_for=[{EN: "lager", PL: "piwo dolnej fermentacji"}],
)
C_ALBICANS = Species(
    name="Candida albicans", known_for=[{EN: "candidiasis", PL: "drożdżyca, kandydoza"}]
)
H_LACTIFLUORUM = Species(
    name="Hypomyces lactifluorum", local_names={EN: "lobster mushroom"}
)
M_ESCULENTA = Species(
    name="Morchella esculenta", local_names={EN: "morel mushroom", PL: "smardz jadalny"}
)
T_MAGNATUM = Species(
    name="Tuber magnatum", local_names={EN: "white truffle", PL: "trufla biała"}
)
C_ARBUSCULA = Species(
    name="Cladonia arbuscula",
    local_names={EN: "shrubby cup lichen", PL: "chrobotek leśny"},
)
F_CAPERATA = Species(
    name="Flavoparmelia caperata", local_names={EN: "common greenshield lichen"}
)
C_PURPUREA = Species(
    name="Claviceps purpurea",
    local_names={PL: "buławinka czerwona"},
    known_for=[{EN: "ergot", PL: "sporysz"}],
)
O_UNILATERALIS = Species(
    name="Ophiocordyceps unilateralis",
    known_for=[{EN: "controlling the behavior of infected ants"}],
)

PENICILLIUM_SECTION = Clade(children=[P_DIGITATUM, P_EXPANSUM])

STACHYBOTRYS = Genus(name="Stachybotrys", children=[S_CHARTARUM])
ASPERGILLUS = Genus(name="Aspergillus", children=[A_ORYZAE])
# research revealed multiple contradicting subtrees, there seems to be no consensus
PENICILLIUM = Genus(
    name="Penicillium",
    children=[P_CAMEMBERTI, P_CHRYSOGENUM, PENICILLIUM_SECTION, P_ROQUEFORTI],
)
SACCHAROMYCES = Genus(name="Saccharomyces", children=[S_CEREVISIAE, S_PASTORIANUS])
CANDIDA = Genus(name="Candida", children=[C_ALBICANS])
HYPOMYCES = Genus(name="Hypomyces", children=[H_LACTIFLUORUM])
MORCHELLA = Genus(name="Morchella", children=[M_ESCULENTA])
TUBER = Genus(name="Tuber", children=[T_MAGNATUM])
CLADONIA = Genus(name="Cladonia", children=[C_ARBUSCULA])
FLAVOPARMELIA = Genus(name="Flavoparmelia", children=[F_CAPERATA])
CLAVICEPS = Genus(name="Claviceps", children=[C_PURPUREA])
OPHIOCORDYCEPS = Genus(name="Ophiocordyceps", children=[O_UNILATERALIS])

STACHYBOTRYACEAE = Family(name="Stachybotryaceae", children=[STACHYBOTRYS])
TRICHOCOMACEAE = Family(name="Trichocomaceae", children=[ASPERGILLUS, PENICILLIUM])
SACCHAROMYCETACEAE = Family(
    name="Saccharomycetaceae", children=[SACCHAROMYCES, CANDIDA]
)
HYPOCREACEAE = Family(name="Hypocreaceae", children=[HYPOMYCES])
MORCHELLACEAE = Family(name="Morchellaceae", children=[MORCHELLA])
TUBERACEAE = Family(name="Tuberaceae", children=[TUBER])
CLADONIACEAE = Family(name="Cladoniaceae", children=[CLADONIA])
PARMELIACEAE = Family(name="Parmeliaceae", children=[FLAVOPARMELIA])
CLAVICIPITACEAE = Family(name="Clavicipitaceae", children=[CLAVICEPS])
OPHIOCORDYCIPITACEAE = Family(name="Ophiocordycipitaceae", children=[OPHIOCORDYCEPS])

# https://www.researchgate.net/publication/325346148_Introgression_and_gene_family_contraction_drive_the_evolution_of_lifestyle_and_host_shifts_of_hypocrealean_fungi
HYPOCREALES_B = Clade(children=[CLAVICIPITACEAE, OPHIOCORDYCIPITACEAE])
HYPOCREALES_A = Clade(children=[HYPOCREACEAE, HYPOCREALES_B])

HYPOCREALES = Order(name="Hypocreales", children=[STACHYBOTRYACEAE, HYPOCREALES_A])
EUROTIALES = Order(name="Eurotiales", children=[TRICHOCOMACEAE])
SACCHAROMYCETALES = Order(name="Saccharomycetales", children=[SACCHAROMYCETACEAE])
PEZIZALES = Order(name="Pezizales", children=[MORCHELLACEAE, TUBERACEAE])
LECANORALES = Order(name="Lecanorales", children=[CLADONIACEAE, PARMELIACEAE])

SORDARIOMYCETES = Class(name="Sordariomycetes", children=[HYPOCREALES])
EUROTIOMYCETES = Class(name="Eurotiomycetes", children=[EUROTIALES])
SACCHAROMYCETES = Class(name="Saccharomycetes", children=[SACCHAROMYCETALES])
PEZIZOMYCETES = Class(name="Pezizomycetes", children=[PEZIZALES])
LECANOROMYCETES = Class(name="Lecanoromycetes", children=[LECANORALES])

DOTHIDEOMYCETA = Clade(
    name="Dothideomyceta", children=[EUROTIOMYCETES, LECANOROMYCETES]
)
LEOTIOMYCETA = Clade(name="Leotiomyceta", children=[SORDARIOMYCETES, DOTHIDEOMYCETA])
PEZIZOMYCOTINA = Subphylum(
    name="Pezizomycotina", children=[LEOTIOMYCETA, PEZIZOMYCETES]
)

ASCOMYCOTA = Phylum(name="Ascomycota", children=[PEZIZOMYCOTINA, SACCHAROMYCETES])

EUMYCOTA = Kingdom(name="Eumycota", children=[ASCOMYCOTA, BASIDIOMYCOTA])
