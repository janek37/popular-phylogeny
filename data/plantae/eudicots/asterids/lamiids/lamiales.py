from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .lamiaceae import LAMIACEAE
from .oleaceae import OLEACEAE

A_MAJUS = Species(
    name="Antirrhinum majus",
    local_names={EN: "common snapdragon", PL: "lwia paszcza, wyżlin większy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Yellow-Snapdragon-Flower(Antirrhinum_majus)_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Yellow-Snapdragon-Flower%28Antirrhinum_majus%29_02.jpg",
        author="Sabina Bajracharya",
        license=License.CC_BY_SA_4_0,
    ),
)
S_INDICUM = Species(
    name="Sesamum indicum",
    local_names={EN: "sesame", PL: "sezam indyjski"},
    known_for=[
        {
            EN: "edible seeds",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Sesame_seeds.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Sesame_seeds.JPG",
                author="Jitender Kumar",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sesamum_indicum_13.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Sesamum_indicum_13.JPG",
        author="Vinayaraj",
        license=License.CC_BY_SA_3_0,
    ),
)
P_MAJOR = Species(
    name="Plantago major",
    local_names={EN: "broadleaf plantain", PL: "babka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Plantago_major_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Plantago_major_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
V_THAPSUS = Species(
    name="Verbascum thapsus",
    local_names={EN: "common mullein", PL: "dziewanna drobnokwiatowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Verbascum_thapsus_Dziewanna_drobnokwiatowa_2015_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c8/Verbascum_thapsus_Dziewanna_drobnokwiatowa_2015_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
VERBENA_OFFICINALIS = Species(
    name="Verbena officinalis",
    local_names={EN: "common vervain", PL: "werbena pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Verbena_officinalis_2_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Verbena_officinalis_2_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
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
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aloysia_citriodora_002.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Aloysia_citriodora_002.jpg",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
VERONICA_OFFICINALIS = Species(
    name="Veronica officinalis",
    local_names={
        EN: "heath speedwell, common gypsyweed, common speedwell, Paul's betony",
        PL: "przetacznik lekarski, przetacznik leśny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Veronica_officinalis_kz02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/47/Veronica_officinalis_kz02.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
D_PURPUREA = Species(
    name="Digitalis purpurea",
    local_names={EN: "common foxglove", PL: "naparstnica purpurowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Digitalis_purpurea_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/43/Digitalis_purpurea_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
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
