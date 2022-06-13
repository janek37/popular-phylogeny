from clade import (
    Clade,
    Family,
    Genus,
    Order,
    Species,
    Subfamily,
    Suborder,
    Subtribe,
    Superfamily,
    Tribe,
)
from constants import EN, PL, URL
from image import Image, License

M_LYONSI = Species(
    name="Moeritherium lyonsi",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Moeritherium_NT_small.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Moeritherium_NT_small.jpg",
        author="Nobu Tamura email:nobu.tamura@yahoo.com https://spinops.blogspot.com/",
        license=License.CC_BY_SA_4_0,
    ),
)
B_GRAVE = Species(
    name="Barytherium grave",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Barytherium_NT.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Barytherium_NT.jpg",
        author="Nobu Tamura Email:nobu.tamura@yahoo.com http://spinops.blogspot.com/ http://paleoexhibit.blogspot.com/",
        license=License.CC_BY_SA_4_0,
    ),
)
P_GRANGERI = Species(
    name="Platybelodon grangeri",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Platybelodon_NT_small.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Platybelodon_NT_small.jpg",
        author="Nobu Tamura email:nobu.tamura@yahoo.com  http://spinops.blogspot.com/ http://paleoexhibit.blogspot.com/",
        license=License.CC_BY_SA_4_0,
    ),
)
D_GIGANTEUM = Species(
    name="Deinotherium giganteum",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Deinotherium12.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Deinotherium12.jpg",
        author="Creator:Dmitry Bogdanov",
        license=License.CC_BY_3_0,
    ),
)
P_BEADNELLI = Species(
    name="Palaeomastodon beadnelli",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Palaeomastodon_NT_small.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Palaeomastodon_NT_small.jpg",
        author="Nobu Tamura email:nobu.tamura@yahoo.com  http://spinops.blogspot.com/",
        license=License.CC_BY_SA_4_0,
    ),
)
M_AMERICANUM = Species(
    name="Mammut americanum",
    local_names={EN: "American mastodon", PL: "mastodont amerykański"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mammut_americanum.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Mammut_americanum.png",
        author="Joaquin Eng Ponce",
        license=License.CC_BY_SA_4_0,
    ),
)
S_GANESA = Species(
    name="Stegodon ganesa",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stegodon_ganesa_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Stegodon_ganesa_2.jpg",
        author="DiBgd",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SYRTICUS = Species(
    name="Stegotetrabelodon syrticus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stegotetrabelodon11.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Stegotetrabelodon11.jpg",
        author="ДиБгд",
        license=License.CC_BY_SA_4_0,
    ),
)
L_AFRICANA = Species(
    name="Loxodonta africana",
    local_names={
        EN: "African bush elephant, African savanna elephant",
        PL: "słoń afrykański",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elefante_africano_de_sabana_(Loxodonta_africana),_Elephant_Sands,_Botsuana,_2018-07-28,_DD_113.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Elefante_africano_de_sabana_%28Loxodonta_africana%29%2C_Elephant_Sands%2C_Botsuana%2C_2018-07-28%2C_DD_113.jpg",
        author="Diego Delso",
        license=License.CC_BY_SA_4_0,
    ),
)
P_ANTIQUUS = Species(
    name="Palaeoloxodon antiquus",
    local_names={EN: "straight-tusked elephant", PL: "słoń leśny"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elephas-antiquus,_front_to_the_left.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Elephas-antiquus%2C_front_to_the_left.jpg",
        author="DFoidl",
        license=License.CC_BY_SA_3_0,
    ),
)
P_FALCONERI = Species(
    name="Palaeoloxodon falconeri",
    local_names={EN: "Maltese pygmy elephant, Sicilian dwarf elephant"},
    known_for=[
        {EN: "possible source of the cyclops myth"},
        {
            EN: "Mr. Tusks from Dinosaur Comics",
            URL: "https://qwantz.com/index.php?comic=1078",
        },
    ],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elephas_falconeri.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Elephas_falconeri.jpg",
        author="Apokryltaros at English Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
M_PRIMIGENIUS = Species(
    name="Mammuthus primigenius",
    local_names={EN: "woolly mammoth", PL: "mamut włochaty"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202003_Woolly_mammoth.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/94/202003_Woolly_mammoth.svg",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
E_MAXIMUS = Species(
    name="Elephas maximus",
    local_names={EN: "Asian elephant", PL: "słoń indyjski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elephas_maximus_(Bandipur).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/98/Elephas_maximus_%28Bandipur%29.jpg",
        author="Yathin S Krishnappa",
        license=License.CC_BY_SA_3_0,
    ),
)

MOERITHERIUM = Genus(name="Moeritherium", children=[M_LYONSI])
BARYTHERIUM = Genus(name="Barytherium", children=[B_GRAVE])
PLATYBELODON = Genus(name="Platybelodon", children=[P_GRANGERI])
DEINOTHERIUM = Genus(name="Deinotherium", children=[D_GIGANTEUM])
PALAEOMASTODON = Genus(name="Palaeomastodon", children=[P_BEADNELLI])
MAMMUT = Genus(name="Mammut", children=[M_AMERICANUM])
STEGODON = Genus(name="Stegodon", children=[S_GANESA])
STEGOTETRABELODON = Genus(name="Stegotetrabelodon", children=[S_SYRTICUS])
LOXODONTA = Genus(name="Loxodonta", children=[L_AFRICANA])
PALAEOLOXODON = Genus(name="Palaeoloxodon", children=[P_ANTIQUUS, P_FALCONERI])
MAMMUTHUS = Genus(name="Mammuthus", children=[M_PRIMIGENIUS])
ELEPHAS = Genus(name="Elephas", children=[E_MAXIMUS])

ELEPHANTINA = Subtribe(name="Elephantina", children=[MAMMUTHUS, ELEPHAS])

ELEPHANTINI = Tribe(name="Elephantini", children=[ELEPHANTINA, PALAEOLOXODON])

ELEPHANTINAE = Subfamily(name="Elephantinae", children=[LOXODONTA, ELEPHANTINI])

MOERITHERIIDAE = Family(name="Moeritheriidae", children=[MOERITHERIUM])
BARYTHERIIDAE = Family(name="Barytheriidae", children=[BARYTHERIUM])
AMEBELODONTIDAE = Family(name="Amebelodontidae", children=[PLATYBELODON])
DEINOTHERIIDAE = Family(name="Deinotheriidae", children=[DEINOTHERIUM])
PALAEOMASTODONTIDAE = Family(name="Palaeomastodontidae", children=[PALAEOMASTODON])
MAMMUTIDAE = Family(name="Mammutidae", children=[MAMMUT])
STEGODONTIDAE = Family(name="Stegodontidae", children=[STEGODON])
ELEPHANTIDAE = Family(name="Elephantidae", children=[ELEPHANTINAE, STEGOTETRABELODON])

ELEPHANTOIDEA = Superfamily(
    name="Elephantoidea", children=[ELEPHANTIDAE, STEGODONTIDAE]
)

ELEPHANTIDA = Clade(name="Elephantida", children=[ELEPHANTOIDEA, AMEBELODONTIDAE])

ELEPHANTIMORPHA = Clade(name="Elephantimorpha", children=[ELEPHANTIDA, MAMMUTIDAE])

PLESIELEPHANTIFORMES = Suborder(
    name="Plesielephantiformes", children=[BARYTHERIIDAE, DEINOTHERIIDAE]
)
ELEPHANTIFORMES = Suborder(
    name="Elephantiformes", children=[ELEPHANTIMORPHA, PALAEOMASTODONTIDAE]
)

# https://en.wikipedia.org/wiki/Elephant#Evolution_and_extinct_relatives
PROBOSCIDEA_A = Clade(children=[ELEPHANTIFORMES, PLESIELEPHANTIFORMES])

PROBOSCIDEA = Order(name="Proboscidea", children=[PROBOSCIDEA_A, MOERITHERIIDAE])
