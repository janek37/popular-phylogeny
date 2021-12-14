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

# region PORIFERA
A_FISTULARIS = Species(
    name="Aplysina fistularis",
    local_names={EN: "yellow sponge"},
    known_for={EN: "SpongeBob SquarePants"},
)
APLYSINA = Genus(name="Aplysina", children=[A_FISTULARIS])
APLYSINIDAE = Family(name="Aplysinidae", children=[APLYSINA])
VERONGIDA = Order(name="Verongida", children=[APLYSINIDAE])
DEMOSPONGIAE = Class(name="Demospongiae", children=[VERONGIDA])
PORIFERA = Phylum(name="Porifera", children=[DEMOSPONGIAE])
# endregion PORIFERA

# region PLATYHELIMNTES
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

FASCIOLA = Genus(name="Fasciola", children=[F_HEPATICA])
TAENIA = Genus(name="Taenia", children=[T_SAGINATA, T_SOLIUM])

FASCIOLIDAE = Family(name="Fasciolidae", children=[FASCIOLA])
TAENIIDAE = Family(name="Taeniidae", children=[TAENIA])

PLAGIORCHIIDA = Order(name="Plagiorchiida", children=[FASCIOLIDAE])
CYCLOPHYLLIDEA = Order(name="Cyclophyllidea", children=[TAENIIDAE])

DIGENEA = Subclass(name="Digenea", children=[PLAGIORCHIIDA])

TREMATODA = Class(name="Trematoda", children=[DIGENEA])  # not sure about class

CESTODA = Class(name="Cestoda", children=[CYCLOPHYLLIDEA])

PLATYHELMINTHES = Phylum(name="Platyhelminthes", children=[TREMATODA, CESTODA])
# endregion PLATYHELIMNTES

# region ANNELIDA
L_TERRESTRIS = Species(
    name="Lumbricus terrestris",
    local_names={EN: "common earthworm", PL: "dżdżownica ziemna"},
)
H_MEDICINALIS = Species(
    name="Hirudo medicinalis",
    local_names={EN: "European medicinal leech", PL: "pijawka lekarska"},
)

LUMBRICUS = Genus(name="Lumbricus", children=[L_TERRESTRIS])
HIRUDO = Genus(name="Hirudo", children=[H_MEDICINALIS])

LUMBRICIDAE = Family(name="Lumbricidae", children=[LUMBRICUS])
HIRUDINIDAE = Family(name="Hirudinidae", children=[HIRUDO])

OPISTHOPORA = Order(name="Opisthopora", children=[LUMBRICIDAE])
ARHYNCHOBDELLIDA = Order(name="Arhynchobdellida", children=[HIRUDINIDAE])

CITELLATA = Class(name="Citellata", children=[OPISTHOPORA, ARHYNCHOBDELLIDA])

ANNELIDA = Phylum(name="Annelida", children=[CITELLATA])
# endregion ANNELIDA

# region NEMATODA
A_LUMBRICOIDES = Species(
    name="Ascaris lumbricoides",
    local_names={EN: "large roundworm", PL: "glista ludzka"},
)
E_VERMICULARIS = Species(
    name="Enterobius vermicularis",
    local_names={EN: "pinworm, threadworm", PL: "owsik ludzki"},
)

ASCARIS = Genus(name="Ascaris", children=[A_LUMBRICOIDES])
ENTEROBIUS = Genus(name="Enterobius", children=[E_VERMICULARIS])

ASCARIDIDAE = Family(name="Ascarididae", children=[ASCARIS])
OXYURIDAE = Family(name="Oxyuridae", children=[ENTEROBIUS])

ASCARIDIDA = Order(name="Ascaridida", children=[ASCARIDIDAE])
RHABDITIDA = Order(name="Rhabditida", children=[OXYURIDAE])

CHROMADOREA = Class(name="Chromadorea", children=[ASCARIDIDA, RHABDITIDA])

NEMATODA = Phylum(name="Nematoda", children=[CHROMADOREA])
# endregion NEMATODA

LOPHOTROCHOZOA = Superphylum(name="Lophotrochozoa", children=[ANNELIDA, MOLLUSCA])
ECDYSOZOA = Superphylum(name="Ecdysozoa", children=[NEMATODA])

PLATYTROCHOZOA = Clade(
    name="Platytrochozoa", children=[PLATYHELMINTHES, LOPHOTROCHOZOA]
)
PROTOSTOMIA = Class(
    name="Protostomia",
    children=[PLATYTROCHOZOA, ECDYSOZOA],
    local_names={PL: "pierwouste"},
)
PARAHOXOZOA = Clade(name="ParaHoxozoa", children=[CNIDARIA, PROTOSTOMIA])

ANIMALIA = Kingdom(name="Animalia", children=[PORIFERA, PARAHOXOZOA])