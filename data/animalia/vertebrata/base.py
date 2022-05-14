from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Infraphylum,
    Order,
    Species,
    Subclass,
    Subphylum,
    Superclass,
)
from constants import EN, PL
from image import Image, License

from .actinopterygii import ACTINOPTERYGII
from .amphibia import AMPHIBIA
from .chondrichthyes import CHONDRICHTHYES
from .mammalia import MAMMALIA
from .reptilia import REPTILIA

# region AGNATHA
M_GLUTINOSA = Species(
    name="Myxine glutinosa",
    local_names={EN: "Atlantic hagfish", PL: "śluzica pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myxine_glutinosa_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/Myxine_glutinosa_Gervais.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_MARINUS = Species(
    name="Petromyzon marinus",
    local_names={EN: "sea lamprey", PL: "minóg morski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Petromyzon_marinus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Petromyzon_marinus.jpg",
        author="Ellen Edmonson",
        license=License.PUBLIC_DOMAIN,
    ),
)

MYXINE = Genus(name="Myxine", children=[M_GLUTINOSA])
PETROMYZON = Genus(name="Petromyzon", children=[P_MARINUS])

MYXINIDAE = Family(name="Myxinidae", children=[MYXINE])
PETROMYZONTIDAE = Family(name="Petromyzontidae", children=[PETROMYZON])

MYXINIFORMES = Order(name="Myxiniformes", children=[MYXINIDAE])
PETROMYZONTIFORMES = Order(name="Petromyzontiformes", children=[PETROMYZONTIDAE])

MYXINI = Class(name="Myxini", children=[MYXINIFORMES])
HYPEROARTIA = Class(name="Hyperoartia", children=[PETROMYZONTIFORMES])

AGNATHA = Infraphylum(name="Agnatha", children=[MYXINI, HYPEROARTIA])
# endregion AGNATHA

# region SARCOPTERYGII
L_CHALUMNAE = Species(
    name="Latimeria chalumnae",
    local_names={EN: "West Indian Ocean coelacanth, gombessa", PL: "latimeria"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coelacanth_model,_Devonian_-_Houston_Museum_of_Natural_Science_-_DSC01709_(white_background).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Coelacanth_model%2C_Devonian_-_Houston_Museum_of_Natural_Science_-_DSC01709_%28white_background%29.png",
        author="Daderot",
        license=License.CC0,
    ),
)
N_FORSTERI = Species(
    name="Neoceratodus forsteri",
    local_names={
        EN: "Australian lungfish, Queensland lungfish, Burnett salmon, barramunda",
        PL: "barramunda, rogoząb australijski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Neoceratodus_forsteri,_2014-09-19.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1f/Neoceratodus_forsteri%2C_2014-09-19.JPG",
        author="https://upload.wikimedia.org/wikipedia/commons/1/1f/Neoceratodus_forsteri%2C_2014-09-19.JPG",
        license=License.CC_BY_SA_4_0,
    ),
)
D_LIMBATUS = Species(
    name="Dimetrodon limbatus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dimetrodon_grandis_3D_Model_Reconstruction.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Dimetrodon_grandis_3D_Model_Reconstruction.png",
        author="Max Bellomio",
        license=License.CC_BY_SA_4_0,
    ),
)

LATIMERIA = Genus(name="Latimeria", children=[L_CHALUMNAE])
NEOCERATODUS = Genus(name="Neoceratodus", children=[N_FORSTERI])
DIMETRODON = Genus(name="Dimetrodon", children=[D_LIMBATUS])

LATIMERIIDAE = Family(name="Latimeriidae", children=[LATIMERIA])
NEOCERATODONTIDAE = Family(name="Neoceratodontidae", children=[NEOCERATODUS])
SPHENACODONTIDAE = Family(name="Sphenacodontidae", children=[DIMETRODON])

COELACANTHIFORMES = Order(name="Coelacanthiformes", children=[LATIMERIIDAE])
DIPNOI = Order(name="Dipnoi", children=[NEOCERATODONTIDAE])

ACTINISTIA = Subclass(name="Actinistia", children=[COELACANTHIFORMES])

SAUROPSIDA = Clade(name="Sauropsida", children=[REPTILIA])
SYNAPSIDA = Clade(name="Synapsida", children=[SPHENACODONTIDAE, MAMMALIA])

AMNIOTA = Clade(name="Amniota", children=[SAUROPSIDA, SYNAPSIDA])

TETRAPODA = Superclass(name="Tetrapoda", children=[AMPHIBIA, AMNIOTA])

RHIPIDISTIA = Clade(name="Rhipidistia", children=[DIPNOI, TETRAPODA])

SARCOPTERYGII = Clade(name="Sarcopterygii", children=[ACTINISTIA, RHIPIDISTIA])
# endregion SARCOPTERYGII

EUTELEOSTOMI = Clade(name="Euteleostomi", children=[ACTINOPTERYGII, SARCOPTERYGII])

GNATHOSTOMATA = Infraphylum(
    name="Gnathostomata", children=[CHONDRICHTHYES, EUTELEOSTOMI]
)

VERTEBRATA = Subphylum(name="Vertebrata", children=[AGNATHA, GNATHOSTOMATA])
