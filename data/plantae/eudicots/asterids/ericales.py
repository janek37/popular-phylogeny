from clade import Clade, Family, Genus, Order, Species, Subfamily, Subgenus, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

B_EXCELSA = Species(
    name="Bertholletia excelsa",
    local_names={EN: "Brazil nut", PL: "orzesznica brazylijska, orzesznica wyniosła"},
    known_for=[
        {
            PL: "orzechy brazylijskie",
            EN: "edible nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Bertholletia_excelsa_seeds_closeup.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Bertholletia_excelsa_seeds_closeup.jpg",
                author="רנדום",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:COCO_DE_CASTA%C3%91A_(BERTHOLLETIA_EXCELSA).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/COCO_DE_CASTA%C3%91A_%28BERTHOLLETIA_EXCELSA%29.jpg",
        author="Miguel Jorge Villavicencio Oliva",
        license=License.CC_BY_SA_4_0,
    ),
)
D_EBENUM = Species(
    name="Diospyros ebenum",
    local_names={EN: "Ceylon ebony", PL: "hebanowe drzewo, hurma hebanowa"},
    known_for=[
        {
            EN: "ebony, black wood",
            PL: "heban",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Diospyros_ebenum_09082017.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Diospyros_ebenum_09082017.jpg",
                author="Philg88",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kaluwara-Diospyros_ebenum-Sri_Lanka_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/Kaluwara-Diospyros_ebenum-Sri_Lanka_%282%29.jpg",
        author="Ji-Elle",
        license=License.CC_BY_SA_3_0,
    ),
)
D_KAKI = Species(
    name="Diospyros kaki",
    local_names={EN: "Oriental persimmon", PL: "heban wiśniówka, hurma wschodnia"},
    known_for=[
        {
            EN: "kaki fruit",
            PL: "owoc kaki",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Fuyu_Persimmon_(Diospyros_Kaki).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Fuyu_Persimmon_%28Diospyros_Kaki%29.jpg",
                author="Joe Ravi",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Diospyros_kaki_-_persimmon_at_Paro_during_LGFC_-_Bhutan_2019_(3).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Diospyros_kaki_-_persimmon_at_Paro_during_LGFC_-_Bhutan_2019_%283%29.jpg",
        author="Vinayaraj",
        license=License.CC_BY_SA_4_0,
    ),
)
P_VULGARIS = Species(
    name="Primula vulgaris",
    local_names={EN: "common primrose", PL: "pierwiosnek bezłodygowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Primula_acaulis_subsp._acaulis_(%C3%87uha_%C3%A7i%C3%A7e%C4%9Fi)_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Primula_acaulis_subsp._acaulis_%28%C3%87uha_%C3%A7i%C3%A7e%C4%9Fi%29_03.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
C_SINENSIS = Species(
    name="Camellia sinensis",
    local_names={EN: "tea plant", PL: "herbata chińska"},
    known_for=[
        {
            EN: "tea",
            PL: "herbata",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Leaves_of_green_tea.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Leaves_of_green_tea.jpg",
                author="Editor at Large",
                license=License.CC_BY_SA_2_5,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Camellia_sinensis_Bois_Cheri.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Camellia_sinensis_Bois_Cheri.jpg",
        author="Pancrat",
        license=License.CC_BY_SA_3_0,
    ),
)
C_JAPONICA = Species(
    name="Camellia japonica",
    local_names={EN: "common camellia", PL: "kamelia japońska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Camellia_Japonica_L.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2a/Camellia_Japonica_L.jpg",
        author="Bongsun",
        license=License.CC_BY_SA_3_0,
    ),
)
S_RUBRA = Species(
    name="Sarracenia rubra",
    local_names={EN: "sweet pitcherplant", PL: "kapturnica"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sarraceniaceae_Sarracenia_rubra_gulfensis_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Sarraceniaceae_Sarracenia_rubra_gulfensis_1.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
A_DELICIOSA = Species(
    name="Actinidia deliciosa",
    local_names={EN: "fuzzy kiwifruit", PL: "aktinidia smakowita"},
    known_for=[
        {
            PL: "owoce kiwi",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Kiwifruit-Actinidia_deliciosa_half.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/ae/Kiwifruit-Actinidia_deliciosa_half.jpg",
                author="Thomas N. aka Karpour",
                license=License.CC_BY_SA_2_0_DE,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Actinidia_deliciosa_Kiwi_Fruit_%E1%83%99%E1%83%98%E1%83%95%E1%83%98.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Actinidia_deliciosa_Kiwi_Fruit_%E1%83%99%E1%83%98%E1%83%95%E1%83%98.JPG",
        author="Lazaregagnidze",
        license=License.CC_BY_SA_3_0,
    ),
)
C_VULGARIS = Species(
    name="Calluna vulgaris",
    local_names={EN: "common heather", PL: "wrzos zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Calluna_vulgaris_-_Heather_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/23/Calluna_vulgaris_-_Heather_01.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
V_VITIS_IDAEA = Species(
    name="Vaccinium vitis-idaea",
    local_names={EN: "lingonberry, cowberry", PL: "borówka brusznica"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vaccinium_vitis-idaea_20060824_003.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Vaccinium_vitis-idaea_20060824_003.jpg",
        author="Jonas Bergsten",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
V_OXYCOCCOS = Species(
    name="Vaccinium oxycoccos",
    local_names={EN: "small/common cranberry", PL: "żurawina błotna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:VACCINIUM_OXYCOCCOS._(1).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/01/VACCINIUM_OXYCOCCOS._%281%29.jpg",
        author="Espirat",
        license=License.CC_BY_SA_4_0,
    ),
)
V_MACROCARPON = Species(
    name="Vaccinium macrocarpon",
    local_names={EN: "large/American cranberry", PL: "żurawina wielkoowocowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vaccinium_macrocarpon_(15054125499).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Vaccinium_macrocarpon_%2815054125499%29.jpg",
        author="Kristine Paulus",
        license=License.CC_BY_2_0,
    ),
)
V_MYRTILLUS = Species(
    name="Vaccinium myrtillus",
    local_names={
        EN: "European blueberry, bilberry",
        PL: "czarna jagoda, czernica, borówka czarna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vaccinium_myrtillus_30999834.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Vaccinium_myrtillus_30999834.jpg",
        author="Татьяна Прозорова",
        license=License.CC0,
    ),
)
V_CORYMBOSUM = Species(
    name="Vaccinium corymbosum",
    local_names={
        EN: "northern highbush blueberry",
        PL: "borówka amerykańska, borówka wysoka",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vaccinium_corymbosum_in_The_Netherlands.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/Vaccinium_corymbosum_in_The_Netherlands.jpg",
        author="Rasbak at Dutch Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
R_CATAWBIENSE = Species(
    name="Rhododendron catawbiense",
    local_names={
        PL: "rododendron, różanecznik katawbijski",
        EN: "Catawba rosebay, Catawba rhododendron",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhododendron_%27Nova_Zembla%27_r1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Rhododendron_%27Nova_Zembla%27_r1.jpg",
        author="Jerzy Opioła",
        license=License.CC_BY_SA_3_0,
    ),
)
R_LUTEUM = Species(
    name="Rhododendron luteum",
    local_names={
        PL: "azalia pontyjska, różanecznik żółty",
        EN: "yellow azalea, honeysuckle azalea",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhododendron_luteum_100.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Rhododendron_luteum_100.JPG",
        author="Kor!An (Андрей Корзун)",
        license=License.CC_BY_SA_3_0,
    ),
)

# possibly vitis-idaea should be closest to macrocarpon? conflicting data
VACCINIUM_SUBGENUS_OXYCOCCUS = Subgenus(
    name="Vaccinium subg. Oxycoccus", children=[V_OXYCOCCOS, V_MACROCARPON]
)
VACCINIUM_SUBGENUS_VACCINIUM = Subgenus(
    name="Vaccinium subg. Vaccinium",
    children=[V_VITIS_IDAEA, V_MYRTILLUS, V_CORYMBOSUM],
)

BERTHOLLETIA = Genus(name="Bertholletia", children=[B_EXCELSA])
DIOSPYROS = Genus(name="Diospyros", children=[D_EBENUM, D_KAKI])
PRIMULA = Genus(name="Primula", children=[P_VULGARIS])
CAMELLIA = Genus(name="Camellia", children=[C_SINENSIS, C_JAPONICA])
SARRACENIA = Genus(name="Sarracenia", children=[S_RUBRA])
ACTINIDIA = Genus(name="Actinidia", children=[A_DELICIOSA])
CALLUNA = Genus(name="Calluna", children=[C_VULGARIS])
VACCINIUM = Genus(
    name="Vaccinium",
    children=[VACCINIUM_SUBGENUS_VACCINIUM, VACCINIUM_SUBGENUS_OXYCOCCUS],
)
RHODODENDRON = Genus(name="Rhododendron", children=[R_CATAWBIENSE, R_LUTEUM])

ERICEAE = Tribe(name="Ericeae", children=[CALLUNA])
VACCINIEAE = Tribe(name="Vaccinieae", children=[VACCINIUM])
RHODOREAE = Tribe(name="Rhodoreae", children=[RHODODENDRON])

LECYTHIDOIDEAE = Subfamily(name="Lecythidoideae", children=[BERTHOLLETIA])
PRIMULOIDEAE = Subfamily(name="Primuloideae", children=[PRIMULA])
ERICOIDEAE = Subfamily(name="Ericoideae", children=[ERICEAE, RHODOREAE])
VACCINIOIDEAE = Subfamily(name="Vaccinioideae", children=[VACCINIEAE])

LECYTHIDACEAE = Family(name="Lecythidaceae", children=[LECYTHIDOIDEAE])
EBANACEAE = Family(name="Ebanaceae", children=[DIOSPYROS])
PRIMULACEAE = Family(name="Primulaceae", children=[PRIMULOIDEAE])
THEACEAE = Family(name="Theaceae", children=[CAMELLIA])
SARRACENIACEAE = Family(name="Sarraceniaceae", children=[SARRACENIA])
ACTINIDIACEAE = Family(name="Actinidiaceae", children=[ACTINIDIA])
ERICACEAE = Family(name="Ericaceae", children=[ERICOIDEAE, VACCINIOIDEAE])

PRIMULOIDS = Clade(name="primuloids", children=[EBANACEAE, PRIMULACEAE])
SARRACENIOIDS = Clade(name="sarracenioids", children=[SARRACENIACEAE, ACTINIDIACEAE])

ERICALES_A = Clade(children=[ERICACEAE, SARRACENIOIDS])
ERICALES_B = Clade(children=[ERICALES_A, THEACEAE])
ERICALES_C = Clade(children=[ERICALES_B, PRIMULOIDS])

ERICALES = Order(name="Ericales", children=[LECYTHIDACEAE, ERICALES_C])
