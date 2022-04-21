from clade import Clade, Class, Family, Genus, Order, Species, Superorder
from constants import EN, PL
from image import Image, License

from .araneae import ARANEAE

D_PTERONYSSINUS = Species(
    name="Dermatophagoides pteronyssinus",
    local_names={
        EN: "European house dust mite",
        PL: "roztocze kurzu domowego, skórożarłoczek skryty",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:House_dust_mite_(Dermatophagoides_pteronyssinus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/House_dust_mite_%28Dermatophagoides_pteronyssinus%29.jpg",
        author="Gilles San Martin from Namur, Belgium",
        license=License.CC_BY_SA_2_0,
    ),
)
S_SCABIEI = Species(
    name="Sarcoptes scabiei",
    local_names={EN: "itch mite", PL: "świerzbowiec ludzki"},
    known_for=[{EN: "scabies", PL: "świerzb"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sarcoptes-scabiei.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Sarcoptes-scabiei.JPG",
        author="Alan R Walker",
        license=License.CC_BY_SA_3_0,
    ),
)
I_RICINUS = Species(
    name="Ixodes ricinus",
    local_names={EN: "castor bean tick", PL: "kleszcz pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ixodes_ricinus_on_dry_grass.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1f/Ixodes_ricinus_on_dry_grass.jpg",
        author="W.alter",
        license=License.CC_BY_SA_4_0,
    ),
)
C_VITTATUS = Species(
    name="Centruroides vittatus",
    local_names={EN: "striped bark scorpion"},
    known_for=[{EN: "most common scorpion in North America"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Centruroides_vittatus_P1410866a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/Centruroides_vittatus_P1410866a.jpg",
        author="Tomascastelazo",
        license=License.CC_BY_SA_4_0,
    ),
)
L_QUINQUESTRIATUS = Species(
    name="Leiurus quinquestriatus",
    local_names={EN: "deathstalker"},
    known_for=[
        {EN: "one of the most common scorpions in North Africa and the Middle East"},
        {EN: "second most venomous scorpion"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Deathstalker_(Leiurus_quinquestriatus)_6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Deathstalker_%28Leiurus_quinquestriatus%29_6.jpg",
        author="מינוזיג",
        license=License.CC_BY_SA_4_0,
    ),
)
P_IMPERATOR = Species(
    name="Pandinus imperator",
    local_names={EN: "emperor scorpion", PL: "skorpion cesarski"},
    known_for=[{EN: "one of the largest scorpions"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Emperor_scorpion_or_Imperial_scorpion_(Pandinus_imperator).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Emperor_scorpion_or_Imperial_scorpion_%28Pandinus_imperator%29.jpg",
        author='"Mike" Michael L. Baird',
        license=License.CC_BY_2_0,
    ),
)

DERMATOPHAGOIDES = Genus(name="Dermatophagoides", children=[D_PTERONYSSINUS])
SARCOPTES = Genus(name="Sarcoptes", children=[S_SCABIEI])
IXODES = Genus(name="Ixodes", children=[I_RICINUS])
CENTRUROIDES = Genus(name="Centruroides", children=[C_VITTATUS])
LEIRUS = Genus(name="Leirus", children=[L_QUINQUESTRIATUS])
PANDINUS = Genus(name="Pandinus", children=[P_IMPERATOR])

PYROGLYPHIDAE = Family(name="Pyroglyphidae", children=[DERMATOPHAGOIDES])
SARCOPTIDAE = Family(name="Sarcoptidae", children=[SARCOPTES])
IXODIDAE = Family(name="Ixodidae", children=[IXODES])
BUTHIDAE = Family(name="Buthidae", children=[CENTRUROIDES, LEIRUS])
SCORPIONIDAE = Family(name="Scorpionidae", children=[PANDINUS])

SARCOPTIFORMES = Order(name="Sarcoptiformes", children=[PYROGLYPHIDAE, SARCOPTIDAE])
IXODIDA = Order(name="Ixodida", children=[IXODIDAE])
SCORPIONES = Order(name="Scorpiones", children=[BUTHIDAE, SCORPIONIDAE])

ACARIFORMES = Superorder(name="Acariformes", children=[SARCOPTIFORMES])
PARASITIFORMES = Superorder(name="Parasitiformes", children=[IXODIDA])

ARACHNOPULMONATA = Clade(name="Arachnopulmonata", children=[SCORPIONES, ARANEAE])

# https://www.researchgate.net/publication/260336374_Spiders_Arachnida_Araneae_of_the_Canadian_Prairies
ARACHNIDA_A = Clade(children=[ACARIFORMES, PARASITIFORMES])

ARACHNIDA = Class(name="Arachnida", children=[ARACHNIDA_A, ARACHNOPULMONATA])
