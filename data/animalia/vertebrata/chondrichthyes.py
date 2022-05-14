from clade import Clade, Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL
from image import Image, License

from .selachimorpha import SELACHIMORPHA

C_MONSTROSA = Species(
    name="Chimaera monstrosa",
    local_names={EN: "rabbit fish, rat fish", PL: "chimera pospolita, przeraza"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chimaera_monstrosa1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1a/Chimaera_monstrosa1.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN,
    ),
)
D_BATIS = Species(
    name="Dipturus batis",
    local_names={EN: "common skate, blue skate", PL: "raja gładka, płaszczka naga"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dipturus_batis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Dipturus_batis.jpg",
        author="Unknown",
        license=License.PUBLIC_DOMAIN,
    ),
)
B_BREVICAUDATA = Species(
    name="Bathytoshia brevicaudata",
    local_names={EN: "short-tail stingray, smooth stingray"},
    known_for=[
        {EN: "death of Steve Irwin"},
        {EN: "the largest stingray in the world", PL: "największa ogończa świata"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dasyatidae_Bathytoshia_brevicaudata_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/25/Dasyatidae_Bathytoshia_brevicaudata_1.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
P_PRISTIS = Species(
    name="Pristis pristis",
    local_names={
        EN: "common sawfish, largetooth sawfish",
        PL: "ryba piła, piła zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pristis_pristis_townsville.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e2/Pristis_pristis_townsville.jpg",
        author="Simon Fraser University - University Communications & Marketing",
        license=License.CC_BY_2_0,
    ),
)
M_BIROSTRIS = Species(
    name="Mobula birostris",
    local_names={EN: "giant oceanic manta ray", PL: "manta, diabeł morski"},
    known_for=[{EN: "the largest ray", PL: "największa płaszczka"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Manta_birostris-Thailand4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/df/Manta_birostris-Thailand4.jpg",
        author="jon hanson from london, UK",
        license=License.CC_BY_SA_2_0,
    ),
)

CHIMAERA = Genus(name="Chimaera", children=[C_MONSTROSA])
DIPTURUS = Genus(name="Dipturus", children=[D_BATIS])
BATHYTOSHIA = Genus(name="Bathytoshia", children=[B_BREVICAUDATA])
PRISTIS = Genus(name="Pristis", children=[P_PRISTIS])
MOBULA = Genus(name="Mobula", children=[M_BIROSTRIS])

CHIMAERIDAE = Family(name="Chimaeridae", children=[CHIMAERA])
RAJIDAE = Family(name="Rajidae", children=[DIPTURUS])
DASYATIDAE = Family(name="Dasyatidae", children=[BATHYTOSHIA])
PRISTIDAE = Family(name="Pristidae", children=[PRISTIS])
MOBULIDAE = Family(name="Mobulidae", children=[MOBULA])

CHIMAERIFORMES = Order(name="Chimaeriformes", children=[CHIMAERIDAE])
RAJIFORMES = Order(name="Rajiformes", children=[RAJIDAE])
MYLIOBATIFORMES = Order(name="Myliobatiformes", children=[DASYATIDAE, MOBULIDAE])
RHINOPRISTIFORMES = Order(name="Rhinopristiformes", children=[PRISTIDAE])

BATOIDEA_A = Clade(children=[RAJIFORMES, MYLIOBATIFORMES])
BATOIDEA = Superorder(name="Batoidea", children=[BATOIDEA_A, RHINOPRISTIFORMES])

ELASMOBRANCHII = Subclass(name="Elasmobranchii", children=[SELACHIMORPHA, BATOIDEA])

CHONDRICHTHYES = Class(name="Chondrichthyes", children=[CHIMAERIFORMES, ELASMOBRANCHII])
