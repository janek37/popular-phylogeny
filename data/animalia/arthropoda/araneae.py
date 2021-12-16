from clade import Family, Genus, Infraorder, Order, Species, Superfamily
from constants import EN, PL

B_SMITHI = Species(
    name="Brachypelma smithi",
    local_names={EN: "Mexican redknee tarantula"},
    known_for=[
        {
            EN: "one of the popular pet tarantulas",
            PL: "jeden z popularnych ptaszników hodowanych w domach",
        }
    ],
)
A_DIADEMATUS = Species(
    name="Araneus diadematus",
    local_names={EN: "European garden spider", PL: "krzyżak ogrodowy"},
)
L_MACTANS = Species(
    name="Latrodectus mactans",
    local_names={EN: "southern black widow", PL: "czarna wdowa"},
)
P_PHALANGIOIDES = Species(
    name="Pholcus phalangioides",
    local_names={EN: "daddy long-legs spider", PL: "nasosznik trzęś"},
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
