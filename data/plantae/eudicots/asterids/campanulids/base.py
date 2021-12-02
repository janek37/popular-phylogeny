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
S_NIGRA = Species(
    name="Sambucus nigra",
    local_names={EN: "black elder, European elderberry", PL: "bez czarny"},
)
V_OPULUS = Species(
    name="Viburnum opulus", local_names={EN: "guelder-rose", PL: "kalina koralowa"}
)
V_OFFICINALIS = Species(
    name="Valeriana officinalis",
    local_names={EN: "valerian", PL: "kozłek lekarski"},
    known_for=[{PL: "krople walerianowe"}],
)

ILEX = Genus(name="Ilex", children=[I_AQUIFOLIUM, I_PARAGUARIENSIS])
SAMBUCUS = Genus(name="Sambucus", children=[S_NIGRA])
VIBURNUM = Genus(name="Viburnum", children=[V_OPULUS])
VALERIANA = Genus(name="Valeriana", children=[V_OFFICINALIS])

AQUIFOLIACEAE = Family(name="Aquifoliaceae", children=[ILEX])
ADOXACEAE = Family(name="Adoxaceae", children=[SAMBUCUS, VIBURNUM])
CAPRIFOLIACEAE = Family(name="Caprifoliaceae", children=[VALERIANA])

AQUIFOLIALES = Order(name="Aquifoliales", children=[AQUIFOLIACEAE])
DIPSACALES = Order(name="Dipsacales", children=[ADOXACEAE, CAPRIFOLIACEAE])

CAMPANULIDS_B = Clade(children=[APIALES, DIPSACALES])
CAMPANULIDS_A = Clade(children=[ASTERALES, CAMPANULIDS_B])
CAMPANULIDS = Clade(name="campanulids", children=[AQUIFOLIALES, ASTERALES])
