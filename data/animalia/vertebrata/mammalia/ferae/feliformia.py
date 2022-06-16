from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily
from constants import EN, PL, URL
from image import Image, License

from .felidae import FELIDAE

H_HYAENA = Species(
    name="Hyaena hyaena",
    local_names={EN: "striped hyena", PL: "hiena pręgowana"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Striped_hyena_(Hyaena_hyaena)_-_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Striped_hyena_%28Hyaena_hyaena%29_-_cropped.jpg",
        author="Rushikesh Deshmukh DOP",
        license=License.CC_BY_SA_4_0,
    ),
)
C_CROCUTA = Species(
    name="Crocuta crocuta",
    local_names={
        EN: "spotted hyena, laughing hyena",
        PL: "hiena centkowana, krokuta cętkowana",
    },
    known_for=[
        {
            EN: "Shenzi, Banzai and Ed from The Lion King",
            URL: "https://disney.fandom.com/wiki/Shenzi,_Banzai,_and_Ed",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crocuta_crocuta_-_Etosha_2015.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Crocuta_crocuta_-_Etosha_2015.jpg",
        author="Yathin S Krishnappa",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SURICATTA = Species(
    name="Suricata suricatta",
    local_names={EN: "meerkat, suricate", PL: "surykatka szara"},
    known_for=[
        {EN: "Timon from The Lion King", URL: "https://disney.fandom.com/wiki/Timon"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Suricata_suricatta_suricatta_97088339.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Suricata_suricatta_suricatta_97088339.jpg",
        author="Dave Brown",
        license=License.CC0,
    ),
)
M_MUNGO = Species(
    name="Mungos mungo",
    local_names={EN: "banded mongoose", PL: "mangusta pręgowana, mungo pręgowany"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Banded_Mongoose_(Mungos_mungo)_foraging_outside_the_fence_..._(30800475932)_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Banded_Mongoose_%28Mungos_mungo%29_foraging_outside_the_fence_..._%2830800475932%29_%282%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
C_FEROX = Species(
    name="Cryptoprocta ferox",
    local_names={EN: "fossa", PL: "fossa madagaskarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cryptoprocta_Ferox.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Cryptoprocta_Ferox.JPG",
        author="Ran Kirlian",
        license=License.CC_BY_SA_3_0,
    ),
)

HYAENA = Genus(name="Hyaena", children=[H_HYAENA])
CROCUTA = Genus(name="Crocuta", children=[C_CROCUTA])
SURICATA = Genus(name="Suricata", children=[S_SURICATTA])
URVA = Genus(name="Urva", children=[M_MUNGO])
CRYPTOPROCTA = Genus(name="Cryptoprocta", children=[C_FEROX])

HYAENINAE = Subfamily(name="Hyaeninae", children=[HYAENA, CROCUTA])

HYAENIDAE = Family(name="Hyaenidae", children=[HYAENINAE])
HERPESTIDAE = Family(name="Herpestidae", children=[SURICATA, URVA])
EUPLERIDAE = Family(name="Eupleridae", children=[CRYPTOPROCTA])

HERPESTOIDEA_A = Clade(children=[HERPESTIDAE, EUPLERIDAE])

HERPESTOIDEA = Superfamily(name="Herpestoidea", children=[HYAENIDAE, HERPESTOIDEA_A])

FELIFORMIA = Suborder(name="Feliformia", children=[HERPESTOIDEA, FELIDAE])
