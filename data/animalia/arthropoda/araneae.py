from clade import Clade, Family, Genus, Infraorder, Order, Species, Superfamily
from constants import EN, PL
from image import Image, License

B_SMITHI = Species(
    name="Brachypelma smithi",
    local_names={EN: "Mexican redknee tarantula"},
    known_for=[
        {
            EN: "one of the popular pet tarantulas",
            PL: "jeden z popularnych ptaszników hodowanych w domach",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brachypelma_smithi_2009_G02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/Brachypelma_smithi_2009_G02.jpg",
        author="George Chernilevsky",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
A_DIADEMATUS = Species(
    name="Araneus diadematus",
    local_names={EN: "European garden spider", PL: "krzyżak ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Araneus_diadematus_MHNT_Femelle_Fronton.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Araneus_diadematus_MHNT_Femelle_Fronton.jpg",
        author="Didier Descouens",
        license=License.CC_BY_SA_3_0,
    ),
)
L_MACTANS = Species(
    name="Latrodectus mactans",
    local_names={EN: "southern black widow", PL: "czarna wdowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Latrodectus_mactans_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Latrodectus_mactans_1.jpg",
        author="Rick Kimpel",
        license=License.CC_BY_SA_2_0,
    ),
)
P_PHALANGIOIDES = Species(
    name="Pholcus phalangioides",
    local_names={EN: "daddy long-legs spider", PL: "nasosznik trzęś"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pholcus.phalangioides.6905.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bf/Pholcus.phalangioides.6905.jpg",
        author="Olei",
        license=License.CC_BY_SA_2_5,
    ),
)
B_KIPLINGI = Species(
    name="Bagheera kiplingi",
    known_for=[{EN: "the only known herbivorous spider"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bagheera_kiplingi_male_JAL14-9421.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Bagheera_kiplingi_male_JAL14-9421.jpg",
        author="Wayne Maddison",
        license=License.CC_BY_3_0,
    ),
)
S_SCENICUS = Species(
    name="Salticus scenicus",
    local_names={EN: "zebra jumping spider", PL: "skakun arlekinowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kaldari_Salticus_scenicus_female_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Kaldari_Salticus_scenicus_female_03.jpg",
        author="Kaldari",
        license=License.CC0,
    ),
)

BRACHYPELMA = Genus(name="Brachypelma", children=[B_SMITHI])
ARANEUS = Genus(name="Araneus", children=[A_DIADEMATUS])
LATRODECTUS = Genus(name="Latrodectus", children=[L_MACTANS])
PHOLCUS = Genus(name="Pholcus", children=[P_PHALANGIOIDES])
BAGHEERA = Genus(name="Bagheera", children=[B_KIPLINGI])
SALTICUS = Genus(name="Salticus", children=[S_SCENICUS])

THERAPHOSIDAE = Family(
    name="Theraphosidae",
    children=[BRACHYPELMA],
    local_names={PL: "ptasznikowate", EN: "tarantulas"},
)
ARANEIDAE = Family(name="Araneidae", children=[ARANEUS])
THERIDIIDAE = Family(name="Theridiidae", children=[LATRODECTUS])
PHOLCIDAE = Family(name="Pholcidae", children=[PHOLCUS])
SALTICIDAE = Family(name="Salticidae", children=[BAGHEERA, SALTICUS])

ARANEOIDEA = Superfamily(name="Araneoidea", children=[ARANEIDAE, THERIDIIDAE])
PHOLCOIDEA = Superfamily(name="Pholcoidea", children=[PHOLCIDAE])
SALTICOIDEA = Superfamily(name="Salticoidea", children=[SALTICIDAE])

# https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/araneomorphae
ARANEOMORPHAE_A = Clade(children=[ARANEOIDEA, SALTICOIDEA])

MYGALOMORPHAE = Infraorder(name="Mygalomorphae", children=[THERAPHOSIDAE])
ARANEOMORPHAE = Infraorder(name="Araneomorphae", children=[ARANEOMORPHAE_A, PHOLCOIDEA])

ARANEAE = Order(name="Araneae", children=[MYGALOMORPHAE, ARANEOMORPHAE])
