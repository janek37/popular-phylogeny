from clade import Clade, Class, Family, Genus, Order, Species, Superorder
from constants import EN, PL

D_PTERONYSSINUS = Species(
    name="Dermatophagoides pteronyssinus",
    local_names={
        EN: "European house dust mite",
        PL: "roztocze kurzu domowego, skórożarłoczek skryty",
    },
)
I_RICINUS = Species(
    name="Ixodes ricinus", local_names={EN: "castor bean tick", PL: "kleszcz pospolity"}
)
C_VITTATUS = Species(
    name="Centruroides vittatus",
    local_names={EN: "striped bark scorpion"},
    known_for=[{EN: "most common scorpion in North America"}],
)
L_QUINQUESTRIATUS = Species(
    name="Leiurus quinquestriatus",
    local_names={EN: "deathstalker"},
    known_for=[
        {EN: "one of the most common scorpions in North Africa and the Middle East"},
        {EN: "second most venomous scorpion"},
    ],
)
P_IMPERATOR = Species(
    name="Pandinus imperator",
    local_names={EN: "emperor scorpion", PL: "skorpion cesarski"},
    known_for=[{EN: "one of the largest scorpions"}],
)

DERMATOPHAGOIDES = Genus(name="Dermatophagoides", children=[D_PTERONYSSINUS])
IXODES = Genus(name="Ixodes", children=[I_RICINUS])
CENTRUROIDES = Genus(name="Centruroides", children=[C_VITTATUS])
LEIRUS = Genus(name="Leirus", children=[L_QUINQUESTRIATUS])
PANDINUS = Genus(name="Pandinus", children=[P_IMPERATOR])

PYROGLYPHIDAE = Family(name="Pyroglyphidae", children=[DERMATOPHAGOIDES])
IXODIDAE = Family(name="Ixodidae", children=[IXODES])
BUTHIDAE = Family(name="Buthidae", children=[CENTRUROIDES, LEIRUS])
SCORPIONIDAE = Family(name="Scorpionidae", children=[PANDINUS])

SARCOPTIFORMES = Order(name="Sarcoptiformes", children=[PYROGLYPHIDAE])
IXODIDA = Order(name="Ixodida", children=[IXODIDAE])
SCORPIONES = Order(name="Scorpiones", children=[BUTHIDAE, SCORPIONIDAE])

ACARIFORMES = Superorder(name="Acariformes", children=[SARCOPTIFORMES])
PARASITIFORMES = Superorder(name="Parasitiformes", children=[IXODIDA])

ARACHNOPULMONATA = Clade(name="Arachnopulmonata", children=[SCORPIONES])

# https://www.researchgate.net/publication/260336374_Spiders_Arachnida_Araneae_of_the_Canadian_Prairies
ARACHNIDA_A = Clade(children=[ACARIFORMES, PARASITIFORMES])

ARACHNIDA = Class(name="Arachnida", children=[ARACHNIDA_A, ARACHNOPULMONATA])
