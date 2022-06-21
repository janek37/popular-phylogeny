from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

B_BUBO = Species(
    name="Bubo bubo",
    local_names={EN: "eurasian eagle-owl", PL: "puchacz zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bubo_bubo_sibiricus_-_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Bubo_bubo_sibiricus_-_01.JPG",
        author="Carlos Delgado",
        license=License.CC_BY_SA_4_0,
    ),
)
B_VIRGINIANUS = Species(
    name="Bubo virginianus",
    local_names={EN: "great horned owl, tiger owl", PL: "puchacz wirginijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bubo_virginianus_-Reifel_Migratory_Bird_Sanctuary-8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Bubo_virginianus_-Reifel_Migratory_Bird_Sanctuary-8.jpg",
        author="Brendan Lally",
        license=License.CC_BY_2_0,
    ),
)
B_SCANDIACUS = Species(
    name="Bubo scandiacus",
    local_names={EN: "snowy owl", PL: "sowa śnieżna, puchacz śnieżny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Snowy_Owl_(Bubo_scandiacus)_(23179229549).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Snowy_Owl_%28Bubo_scandiacus%29_%2823179229549%29.jpg",
        author="Andrew C",
        license=License.CC_BY_2_0,
    ),
)
S_ALUCO = Species(
    name="Strix aluco",
    local_names={EN: "tawny owl, brown owl", PL: "puszczyk zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Strix_aluco_3_(Martin_Mecnarowski).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Strix_aluco_3_%28Martin_Mecnarowski%29.jpg",
        author="Martin Mecnarowski (http://www.photomecan.eu/)",
        license=License.CC_BY_SA_3_0,
    ),
)
A_NOCTUA = Species(
    name="Athene noctua",
    local_names={EN: "little owl", PL: "pójdźka zwyczajna"},
    known_for=[{EN: "owl of Athena/Minerva"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Little_owl_(Athene_noctua)_Morocco,_tetouan_By_Takhrefa_Ismael.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Little_owl_%28Athene_noctua%29_Morocco%2C_tetouan_By_Takhrefa_Ismael.jpg",
        author="Takhrefa ismael",
        license=License.CC_BY_SA_4_0,
    ),
)
A_OTUS = Species(
    name="Asio otus",
    local_names={EN: "long-eared owl, cat owl", PL: "uszatka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Long-eared_owl_in_Central_Park_(50208).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Long-eared_owl_in_Central_Park_%2850208%29.jpg",
        author="Rhododendrites",
        license=License.CC_BY_SA_4_0,
    ),
)
T_ALBA = Species(
    name="Tyto alba",
    local_names={EN: "barn owl", PL: "płomykówka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flickr_-_Rainbirder_-_Barn_Owl_(Tyto_alba).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/98/Flickr_-_Rainbirder_-_Barn_Owl_%28Tyto_alba%29.jpg",
        author="Steve Garvie from Dunfermline, Fife, Scotland",
        license=License.CC_BY_SA_2_0,
    ),
)

# https://www.sciencedirect.com/science/article/abs/pii/S1055790312004642
# https://ars.els-cdn.com/content/image/1-s2.0-S1055790312004642-gr2.jpg
BUBO_A = Clade(children=[B_VIRGINIANUS, B_SCANDIACUS])

BUBO = Genus(name="Bubo", children=[B_BUBO, BUBO_A])
STRIX = Genus(name="Strix", children=[S_ALUCO])
ATHENE = Genus(name="Athene", children=[A_NOCTUA])
ASIO = Genus(name="Asio", children=[A_OTUS])
TYTO = Genus(name="Tyto", children=[T_ALBA])

STRIGIDAE_A = Clade(children=[BUBO, STRIX])
STRIGIDAE_B = Clade(children=[STRIGIDAE_A, ASIO])

STRIGIDAE = Family(name="Strigidae", children=[STRIGIDAE_B, ATHENE])
TYTONIDAE = Family(name="Tytonidae", children=[TYTO])

STRIGIFORMES = Order(name="Strigiformes", children=[STRIGIDAE, TYTONIDAE])
