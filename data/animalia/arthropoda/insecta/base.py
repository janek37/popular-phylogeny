from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Infraclass,
    Order,
    Species,
    Subclass,
    Superorder,
)
from constants import EN, PL
from image import Image, License

from .coleoptera import COLEOPTERA
from .diptera import DIPTERA
from .hydropalaeoptera import HYDROPALAEOPTERA
from .hymenoptera import HYMENOPTERA
from .lepidoptera import LEPIDOPTERA
from .paraneoptera import PARANEOPTERA
from .polyneoptera import POLYNEOPTERA
from .siphonaptera import SIPHONAPTERA

L_SACCHARINUM = Species(
    name="Lepisma saccharinum",
    local_names={EN: "silverfish", PL: "rybik cukrowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lepisma_saccharina_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Lepisma_saccharina_4.jpg",
        author="Iblis-Lakon",
        license=License.CC_BY_SA_3_0,
    ),
)

LEPISMA = Genus(name="Lepisma", children=[L_SACCHARINUM])

LEPISMATIDAE = Family(name="Lepismatidae", children=[LEPISMA])

ZYGENTOMA = Order(name="Zygentoma", children=[LEPISMATIDAE])

ANTLIOPHORA = Clade(name="Antliophora", children=[DIPTERA, SIPHONAPTERA])

PANORPIDA = Superorder(name="Panorpida", children=[LEPIDOPTERA, ANTLIOPHORA])

# insect phylogeny is not stable, I'm using the current tree at
# https://en.wikipedia.org/wiki/Insect
# but there are many contradictions in Wikipedia alone
APARAGLOSSATA = Clade(name="Aparaglossata", children=[COLEOPTERA, PANORPIDA])

ENDOPTERYGOTA = Clade(
    name="Endopterygota", children=[HYMENOPTERA, APARAGLOSSATA]
)  # = Holometabola

EUMETABOLA = Clade(name="Eumetabola", children=[PARANEOPTERA, ENDOPTERYGOTA])

NEOPTERA = Infraclass(
    name="Neoptera", children=[POLYNEOPTERA, EUMETABOLA]
)  # or Division?

PTERYGOTA = Subclass(name="Pterygota", children=[HYDROPALAEOPTERA, NEOPTERA])

INSECTA = Class(name="Insecta", children=[ZYGENTOMA, PTERYGOTA])
