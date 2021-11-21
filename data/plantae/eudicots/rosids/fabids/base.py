from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .fabales import FABALES
from .fagales import FAGALES
from .malpighiales import MALPIGHIALES
from .rosales import ROSALES

O_ACETOSELLA = Species(
    name='Oxalis acetosella',
    local_names={EN: 'wood sorrel', PL: 'szczawik zajęczy'},
    known_for={EN: 'edible leaves tasting similar to unrelated common sorrel'},
)

OXALIS = Genus(name='Oxalis', children=[O_ACETOSELLA])

OXALIDACEAE = Family(name='Oxalidaceae', children=[OXALIS])

OXALIDALES = Order(name='Oxalidales', children=[OXALIDACEAE])

NFC_A = Clade(children=[ROSALES, FAGALES])

COM_CLADE = Clade(name='COM clade', children=[MALPIGHIALES, OXALIDALES])
NITROGEN_FIXING_CLADE = Clade(name='nitrogen‑fixing clade', children=[FABALES, NFC_A])

FABIDS = Clade(name='fabids', children=[COM_CLADE, NITROGEN_FIXING_CLADE])
