from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, PL
from image import Image, License

P_VAMPYRUS = Species(
    name="Pteropus vampyrus",
    local_names={
        EN: "large flying fox, large fruit bat",
        PL: "pies latający, rudawka malajska",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Philippine_Giant_Fruit_Bat_Pteropus_vampyrus_lanensis_(16523314302).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Philippine_Giant_Fruit_Bat_Pteropus_vampyrus_lanensis_%2816523314302%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
D_ROTUNDUS = Species(
    name="Desmodus rotundus",
    local_names={EN: "common vampire bat", PL: "wampir zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Desmodus_rotundus_1847.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/27/Desmodus_rotundus_1847.jpg",
        author="in Alcide Dessalines d'Orbigny",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_PIPISTRELLUS = Species(
    name="Pipistrellus pipistrellus",
    local_names={EN: "common pipistrelle", PL: "karlik malutki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vespertilio_pipistrellus_-_1700-1880_-_Print_-_Iconographia_Zoologica_-_Special_Collections_University_of_Amsterdam_-_UBA01_IZ20800115.tif",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Vespertilio_pipistrellus_-_1700-1880_-_Print_-_Iconographia_Zoologica_-_Special_Collections_University_of_Amsterdam_-_UBA01_IZ20800115.tif",
        author="Special Collections of the University of Amsterdam",
        license=License.PUBLIC_DOMAIN,
    ),
)
M_LUCIFUGUS = Species(
    name="Myotis lucifugus",
    local_names={EN: "little brown bat", PL: "nocek myszouchy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myotis_lucifugus_illustration.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Myotis_lucifugus_illustration.jpg",
        author="Chapman, Frank M.; Seton, Ernest Thompson; Wright, Mabel Osgood",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_AURITUS = Species(
    name="Plecotus auritus",
    local_names={
        EN: "brown long-eared bat, common long-eared bat",
        PL: "gacek wielkouch, gacek brunatny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brown_long-eared_bat_(Plecotus_auritus)_-_geograph.org.uk_-_1415542.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Brown_long-eared_bat_%28Plecotus_auritus%29_-_geograph.org.uk_-_1415542.jpg",
        author="Evelyn Simak",
        license=License.CC_BY_SA_2_0,
    ),
)

PTEROPUS = Genus(name="Pteropus", children=[P_VAMPYRUS])
DESMODUS = Genus(name="Desmodus", children=[D_ROTUNDUS])
PIPISTRELLUS = Genus(name="Pipistrellus", children=[P_PIPISTRELLUS])
MYOTIS = Genus(name="Myotis", children=[M_LUCIFUGUS])
PLECOTUS = Genus(name="Plecotus", children=[P_AURITUS])

VESPERTILIONINAE = Subfamily(name="Vespertilioninae", children=[PIPISTRELLUS, PLECOTUS])
MYOTINAE = Subfamily(name="Myotinae", children=[MYOTIS])

PTEROPODIDAE = Family(name="Pteropodidae", children=[PTEROPUS])
PHYLLOSTOMIDAE = Family(name="Phyllostomidae", children=[DESMODUS])
VESPERTILIONIDAE = Family(
    name="Vespertilionidae", children=[VESPERTILIONINAE, MYOTINAE]
)

CHIROPTERA_A = Clade(children=[PHYLLOSTOMIDAE, VESPERTILIONIDAE])

CHIROPTERA = Order(name="Chiroptera", children=[PTEROPODIDAE, CHIROPTERA_A])
