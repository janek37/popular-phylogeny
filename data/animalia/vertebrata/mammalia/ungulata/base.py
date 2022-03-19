from clade import Clade, Order

from .perissodactyla import PERISSODACTYLA
from .tylopoda import TYLOPODA

ARTIODACTYLA = Order(name="Artiodactyla", children=[TYLOPODA])

UNGULATA = Clade(name="Ungulata", children=[PERISSODACTYLA, ARTIODACTYLA])
