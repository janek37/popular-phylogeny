from clade import Clade, Order

from .perissodactyla import PERISSODACTYLA
from .ruminantia import RUMINANTIA
from .suina import SUINA
from .tylopoda import TYLOPODA
from .whippomorpha import WHIPPOMORPHA

CETRUMINANTIA = Clade(name="Cetruminantia", children=[WHIPPOMORPHA, RUMINANTIA])

ARTIOFABULA = Clade(name="Artiofabula", children=[SUINA, CETRUMINANTIA])

ARTIODACTYLA = Order(name="Artiodactyla", children=[TYLOPODA, ARTIOFABULA])

UNGULATA = Clade(name="Ungulata", children=[PERISSODACTYLA, ARTIODACTYLA])
