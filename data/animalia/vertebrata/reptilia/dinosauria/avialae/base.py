from clade import Clade, Class, Family, Genus, Infraclass, Species, Superorder
from constants import EN

from .galliformes import GALLIFORMES
from .palaeognathe import PALAEOGNATHAE

A_SIEMENSII = Species(
    name="Archaeopteryx siemensii",
    known_for=[{EN: "famous fossil of the Berlin specimen"}],
)

ARCHAEOPTERYX = Genus(name="Archaeopteryx", children=[A_SIEMENSII])

ARCHAEOPTERYGIDAE = Family(name="Archaeopterygidae", children=[ARCHAEOPTERYX])

GALLOANSERAE = Superorder(name="Galloanserae", children=[GALLIFORMES])

NEOGNATHAE = Infraclass(name="Neognathae", children=[GALLOANSERAE])

AVES = Class(name="Aves", children=[PALAEOGNATHAE, NEOGNATHAE])

AVIALAE = Clade(name="Avialae", children=[ARCHAEOPTERYGIDAE, AVES])
