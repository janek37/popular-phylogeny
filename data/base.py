from clade import Clade, Domain
from .animalia import ANIMALIA
from .bacteria import BACTERIA
from .fungi import EUMYCOTA
from .plantae import ARCHAEOPLASTIDA
from .protista import SAR, METAMONADA, AMOEBOZOA


OPISTHOKONTA = Clade(name='Opisthokonta', children=[EUMYCOTA, ANIMALIA])

AMORPHEA = Clade(name='Amorphea', children=[AMOEBOZOA, OPISTHOKONTA])

DIAPHORETICKES = Clade(name='Diaphoretices', children=[ARCHAEOPLASTIDA, SAR])
OPIMODA = Clade(name='Opimoda', children=[AMORPHEA, METAMONADA])

EUKARYOTA = Domain(name='Eukaryota', children=[OPIMODA, DIAPHORETICKES])

LIFE = Clade(children=[BACTERIA, EUKARYOTA])
