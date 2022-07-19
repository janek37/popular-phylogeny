from clade import Clade, Family, Genus, Order, Species
from constants import EN, IMAGE, PL
from image import Image, License

from .fabids import FABIDS
from .malvids import MALVIDS

V_VINIFERA = Species(
    name="Vitis vinifera",
    local_names={EN: "common grape vine", PL: "winorośl właściwa"},
    known_for=[
        {
            EN: "grapes",
            PL: "winogrona",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Green_grapes_in_turquoise_bowl.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Green_grapes_in_turquoise_bowl.jpg",
                author="DomenikaBo",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "wine",
            PL: "wino",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Red_Wine_Glass.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/c0/Red_Wine_Glass.jpg",
                author="André Karwath aka Aka",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "raisins",
            PL: "rodzynki",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pasas.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Pasas.JPG",
                author="Jorge Barrios",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vitis_vinifera_20120823.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Vitis_vinifera_20120823.jpg",
        author="Luis Fernández García",
        license=License.CC_BY_SA_3_0,
    ),
)

VITIS = Genus(name="Vitis", children=[V_VINIFERA])

VITACEAE = Family(name="Vitaceae", children=[VITIS])

VITALES = Order(name="Vitales", children=[VITACEAE])

EUROSIDS = Clade(name="eurosids", children=[FABIDS, MALVIDS])

ROSIDS = Clade(name="rosids", children=[VITALES, EUROSIDS])
