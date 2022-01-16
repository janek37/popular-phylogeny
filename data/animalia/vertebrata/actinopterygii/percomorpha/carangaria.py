from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

S_BARRACUDA = Species(
    name="Sphyraena barracuda",
    local_names={EN: "great barracuda", PL: "barrakuda wielka"},
)
X_GLADIUS = Species(
    name="Xiphias gladius", local_names={EN: "swordfish", PL: "miecznik, włócznik"}
)
I_PLATYPTERUS = Species(
    name="Istiophorus platypterus",
    local_names={EN: "Indo-Pacific sailfish", PL: "żaglica"},
    known_for=[{EN: "one of the fastest fish in the ocean"}],
)
P_FLESUS = Species(
    name="Platichthys flesus",
    local_names={EN: "European flounder", PL: "flądra, stornia"},
)
H_HIPPOGLOSSUS = Species(
    name="Hippoglossus hippoglossus",
    local_names={EN: "Atlantic halibut", PL: "halibut atlantycki"},
)
S_SOLEA = Species(
    name="Solea solea", local_names={EN: "common sole", PL: "sola zwyczajna"}
)

SPHYRAENA = Genus(name="Sphyraena", children=[S_BARRACUDA])
XIPHIAS = Genus(name="Xiphias", children=[X_GLADIUS])
ISTIOPHORUS = Genus(name="Istiophorus", children=[I_PLATYPTERUS])
PLATICHTHYS = Genus(name="Platichthys", children=[P_FLESUS])
HIPPOGLOSSUS = Genus(name="Hippoglossus", children=[H_HIPPOGLOSSUS])
SOLEA = Genus(name="Solea", children=[S_SOLEA])

SPHYRAENIDAE = Family(name="Sphyraenidae", children=[SPHYRAENA])
XIPHIIDAE = Family(name="Xiphiidae", children=[XIPHIAS])
ISTIOPHORIDAE = Family(name="Istiophoridae", children=[ISTIOPHORUS])
PLEURONECTIDAE = Family(name="Pleuronectidae", children=[PLATICHTHYS, HIPPOGLOSSUS])
SOLEIDAE = Family(name="Soleidae", children=[SOLEA])

# no source, but rather obvious
ISTIOPHORIFORMES_A = Clade(children=[XIPHIIDAE, ISTIOPHORIDAE])

# not sure about Sphyraenidae, conflicting information
ISTIOPHORIFORMES = Order(
    name="Istiophoriformes", children=[SPHYRAENIDAE, ISTIOPHORIFORMES_A]
)
PLEURONECTIFORMES = Order(name="Pleuronectiformes", children=[PLEURONECTIDAE, SOLEIDAE])

CARANGARIA = Clade(name="Carangaria", children=[ISTIOPHORIFORMES, PLEURONECTIFORMES])
