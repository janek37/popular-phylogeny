from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

from .columbiformes import COLUMBIFORMES
from .passerea import PASSEREA

P_RUBER = Species(
    name="Phoenicopterus ruber",
    local_names={EN: "American flamingo", PL: "flaming karmazynowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phoenicopterus_ruber_Bonaire_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Phoenicopterus_ruber_Bonaire_1.jpg",
        author="Paul Asman and Jill Lenoble",
        license=License.CC_BY_2_0,
    ),
)
P_CRISTATUS = Species(
    name="Podiceps cristatus",
    local_names={EN: "great-crested grabe", PL: "perkoz dwuczuby"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Podiceps_cristatus_189221720.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/53/Podiceps_cristatus_189221720.jpg",
        author="Daniel S. Katz",
        license=License.CC_BY_4_0,
    ),
)

PHOENICOPTERUS = Genus(name="Phoenicopterus", children=[P_RUBER])
PODICEPS = Genus(name="Podiceps", children=[P_CRISTATUS])

PHOENICOPTERIDAE = Family(name="Phoenicopteridae", children=[PHOENICOPTERUS])
PODICIPEDIDAE = Family(name="Podicipedidae", children=[PODICEPS])

PHOENICOPTERIFORMES = Order(name="Phoenicopteriformes", children=[PHOENICOPTERIDAE])
PODICIPEDIFORMES = Order(name="Podicipediformes", children=[PODICIPEDIDAE])

MIRANDORNITHES = Clade(
    name="Mirandornithes", children=[PHOENICOPTERIFORMES, PODICIPEDIFORMES]
)

NEOAVES = Clade(name="Neoaves", children=[MIRANDORNITHES, COLUMBIFORMES, PASSEREA])
