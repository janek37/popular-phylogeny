from clade import Family, Genus, Order, Species, Tribe
from constants import EN, PL

from .lamiaceae import LAMIACEAE
from .oleaceae import OLEACEAE

A_MAJUS = Species(
    name="Antirrhinum majus",
    local_names={EN: "common snapdragon", PL: "lwia paszcza, wyżlin większy"},
)
S_INDICUM = Species(
    name="Sesamum indicum", local_names={EN: "sesame", PL: "sezam indyjski"}
)
P_MAJOR = Species(
    name="Plantago major", local_names={EN: "broadleaf plantain", PL: "babka zwyczajna"}
)
V_THAPSUS = Species(
    name="Verbascum thapsus",
    local_names={EN: "common mullein", PL: "dziewanna drobnokwiatowa"},
)
V_OFFICINALIS = Species(
    name="Verbena officinalis",
    local_names={EN: "common vervain", PL: "werbena pospolita"},
)

ANTIRRHINUM = Genus(name="Antirrhinum", children=[A_MAJUS])
SESAMUM = Genus(name="Sesamum", children=[S_INDICUM])
PLANTAGO = Genus(name="Plantago", children=[P_MAJOR])
VERBASCUM = Genus(name="Verbascum", children=[V_THAPSUS])
VERBENA = Genus(name="Verbena", children=[V_OFFICINALIS])

ANTIRRHINEAE = Tribe(name="Antirrhineae", children=[ANTIRRHINUM])
PLANTAGINEAE = Tribe(name="Plantagineae", children=[PLANTAGO])

PLANTAGINACEAE = Family(name="Plantaginaceae", children=[ANTIRRHINEAE, PLANTAGINEAE])
PEDALIACEAE = Family(name="Pedaliaceae", children=[SESAMUM])
SCROPHULARIACEAE = Family(name="Scrophulariaceae", children=[VERBASCUM])
VERBENACEAE = Family(name="Verbenaceae", children=[VERBENA])

LAMIALES = Order(
    name="Lamiales",
    children=[
        LAMIACEAE,
        OLEACEAE,
        PLANTAGINACEAE,
        PEDALIACEAE,
        SCROPHULARIACEAE,
        VERBENACEAE,
    ],
)
