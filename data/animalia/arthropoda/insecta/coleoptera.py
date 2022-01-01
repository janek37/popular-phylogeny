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

D_MARGINALIS = Species(
    name="Dytiscus marginalis",
    local_names={EN: "great diving beetle", PL: "pływak żółtobrzeżek"},
)
P_CRUXMAJOR = Species(
    name="Panagaeus cruxmajor",
    local_names={EN: "crucifix ground beetle", PL: "świętek krzyżaczek"},
)
C_AURATUS = Species(
    name="Carabus auratus",
    local_names={EN: "golden ground beetle", PL: "biegacz złocisty"},
)
G_STERCORARIUS = Species(
    name="Geotrupes stercorarius", local_names={EN: "dor beetle", PL: "żuk gnojowy"}
)
L_CERVUS = Species(
    name="Lucanus cervus",
    local_names={EN: "European stag beetle", PL: "jelonek rogacz"},
)
S_SACER = Species(
    name="Scarabaeus sacer",
    local_names={EN: "sacred scarab", PL: "skarabeusz, poświętnik czczony"},
)
M_MELOLONTHA = Species(
    name="Melolontha melolontha",
    local_names={EN: "Maybug, cockchafer", PL: "chrabąszcz majowy"},
)
O_NASICORNIS = Species(
    name="Oryctes nasicornis",
    local_names={EN: "European rhinoceros beetle", PL: "rohatyniec nosorożec"},
)
L_NOCTILUCA = Species(
    name="Lampyris noctiluca",
    local_names={EN: "common glow-worm", PL: "świetlik świętojański"},
)
A_PUNCTATUM = Species(
    name="Anobium punctatum",
    local_names={EN: "common furniture beetle", PL: "kołatek domowy"},
)
C_SEPTEMPUNCTATA = Species(
    name="Coccinella septempunctata",
    local_names={
        EN: "seven-spot ladybird, seven-spotted ladybug, C-7",
        PL: "boża krówka, biedronka siedmiokropka",
    },
)
H_AXYRIDIS = Species(
    name="Harmonia axyridis",
    local_names={EN: "harlequin, Asian ladybeetle", PL: "biedronka azjatycka"},
)
L_DECEMLINEATA = Species(
    name="Leptinotarsa decemlineata",
    local_names={EN: "Colorado potato beetle", PL: "stonka ziemniaczana"},
)
S_GRANARIUS = Species(
    name="Sitophilus granarius", local_names={EN: "wheat weevil", PL: "wołek zbożowy"}
)
D_PONDEROSAE = Species(
    name="Dendroctonus ponderosae", local_names={EN: "mountain pine beetle"}
)
I_TYPOGRAPHUS = Species(
    name="Ips typographus",
    local_names={EN: "European spruce bark beetle", PL: "kornik drukarz"},
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
