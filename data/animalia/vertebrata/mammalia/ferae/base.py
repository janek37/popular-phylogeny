from clade import Family, Genus, Mirorder, Order, Species
from constants import EN, PL

from .caniformia import CANIFORMIA
from .feliformia import FELIFORMIA

M_CRASSICAUDATA = Species(
    name="Manis crassicaudata",
    local_names={EN: "Indian pangolin", PL: "łuskowiec indyjski"},
)

MANIS = Genus(name="Manis", children=[M_CRASSICAUDATA])

MANIDAE = Family(name="Manidae", children=[MANIS])

PHOLIDOTA = Order(name="Pholidota", children=[MANIDAE])
CARNIVORA = Order(name="Carnivora", children=[FELIFORMIA, CANIFORMIA])

FERAE = Mirorder(name="Ferae", children=[PHOLIDOTA, CARNIVORA])
