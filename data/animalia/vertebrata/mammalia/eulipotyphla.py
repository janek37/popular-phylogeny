from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

T_EUROPAEA = Species(
    name="Talpa europaea",
    local_names={EN: "European mole, common mole", PL: "kret europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Talpa_europaea_(Freising,_Deutschland)_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Talpa_europaea_%28Freising%2C_Deutschland%29_4.jpg",
        author="Christoph Moning",
        license=License.CC_BY_4_0,
    ),
)
E_EUROPAEUS = Species(
    name="Erinaceus europaeus",
    local_names={EN: "European hedgehog, common hedgehog"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Erinaceus_europaeus_(Linnaeus,_1758).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Erinaceus_europaeus_%28Linnaeus%2C_1758%29.jpg",
        author="Michael Gäbler",
        license=License.CC_BY_SA_3_0,
    ),
)
S_ARANEUS = Species(
    name="Sorex araneus",
    local_names={EN: "common shrew, Eurasian shrew", PL: "ryjówka aksamitna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:SorexAraneus_wwalas_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/SorexAraneus_wwalas_01.JPG",
        author="WWalas",
        license=License.CC_BY_SA_3_0,
    ),
)

TALPA = Genus(name="Talpa", children=[T_EUROPAEA])
ERINACEUS = Genus(name="Erinaceus", children=[E_EUROPAEUS])
SOREX = Genus(name="Sorex", children=[S_ARANEUS])

TALPIDAE = Family(name="Talpidae", children=[TALPA])
ERINACEIDAE = Family(name="Erinaceidae", children=[ERINACEUS])
SORICIDAE = Family(name="Soricidae", children=[SOREX])

EULIPOTYPHLA_A = Clade(children=[ERINACEIDAE, SORICIDAE])

EULIPOTYPHLA = Order(name="Eulipotyphla", children=[TALPIDAE, EULIPOTYPHLA_A])
