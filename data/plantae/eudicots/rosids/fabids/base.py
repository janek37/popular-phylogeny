from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

from .cucurbitales import CUCURBITALES
from .fabales import FABALES
from .fagales import FAGALES
from .malpighiales import MALPIGHIALES
from .rosales import ROSALES

O_ACETOSELLA = Species(
    name="Oxalis acetosella",
    local_names={EN: "wood sorrel", PL: "szczawik zajęczy"},
    known_for=[{EN: "edible leaves tasting similar to unrelated common sorrel"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oxalis_acetosella-1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Oxalis_acetosella-1.jpg",
        author="Hanna Zelenko",
        license=License.CC_BY_SA_3_0,
    ),
)

OXALIS = Genus(name="Oxalis", children=[O_ACETOSELLA])

OXALIDACEAE = Family(name="Oxalidaceae", children=[OXALIS])

OXALIDALES = Order(name="Oxalidales", children=[OXALIDACEAE])

FAGALES_CUCURBITALES = Clade(children=[FAGALES, CUCURBITALES])
NFC_A = Clade(children=[ROSALES, FAGALES_CUCURBITALES])

COM_CLADE = Clade(name="COM clade", children=[MALPIGHIALES, OXALIDALES])
NITROGEN_FIXING_CLADE = Clade(name="nitrogen‑fixing clade", children=[FABALES, NFC_A])

FABIDS = Clade(name="fabids", children=[COM_CLADE, NITROGEN_FIXING_CLADE])
