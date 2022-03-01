from clade import Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL

P_LONGICEPS = Species(name="Pteranodon longiceps", extinct=True)
P_ANTIQUUS = Species(
    name="Pterodactylus antiquus", local_names={PL: "pterodaktyl"}, extinct=True
)
Q_NORTHROPI = Species(
    name="Quetzalcoatlus northropi",
    known_for=[{EN: "the largest known flying animal"}],
    extinct=True,
)

PTERANODON = Genus(name="Pteranodon", children=[P_LONGICEPS])
PTERODACTYLUS = Genus(name="Pterodactylus", children=[P_ANTIQUUS])
QUETZALCOATLUS = Genus(name="Quetzalcoatlus", children=[Q_NORTHROPI])

PTERANODONTIDAE = Family(name="Pteranodontidae", children=[PTERANODON])
AZHDARCHIDAE = Family(name="Azhdarchidae", children=[QUETZALCOATLUS])

EUPTERODACTYLOIDEA = Infraorder(
    name="Eupterodactyloidea", children=[PTERANODONTIDAE, AZHDARCHIDAE]
)

PTERODACTYLOIDEA = Suborder(
    name="Pterodactyloidea", children=[EUPTERODACTYLOIDEA, PTERODACTYLUS]
)

PTEROSAURIA = Order(name="Pterosauria", children=[PTERODACTYLOIDEA])
