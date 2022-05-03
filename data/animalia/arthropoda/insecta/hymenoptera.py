from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, PL
from image import Image, License

V_VULGARIS = Species(
    name="Vespula vulgaris",
    local_names={EN: "common wasp, common yellow-jacket", PL: "osa pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vespula_vulgaris5.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Vespula_vulgaris5.jpg",
        author="Holger Gröschl",
        license=License.CC_BY_SA_2_0_DE,
    ),
)
V_CRABRO = Species(
    name="Vespa crabro",
    local_names={EN: "European hornet", PL: "szerszeń europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hornet-vespa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fd/Hornet-vespa.jpg",
        author="PiccoloNamek",
        license=License.CC_BY_SA_3_0,
    ),
)
S_INVICTA = Species(
    name="Solenopsis invicta",
    local_names={EN: "red imported fire ant", PL: "mrówka ognista"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:S._invicta_worker_foraging.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c9/S._invicta_worker_foraging.jpg",
        author="Russ Ottens",
        license=License.CC_BY_3_0_US,
    ),
)
L_NIGER = Species(
    name="Lasius niger",
    local_names={EN: "black garden ant, common black ant", PL: "hurtnica pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lasius_niger_03.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Lasius_niger_03.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
M_RUBRA = Species(
    name="Myrmica rubra",
    local_names={
        EN: "European fire ant, common red ant",
        PL: "czerwona mrówka, wścieklica zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myrmica_rubra_02.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Myrmica_rubra_02.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
M_PHARAONIS = Species(
    name="Monomorium pharaonis",
    local_names={EN: "pharaoh ant", PL: "mrówka faraona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:M.pharaonis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/M.pharaonis.jpg",
        author="Землеройкин",
        license=License.CC_BY_SA_4_0,
    ),
)
A_MELLIFERA = Species(
    name="Apis mellifera",
    local_names={EN: "western honey bee, European honey bee", PL: "pszczoła miodna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apis_mellifera_-_Brassica_napus_-_Valingu.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Apis_mellifera_-_Brassica_napus_-_Valingu.jpg",
        author="Ivar Leidus",
        license=License.CC_BY_SA_4_0,
    ),
)
B_TERRESTRIS = Species(
    name="Bombus terrestris",
    local_names={
        EN: "buff-tailed bumblebee, large earth bumblebee",
        PL: "trzmiel ziemny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:2010-04-28_(35)_Erdhummel,_Buff-tailed_bumblebee,_Bombus_terrestris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/2010-04-28_%2835%29_Erdhummel%2C_Buff-tailed_bumblebee%2C_Bombus_terrestris.jpg",
        author="Vera Buhl",
        license=License.CC_BY_SA_3_0,
    ),
)

VESPULA = Genus(name="Vespula", children=[V_VULGARIS])
VESPA = Genus(name="Vespa", children=[V_CRABRO])
SOLENOPSIS = Genus(name="Solenopsis", children=[S_INVICTA])
LASIUS = Genus(name="Lasius", children=[L_NIGER])
MYRMICA = Genus(name="Myrmica", children=[M_RUBRA])
MONOMORIUM = Genus(name="Monomorium", children=[M_PHARAONIS])
APIS = Genus(name="Apis", children=[A_MELLIFERA])
BOMBUS = Genus(name="Bombus", children=[B_TERRESTRIS])

SOLENOPSIDINI = Tribe(name="Solenopsidini", children=[SOLENOPSIS, MONOMORIUM])
MYRMICINI = Tribe(name="Myrmicini", children=[MYRMICA])

MYRMICINAE = Subfamily(name="Myrmicinae", children=[SOLENOPSIDINI, MYRMICINI])
FORMICINAE = Subfamily(name="Formicinae", children=[LASIUS])

VESPIDAE = Family(name="Vespidae", children=[VESPULA, VESPA])
FORMICIDAE = Family(name="Formicidae", children=[MYRMICINAE, FORMICINAE])
APIDAE = Family(name="Apidae", children=[APIS, BOMBUS])

# Tree based on https://en.wikipedia.org/wiki/Apocrita
HYMENOPTERA_A = Clade(children=[FORMICIDAE, APIDAE])

HYMENOPTERA = Order(name="Hymenoptera", children=[VESPIDAE, HYMENOPTERA_A])
