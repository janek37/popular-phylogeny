from clade import Clade, Phylum

from .bivalvia import BIVALVIA
from .cephalopoda import CEPHALOPODA
from .gastropoda import GASTROPODA

MOLLUSCA_A = Clade(children=[GASTROPODA, BIVALVIA])

MOLLUSCA = Phylum(name="Mollusca", children=[MOLLUSCA_A, CEPHALOPODA])
