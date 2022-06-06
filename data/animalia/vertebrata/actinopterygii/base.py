from clade import Class, Family, Genus, Order, Species, Subclass
from constants import EN, PL
from image import Image, License

from .teleostei import TELEOSTEI

A_STURIO = Species(
    name="Acipenser sturio",
    local_names={EN: "common sturgeon, European sea sturgeon", PL: "jesiotr zachodni"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acipenser_sturio_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Acipenser_sturio_%28cropped%29.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN,
    ),
)

ACIPENSER = Genus(name="Acipenser", children=[A_STURIO])

ACIPENSERIDAE = Family(name="Acipenseridae", children=[ACIPENSER])

ACIPENSERIFORMES = Order(name="Acipenseriformes", children=[ACIPENSERIDAE])

CHONDROSTEI = Subclass(name="Chondrostei", children=[ACIPENSERIFORMES])
NEOPTERYGII = Subclass(name="Neopterygii", children=[TELEOSTEI])

ACTINOPTERYGII = Class(name="Actinopterygii", children=[CHONDROSTEI, NEOPTERYGII])
