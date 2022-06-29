from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

from .campanulids import CAMPANULIDS
from .ericales import ERICALES
from .lamiids import LAMIIDS

H_MACROPHYLLA = Species(
    name="Hydrangea macrophylla",
    local_names={EN: "bigleaf hydrangea, hortensia", PL: "hortensja ogrodowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hydrangea_macrophylla_%27Verena%27_2019-07-20_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Hydrangea_macrophylla_%27Verena%27_2019-07-20_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)

HYDRANGEA = Genus(name="Hydrangea", children=[H_MACROPHYLLA])

HYDRANGEACEAE = Family(name="Hydrangeaceae", children=[HYDRANGEA])

CORNALES = Order(name="Cornales", children=[HYDRANGEACEAE])

EUASTERIDS = Clade(children=[CAMPANULIDS, LAMIIDS])

ASTERIDS_A = Clade(children=[ERICALES, EUASTERIDS])
ASTERIDS = Clade(name="Asterids", children=[CORNALES, ASTERIDS_A])
