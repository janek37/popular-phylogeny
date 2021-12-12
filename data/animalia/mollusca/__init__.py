from clade import Phylum

from .bivalvia import BIVALVIA
from .gastropoda import GASTROPODA

MOLLUSCA = Phylum(name="Mollusca", children=[GASTROPODA, BIVALVIA])
