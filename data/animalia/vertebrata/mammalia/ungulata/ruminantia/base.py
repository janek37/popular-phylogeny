from clade import Clade, Family, Genus, Infraorder, Species, Suborder, Superfamily
from constants import EN, PL
from image import Image, License

from .aegodontia import AEGODONTIA
from .bovinae import BOVINAE
from .cervidae import CERVIDAE

T_JAVANICUS = Species(
    name="Tragulus javanicus",
    local_names={EN: "Java mouse-deer", PL: "kanczyl jawajski"},
    known_for=[{EN: "the smallest living hoofed mammal"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:ZooParc_de_Beauval_Cerf-souris_Chevrotain_malais_Tragulus_javanicus_08082019_06_9204.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/ZooParc_de_Beauval_Cerf-souris_Chevrotain_malais_Tragulus_javanicus_08082019_06_9204.jpg",
        author="Vassil",
        license=License.CC0,
    ),
)
O_JOHNSTONI = Species(
    name="Okapia johnstoni",
    local_names={EN: "okapi", PL: "okapi leśne"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Saint-Aignan_(Loir-et-Cher)._Okapi.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Saint-Aignan_%28Loir-et-Cher%29._Okapi.jpg",
        author="Daniel Jolivet",
        license=License.CC_BY_2_0,
    ),
)
G_CAMELOPARDALIS = Species(
    name="Giraffa camelopardalis",
    local_names={EN: "giraffe", PL: "żyrafa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Giraffa_camelopardalis_angolensis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e0/Giraffa_camelopardalis_angolensis.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
A_AMERICANA = Species(
    name="Antilocapra americana",
    local_names={EN: "pronghorn, American antelope", PL: "widłoróg amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pronghorn_on_Seedskadee_National_Wildlife_Refuge_(34596950833)_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Pronghorn_on_Seedskadee_National_Wildlife_Refuge_%2834596950833%29_%28cropped%29.jpg",
        author="USFWS Mountain-Prairie",
        license=License.CC_BY_2_0,
    ),
)

TRAGULUS = Genus(
    name="Tragulus",
    children=[T_JAVANICUS],
    local_names={EN: "mouse-deer", PL: "myszojeleń, kanczyl"},
)
OKAPIA = Genus(name="Okapia", children=[O_JOHNSTONI])
GIRAFFA = Genus(name="Giraffa", children=[G_CAMELOPARDALIS])
ANTILOCAPRA = Genus(name="Antilocapra", children=[A_AMERICANA])

TRAGULIDAE = Family(name="Tragulidae", children=[TRAGULUS])
GIRAFFIDAE = Family(name="Giraffidae", children=[OKAPIA, GIRAFFA])
ANTILOCAPRIDAE = Family(name="Antilocapridae", children=[ANTILOCAPRA])
BOVIDAE = Family(name="Bovidae", children=[BOVINAE, AEGODONTIA])

GIRAFFOIDEA = Superfamily(name="Giraffoidea", children=[GIRAFFIDAE, ANTILOCAPRIDAE])

PECORA_A = Clade(children=[CERVIDAE, BOVIDAE])

PECORA = Infraorder(name="Pecora", children=[GIRAFFOIDEA, PECORA_A])

RUMINANTIA = Suborder(name="Ruminantia", children=[TRAGULIDAE, PECORA])
