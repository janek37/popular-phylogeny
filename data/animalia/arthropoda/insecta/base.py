from clade import Class, Family, Genus, Order, Species, Subclass
from constants import EN, PL

from .hydropalaeoptera import HYDROPALAEOPTERA

L_SACCHARINUM = Species(
    name="Lepisma saccharinum", local_names={EN: "silverfish", PL: "rybik cukrowy"}
)

LEPISMA = Genus(name="Lepisma", children=[L_SACCHARINUM])

LEPISMATIDAE = Family(name="Lepismatidae", children=[LEPISMA])

ZYGENTOMA = Order(name="Zygentoma", children=[LEPISMATIDAE])

PTERYGOTA = Subclass(name="Pterygota", children=[HYDROPALAEOPTERA])

INSECTA = Class(name="Insecta", children=[ZYGENTOMA, PTERYGOTA])
