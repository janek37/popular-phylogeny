from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .brassicales import BRASSICALES
from .malvales import MALVALES
from .myrtales import MYRTALES
from .sapindales import SAPINDALES

P_PELTATUM = Species(
    name='Pelargonium peltatum',
    local_names={EN: 'ivy-leaved pelargonium, cascading geranium', PL: 'pelargonia bluszczolistna'},
)

PELARGONIUM = Genus(name='Pelargonium', children=[P_PELTATUM])

GERANIACEAE = Family(name='Geraniaceae', children=[PELARGONIUM])

GERANIALES = Order(name='Gerniales', children=[GERANIACEAE])

GERANIALES_MYRTALES = Clade(children=[GERANIALES, MYRTALES])
MALVALES_BRASSICALES = Clade(children=[MALVALES, BRASSICALES])
MALVIDS_A = Clade(children=[SAPINDALES, MALVALES_BRASSICALES])
MALVIDS = Clade(name='Malvids', children=[GERANIALES_MYRTALES, MALVIDS_A])
