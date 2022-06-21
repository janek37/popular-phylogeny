from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

P_ONOCROTALUS = Species(
    name="Pelecanus onocrotalus",
    local_names={EN: "great white pelican", PL: "pelikan różowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pelecanus_onocrotalus_-_Great_White_Pelican,_Adana_2016-12-18_01-3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Pelecanus_onocrotalus_-_Great_White_Pelican%2C_Adana_2016-12-18_01-3.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
A_CINEREA = Species(
    name="Ardea cinerea",
    local_names={EN: "grey heron", PL: "czapla siwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Grey_heron_2022_04_03_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9a/Grey_heron_2022_04_03_03.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)
N_NYCTICORAX = Species(
    name="Nycticorax nycticorax",
    local_names={EN: "black-crowned night heron", PL: "ślepowron zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nycticorax_nycticorax12.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/96/Nycticorax_nycticorax12.jpg",
        author="Calibas",
        license=License.CC_BY_SA_3_0,
    ),
)
T_AETHIOPICUS = Species(
    name="Threskiornis aethiopicus",
    local_names={EN: "African sacred ibis", PL: "ibis czczony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:African_Sacred_Ibis,_Threskiornis_aethiopicus,_at_Pilanesberg_National_Park,_South_Africa_(45081681391).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/African_Sacred_Ibis%2C_Threskiornis_aethiopicus%2C_at_Pilanesberg_National_Park%2C_South_Africa_%2845081681391%29.jpg",
        author="Derek Keats from Johannesburg, South Africa",
        license=License.CC_BY_2_0,
    ),
)
B_REX = Species(
    name="Balaeniceps rex",
    local_names={EN: "shoebill, whalehead", PL: "trzewikodziób"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schuhschnabel_(Balaeniceps_rex).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Schuhschnabel_%28Balaeniceps_rex%29.jpg",
        author="Bildflut",
        license=License.CC0,
    ),
)

PELECANUS = Genus(name="Pelecanus", children=[P_ONOCROTALUS])
ARDEA = Genus(name="Ardea", children=[A_CINEREA])
NYCTICORAX = Genus(name="Nycticorax", children=[N_NYCTICORAX])
THRESKIORNIS = Genus(name="Threskiornis", children=[T_AETHIOPICUS])
BALAENICEPS = Genus(name="Balaeniceps", children=[B_REX])

PELECANIDAE = Family(name="Pelecanidae", children=[PELECANUS])
ARDEIDAE = Family(name="Ardeidae", children=[ARDEA, NYCTICORAX])
THRESKIORNITHIDAE = Family(name="Threskiornithidae", children=[THRESKIORNIS])
BALAENICIPITIDAE = Family(name="Balaenicipitidae", children=[BALAENICEPS])

PELECANIFORMES_A = Clade(children=[PELECANIDAE, BALAENICIPITIDAE])
PELECANIFORMES_B = Clade(children=[PELECANIFORMES_A, ARDEIDAE])
PELECANIFORMES = Order(
    name="Pelecaniformes", children=[PELECANIFORMES_B, THRESKIORNITHIDAE]
)
