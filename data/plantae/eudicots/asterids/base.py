from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .ericales import ERICALES

H_MACROPHYLLA = Species(
    name="Hydrangea macrophylla",
    local_names={EN: "bigleaf hydrangea, hortensia", PL: "hortensja ogrodowa"},
)

HYDRANGEA = Genus(name="Hydrangea", children=[H_MACROPHYLLA])

HYDRANGEACEAE = Family(name="Hydrangeaceae", children=[HYDRANGEA])

CORNALES = Order(name="Cornales", children=[HYDRANGEACEAE])

ASTERIDS = Clade(name="Asterids", children=[CORNALES, ERICALES])
