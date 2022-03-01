from clade import Clade, Class, Family, Genus, Infraclass, Species, Superorder
from constants import EN

from .anseriformes import ANSERIFORMES
from .galliformes import GALLIFORMES
from .neoaves import NEOAVES
from .palaeognathe import PALAEOGNATHAE

A_SIEMENSII = Species(
    name="Archaeopteryx siemensii",
    known_for=[{EN: "famous fossil of the Berlin specimen"}],
    extinct=True,
)

ARCHAEOPTERYX = Genus(name="Archaeopteryx", children=[A_SIEMENSII])

ARCHAEOPTERYGIDAE = Family(name="Archaeopterygidae", children=[ARCHAEOPTERYX])

GALLOANSERAE = Superorder(name="Galloanserae", children=[GALLIFORMES, ANSERIFORMES])

NEOGNATHAE = Infraclass(name="Neognathae", children=[GALLOANSERAE, NEOAVES])

AVES = Class(name="Aves", children=[PALAEOGNATHAE, NEOGNATHAE])

AVIALAE = Clade(name="Avialae", children=[ARCHAEOPTERYGIDAE, AVES])
