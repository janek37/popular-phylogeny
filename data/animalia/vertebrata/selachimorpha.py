from clade import Clade, Family, Genus, Order, Species, Superorder
from constants import EN, PL
from image import Image, License

C_CARCHARIAS = Species(
    name="Carcharodon carcharias",
    local_names={EN: "great white shark", PL: "żarłacz biały, rekin ludojad"},
    known_for=[{EN: "Jaws"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Great_White_Shark_(14730796397).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Great_White_Shark_%2814730796397%29.jpg",
        author="Elias Levy",
        license=License.CC_BY_2_0,
    ),
)
S_ZYGAENA = Species(
    name="Sphyrna zygaena",
    local_names={EN: "smooth hammerhead", PL: "rekin młot, głowomłot pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Smooth_hammerhead_(Duane_Raver).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4a/Smooth_hammerhead_%28Duane_Raver%29.png",
        author="Raver Duane, U.S. Fish and Wildlife Service",
        license=License.PUBLIC_DOMAIN,
    ),
)
R_TYPUS = Species(
    name="Rhincodon typus",
    local_names={EN: "whale shark", PL: "rekin wielorybi"},
    known_for=[{EN: "the largest living nonmammalian vertebrate"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhincodon_typus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a0/Rhincodon_typus.png",
        author="Zac Wolf",
        license=License.CC_BY_SA_2_5,
    ),
)
G_CUVIER = Species(
    name="Galeocerdo cuvier",
    local_names={EN: "tiger shark", PL: "żarłacz tygrysi"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tiger_Shark_Galeocerdo_Cuvier_(223179837).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Tiger_Shark_Galeocerdo_Cuvier_%28223179837%29.jpeg",
        author="Kris Mikael Krister",
        license=License.CC_BY_3_0,
    ),
)
P_GLAUCA = Species(
    name="Prionace glauca",
    local_names={EN: "blue shark", PL: "żarłacz błękitny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prionace_glauca_nmfs.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Prionace_glauca_nmfs.jpg",
        author="NMFS, E. Hoffmayer, S. Iglésias and R. McAuley",
        license=License.NOAA,
    ),
)
O_MEGALODON = Species(
    name="Otodus megalodon",
    local_names={EN: "megalodon"},
    known_for=[{EN: "giant extinct shark"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Megalodon_restoration.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f4/Megalodon_restoration.png",
        author="Oliver E. Demuth",
        license=License.CC_BY_SA_4_0,
    ),
)
S_ACANTHIAS = Species(
    name="Squalus acanthias",
    local_names={EN: "spiny dogfish", PL: "koleń pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Squalus_acanthias_stellwagen.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/Squalus_acanthias_stellwagen.jpg",
        author="Doug Costa, NOAA/Stellwagen Bank National Marine Sanctuary",
        license=License.NOAA,
    ),
)
S_SQUATINA = Species(
    name="Squatina squatina",
    local_names={EN: "angelshark, monkfish", PL: "raszpla zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Squatina_squatina.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/42/Squatina_squatina.jpg",
        author="Anonymous",
        license=License.PUBLIC_DOMAIN,
    ),
)

CARCHARODON = Genus(name="Carcharodon", children=[C_CARCHARIAS])
SPHYRNA = Genus(name="Sphyrna", children=[S_ZYGAENA])
RHINCODON = Genus(name="Rhincodon", children=[R_TYPUS])
GALEOCERDO = Genus(name="Galeocerdo", children=[G_CUVIER])
PRIONACE = Genus(name="Prionace", children=[P_GLAUCA])
OTODUS = Genus(name="Otodus", children=[O_MEGALODON])
SQUALUS = Genus(name="Squalus", children=[S_ACANTHIAS])
SQUATINA = Genus(name="Squatina", children=[S_SQUATINA])

LAMNIDAE = Family(name="Lamnidae", children=[CARCHARODON])
SPHYRNIDAE = Family(name="Sphyrnidae", children=[SPHYRNA])
RHINCODONTIDAE = Family(name="Rhincodontidae", children=[RHINCODON])
CARCHARHINIDAE = Family(name="Carcharhinidae", children=[GALEOCERDO, PRIONACE])
OTODONTIDAE = Family(name="Otodontidae", children=[OTODUS])
SQUALIDAE = Family(name="Squalidae", children=[SQUALUS])
SQUATINIDAE = Family(name="Squatinidae", children=[SQUATINA])

LAMNIFORMES = Order(name="Lamniformes", children=[LAMNIDAE, OTODONTIDAE])
CARCHARHINIFORMES = Order(
    name="Carcharhiniformes", children=[SPHYRNIDAE, CARCHARHINIDAE]
)
ORECTOLOBIFORMES = Order(name="Orectolobiformes", children=[RHINCODONTIDAE])
SQUALIFORMES = Order(name="Squaliformes", children=[SQUALIDAE])
SQUATINIFORMES = Order(name="Squatiniformes", children=[SQUATINIDAE])

SELACHIMORPHA_A = Clade(children=[LAMNIFORMES, CARCHARHINIFORMES])
SELACHIMORPHA_B = Clade(children=[SELACHIMORPHA_A, ORECTOLOBIFORMES])
SELACHIMORPHA_C = Clade(children=[SQUALIFORMES, SQUATINIFORMES])
SELACHIMORPHA = Superorder(
    name="Selachimorpha", children=[SELACHIMORPHA_B, SELACHIMORPHA_C]
)
