from clade import Clade, Family, Genus, Order, Species, Tribe
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
VERBENA_OFFICINALIS = Species(
    name="Verbena officinalis",
    local_names={EN: "common vervain", PL: "werbena pospolita"},
)
A_CITRODORA = Species(
    name="Aloysia citrodora",
    local_names={
        EN: "lemon verbena",
        PL: (
            "werbena cytrynowa, miłowonka trójlistna, "
            "cukrownica trójlistna, lippia trójlistna"
        ),
    },
)
VERONICA_OFFICINALIS = Species(
    name="Veronica officinalis",
    local_names={
        EN: "heath speedwell, common gypsyweed, common speedwell, Paul's betony",
        PL: "przetacznik lekarski, przetacznik leśny",
    },
)
D_PURPUREA = Species(
    name="Digitalis purpurea",
    local_names={EN: "common foxglove", PL: "naparstnica purpurowa"},
)

ANTIRRHINUM = Genus(name="Antirrhinum", children=[A_MAJUS])
SESAMUM = Genus(name="Sesamum", children=[S_INDICUM])
PLANTAGO = Genus(name="Plantago", children=[P_MAJOR])
VERBASCUM = Genus(name="Verbascum", children=[V_THAPSUS])
VERBENA = Genus(name="Verbena", children=[VERBENA_OFFICINALIS])
ALOYSIA = Genus(name="Aloysia", children=[A_CITRODORA])
VERONICA = Genus(name="Veronica", children=[VERONICA_OFFICINALIS])
DIGITALIS = Genus(name="Digitalis", children=[D_PURPUREA])

ANTIRRHINEAE = Tribe(name="Antirrhineae", children=[ANTIRRHINUM])
PLANTAGINEAE = Tribe(name="Plantagineae", children=[PLANTAGO])
VERONICEAE = Tribe(name="Veroniceae", children=[VERONICA])
DIGITALIDEAE = Tribe(name="Digitalideae", children=[DIGITALIS])

# https://plantphylogeny.landcareresearch.co.nz/webforms/viewtree.aspx?ObjectID=e76e59b6-29e9-4544-b38f-fc811f8f43a6
PLANTAGINACEAE_A = Clade(children=[PLANTAGINEAE, VERONICEAE])
PLANTAGINACEAE_B = Clade(children=[DIGITALIDEAE, PLANTAGINACEAE_A])

PLANTAGINACEAE = Family(
    name="Plantaginaceae", children=[ANTIRRHINEAE, PLANTAGINACEAE_B]
)
PEDALIACEAE = Family(name="Pedaliaceae", children=[SESAMUM])
SCROPHULARIACEAE = Family(name="Scrophulariaceae", children=[VERBASCUM])
VERBENACEAE = Family(name="Verbenaceae", children=[VERBENA, ALOYSIA])

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
