from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, IMAGE, PL, URL
from image import Image, License

C_HABESSINICA = Species(
    name="Commiphora habessinica",
    local_names={EN: "Abyssinian myrrh", PL: "balsamowiec mirra"},
    known_for=[
        {
            EN: "myrrh",
            PL: "mirra",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Myrrhe.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Myrrhe.jpg",
                author="GeoTrinity",
                license=License.CC_BY_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Commiphora_myrrha_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-019.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Commiphora_myrrha_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-019.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_OCCIDENTALE = Species(
    name="Anacardium occidentale",
    local_names={EN: "cashew", PL: "nerkowiec, nanercz zachodni"},
    known_for=[
        {
            EN: "cashew nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:A_closeup_of_cashew_nut.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/ea/A_closeup_of_cashew_nut.JPG",
                author="Thamizhpparithi Maari",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anacardium_occidentale--_Cashew_apple_and_nut_(30853573405).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/39/Anacardium_occidentale--_Cashew_apple_and_nut_%2830853573405%29.jpg",
        author="Dick Culbert from Gibsons, B.C., Canada",
        license=License.CC_BY_2_0,
    ),
)
M_INDICA = Species(
    name="Mangifera indica",
    local_names={EN: "mango", PL: "mango indyjskie"},
    known_for=[
        {
            EN: "edible fruit",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Mangos_-_single_and_halved.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/Mangos_-_single_and_halved.jpg",
                author="Ivar Leidus",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mangifera_indica_(2463006073).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/da/Mangifera_indica_%282463006073%29.jpg",
        author="Dinesh Valke from Thane, India",
        license=License.CC_BY_SA_2_0,
    ),
)
S_MOLLE = Species(
    name="Schinus molle",
    local_names={EN: "Peruvian pepper tree", PL: "schinus peruwiański"},
    known_for=[
        {
            EN: "pink peppercorn",
            PL: "pieprz czerwony",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pink_Peppercorns_-_Schinus_molle.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Pink_Peppercorns_-_Schinus_molle.jpg",
                author="Netherzone",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schinus_Molle.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Schinus_Molle.jpg",
        author="Squeezeweasel at en.wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
P_VERA = Species(
    name="Pistacia vera",
    local_names={EN: "pistacchio", PL: "pistacja właściwa"},
    known_for=[
        {
            EN: "pistacchio nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pistacchio_di_Bronte_appena_raccolto.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/23/Pistacchio_di_Bronte_appena_raccolto.jpg",
                author="Fabio Ingrosso from Italy",
                license=License.CC_BY_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pistacchio_di_Bronte.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a8/Pistacchio_di_Bronte.jpg",
        author="Paolo Galli",
        license=License.CC_BY_SA_3_0,
    ),
)
T_RADICANS = Species(
    name="Toxicodendron radicans",
    local_names={EN: "(eastern) poison ivy", PL: "trujący bluszcz, sumak pnący"},
    known_for=[
        {
            EN: "Poison Ivy from Batman franchise",
            URL: "https://batman.fandom.com/wiki/Poison_Ivy",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Toxicodendron_radicans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Toxicodendron_radicans.jpg",
        author="Esculapio",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
R_TYPHINA = Species(
    name="Rhus typhina",
    local_names={EN: "staghorn sumac", PL: "sumak octowiec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Korina_2011-07-04_Rhus_typhina_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Korina_2011-07-04_Rhus_typhina_2.jpg",
        author="Katrin Schneider / korina.info",
        license=License.CC_BY_SA_4_0,
    ),
)
A_HIPPOCASTANUM = Species(
    name="Aesculus hippocastanum",
    local_names={EN: "horse chestnut", PL: "kasztanowiec pospolity"},
    known_for=[
        {
            EN: "conkers",
            PL: "kasztany",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Aesculus_hippocastanum_fruit.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/14/Aesculus_hippocastanum_fruit.jpg",
                author="Solipsist",
                license=License.CC_BY_SA_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aesculus_hippocastanum_flowers_in_Lakewood_Ohio.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Aesculus_hippocastanum_flowers_in_Lakewood_Ohio.jpg",
        author="Fiachmara",
        license=License.CC_BY_SA_4_0,
    ),
)
A_PSEUDOPLATANUS = Species(
    name="Acer pseudoplatanus",
    local_names={EN: "sycamore", PL: "klon jawor"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acer_pseudoplatanus_3_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5a/Acer_pseudoplatanus_3_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
A_PLATANOIDES = Species(
    name="Acer platanoides",
    local_names={EN: "Norway maple", PL: "klon zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Spitz-Ahorn(mbo).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Spitz-Ahorn%28mbo%29.jpg",
        author="Martin Bobka (= Martin120)",
        license=License.CC_BY_SA_2_5,
    ),
)
A_SACCHARUM = Species(
    name="Acer saccharum",
    local_names={EN: "sugar mapple", PL: "klon cukrowy"},
    known_for=[
        {
            EN: "maple syrup",
            PL: "syrop klonowy",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Maple_syrup.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Maple_syrup.jpg",
                author="User:Miguel Andrade",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acer_saccharum_1-jgreenlee_(5098070608).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Acer_saccharum_1-jgreenlee_%285098070608%29.jpg",
        author="Superior National Forest",
        license=License.CC_BY_2_0,
    ),
)
L_CHINENSIS = Species(
    name="Litchi chinensis",
    local_names={EN: "lychee", PL: "liczi chińskie"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Litchi_chinensis_fruits.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Litchi_chinensis_fruits.JPG",
        author="B.navez",
        license=License.CC_BY_SA_3_0,
    ),
)
P_CUPANA = Species(
    name="Paullinia cupana",
    local_names={EN: "guaraná", PL: "paulinia guarana"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Guaran%C3%A1_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Guaran%C3%A1_02.jpg",
        author="AnitaFortis",
        license=License.CC_BY_SA_3_0,
    ),
)
C_SINENSIS = Species(
    name="Citrus × sinensis",
    local_names={EN: "sweet orange", PL: "pomarańcza chińska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:OrangeBloss_wb.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/OrangeBloss_wb.jpg",
        author="Ellen Levy Finch (Elf)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_LIMON = Species(
    name="Citrus limon",
    local_names={EN: "lemon", PL: "cytryna zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:P1030323.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/P1030323.JPG",
        author="Elena Chochkova",
        license=License.CC_BY_SA_4_0,
    ),
)
C_PARADISI = Species(
    name="Citrus × paradisi",
    local_names={EN: "grapefruit", PL: "grejpfrut"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trauttmansdorff_gardens_-_Citrus_x_paradisi_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Trauttmansdorff_gardens_-_Citrus_x_paradisi_01.JPG",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
C_MAXIMA = Species(
    name="Citrus maxima",
    local_names={EN: "pomelo", PL: "pomelo, pomarańcza olbrzymia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrus_maxima_-_Shaddock,_Adana_2017-11-12_01-5.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Citrus_maxima_-_Shaddock%2C_Adana_2017-11-12_01-5.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
C_AURANTIIFOLIA = Species(
    name="Citrus × aurantiifolia",
    local_names={EN: "key lime", PL: "limonka, limetka, lima"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrus_aurantiifolia_by_Kadavoor.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Citrus_aurantiifolia_by_Kadavoor.jpg",
        author="Jeevan Jose, Kerala, India",
        license=License.CC_BY_SA_4_0,
    ),
)
C_RETICULATA = Species(
    name="Citrus reticulata",
    local_names={EN: "mandarin orange", PL: "mandarynka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrus_reticulata_April_2013_Nordbaden.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/10/Citrus_reticulata_April_2013_Nordbaden.JPG",
        author="4028mdk09",
        license=License.CC_BY_SA_3_0,
    ),
)
C_TANGERINA = Species(
    name="Citrus x tangerina",
    local_names={EN: "tangerine", PL: "mandarynka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:TangerineFruit.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2a/TangerineFruit.jpg",
        author="Barfooz (Brent Ramerth)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CLEMENTINA = Species(
    name="Citrus × clementina",
    local_names={EN: "clementine", PL: "klementynka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrus_Clementina_-_panoramio.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6c/Citrus_Clementina_-_panoramio.jpg",
        author="fotogoocom",
        license=License.CC_BY_3_0,
    ),
)
C_JAPONICA = Species(
    name="Citrus japonica",
    local_names={EN: "kumquat", PL: "kumkwat"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrus_japonica_%27Centennial_Variegated%27_-_Kumquat_-_fruit.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8a/Citrus_japonica_%27Centennial_Variegated%27_-_Kumquat_-_fruit.jpg",
        author="James Steakley",
        license=License.CC_BY_SA_3_0,
    ),
)
Z_BUNGEANUM = Species(
    name="Zanthoxylum bungeanum",
    local_names={
        EN: "Sichuan/Szechuan pepper",
        PL: "pieprz syczuanski, żółtodrzew Bungego",
    },
    known_for=[
        {
            EN: "Szechuan sauce",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:McDonalds_Szechuan_Sauce_2018.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/McDonalds_Szechuan_Sauce_2018.jpg",
                author="RightCowLeftCoast",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zanthoxylum_simulans_kz1.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/Zanthoxylum_simulans_kz1.JPG",
        author="Kenraiz",
        license=License.CC_BY_SA_3_0,
    ),
)
R_GRAVEOLENS = Species(
    name="Ruta graveolens",
    local_names={EN: "common rue, herb-of-grace", PL: "ruta zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ruta_graveolens_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-259.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3d/Ruta_graveolens_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-259.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

ACER_SECTION_ACER = Clade(
    name="Acer sect. Acer", children=[A_PSEUDOPLATANUS, A_SACCHARUM]
)  # Section

CORE_CITRUSES = Clade(
    children=[
        C_SINENSIS,
        C_LIMON,
        C_PARADISI,
        C_MAXIMA,
        C_AURANTIIFOLIA,
        C_RETICULATA,
        C_TANGERINA,
        C_CLEMENTINA,
        C_JAPONICA,
    ]
)

COMMIPHORA = Genus(name="Commiphora", children=[C_HABESSINICA])
ANACARDIUM = Genus(name="Anacardium", children=[A_OCCIDENTALE])
MANGIFERA = Genus(name="Mangifera", children=[M_INDICA])
SCHINUS = Genus(name="Schinus", children=[S_MOLLE])
PISTACIA = Genus(name="Pistacia", children=[P_VERA])
TOXICODENDRON = Genus(name="Toxicodendron", children=[T_RADICANS])
RHUS = Genus(name="Rhus", children=[R_TYPHINA])
AESCULUS = Genus(name="Aesculus", children=[A_HIPPOCASTANUM])
ACER = Genus(name="Acer", children=[ACER_SECTION_ACER, A_PLATANOIDES])
LITCHI = Genus(name="Litchi", children=[L_CHINENSIS])
PAULINIA = Genus(name="Paulinia", children=[P_CUPANA])
CITRUS = Genus(name="Citrus", children=[CORE_CITRUSES, C_JAPONICA])
ZANTHOXYLUM = Genus(name="Zanthoxylum", children=[Z_BUNGEANUM])
RUTA = Genus(name="Ruta", children=[R_GRAVEOLENS])

# https://www.researchgate.net/publication/323561612_Anacardiaceae_Phylogeny_Poster_2018
ANACORDIOIDEAE_A = Clade(children=[ANACARDIUM, MANGIFERA])
ANACORDIOIDEAE_D = Clade(children=[PISTACIA, RHUS])
ANACORDIOIDEAE_B = Clade(children=[TOXICODENDRON, ANACORDIOIDEAE_D])
ANACORDIOIDEAE_C = Clade(children=[ANACORDIOIDEAE_B, SCHINUS])

ANACARDIOIDEAE = Subfamily(
    name="Anacardioideae", children=[ANACORDIOIDEAE_A, ANACORDIOIDEAE_C]
)
HIPPOCASTANOIDEAE = Subfamily(name="Hippocastanoideae", children=[AESCULUS, ACER])
SAPINDOIDEAE = Subfamily(name="Sapindoideae", children=[LITCHI, PAULINIA])
AURANTIOIDEAE = Subfamily(name="Aurantioideae", children=[CITRUS])
ZANTHOXYLOIDEAE = Subfamily(name="Zanthoxyloideae", children=[ZANTHOXYLUM])
RUTOIDEAE = Subfamily(name="Rutoideae", children=[RUTA])

RUTACEAE_A = Clade(children=[AURANTIOIDEAE, RUTOIDEAE])

BURSERACEAE = Family(name="Burseraceae", children=[COMMIPHORA])
ANACARDIACEAE = Family(name="Anacardiaceae", children=[ANACARDIOIDEAE])
SAPINDACEAE = Family(name="Sapindaceae", children=[HIPPOCASTANOIDEAE, SAPINDOIDEAE])
RUTACEAE = Family(name="Rutaceae", children=[RUTACEAE_A, ZANTHOXYLOIDEAE])

# https://www.researchgate.net/publication/311503129_An_Expanded_Nuclear_Phylogenomic_PCR_Toolkit_for_Sapindales
SAPINDALES_A = Clade(children=[BURSERACEAE, ANACARDIACEAE])
SAPINDALES_B = Clade(children=[SAPINDACEAE, RUTACEAE])

SAPINDALES = Order(name="Sapindales", children=[SAPINDALES_A, SAPINDALES_B])
