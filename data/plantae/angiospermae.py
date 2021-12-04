from clade import Clade, Family, Genus, Order, Phylum, Species
from constants import EN, PL

from .eudicots import EUDICOTYLEDONES
from .monocots import MONOCOTYLEDONES

# based on APG IV

N_ALBA = Species(
    name="Nymphaea alba",
    local_names={
        EN: "European white water lily, white nenuphar",
        PL: "lilia wodna, nenufar, grzybiebie białe",
    },
)
I_VERUM = Species(
    name="Illicium verum",
    local_names={EN: "star anise", PL: "anyż gwiaździsty, badian właściwy"},
    known_for=[
        {EN: "spice", PL: "roślina przyprawowa"},
        {EN: "drug precursor (Tamiflu)", PL: "roślina lecznicza (Tamiflu)"},
    ],
)
M_VIRGINIANA = Species(
    name="Magnolia virginiana", local_names={EN: "sweetbay magnolia"}
)
M_FRAGRANS = Species(
    name="Myristica fragrans", known_for=[{PL: "gałka muszkatołowa"}, {EN: "nutmeg"}]
)
L_NOBILIS = Species(
    name="Laurus nobilis",
    local_names={EN: "laurel", PL: "wawrzyn szlachetny"},
    known_for=[
        {EN: "bay leaf", PL: "liść laurowy"},
        {EN: "laurel wreath", PL: "wieniec laurowy"},
    ],
)
C_VERUM = Species(name="Cinnamomum verum", known_for=[{EN: "cinnamon", PL: "cynamon"}])
C_CAMPHORA = Species(
    name="Cinnamomum camphora", known_for=[{EN: "camphor", PL: "kamfora"}]
)
P_AMERICANA = Species(
    name="Persea americana", local_names={EN: "avocado", PL: "awokado"}
)
P_NIGRUM = Species(
    name="Piper nigrum", local_names={EN: "black pepper", PL: "pieprz czarny"}
)
P_METHYSTICUM = Species(
    name="Piper methysticum",
    local_names={EN: "kava", PL: "kava, pieprz metystynowy"},
    known_for=[{EN: "psychoactive properties"}],
)
# Schinus molle (rosids)

NYMPAHEA = Genus(name="Nymphea", children=[N_ALBA])
ILLICIUM = Genus(name="Illicium", children=[I_VERUM])
MAGNOLIA = Genus(name="Magnolia", children=[M_VIRGINIANA])
MYRISTICA = Genus(name="Myristica", children=[M_FRAGRANS])
LAURUS = Genus(name="Laurus", children=[L_NOBILIS])
CINNAMOMUM = Genus(name="Cinnamomum", children=[C_VERUM, C_CAMPHORA])
PERSEA = Genus(name="Persea", children=[P_AMERICANA])
PIPER = Genus(name="Piper", children=[P_NIGRUM, P_METHYSTICUM])

# multiple sources, e.g.
# https://www.researchgate.net/publication/340412028_The_Litsea_genome_and_the_evolution_of_the_laurel_family
LAURUS_CINNAMOMUM = Clade(children=[LAURUS, CINNAMOMUM])

NYMPHAEACEAE = Family(name="Nymphaeaceae", children=[NYMPAHEA])
SCHISANDRACEAE = Family(name="Schisandraceae", children=[ILLICIUM])
MAGNOLIACEAE = Family(name="Magnoliaceae", children=[MAGNOLIA])
MYRISTICACEAE = Family(name="Myristicaceae", children=[MYRISTICA])
LAURACEAE = Family(name="Lauraceae", children=[LAURUS_CINNAMOMUM, PERSEA])
PIPERACEAE = Family(name="Piperaceae", children=[PIPER])

NYMPHAEALES = Order(name="Nymphaeales", children=[NYMPHAEACEAE])
AUSTROBAILEYALES = Order(name="Austrobaileyales", children=[SCHISANDRACEAE])
MAGNOLIALES = Order(name="Magnoliales", children=[MAGNOLIACEAE, MYRISTICACEAE])
LAURALES = Order(name="Laurales", children=[LAURACEAE])
PIPERALES = Order(name="Piperales", children=[PIPERACEAE])

MAGNOLIALES_LAURALES = Clade(children=[MAGNOLIALES, LAURALES])

MAGNOLIIDAE = Clade(name="Magnoliidae", children=[MAGNOLIALES_LAURALES, PIPERALES])

MONOCOTYLEDONES_EUDICOTYLEDONES = Clade(children=[MONOCOTYLEDONES, EUDICOTYLEDONES])

ANGIOSPERMAE_B = Clade(children=[MAGNOLIIDAE, MONOCOTYLEDONES_EUDICOTYLEDONES])

ANGIOSPERMAE_A = Clade(children=[AUSTROBAILEYALES, ANGIOSPERMAE_B])

ANGIOSPERMAE = Phylum(name="Angiospermae", children=[NYMPHAEALES, ANGIOSPERMAE_A])
