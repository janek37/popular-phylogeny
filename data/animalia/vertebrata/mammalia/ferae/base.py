from clade import Family, Genus, Mirorder, Order, Species
from constants import EN, PL
from image import Image, License

from .caniformia import CANIFORMIA
from .feliformia import FELIFORMIA

M_CRASSICAUDATA = Species(
    name="Manis crassicaudata",
    local_names={EN: "Indian pangolin", PL: "łuskowiec indyjski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pangolin_brought_to_the_Range_office,_KMTR_AJTJ_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Pangolin_brought_to_the_Range_office%2C_KMTR_AJTJ_cropped.jpg",
        author="A. J. T. Johnsingh, WWF-India and NCF",
        license=License.CC_BY_SA_4_0,
    ),
)

MANIS = Genus(name="Manis", children=[M_CRASSICAUDATA])

MANIDAE = Family(name="Manidae", children=[MANIS])

PHOLIDOTA = Order(name="Pholidota", children=[MANIDAE])
CARNIVORA = Order(name="Carnivora", children=[FELIFORMIA, CANIFORMIA])

FERAE = Mirorder(name="Ferae", children=[PHOLIDOTA, CARNIVORA])
