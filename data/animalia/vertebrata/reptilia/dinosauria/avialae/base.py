from clade import Clade, Class, Family, Genus, Species
from constants import EN

from .palaeognathe import PALAEOGNATHAE

A_SIEMENSII = Species(
    name="Archaeopteryx siemensii",
    known_for=[{EN: "famous fossil of the Berlin specimen"}],
)

ARCHAEOPTERYX = Genus(name="Archaeopteryx", children=[A_SIEMENSII])

ARCHAEOPTERYGIDAE = Family(name="Archaeopterygidae", children=[ARCHAEOPTERYX])

AVES = Class(name="Aves", children=[PALAEOGNATHAE])

AVIALAE = Clade(name="Avialae", children=[ARCHAEOPTERYGIDAE, AVES])
