from clade import Clade, Class, Family, Genus, Order, Phylum, Species
from constants import EN

from .bivalvia import BIVALVIA
from .cephalopoda import CEPHALOPODA
from .gastropoda import GASTROPODA

C_GLAUCUS = Species(name="Chiton glaucus", local_names={EN: "blue green chiton"})

CHITON = Genus(name="Chiton", children=[C_GLAUCUS])

CHITONIDAE = Family(name="Chitonidae", children=[CHITON])

CHITONIDA = Order(name="Chitonida", children=[CHITONIDAE])

POLYPLACOPHORA = Class(name="Polyplacophora", children=[CHITONIDA])

# https://www.researchgate.net/publication/328201049_Staggered_Hox_expression_is_more_widespread_among_molluscs_than_previously_appreciated
MOLLUSCA_A = Clade(children=[GASTROPODA, BIVALVIA])
MOLLUSCA_B = Clade(children=[MOLLUSCA_A, CEPHALOPODA])

MOLLUSCA = Phylum(name="Mollusca", children=[MOLLUSCA_B, POLYPLACOPHORA])
