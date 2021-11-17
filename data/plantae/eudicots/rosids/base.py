from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .fabales import FABALES
from .malpighiales import MALPIGHIALES
from .rosales import ROSALES

V_VINIFERA = Species(
    name='Vitis vinifera',
    local_names={EN: 'common grape vine', PL: 'winorośl właściwa'},
    known_for=[{EN: 'grapes', PL: 'winogrona'}, {EN: 'wine', PL: 'wino'}, {EN: 'raisins', PL: 'rodzynki'}],
)
O_ACETOSELLA = Species(
    name='Oxalis acetosella',
    local_names={EN: 'wood sorrel', PL: 'szczawik zajęczy'},
    known_for={EN: 'edible leaves tasting similar to unrelated common sorrel'},
)

VITIS = Genus(name='Vitis', children=[V_VINIFERA])
OXALIS = Genus(name='Oxalis', children=[O_ACETOSELLA])

VITACEAE = Family(name='Vitaceae', children=[VITIS])
OXALIDACEAE = Family(name='Oxalidaceae', children=[OXALIS])

VITALES = Order(name='Vitales', children=[VITACEAE])
OXALIDALES = Order(name='Oxalidales', children=[OXALIDACEAE])

COM_CLADE = Clade(name='COM clade', children=[MALPIGHIALES, OXALIDALES])
NITROGEN_FIXING_CLADE = Clade(name='nitrogen‑fixing clade', children=[FABALES, ROSALES])

FABIDS = Clade(name='fabids', children=[COM_CLADE, NITROGEN_FIXING_CLADE])

EUROSIDS = Clade(name='eurosids', children=[FABIDS])

ROSIDS = Clade(name='rosids', children=[VITALES, EUROSIDS])
