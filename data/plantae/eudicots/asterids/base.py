from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .campanulids import CAMPANULIDS
from .ericales import ERICALES
from .lamiids import LAMIIDS

H_MACROPHYLLA = Species(
    name="Hydrangea macrophylla",
    local_names={EN: "bigleaf hydrangea, hortensia", PL: "hortensja ogrodowa"},
)

HYDRANGEA = Genus(name="Hydrangea", children=[H_MACROPHYLLA])

HYDRANGEACEAE = Family(name="Hydrangeaceae", children=[HYDRANGEA])

CORNALES = Order(name="Cornales", children=[HYDRANGEACEAE])

EUASTERIDS = Clade(children=[CAMPANULIDS, LAMIIDS])

ASTERIDS_A = Clade(children=[ERICALES, EUASTERIDS])
ASTERIDS = Clade(name="Asterids", children=[CORNALES, ASTERIDS_A])
