from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .faboideae import FABOIDEAE

T_INDICA = Species(
    name="Tamarindus indica",
    local_names={EN: "tamarind", PL: "tamaryndowiec indyjski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tamarindus_indica_(7046701667).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f8/Tamarindus_indica_%287046701667%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
M_PUDICA = Species(
    name="Mimosa pudica",
    local_names={PL: "mimoza wstydliwa", EN: "sensitive plant, touch-me-not"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mimosa_pudica_a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Mimosa_pudica_a.jpg",
        author="Goga504",
        license=License.CC_BY_SA_4_0,
    ),
)
V_TORTILIS = Species(
    name="Vachellia tortilis",
    local_names={PL: "akacja", EN: "umbrella thorn acacia"},
    known_for=[
        {EN: "biblical mentions"},
        {
            EN: "Tree of Ténéré, formerly the loneliest tree",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Arbre-du-tenere-1961.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/f0/Arbre-du-tenere-1961.jpg",
                author="Michel Mazeau",
                license=License.CC_BY_SA_2_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vachellia_tortilis_subsp._heteracantha_20D_4561.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2a/Vachellia_tortilis_subsp._heteracantha_20D_4561.jpg",
        author="SAplants",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SENEGAL = Species(
    name="Senegalia senegal",
    local_names={EN: "gum acacia, gum arabic tree", PL: "akacja senegalska"},
    known_for=[
        {
            EN: "gum arabic",
            PL: "guma arabska",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Gummi_arabicum_pieces_and_powder.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Gummi_arabicum_pieces_and_powder.jpg",
                author="Simon A. Eugster",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acacia_senegal_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-004.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/Acacia_senegal_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-004.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_SILIQUA = Species(
    name="Ceratonia siliqua",
    local_names={EN: "carob, locust tree", PL: "drzewo karobowe, szarańczyn strąkowy"},
    known_for=[
        {
            EN: "St John's bread",
            PL: "chleb świętojański",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Carob_flour_%CF%87%CE%B1%CF%81%CE%BF%CF%85%CF%80%CE%AC%CE%BB%CE%B5%CF%85%CF%81%CE%BF.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Carob_flour_%CF%87%CE%B1%CF%81%CE%BF%CF%85%CF%80%CE%AC%CE%BB%CE%B5%CF%85%CF%81%CE%BF.jpg",
                author="Sotiria Simota",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ceratonia_siliqua_Carob_Tree_%E1%83%99%E1%83%94%E1%83%A0%E1%83%90%E1%83%A2%E1%83%98_(3).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Ceratonia_siliqua_Carob_Tree_%E1%83%99%E1%83%94%E1%83%A0%E1%83%90%E1%83%A2%E1%83%98_%283%29.JPG",
        author="Lazaregagnidze",
        license=License.CC_BY_SA_4_0,
    ),
)

TAMARINDUS = Genus(name="Tamarindus", children=[T_INDICA])
MIMOSA = Genus(name="Mimosa", children=[M_PUDICA])
VACHELLIA = Genus(name="Vachellia", children=[V_TORTILIS])
SENEGALIA = Genus(name="Senegalia", children=[S_SENEGAL])
CERATONIA = Genus(name="Ceratonia", children=[C_SILIQUA])

AMHERSTIEAE = Tribe(name="Amherstieae", children=[TAMARINDUS])

MIMOSOIDEAE_A = Clade(children=[MIMOSA, SENEGALIA])
MIMOSOIDEAE = Clade(name="Mimosoideae", children=[MIMOSOIDEAE_A, VACHELLIA])

DETARIOIDEAE = Subfamily(name="Detarioideae", children=[AMHERSTIEAE])
CAESALPINIOIDEAE = Subfamily(name="Caesalpinioideae", children=[MIMOSOIDEAE, CERATONIA])

CAESALPINIOIDEAE_FABOIDEAE = Clade(children=[CAESALPINIOIDEAE, FABOIDEAE])
FABACEAE = Family(name="Fabaceae", children=[DETARIOIDEAE, CAESALPINIOIDEAE_FABOIDEAE])

FABALES = Order(name="Fabales", children=[FABACEAE])
