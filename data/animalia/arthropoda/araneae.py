from clade import Family, Genus, Infraorder, Order, Species, Superfamily
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

BRACHYPELMA = Genus(name="Brachypelma", children=[B_SMITHI])
ARANEUS = Genus(name="Araneus", children=[A_DIADEMATUS])
LATRODECTUS = Genus(name="Latrodectus", children=[L_MACTANS])
PHOLCUS = Genus(name="Pholcus", children=[P_PHALANGIOIDES])

THERAPHOSIDAE = Family(
    name="Theraphosidae",
    children=[BRACHYPELMA],
    local_names={PL: "ptasznikowate", EN: "tarantulas"},
)
ARANEIDAE = Family(name="Araneidae", children=[ARANEUS])
THERIDIIDAE = Family(name="Theridiidae", children=[LATRODECTUS])
PHOLCIDAE = Family(name="Pholcidae", children=[PHOLCUS])

ARANEOIDEA = Superfamily(name="Araneoidea", children=[ARANEIDAE, THERIDIIDAE])
PHOLCOIDEA = Superfamily(name="Pholcoidea", children=[PHOLCIDAE])

MYGALOMORPHAE = Infraorder(name="Mygalomorphae", children=[THERAPHOSIDAE])
ARANEOMORPHAE = Infraorder(name="Araneomorphae", children=[ARANEOIDEA, PHOLCOIDEA])

ARANEAE = Order(name="Araneae", children=[MYGALOMORPHAE, ARANEOMORPHAE])
