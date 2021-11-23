from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .sapindales import SAPINDALES

P_PELTATUM = Species(
    name='Pelargonium peltatum',
    local_names={EN: 'ivy-leaved pelargonium, cascading geranium', PL: 'pelargonia bluszczolistna'},
)

PELARGONIUM = Genus(name='Pelargonium', children=[P_PELTATUM])

GERANIACEAE = Family(name='Geraniaceae', children=[PELARGONIUM])

GERANIALES = Order(name='Gerniales', children=[GERANIACEAE])

MALVIDS = Clade(name='Malvids', children=[GERANIALES, SAPINDALES])
