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

from .coleoptera import COLEOPTERA
from .hydropalaeoptera import HYDROPALAEOPTERA
from .hymenoptera import HYMENOPTERA
from .lepidoptera import LEPIDOPTERA
from .paraneoptera import PARANEOPTERA
from .polyneoptera import POLYNEOPTERA

L_SACCHARINUM = Species(
    name="Lepisma saccharinum", local_names={EN: "silverfish", PL: "rybik cukrowy"}
)

LEPISMA = Genus(name="Lepisma", children=[L_SACCHARINUM])

LEPISMATIDAE = Family(name="Lepismatidae", children=[LEPISMA])

ZYGENTOMA = Order(name="Zygentoma", children=[LEPISMATIDAE])

PANORPIDA = Superorder(name="Panorpida", children=[LEPIDOPTERA])

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
