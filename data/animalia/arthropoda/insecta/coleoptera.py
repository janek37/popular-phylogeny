from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Order,
    Species,
    Subfamily,
    Suborder,
    Superfamily,
)
from constants import EN, PL
from image import Image, License

D_MARGINALIS = Species(
    name="Dytiscus marginalis",
    local_names={EN: "great diving beetle", PL: "pływak żółtobrzeżek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schiermonnikoog_-_Gewone_geelrand_(Dytiscus_marginalis).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Schiermonnikoog_-_Gewone_geelrand_%28Dytiscus_marginalis%29.jpg",
        author="Rudolphous",
        license=License.CC_BY_SA_4_0,
    ),
)
P_CRUXMAJOR = Species(
    name="Panagaeus cruxmajor",
    local_names={EN: "crucifix ground beetle", PL: "świętek krzyżaczek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Panagaeus_cruxmajor_bl.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Panagaeus_cruxmajor_bl.jpg",
        author="Siga",
        license=License.CC_BY_SA_3_0,
    ),
)
C_AURATUS = Species(
    name="Carabus auratus",
    local_names={EN: "golden ground beetle", PL: "biegacz złocisty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carabus_auratus_1_(US).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0a/Carabus_auratus_1_%28US%29.jpg",
        author="URSchmidt",
        license=License.CC_BY_3_0,
    ),
)
G_STERCORARIUS = Species(
    name="Geotrupes stercorarius",
    local_names={EN: "dor beetle", PL: "żuk gnojowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Geotrupes_stercorarius_(Linn%C3%A9,_1758)_Male_(19372749035).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Geotrupes_stercorarius_%28Linn%C3%A9%2C_1758%29_Male_%2819372749035%29.png",
        author="Udo Schmidt from Deutschland",
        license=License.CC_BY_SA_2_0,
    ),
)
L_CERVUS = Species(
    name="Lucanus cervus",
    local_names={EN: "European stag beetle", PL: "jelonek rogacz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lucanus_cervus_Cantilaga.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8c/Lucanus_cervus_Cantilaga.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SACER = Species(
    name="Scarabaeus sacer",
    local_names={EN: "sacred scarab", PL: "skarabeusz, poświętnik czczony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Scarabaeus_sacer_Linn%C3%A9,_1758_(28486691625).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Scarabaeus_sacer_Linn%C3%A9%2C_1758_%2828486691625%29.png",
        author="Udo Schmidt from Deutschland",
        license=License.CC_BY_SA_2_0,
    ),
)
M_MELOLONTHA = Species(
    name="Melolontha melolontha",
    local_names={EN: "Maybug, cockchafer", PL: "chrabąszcz majowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Melolontha_melolontha01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Melolontha_melolontha01.jpg",
        author="Tik",
        license=License.CC_BY_SA_3_0,
    ),
)
O_NASICORNIS = Species(
    name="Oryctes nasicornis",
    local_names={EN: "European rhinoceros beetle", PL: "rohatyniec nosorożec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oryctes_nasicornis_male_Bytom.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c8/Oryctes_nasicornis_male_Bytom.jpg",
        author="Adrian Tync",
        license=License.CC_BY_SA_4_0,
    ),
)
L_NOCTILUCA = Species(
    name="Lampyris noctiluca",
    local_names={EN: "common glow-worm", PL: "świetlik świętojański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lampyris_noctiluca_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/12/Lampyris_noctiluca_01.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
A_PUNCTATUM = Species(
    name="Anobium punctatum",
    local_names={EN: "common furniture beetle", PL: "kołatek domowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coleoptera-_Anobium_punctatum_(m)_(2700587600).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Coleoptera-_Anobium_punctatum_%28m%29_%282700587600%29.jpg",
        author="Mick Talbot from Lincoln (U.K.), England",
        license=License.CC_BY_2_0,
    ),
)
C_SEPTEMPUNCTATA = Species(
    name="Coccinella septempunctata",
    local_names={
        EN: "seven-spot ladybird, seven-spotted ladybug, C-7",
        PL: "boża krówka, biedronka siedmiokropka",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coccinella-septempunctata--Trp-1.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Coccinella-septempunctata--Trp-1.png",
        author="Vega asensio, modified by MathKnight",
        license=License.CC_BY_SA_3_0,
    ),
)
H_AXYRIDIS = Species(
    name="Harmonia axyridis",
    local_names={EN: "harlequin, Asian ladybeetle", PL: "biedronka azjatycka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Harmonia_axyridis_imagines_20090801.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Harmonia_axyridis_imagines_20090801.jpg",
        author="Pbech",
        license=License.CC0,
    ),
)
L_DECEMLINEATA = Species(
    name="Leptinotarsa decemlineata",
    local_names={EN: "Colorado potato beetle", PL: "stonka ziemniaczana"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leptinotarsa-decemlineata-02-fws.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/Leptinotarsa-decemlineata-02-fws.jpg",
        author="Francisco Welter-Schultes",
        license=License.CC0,
    ),
)
S_GRANARIUS = Species(
    name="Sitophilus granarius",
    local_names={EN: "wheat weevil", PL: "wołek zbożowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:COLE_Curculionidae_Sitophilus_granarius.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/COLE_Curculionidae_Sitophilus_granarius.png",
        author="Des Helmore / Manaaki Whenua – Landcare Research",
        license=License.CC_BY_SA_4_0,
    ),
)
D_PONDEROSAE = Species(
    name="Dendroctonus ponderosae",
    local_names={EN: "mountain pine beetle"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:The_mountain_pine_beetle.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/57/The_mountain_pine_beetle.jpg",
        author="Steve Clarkson",
        license=License.PUBLIC_DOMAIN,
    ),
)
I_TYPOGRAPHUS = Species(
    name="Ips typographus",
    local_names={EN: "European spruce bark beetle", PL: "kornik drukarz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ips-typographus-09-fws.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Ips-typographus-09-fws.jpg",
        author="Francisco Welter-Schultes",
        license=License.CC0,
    ),
)

DYTISCUS = Genus(name="Dytiscus", children=[D_MARGINALIS])
PANAGAEUS = Genus(name="Panagaeus", children=[P_CRUXMAJOR])
CARABUS = Genus(name="Carabus", children=[C_AURATUS])
GEOTRUPES = Genus(name="Geotrupes", children=[G_STERCORARIUS])
LUCANUS = Genus(name="Lucanus", children=[L_CERVUS])
SCARABAEUS = Genus(name="Scarabaeus", children=[S_SACER])
MELOLONTHA = Genus(name="Melolontha", children=[M_MELOLONTHA])
ORYCTES = Genus(name="Oryctes", children=[O_NASICORNIS])
LAMPYRIS = Genus(name="Lampyris", children=[L_NOCTILUCA])
ANOBIUM = Genus(name="Anobium", children=[A_PUNCTATUM])
COCCINELLA = Genus(name="Coccinella", children=[C_SEPTEMPUNCTATA])
HARMONIA = Genus(name="Harmonia", children=[H_AXYRIDIS])
LEPTINOTARSA = Genus(name="Leptinotarsa", children=[L_DECEMLINEATA])
SITOPHILUS = Genus(name="Sitophilus", children=[S_GRANARIUS])
DENDROCTONUS = Genus(name="Dendroctonus", children=[D_PONDEROSAE])
IPS = Genus(name="Ips", children=[I_TYPOGRAPHUS])

DRYOPHTHORINAE = Subfamily(name="Dryophthorinae", children=[SITOPHILUS])
SCOLYTINAE = Subfamily(name="Scolytinae", children=[DENDROCTONUS, IPS])

DYTISCIDAE = Family(name="Dytiscidae", children=[DYTISCUS])
CARABIDAE = Family(name="Carabidae", children=[PANAGAEUS, CARABUS])
GEOTRUPIDAE = Family(name="Geotrupidae", children=[GEOTRUPES])
LUCANIDAE = Family(name="Lucanidae", children=[LUCANUS])
SCARABAEIDAE = Family(name="Scarabaeidae", children=[SCARABAEUS, MELOLONTHA, ORYCTES])
LAMPYRIDAE = Family(name="Lampyridae", children=[LAMPYRIS])
PTINIDAE = Family(name="Ptinidae", children=[ANOBIUM])
COCCINELLIDAE = Family(name="Coccinellidae", children=[COCCINELLA, HARMONIA])
CHRYSOMELIDAE = Family(name="Chrysomelidae", children=[LEPTINOTARSA])
CURCULIONIDAE = Family(name="Curculionidae", children=[DRYOPHTHORINAE, SCOLYTINAE])

SCARABAEOIDEA = Superfamily(
    name="Scarabaeoidea", children=[GEOTRUPIDAE, LUCANIDAE, SCARABAEIDAE]
)
ELATEROIDEA = Superfamily(name="Elateroidea", children=[LAMPYRIDAE])
BOSTRICHOIDEA = Superfamily(name="Bostrichoidea", children=[PTINIDAE])
COCCINELLOIDEA = Superfamily(name="Coccinelloidea", children=[COCCINELLIDAE])
CHRYSOMELOIDEA = Superfamily(name="Chrysomeloidea", children=[CHRYSOMELIDAE])
CURCULIONOIDEA = Superfamily(name="Curculionoidea", children=[CURCULIONIDAE])

PHYTOPHAGA = Clade(name="Phytophaga", children=[CHRYSOMELOIDEA, CURCULIONOIDEA])

CUCUJIFORMIA = Infraorder(name="Cucujiformia", children=[COCCINELLOIDEA, PHYTOPHAGA])

# https://en.wikipedia.org/wiki/Beetle
POLYPHAGA_B = Clade(children=[BOSTRICHOIDEA, CUCUJIFORMIA])
POLYPHAGA_A = Clade(children=[ELATEROIDEA, POLYPHAGA_B])

ADEPHAGA = Suborder(name="Adephaga", children=[DYTISCIDAE, CARABIDAE])
POLYPHAGA = Suborder(name="Polyphaga", children=[SCARABAEOIDEA, POLYPHAGA_A])

COLEOPTERA = Order(name="Coleoptera", children=[ADEPHAGA, POLYPHAGA])
