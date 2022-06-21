from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL, URL
from image import Image, License

from .piciformes import PICIFORMES

U_EPOPS = Species(
    name="Upupa epops",
    local_names={EN: "Eurasian hoopoe", PL: "dudek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_hoopoe_-_Upupa_epops_06.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Common_hoopoe_-_Upupa_epops_06.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
B_BICORNIS = Species(
    name="Buceros bicornis",
    local_names={EN: "great hornbill", PL: "dzioborożec wielki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg",
        author="Shantanu Kuveskar",
        license=License.CC_BY_SA_4_0,
    ),
)
T_RUFIROSTRIS = Species(
    name="Tockus rufirostris",
    local_names={EN: "southern red-billed hornbill", PL: "toko białogrzbiety"},
    known_for=[
        {EN: "Zazu from The Lion King", URL: "https://disney.fandom.com/wiki/Zazu"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Southern_Red-billed_Hornbill_(Tockus_rufirostris),_Marakele_NP,_South_Africa_(7745673370).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Southern_Red-billed_Hornbill_%28Tockus_rufirostris%29%2C_Marakele_NP%2C_South_Africa_%287745673370%29.jpg",
        author="Derek Keats from Johannesburg, South Africa",
        license=License.CC_BY_2_0,
    ),
)
A_ATTHIS = Species(
    name="Alcedo atthis",
    local_names={EN: "common kingfisher", PL: "zimorodek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_Kingfisher_Alcedo_atthis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cc/Common_Kingfisher_Alcedo_atthis.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
C_GARRULUS = Species(
    name="Coracias garrulus",
    local_names={EN: "European roller", PL: "kraska zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coracias_garrulus_-_European_roller_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Coracias_garrulus_-_European_roller_02.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)

UPUPA = Genus(name="Upupa", children=[U_EPOPS])
BUCEROS = Genus(name="Buceros", children=[B_BICORNIS])
TOCKUS = Genus(name="Tockus", children=[T_RUFIROSTRIS])
ALCEDO = Genus(name="Alcedo", children=[A_ATTHIS])
CORACIAS = Genus(name="Coracias", children=[C_GARRULUS])

UPUPIDAE = Family(name="Upupidae", children=[UPUPA])
BUCEROTIDAE = Family(name="Bucerotidae", children=[BUCEROS, TOCKUS])
ALCEDINIDAE = Family(name="Alcedinidae", children=[ALCEDO])
CORACIIDAE = Family(name="Coraciidae", children=[CORACIAS])

BUCEROTIFORMES = Order(name="Bucerotiformes", children=[UPUPIDAE, BUCEROTIDAE])
CORACIIFORMES = Order(name="Coraciiformes", children=[ALCEDINIDAE, CORACIIDAE])

PICODYNASTORNITHES = Clade(
    name="Picodynastornithes", children=[CORACIIFORMES, PICIFORMES]
)

CORACIIMORPHAE = Clade(
    name="Coraciimorphae", children=[BUCEROTIFORMES, PICODYNASTORNITHES]
)
