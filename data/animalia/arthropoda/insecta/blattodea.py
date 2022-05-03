from clade import Epifamily, Family, Genus, Order, Species, Superfamily
from constants import EN, PL
from image import Image, License

B_ORIENTALIS = Species(
    name="Blatta orientalis",
    local_names={EN: "oriental cockroach", PL: "karaluch, karaczan wschodni"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Blatta_orientalis_Trento_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Blatta_orientalis_Trento_02.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
P_AMERICANA = Species(
    name="Periplaneta americana",
    local_names={
        EN: "American cockroach",
        PL: "karaluch amerykański, przybyszka amerykańska",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Periplaneta_americana_(6553770333).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Periplaneta_americana_%286553770333%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
B_GERMANICA = Species(
    name="Blattella germanica",
    local_names={EN: "German cockroach", PL: "karaczan prusak"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202203_german_cockroach.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/202203_german_cockroach.svg",
        author="DataBase Center for Life Science",
        license=License.CC_BY_4_0,
    ),
)
G_PORTENTOSA = Species(
    name="Gromphadorhina portentosa",
    local_names={
        EN: "hisser, Madagascar hissing cockroach",
        PL: "karaczan madagaskarski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fauchschabe_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Fauchschabe_01.jpg",
        author="Peter Jarosz (Cybergen)",
        license=License.CC_BY_SA_2_0_DE,
    ),
)
A_MERIDIONALIS = Species(
    name="Amitermes meridionalis",
    local_names={EN: "magnetic termite"},
    known_for=[
        {EN: "wedge-shaped mounds aligned with its main axis running north and south"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flickr_-_brewbooks_-_Magnetic_Termite_mound_-_Litchfield_National_Park.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Flickr_-_brewbooks_-_Magnetic_Termite_mound_-_Litchfield_National_Park.jpg",
        author="brewbooks from near Seattle, USA",
        license=License.CC_BY_SA_2_0,
    ),
)
C_FORMOSANUS = Species(
    name="Coptotermes formosanus",
    local_names={EN: "super-termite, Formosan termite"},
    known_for=[{EN: "devour wood at a faster rate than any other termites"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coptotermes_formosanus_shiraki_USGov_k8204-7.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Coptotermes_formosanus_shiraki_USGov_k8204-7.jpg",
        author="Scott Bauer",
        license=License.USDA,
    ),
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
