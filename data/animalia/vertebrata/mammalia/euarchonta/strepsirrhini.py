from clade import Clade, Family, Genus, Infraorder, Species, Suborder, Superfamily
from constants import EN, PL

L_CATTA = Species(
    name="Lemur catta",
    local_names={EN: "ring-tailed lemur", PL: "lemur katta"},
    known_for=[{EN: "King Julien from Madagascar feanchise"}],
)
D_MADAGASCARIENSIS = Species(
    name="Daubentonia madagascariensis",
    local_names={EN: "aye-aye", PL: "palczak madagaskarski"},
    known_for=[{EN: "Maurice from Madagascar franchise"}],
)
M_BERTHAE = Species(
    name="Microcebus berthae",
    local_names={EN: "Madame Berthe's mouse lemur", PL: "mikrusek malutki"},
    known_for=[
        {EN: "Mort from Madagascar franchise"},
        {EN: "the smallest living primate"},
    ],
)

LEMUR = Genus(name="Lemur", children=[L_CATTA])
DAUBENTONIA = Genus(name="Daubentonia", children=[D_MADAGASCARIENSIS])
MICROCEBUS = Genus(name="Microcebus", children=[M_BERTHAE])

LEMURIDAE = Family(name="Lemuridae", children=[LEMUR])
DAUBENTONIIDAE = Family(name="Daubentoniidae", children=[DAUBENTONIA])
CHEIROGALEIDAE = Family(name="Cheirogaleidae", children=[MICROCEBUS])

# https://en.wikipedia.org/wiki/Taxonomy_of_lemurs
LEMUROIDEA_A = Clade(children=[LEMURIDAE, CHEIROGALEIDAE])

LEMUROIDEA = Superfamily(name="Lemuroidea", children=[LEMUROIDEA_A, DAUBENTONIIDAE])

LEMURIFORMES = Infraorder(name="Lemuriformes", children=[LEMUROIDEA])

STREPSIRRHINI = Suborder(name="Strepsirrhini", children=[LEMURIFORMES])
