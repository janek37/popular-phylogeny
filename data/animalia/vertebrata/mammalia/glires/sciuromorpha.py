from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Tribe
from constants import EN, PL, URL
from image import Image, License

M_AVELLANARIUS = Species(
    name="Muscardinus avellanarius",
    local_names={EN: "hazel dormouse, common dormouse", PL: "orzesznica leszczynowa"},
    known_for=[
        {
            EN: "The Dormouse from Alice in Wonderland",
            URL: "https://en.wikipedia.org/wiki/The_Dormouse",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hazel_dormouse_(Muscardinus_avellanarius),_Skole,_Lviv_Oblast,_Ukraine_(50540055351).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Hazel_dormouse_%28Muscardinus_avellanarius%29%2C_Skole%2C_Lviv_Oblast%2C_Ukraine_%2850540055351%29.jpg",
        author="Frank Vassen from Brussels, Belgium",
        license=License.CC_BY_2_0,
    ),
)
G_GLIS = Species(
    name="Glis glis",
    local_names={EN: "European edible dormouse", PL: "popielica szara"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Glis_glis_.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Glis_glis_.jpg",
        author="Youbadou",
        license=License.CC_BY_4_0,
    ),
)
S_VULGARIS = Species(
    name="Sciurus vulgaris",
    local_names={EN: "red squirrel", PL: "wiewiórka ruda, wiewiórka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Red_squirrel_(Sciurus_vulgaris).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/13/Red_squirrel_%28Sciurus_vulgaris%29.jpg",
        author="Darkone",
        license=License.CC_BY_SA_2_5,
    ),
)
S_CAROLINENSIS = Species(
    name="Sciurus carolinensis",
    local_names={EN: "eastern gray squirrel", PL: "wiewiórka szara"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:EasternGraySquirrel_GAm.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/EasternGraySquirrel_GAm.jpg",
        author="MarshBunny",
        license=License.CC_BY_SA_4_0,
    ),
)
G_VOLANS = Species(
    name="Glaucomys volans",
    local_names={EN: "southern flying squirrel", PL: "assapan południowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Southern_Flying_Squirrel-27527-1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/63/Southern_Flying_Squirrel-27527-1.jpg",
        author="Ken Thomas",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
P_VOLANS = Species(
    name="Pteromys volans",
    local_names={EN: "Siberian flying squirrel", PL: "polatucha syberyjska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pteromysvolans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Pteromysvolans.jpg",
        author="A.Popov",
        license=License.CC_BY_SA_3_0,
    ),
)
M_MARMOTA = Species(
    name="Marmota marmota",
    local_names={EN: "alpine marmot", PL: "świstak alpejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Marmota_marmota_Alpes2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/26/Marmota_marmota_Alpes2.jpg",
        author="François Trazzi",
        license=License.CC_BY_SA_3_0,
    ),
)
M_MONAX = Species(
    name="Marmota monax",
    local_names={EN: "groundhog, woodchuck", PL: "świszcz, świstak amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Marmota_monax-lateral.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Marmota_monax-lateral.jpg",
        author="Peterwchen",
        license=License.CC_BY_SA_4_0,
    ),
)
T_STRIATUS = Species(
    name="Tamias striatus",
    local_names={EN: "eastern chipmunk", PL: "pręgowiec amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eastern_Chipmunk_(Tamias_striatus)_Pennsylvania.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Eastern_Chipmunk_%28Tamias_striatus%29_Pennsylvania.jpg",
        author="Kaldari",
        license=License.CC0,
    ),
)
C_LUDOVICIANUS = Species(
    name="Cynomys ludovicianus",
    local_names={
        EN: "black-tailed prairie dog",
        PL: "piesek preriowy, nieświszczuk czarnoogonowy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Black-Tailed_Prairie_Dog.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fd/Black-Tailed_Prairie_Dog.jpg",
        author="Joe Ravi",
        license=License.CC_BY_SA_3_0,
    ),
)
S_SUSLICUS = Species(
    name="Spermophilus suslicus",
    local_names={
        EN: "speckled ground squirrel, spotted souslik",
        PL: "suseł perełkowany",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Spermophilus_suslicus-small.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Spermophilus_suslicus-small.JPG",
        author="Lobkov V.A.",
        license=License.CC_BY_SA_3_0,
    ),
)

MUSCARDINUS = Genus(name="Muscardinus", children=[M_AVELLANARIUS])
GLIS = Genus(name="Glis", children=[G_GLIS])
SCIURUS = Genus(name="Sciurus", children=[S_VULGARIS, S_CAROLINENSIS])
GLAUCOMYS = Genus(name="Glaucomys", children=[G_VOLANS])
PTEROMYS = Genus(name="Pteromys", children=[P_VOLANS])
MARMOTA = Genus(name="Marmota", children=[M_MARMOTA, M_MONAX])
TAMIAS = Genus(name="Tamias", children=[T_STRIATUS])
CYNOMYS = Genus(name="Cynomys", children=[C_LUDOVICIANUS])
SPERMOPHILUS = Genus(name="Spermophilus", children=[S_SUSLICUS])

# https://www.researchgate.net/publication/327823215_Impacts_Of_Inference_Method_And_Dataset_Filtering_On_Phylogenomic_Resolution_In_A_Rapid_Radiation_of_Ground_Squirrels_Xerinae_Marmotini
MARMOTINI_A = Clade(children=[CYNOMYS, SPERMOPHILUS])
MARMOTINI_B = Clade(children=[MARMOTA, MARMOTINI_A])

SCIURINI = Tribe(name="Sciurini", children=[SCIURUS])
PTEROMYINI = Tribe(
    name="Pteromyini",
    children=[GLAUCOMYS, PTEROMYS],
    local_names={EN: "fyling squirrel", PL: "latające wiewiórki, polatuchy"},
)
MARMOTINI = Tribe(name="Marmotini", children=[MARMOTINI_B, TAMIAS])

SCIURINAE = Subfamily(name="Sciurinae", children=[SCIURINI, PTEROMYINI])
XERINAE = Subfamily(name="Xerinae", children=[MARMOTINI])

GLIRIDAE = Family(name="Gliridae", children=[MUSCARDINUS, GLIS])
SCIURIDAE = Family(name="Sciuridae", children=[SCIURINAE, XERINAE])

SCIUROMORPHA = Suborder(name="Sciuromorpha", children=[GLIRIDAE, SCIURIDAE])
