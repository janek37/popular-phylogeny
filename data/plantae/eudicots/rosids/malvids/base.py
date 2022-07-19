from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

from .brassicales import BRASSICALES
from .malvales import MALVALES
from .myrtales import MYRTALES
from .sapindales import SAPINDALES

P_PELTATUM = Species(
    name="Pelargonium peltatum",
    local_names={
        EN: "ivy-leaved pelargonium, cascading geranium",
        PL: "pelargonia bluszczolistna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pelargonium_peltatum_kz1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Pelargonium_peltatum_kz1.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)

PELARGONIUM = Genus(name="Pelargonium", children=[P_PELTATUM])

GERANIACEAE = Family(name="Geraniaceae", children=[PELARGONIUM])

GERANIALES = Order(name="Geraniales", children=[GERANIACEAE])

GERANIALES_MYRTALES = Clade(children=[GERANIALES, MYRTALES])
MALVALES_BRASSICALES = Clade(children=[MALVALES, BRASSICALES])
MALVIDS_A = Clade(children=[SAPINDALES, MALVALES_BRASSICALES])
MALVIDS = Clade(name="Malvids", children=[GERANIALES_MYRTALES, MALVIDS_A])
