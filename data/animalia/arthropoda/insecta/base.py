from clade import Class, Family, Genus, Infraclass, Order, Species, Subclass
from constants import EN, PL

from .hydropalaeoptera import HYDROPALAEOPTERA
from .polyneoptera import POLYNEOPTERA

L_SACCHARINUM = Species(
    name="Lepisma saccharinum", local_names={EN: "silverfish", PL: "rybik cukrowy"}
)

LEPISMA = Genus(name="Lepisma", children=[L_SACCHARINUM])

LEPISMATIDAE = Family(name="Lepismatidae", children=[LEPISMA])

ZYGENTOMA = Order(name="Zygentoma", children=[LEPISMATIDAE])

# insect phylogeny is not stable, I'm using the current tree at
# https://en.wikipedia.org/wiki/Insect
# but there are many contradictions in Wikipedia alone
NEOPTERA = Infraclass(name="Neoptera", children=[POLYNEOPTERA])  # or Division?

PTERYGOTA = Subclass(name="Pterygota", children=[HYDROPALAEOPTERA, NEOPTERA])

INSECTA = Class(name="Insecta", children=[ZYGENTOMA, PTERYGOTA])
