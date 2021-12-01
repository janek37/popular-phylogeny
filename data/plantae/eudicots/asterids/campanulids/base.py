from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .apiales import APIALES
from .asterales import ASTERALES

I_AQUIFOLIUM = Species(
    name="Ilex aquifolium", local_names={EN: "common holly", PL: "ostrokrzew kolczasty"}
)
I_PARAGUARIENSIS = Species(
    name="Ilex paraguariensis",
    local_names={EN: "yerba mate", PL: "ostrokrzew paragwajski"},
)

ILEX = Genus(name="Ilex", children=[I_AQUIFOLIUM, I_PARAGUARIENSIS])

AQUIFOLIACEAE = Family(name="Aquifoliaceae", children=[ILEX])

AQUIFOLIALES = Order(name="Aquifoliales", children=[AQUIFOLIACEAE])

CAMPANULIDS_A = Clade(children=[ASTERALES, APIALES])
CAMPANULIDS = Clade(name="campanulids", children=[AQUIFOLIALES, ASTERALES])
