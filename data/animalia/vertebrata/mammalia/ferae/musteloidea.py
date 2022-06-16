from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN, PL, URL
from image import Image, License

M_MEPHITIS = Species(
    name="Mephitis mephitis",
    local_names={EN: "striped skunk", PL: "skunks zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mephitis_mephitis_Striped_skunk_alerted_Las_Trampas_sm.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Mephitis_mephitis_Striped_skunk_alerted_Las_Trampas_sm.jpg",
        author="Dcrjsr",
        license=License.CC_BY_4_0,
    ),
)
A_FULGENS = Species(
    name="Ailurus fulgens",
    local_names={EN: "red panda, lesser panda", PL: "panda mała, pandka ruda"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ailurus_fulgens_Cerza.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/Ailurus_fulgens_Cerza.JPG",
        author="Gzzz",
        license=License.CC_BY_SA_3_0,
    ),
)
P_LOTOR = Species(
    name="Procyon lotor",
    local_names={EN: "common raccoon", PL: "szop pracz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Procyon_lotor_03(js).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Procyon_lotor_03%28js%29.jpg",
        author="Jerzy Strzelecki",
        license=License.CC_BY_SA_3_0,
    ),
)
M_CAPENSIS = Species(
    name="Mellivora capensis",
    local_names={EN: "honey badger, ratel", PL: "miodożer, ratel miodożerny"},
    known_for=[{EN: "one of the toughest animals"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Honey_badger.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Honey_badger.jpg",
        author="en:User:Jaganath",
        license=License.CC_BY_SA_3_0,
    ),
)
M_MELES = Species(
    name="Meles meles",
    local_names={EN: "European badger", PL: "borsuk europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Meles_meles_(white_background).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Meles_meles_%28white_background%29.png",
        author="Christof Bobzin (Donkey shot)",
        license=License.CC_BY_3_0,
    ),
)
M_FOINA = Species(
    name="Martes foina",
    local_names={EN: "beech marten", PL: "kuna domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Martes_foina_(white_background).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5f/Martes_foina_%28white_background%29.png",
        author="Петроченко Віктор Іванович",
        license=License.CC_BY_SA_4_0,
    ),
)
G_GULO = Species(
    name="Gulo gulo",
    local_names={EN: "wolverine", PL: "rosomak tundrowy"},
    known_for=[
        {
            EN: "Marvel's Wolverine",
            URL: "https://marvel.fandom.com/wiki/James_Howlett_(Earth-616)",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gulo_gulo_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Gulo_gulo_01.jpg",
        author="User:MatthiasKabel",
        license=License.CC_BY_SA_3_0,
    ),
)
M_FURO = Species(
    name="Mustela furo",
    local_names={EN: "ferret", PL: "fretka domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ferret_Frettchen_(142078571).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Ferret_Frettchen_%28142078571%29.jpeg",
        author="Matthias",
        license=License.CC_BY_3_0,
    ),
)
M_ERMINEA = Species(
    name="Mustela erminea",
    local_names={EN: "stoat, Eurasian ermine", PL: "gronostaj europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mustela.erminea.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Mustela.erminea.jpg",
        author="James Lindsey",
        license=License.CC_BY_SA_2_5,
    ),
)
M_NIVALIS = Species(
    name="Mustela nivalis",
    local_names={
        EN: "least weasel, small weasel, common weasel",
        PL: "łasica pospolita",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mustela-nivalis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c9/Mustela-nivalis.jpg",
        author="Սերգեյ Զալինյան",
        license=License.CC_BY_SA_3_0,
    ),
)
M_PUTORIUS = Species(
    name="Mustela putorius",
    local_names={EN: "European polecat", PL: "tchórz zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mustela_putorius_01-cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2e/Mustela_putorius_01-cropped.jpg",
        author="Peter Trimming",
        license=License.CC_BY_2_0,
    ),
)
M_LUTREOLA = Species(
    name="Mustela lutreola",
    local_names={EN: "European mink", PL: "norka europejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:European_Mink_at_Osnabr%C3%BCck_Zoo_02_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/European_Mink_at_Osnabr%C3%BCck_Zoo_02_%28cropped%29.jpg",
        author="zoofanatic",
        license=License.CC_BY_2_0,
    ),
)
L_LUTRA = Species(
    name="Lutra lutra",
    local_names={EN: "European otter, common otter", PL: "wydra europejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fischotter_Lutra_lutra1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Fischotter_Lutra_lutra1.jpg",
        author="Factumquintus",
        license=License.CC_BY_SA_3_0,
    ),
)

MUSTELA_A = Clade(children=[M_FURO, M_PUTORIUS])
MUSTELA_B = Clade(children=[M_LUTREOLA, MUSTELA_A])
MUSTELA_C = Clade(children=[M_NIVALIS, MUSTELA_B])

MEPHITIS = Genus(name="Mephitis", children=[M_MEPHITIS])
AILURUS = Genus(name="Ailurus", children=[A_FULGENS])
PROCYON = Genus(name="Procyon", children=[P_LOTOR])
MELLIVORA = Genus(name="Mellivora", children=[M_CAPENSIS])
MELES = Genus(name="Meles", children=[M_MELES])
MARTES = Genus(name="Martes", children=[M_FOINA])
GULO = Genus(name="Gulo", children=[G_GULO])
MUSTELA = Genus(name="Mustela", children=[M_ERMINEA, MUSTELA_C])
LUTRA = Genus(name="Lutra", children=[L_LUTRA])

MELLIVORINAE = Subfamily(name="Mellivorinae", children=[MELLIVORA])
MELINAE = Subfamily(name="Melinae", children=[MELES])
GULONINAE = Subfamily(name="Guloninae", children=[MARTES, GULO])
MUSTELINAE = Subfamily(name="Mustelinae", children=[MUSTELA])
LUTRINAE = Subfamily(name="Lutrinae", children=[LUTRA])

MUSTELIDAE_A = Clade(children=[MUSTELINAE, LUTRINAE])
MUSTELIDAE_B = Clade(children=[GULONINAE, MUSTELIDAE_A])
MUSTELIDAE_C = Clade(children=[MELINAE, MUSTELIDAE_B])

MEPHITIDAE = Family(name="Mephitidae", children=[MEPHITIS])
AILURIDAE = Family(name="Ailuridae", children=[AILURUS])
PROCYONIDAE = Family(name="Procyonidae", children=[PROCYON])
MUSTELIDAE = Family(name="Mustelidae", children=[MELLIVORINAE, MUSTELIDAE_C])

MUSTELOIDEA_A = Clade(children=[PROCYONIDAE, MUSTELIDAE])
MUSTELOIDEA_B = Clade(children=[AILURIDAE, MUSTELOIDEA_A])

MUSTELOIDEA = Superfamily(name="Musteloidea", children=[MEPHITIDAE, MUSTELOIDEA_B])
