from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Tribe
from constants import EN, PL
from image import Image, License

N_VIVERRINUS = Species(
    name="Nyctereutes viverrinus",
    local_names={EN: "Japanese raccoon dog, tanuki", PL: "jenot wiwerowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tanuki_in_Higashiyama_Zoo_-_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e7/Tanuki_in_Higashiyama_Zoo_-_2.jpg",
        author="KKPCW",
        license=License.CC_BY_SA_4_0,
    ),
)
V_ZERDA = Species(
    name="Vulpes zerda",
    local_names={EN: "fennec fox", PL: "lis pustynny, fenek pustynny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fennec_Fox_Vulpes_zerda.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9f/Fennec_Fox_Vulpes_zerda.jpg",
        author="Drew Avery",
        license=License.CC_BY_2_0,
    ),
)
V_LAGOPUS = Species(
    name="Vulpes lagopus",
    local_names={
        EN: "Arctic fox, white fox, polar fox, snow fox",
        PL: "piesiec, lis polarny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Iceland-1979445_(cropped_3).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Iceland-1979445_%28cropped_3%29.jpg",
        author="Jonathen Pie https://unsplash.com/@r3dmax",
        license=License.CC0,
    ),
)
V_VULPES = Species(
    name="Vulpes vulpes",
    local_names={EN: "red fox", PL: "lis pospolity, lis rudy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vulpes_vulpes_ssp_fulvus_6568074.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Vulpes_vulpes_ssp_fulvus_6568074.jpg",
        author="Joanne Redwood",
        license=License.CC0,
    ),
)
C_BRACHYURUS = Species(
    name="Chrysocyon brachyurus",
    local_names={EN: "maned wolf", PL: "wilk grzywiasty, pampasowiec grzywiasty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chrysocyon_brachyurus_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c2/Chrysocyon_brachyurus_01.jpg",
        author="Rigelus",
        license=License.CC_BY_SA_3_0,
    ),
)
L_PICTUS = Species(
    name="Lycaon pictus",
    local_names={EN: "African wild dog", PL: "likaon pstry"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lycaon_pictus_(Temminck,_1820).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Lycaon_pictus_%28Temminck%2C_1820%29.jpg",
        author="Michael Gäbler",
        license=License.CC_BY_3_0,
    ),
)
C_AUREUS = Species(
    name="Canis aureus",
    local_names={EN: "golden jackal", PL: "szakal złocisty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Golden_Jackal_(_Indian_Jackal)_canis_aureus_indicus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Golden_Jackal_%28_Indian_Jackal%29_canis_aureus_indicus.jpg",
        author="Shino jacob koottanad",
        license=License.CC_BY_SA_4_0,
    ),
)
C_LATRANS = Species(
    name="Canis latrans",
    local_names={EN: "coyote", PL: "wilk preriowy, kojot preriowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:2009-Coyote-Yosemite.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9c/2009-Coyote-Yosemite.jpg",
        author="Yathin S Krishnappa",
        license=License.CC_BY_SA_3_0,
    ),
)
C_LUPUS = Species(
    name="Canis lupus",
    local_names={EN: "grey wolf", PL: "wilk szary"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Canis-lupus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Canis-lupus.jpg",
        author="Սերգեյ Զալինյան",
        license=License.CC_BY_SA_3_0,
    ),
)
C_FAMILIARIS = Species(
    name="Canis familiaris",
    local_names={EN: "domestic dog", PL: "pies domowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Neo_The_Chosen_Pug.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Neo_The_Chosen_Pug.jpg",
        author="Renexist",
        license=License.CC_BY_SA_4_0,
    ),
)

VULPES_A = Clade(children=[V_LAGOPUS, V_VULPES])

CANINA_A = Clade(children=[C_LUPUS, C_FAMILIARIS])
CANINA_B = Clade(children=[C_LATRANS, CANINA_A])

NYCTEREUTES = Genus(name="Nyctereutes", children=[N_VIVERRINUS])
VULPES = Genus(name="Vulpes", children=[V_ZERDA, VULPES_A])
CHRYSOCYON = Genus(name="Chrysocyon", children=[C_BRACHYURUS])
LYCAON = Genus(name="Lycaon", children=[L_PICTUS])
CANIS = Genus(name="Canis", children=[C_AUREUS, CANINA_B])

CERDOCYONINA = Subtribe(name="Cerdocyonina", children=[CHRYSOCYON])
CANINA = Subtribe(name="Canina", children=[LYCAON, CANIS])

VULPINI = Tribe(name="Vulpini", children=[NYCTEREUTES, VULPES])
CANINI = Tribe(name="Canini", children=[CERDOCYONINA, CANINA])

CANINAE = Subfamily(name="Caninae", children=[VULPINI, CANINI])

CANIDAE = Family(name="Canidae", children=[CANINAE])
