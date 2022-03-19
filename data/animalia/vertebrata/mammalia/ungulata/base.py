from clade import Clade, Order

from .perissodactyla import PERISSODACTYLA
from .suina import SUINA
from .tylopoda import TYLOPODA

ARTIOFABULA = Clade(name="Artiofabula", children=[SUINA])

ARTIODACTYLA = Order(name="Artiodactyla", children=[TYLOPODA, ARTIOFABULA])

UNGULATA = Clade(name="Ungulata", children=[PERISSODACTYLA, ARTIODACTYLA])
