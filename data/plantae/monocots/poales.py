from clade import (
    Clade,
    Family,
    Genus,
    Order,
    Species,
    Subfamily,
    Subtribe,
    Supertribe,
    Tribe,
)
from constants import EN, PL

T_LATIFOLIA = Species(
    name="Typha latifolia",
    local_names={EN: "broadleaf cattail", PL: "pałka wpdna, pałka szerokolistna"},
)
A_COMOSUS = Species(
    name="Ananas comosus", local_names={EN: "pineapple", PL: "ananas jadalny"}
)
P_PRATENSIS = Species(
    name="Poa pratensis",
    local_names={EN: "Kentucky bluegrass, smooth meadow-grass", PL: "wiechlina łąkowa"},
)
F_OVINA = Species(
    name="Festuca ovina", local_names={EN: "sheep fescue", PL: "kostrzewa owcza"}
)
T_AESTIVUM = Species(
    name="Triticum aestivum",
    local_names={EN: "common wheat, bread wheat", PL: "pszenica zwyczajna"},
)
T_DURUM = Species(
    name="Triticum durum",
    local_names={EN: "durum wheat, pasta wheat", PL: "pszenica durum, pszenica twarda"},
    known_for=[{EN: "pasta", PL: "makaron"}, {EN: "couscous", PL: "kuskus"}],
)
H_VULGARE = Species(
    name="Hordeum vulgare", local_names={EN: "barley", PL: "jęczmień zwyczajny"}
)
A_SATIVA = Species(name="Avena sativa", local_names={EN: "oat", PL: "owies zwyczajny"})
S_CEREALE = Species(
    name="Secale cereale", local_names={EN: "rye", PL: "żyto zwyczajne"}
)
O_SATIVA = Species(
    name="Oryza sativa", local_names={EN: "rice, Asian rice", PL: "ryż siewny"}
)
B_OLDHAMII = Species(name="Bambusa oldhamii", local_names={EN: "giant timber bamboo"})
P_MILIACEUM = Species(
    name="Panicum miliaceum",
    local_names={EN: "proso millet", PL: "proso"},
    known_for=[{PL: "kasza jaglana"}],
)
Z_MAYS = Species(name="Zea mays", local_names={EN: "corn, maize", PL: "kukurydza"})
C_CITRATUS = Species(
    name="Cymbopogon citratus",
    local_names={PL: "trawa cytrynowa, palczatka cytrynowa", EN: "lemon grass"},
)
S_BICOLOR = Species(
    name="Sorghum bicolor", local_names={PL: "sorgo dwubarwne", EN: "sorghum"}
)
S_OFFICINARUM = Species(
    name="Saccharum officinarum",
    local_names={PL: "trzcina cukrowa, cukrowiec lekarski", EN: "sugarcane"},
)
P_AUSTRALIS = Species(
    name="Phragmites australis",
    local_names={PL: "trzcina pospolita", EN: "common reed"},
)

TYPHA = Genus(name="Typha", children=[T_LATIFOLIA])
ANANAS = Genus(name="Ananas", children=[A_COMOSUS])
POA = Genus(name="Poa", children=[P_PRATENSIS])
FESTUCA = Genus(name="Festuca", children=[F_OVINA])
TRITICUM = Genus(name="Triticum", children=[T_AESTIVUM, T_DURUM])
HORDEUM = Genus(name="Hordeum", children=[H_VULGARE])
AVENA = Genus(name="Avena", children=[A_SATIVA])
SECALE = Genus(name="Secale", children=[S_CEREALE])
ORYZA = Genus(name="Oryza", children=[O_SATIVA])
BAMBUSA = Genus(name="Bambusa", local_names={PL: "bambus"}, children=[B_OLDHAMII])
PANICUM = Genus(name="Panicum", children=[P_MILIACEUM])
ZEA = Genus(name="Zea", children=[Z_MAYS])
CYMBOPOGON = Genus(name="Citratus", children=[C_CITRATUS])
SORGHUM = Genus(name="Sorghum", children=[S_BICOLOR])
PHRAGMITES = Genus(name="Phragmites1", children=[P_AUSTRALIS])

POINAE = Subtribe(name="Poinae", children=[POA])
LOLIINAE = Subtribe(name="Loliinae", children=[FESTUCA])
AVENINAE = Subtribe(name="Aveninae", children=[AVENA])
ORYZINAE = Subtribe(name="Oryzinae", children=[ORYZA])
BAMBUSINAE = Subtribe(name="Bambusinae", children=[BAMBUSA])
PANICINAE = Subtribe(name="Panicinae", children=[PANICUM])
TRIPSACINAE = Subtribe(name="Tripsacinae", children=[ZEA])
ANDROPOGONINAE = Subtribe(name="Andropogoninae", children=[CYMBOPOGON])
SACCHARINAE = Subtribe(name="Saccharinae", children=[SORGHUM])
MOLINIINAE = Subtribe(name="Moliniinae", children=[PHRAGMITES])

CHLOROPLAST_GROUP_1 = Clade(name="chloroplast group 1", children=[AVENINAE])
CHLOROPLAST_GROUP_2 = Clade(name="chloroplast group 2", children=[POINAE, LOLIINAE])

# many sources, e.g.
# https://www.researchgate.net/publication/6760501_Sequence_variation_of_chloroplast_gene_infA-rpl36_region_occurred_in_some_Triticeae_species
TRITICUM_SECALE = Clade(children=[TRITICUM, SECALE])

# https://www.researchgate.net/publication/262373100_An_evolutionary_perspective_of_C_4_photosynthesis_in_maize
ANDROPOGONINAE_SACCHARINAE = Clade(children=[ANDROPOGONINAE, SACCHARINAE])

POEAE = Tribe(name="Poeae", children=[CHLOROPLAST_GROUP_1, CHLOROPLAST_GROUP_2])
TRITICEAE = Tribe(name="Triticeae", children=[TRITICUM_SECALE, HORDEUM])
ORYZEAE = Tribe(name="Oryzeae", children=[ORYZINAE])
BAMBUSEAE = Tribe(name="Bambuseae", children=[BAMBUSINAE])
PANICEAE = Tribe(name="Paniceae", children=[PANICINAE])
ANDROPOGONEAE = Tribe(
    name="Andropogoneae", children=[TRIPSACINAE, ANDROPOGONINAE_SACCHARINAE]
)
MOLINIEAE = Tribe(name="Molinieae", children=[MOLINIINAE])

POODAE = Supertribe(name="Poodae", children=[POEAE])
TRITICODAE = Supertribe(name="Triticodae", children=[TRITICEAE])
PANICODAE = Supertribe(name="Panicodae", children=[PANICEAE])
ANDROPOGONODAE = Supertribe(name="Andropogonodae", children=[ANDROPOGONEAE])

POOIDEAE = Subfamily(name="Pooideae", children=[POODAE, TRITICODAE])
ORYZOIDEAE = Subfamily(name="Oryzoideae", children=[ORYZEAE])
BAMBUSOIDEAE = Subfamily(name="Bambusoideae", children=[BAMBUSEAE])
PANICOIDEAE = Subfamily(name="Panicoideae", children=[PANICODAE, ANDROPOGONODAE])
ARUNDINOIDEAE = Subfamily(name="Arundinoideae", children=[MOLINIEAE])

POOIDEAE_BAMBUSOIDEAE = Clade(children=[POOIDEAE, BAMBUSOIDEAE])
BOP_CLADE = Clade(name="BOP clade", children=[POOIDEAE_BAMBUSOIDEAE, ORYZOIDEAE])
PACMAD_CLADE = Clade(name="PACMAD clade", children=[PANICOIDEAE, ARUNDINOIDEAE])

TYPHACEAE = Family(name="Typhaceae", children=[TYPHA])
BROMELIACEAE = Family(name="Bromeliaceae", children=[ANANAS])
POACEAE = Family(name="Poaceae", children=[BOP_CLADE, PACMAD_CLADE])

BROMELIAD_CLADE = Clade(name="Bromeliad clade", children=[TYPHACEAE, BROMELIACEAE])

POALES = Order(name="Poales", children=[BROMELIAD_CLADE, POACEAE])
