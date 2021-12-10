from clade import Phylum

from .gastropoda import GASTROPODA

MOLLUSCA = Phylum(name="Mollusca", children=[GASTROPODA])
