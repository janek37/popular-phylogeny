from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
    Subclass,
    Superphylum,
)
from constants import EN, PL

from .cnidaria import CNIDARIA
from .mollusca import MOLLUSCA

A_FISTULARIS = Species(
    name="Aplysina fistularis",
    local_names={EN: "yellow sponge"},
    known_for={EN: "SpongeBob SquarePants"},
)
F_HEPATICA = Species(
    name="Fasciola hepatica",
    local_names={EN: "common liver fluke", PL: "motylica wątrobowa"},
)
T_SAGINATA = Species(
    name="Taenia saginata",
    local_names={EN: "beef tapeworm", PL: "tasiemiec nieuzbrojony"},
)
T_SOLIUM = Species(
    name="Taenia solium", local_names={EN: "pork tapeworm", PL: "tasiemiec uzbrojony"}
)
L_TERRESTRIS = Species(
    name="Lumbricus terrestris",
    local_names={EN: "common earthworm", PL: "dżdżownica ziemna"},
)
H_MEDICINALIS = Species(
    name="Hirudo medicinalis",
    local_names={EN: "European medicinal leech", PL: "pijawka lekarska"},
)

APLYSINA = Genus(name="Aplysina", children=[A_FISTULARIS])
FASCIOLA = Genus(name="Fasciola", children=[F_HEPATICA])
TAENIA = Genus(name="Taenia", children=[T_SAGINATA, T_SOLIUM])
LUMBRICUS = Genus(name="Lumbricus", children=[L_TERRESTRIS])
HIRUDO = Genus(name="Hirudo", children=[H_MEDICINALIS])

APLYSINIDAE = Family(name="Aplysinidae", children=[APLYSINA])
FASCIOLIDAE = Family(name="Fasciolidae", children=[FASCIOLA])
TAENIIDAE = Family(name="Taeniidae", children=[TAENIA])
LUMBRICIDAE = Family(name="Lumbricidae", children=[LUMBRICUS])
HIRUDINIDAE = Family(name="Hirudinidae", children=[HIRUDO])

VERONGIDA = Order(name="Verongida", children=[APLYSINIDAE])
PLAGIORCHIIDA = Order(name="Plagiorchiida", children=[FASCIOLIDAE])
CYCLOPHYLLIDEA = Order(name="Cyclophyllidea", children=[TAENIIDAE])
OPISTHOPORA = Order(name="Opisthopora", children=[LUMBRICIDAE])
ARHYNCHOBDELLIDA = Order(name="Arhynchobdellida", children=[HIRUDINIDAE])

DIGENEA = Subclass(name="Digenea", children=[PLAGIORCHIIDA])

DEMOSPONGIAE = Class(name="Demospongiae", children=[VERONGIDA])
TREMATODA = Class(name="Trematoda", children=[DIGENEA])  # not sure about class
CESTODA = Class(name="Cestoda", children=[CYCLOPHYLLIDEA])
CITELLATA = Class(name="Citellata", children=[OPISTHOPORA, ARHYNCHOBDELLIDA])

PORIFERA = Phylum(name="Porifera", children=[DEMOSPONGIAE])
PLATYHELMINTHES = Phylum(name="Platyhelminthes", children=[TREMATODA, CESTODA])
ANNELIDA = Phylum(name="Annelida", children=[CITELLATA])

LOPHOTROCHOZOA = Superphylum(name="Lophotrochozoa", children=[ANNELIDA, MOLLUSCA])

PLATYTROCHOZOA = Clade(
    name="Platytrochozoa", children=[PLATYHELMINTHES, LOPHOTROCHOZOA]
)
PARAHOXOZOA = Clade(name="ParaHoxozoa", children=[CNIDARIA, PLATYTROCHOZOA])

ANIMALIA = Kingdom(name="Animalia", children=[PORIFERA, PARAHOXOZOA])
