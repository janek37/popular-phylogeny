from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL
from image import Image, License

from .anabantiformes import ANABANTIFORMES
from .carangaria import CARANGARIA
from .eupercaria import EUPERCARIA
from .ovalentaria import OVALENTARIA

S_SCOMBRUS = Species(
    name="Scomber scombrus",
    local_names={EN: "Atlantic mackarel", PL: "makrela atlantycka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Scomber_scombrus_(Pieni).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e5/Scomber_scombrus_%28Pieni%29.jpg",
        author='encyclopedia, "Pieni Tietosanakirja"',
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_THYNNUS = Species(
    name="Thunnus thynnus",
    local_names={EN: "Atlantic bluefin tuna", PL: "tuńczyk pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bluefin-big.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Bluefin-big.jpg",
        author="Unknown author",
        license=License.NOAA,
    ),
)
T_ALBACARES = Species(
    name="Thunnus albacares",
    local_names={EN: "yellowfin tuna", PL: "tuńczyk żółtopłetwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Thunnus_albacares.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Thunnus_albacares.png",
        author="Unknown author",
        license=License.NOAA,
    ),
)
K_PELAMIS = Species(
    name="Katsuwonus pelamis",
    local_names={EN: "skipjack tuna", PL: "tuńczyk pasiasty, bonito"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Naturalis_Biodiversity_Center_-_RMNH.ART.563_-_Katsuwonus_pelamis_(Linnaeus)"
        "_-_Kawahara_Keiga_-_1823_-_1829_-_Siebold_Collection_-_pencil_drawing_-_water_colour.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Naturalis_Biodiversity_Center_-_RMNH.ART.563_-_Katsuwonus_pelamis_%28Linnaeus%29"
        "_-_Kawahara_Keiga_-_1823_-_1829_-_Siebold_Collection_-_pencil_drawing_-_water_colour.jpeg",
        author="(Linnaeus)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
H_HIPPOCAMPUS = Species(
    name="Hippocampus hippocampus",
    local_names={
        EN: "short-snouted seahorse",
        PL: "konik morski, pławikonik europejski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hippocampus_hippocampus_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Hippocampus_hippocampus_Gervais.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_BARBARUS = Species(
    name="Periophthalmus barbarus",
    local_names={EN: "Atlantic mudskipper", PL: "mułoskoczek, poskoczek mułowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Periophtalmus_barbarus_03082014_Aquarium_Canet_en_Roussillon.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Periophtalmus_barbarus_03082014_Aquarium_Canet_en_Roussillon.jpg",
        author="Vassil",
        license=License.CC0,
    ),
)
N_MELANOSTOMUS = Species(
    name="Neogobius melanostomus",
    local_names={EN: "round goby", PL: "babka śniadogłowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Round_goby_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Round_goby_01.jpg",
        author="United States Fish and Wildlife Service",
        license=License.FWS,
    ),
)

SCOMBER = Genus(name="Scomber", children=[S_SCOMBRUS])
THUNNUS = Genus(name="Thunnus", children=[T_THYNNUS, T_ALBACARES])
KATSUWONUS = Genus(name="Katsuwonus", children=[K_PELAMIS])
HIPPOCAMPUS = Genus(name="Hippocampus", children=[H_HIPPOCAMPUS])
PERIOPHTHALMUS = Genus(name="Periophthalmus", children=[P_BARBARUS])
NEOGOBIUS = Genus(name="Neogobius", children=[N_MELANOSTOMUS])

THUNNINI = Tribe(name="Thunnini", children=[THUNNUS, KATSUWONUS])

SCOMBRIDAE = Family(name="Scombridae", children=[SCOMBER, THUNNINI])
SYNGNATHIDAE = Family(name="Syngnathidae", children=[HIPPOCAMPUS])
OXUDERCIDAE = Family(name="Oxudercidae", children=[PERIOPHTHALMUS])
GOBIIDAE = Family(name="Gobiidae", children=[NEOGOBIUS])

SCOMBRIFORMES = Order(name="Scombriformes", children=[SCOMBRIDAE])
SYNGNATHIFORMES = Order(name="Syngnathiformes", children=[SYNGNATHIDAE])
GOBIIFORMES = Order(name="Gobiiformes", children=[OXUDERCIDAE, GOBIIDAE])

PERCOMORPHA_A = Clade(children=[SCOMBRIFORMES, SYNGNATHIFORMES])
PERCOMORPHA_B = Clade(children=[ANABANTIFORMES, CARANGARIA])
PERCOMORPHA_C = Clade(children=[PERCOMORPHA_B, OVALENTARIA])
PERCOMORPHA_D = Clade(children=[PERCOMORPHA_C, EUPERCARIA])
PERCOMORPHA_E = Clade(children=[GOBIIFORMES, PERCOMORPHA_D])
PERCOMORPHA = Clade(name="Percomorpha", children=[PERCOMORPHA_A, PERCOMORPHA_E])
