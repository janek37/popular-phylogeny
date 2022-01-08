from clade import Class, Family, Genus, Order, Species, Subclass
from constants import EN, PL

from .teleostei import TELEOSTEI

A_STURIO = Species(
    name="Acipenser sturio",
    local_names={EN: "common sturgeon, European sea sturgeon", PL: "jesiotr zachodni"},
)

ACIPENSER = Genus(name="Acipenser", children=[A_STURIO])

ACIPENSERIDAE = Family(name="Acipenseridae", children=[ACIPENSER])

ACIPENSERIFORMES = Order(name="Acipenseriformes", children=[ACIPENSERIDAE])

CHONDROSTEI = Subclass(name="Chondrostei", children=[ACIPENSERIFORMES])
NEOPTERYGII = Subclass(name="Neopterygii", children=[TELEOSTEI])

ACTINOPTERYGII = Class(name="Actinopterygii", children=[CHONDROSTEI, NEOPTERYGII])
