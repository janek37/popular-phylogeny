from clade import Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

B_SPLENDENS = Species(
    name="Betta splendens",
    local_names={EN: "betta, Siamese fighting fish", PL: "bojownik wspaniały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:HM_Orange_M_Sarawut.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/10/HM_Orange_M_Sarawut.jpg",
        author="Daniella Vereeken",
        license=License.CC_BY_2_0,
    ),
)
O_GORAMY = Species(
    name="Osphronemus goramy",
    local_names={EN: "giant gouramy", PL: "gurami olbrzymi"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Osphronemus_goramy_2008_G1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Osphronemus_goramy_2008_G1.jpg",
        author="George Chernilevsky",
        license=License.PUBLIC_DOMAIN,
    ),
)
H_TEMMINCKII = Species(
    name="Helostoma temminckii",
    local_names={EN: "kisser, kissing gouramy", PL: "całusek, gurami całujący"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Helostoma_temminckii_in_aquarium.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Helostoma_temminckii_in_aquarium.jpg",
        author="Green Yoshi",
        license=License.CC_BY_SA_3_0,
    ),
)

BETTA = Genus(name="Betta", children=[B_SPLENDENS])
OSPHRONEMUS = Genus(name="Osphronemus", children=[O_GORAMY])
HELOSTOMA = Genus(name="Helostoma", children=[H_TEMMINCKII])

OSPHRONEMIDAE = Family(name="Osphronemidae", children=[BETTA, OSPHRONEMUS])
HELOSTOMATIDAE = Family(name="Helostomatidae", children=[HELOSTOMA])

ANABANTIFORMES = Order(name="Anabantiformes", children=[OSPHRONEMIDAE, HELOSTOMATIDAE])
