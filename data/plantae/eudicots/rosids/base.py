from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .fabids import FABIDS

V_VINIFERA = Species(
    name='Vitis vinifera',
    local_names={EN: 'common grape vine', PL: 'winorośl właściwa'},
    known_for=[{EN: 'grapes', PL: 'winogrona'}, {EN: 'wine', PL: 'wino'}, {EN: 'raisins', PL: 'rodzynki'}],
)

VITIS = Genus(name='Vitis', children=[V_VINIFERA])

VITACEAE = Family(name='Vitaceae', children=[VITIS])

VITALES = Order(name='Vitales', children=[VITACEAE])

EUROSIDS = Clade(name='eurosids', children=[FABIDS])

ROSIDS = Clade(name='rosids', children=[VITALES, EUROSIDS])
