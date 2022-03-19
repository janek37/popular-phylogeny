from clade import Clade, Class, Family, Genus, Kingdom, Order, Phylum, Species
from constants import EN, JP, PL

from .land_plants import EMBRYOPHYTA

P_PALMATA = Species(name="Palmaria palmata", local_names={EN: "dulse"})
C_CRISPUS = Species(name="Chondrus crispus", local_names={EN: "carrageen moss"})
P_TENERA = Species(name="Pyropia tenera", local_names={JP: "nori"})
U_LACTUCA = Species(
    name="Ulva lactuca", local_names={EN: "sea lettuce", PL: "sałata morska"}
)
T_ARBORICOLA = Species(
    name="Trebouxia arboricola", known_for=[{EN: "very common lichen photobiont"}]
)

PALMARIA = Genus(name="Palmaria", children=[P_PALMATA])
CHONDRUS = Genus(name="Chondrus", children=[C_CRISPUS])
PYROPIA = Genus(name="Pyropia", children=[P_TENERA])
ULVA = Genus(name="Ulva", children=[U_LACTUCA])
TREBOUXIA = Genus(name="Trebouxia", children=[T_ARBORICOLA])

PALMARIACEAE = Family(name="Palmariaceae", children=[PALMARIA])
GIGARTINACEAE = Family(name="Gigartinaceae", children=[CHONDRUS])
BANGIACEAE = Family(name="Bangiaceae", children=[PYROPIA])
ULVACEAE = Family(name="Ulvaceae", children=[ULVA])
TREBOUXIACEAE = Family(name="Trebouxiaceae", children=[TREBOUXIA])

PALMARIALES = Order(name="Palmariales", children=[PALMARIACEAE])
GIGARTINALES = Order(name="Gigartinales", children=[GIGARTINACEAE])
BANGIALES = Order(name="Bangiales", children=[BANGIACEAE])
ULVALES = Order(name="Ulvales", children=[ULVACEAE])
TREBOUXIALES = Order(name="Trebouxiales", children=[TREBOUXIACEAE])

FLORIDEOPHYCEAE = Class(name="Florideophyceae", children=[PALMARIALES, GIGARTINALES])
BANGIOPHYCEAE = Class(name="Bangiophyceae", children=[BANGIALES])
ULVOPHYCEAE = Class(name="Ulvophyceae", children=[ULVALES])
TREBOUXIAPHYCEAE = Class(name="Trebouxiaphyceae", children=[TREBOUXIALES])

RODOPHYTA = Phylum(name="Rodophyta", children=[FLORIDEOPHYCEAE, BANGIOPHYCEAE])
CHLOROPHYTA = Phylum(name="Chlorophyta", children=[ULVOPHYCEAE, TREBOUXIAPHYCEAE])

VIRIDIPLANTAE = Clade(name="Viridiplantae", children=[CHLOROPHYTA, EMBRYOPHYTA])

ARCHAEOPLASTIDA = Kingdom(name="Archaeoplastida", children=[RODOPHYTA, VIRIDIPLANTAE])
