from clade import Epifamily, Family, Genus, Order, Species, Superfamily
from constants import EN, PL

B_ORIENTALIS = Species(
    name="Blatta orientalis",
    local_names={EN: "oriental cockroach", PL: "karaluch, karaczan wschodni"},
)
P_AMERICANA = Species(
    name="Periplaneta americana",
    local_names={
        EN: "American cockroach",
        PL: "karaluch amerykański, przybyszka amerykańska",
    },
)
B_GERMANICA = Species(
    name="Blattella germanica",
    local_names={EN: "German cockroach", PL: "karaczan prusak"},
)
G_PORTENTOSA = Species(
    name="Gromphadorhina portentosa",
    local_names={
        EN: "hisser, Madagascar hissing cockroach",
        PL: "karaczan madagaskarski",
    },
)
A_MERIDIONALIS = Species(
    name="Amitermes meridionalis",
    local_names={EN: "magnetic termite"},
    known_for=[
        {EN: "wedge-shaped mounds aligned with its main axis running north and south"}
    ],
)
C_FORMOSANUS = Species(
    name="Coptotermes formosanus",
    local_names={EN: "super-termite, Formosan termite"},
    known_for=[{EN: "devour wood at a faster rate than any other termites"}],
)

BLATTA = Genus(name="Blatta", children=[B_ORIENTALIS])
PERIPLANETA = Genus(name="Periplaneta", children=[P_AMERICANA])
BLATTELLA = Genus(name="Blattella", children=[B_GERMANICA])
GROMPHADORHINA = Genus(name="Gromphadorhina", children=[G_PORTENTOSA])
AMITERMES = Genus(name="Amitermes", children=[A_MERIDIONALIS])
COPTOTERMES = Genus(name="Coptotermes", children=[C_FORMOSANUS])

BLATTIDAE = Family(name="Blattidae", children=[BLATTA, PERIPLANETA])
ECTOBIIDAE = Family(name="Ectobiidae", children=[BLATTELLA])
BLABERIDAE = Family(name="Blaberidae", children=[GROMPHADORHINA])
TERMITIDAE = Family(name="Termitidae", children=[AMITERMES])
RHINOTERMITIDAE = Family(name="Rhinotermitidae", children=[COPTOTERMES])

BLATTOIDAE = Epifamily(name="Blattoidae", children=[BLATTIDAE])
TERMITOIDAE = Epifamily(name="Termitoidae", children=[TERMITIDAE, RHINOTERMITIDAE])

BLATTOIDEA = Superfamily(name="Blattoidea", children=[BLATTOIDAE, TERMITOIDAE])
BLABEROIDEA = Superfamily(name="Blaberoidea", children=[ECTOBIIDAE, BLABERIDAE])

BLATTODEA = Order(name="Blattodea", children=[BLATTOIDEA, BLABEROIDEA])
