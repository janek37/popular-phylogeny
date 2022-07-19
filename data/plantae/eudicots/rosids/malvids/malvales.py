from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

O_PYRAMIDALE = Species(
    name="Ochroma pyramidale",
    local_names={EN: "balsa tree", PL: "balsa, ogorzałka wełnista"},
    known_for=[
        {
            EN: "balsa wood",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Balsa_Wood_Texture.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Balsa_Wood_Texture.jpg",
                author="Joseph Francis",
                license=License.CC_BY_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ochroma_pyramidale_Costa_Rica_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Ochroma_pyramidale_Costa_Rica_2.jpg",
        author="Gabriele Kothe-Heinrich",
        license=License.CC_BY_SA_3_0,
    ),
)
T_EUROPAEA = Species(
    name="Tilia × europaea",
    local_names={EN: "common lime, common linden", PL: "lipa holenderska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tilia_x_europea-2.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/85/Tilia_x_europea-2.JPG",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)
T_CACAO = Species(
    name="Theobroma cacao",
    local_names={EN: "cacao/cocoa tree", PL: "kakaowiec właściwy"},
    known_for=[
        {
            EN: "cocoa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cocoa_Spelled_Out_in_Cocoa_Powder.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Cocoa_Spelled_Out_in_Cocoa_Powder.jpg",
                author="formulatehealth",
                license=License.CC_BY_2_0,
            ),
        },
        {
            EN: "chocolate",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Chocolate_(blue_background).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Chocolate_%28blue_background%29.jpg",
                author="nagualdesign",
                license=License.CC_BY_SA_3_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cacao_Tree_-_Theobroma_cacao_-_panoramio.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/48/Cacao_Tree_-_Theobroma_cacao_-_panoramio.jpg",
        author="Björn S.",
        license=License.CC_BY_SA_3_0,
    ),
)
C_ACUMINATA = Species(
    name="Cola acuminata",
    local_names={PL: "kola zaostrzona"},
    known_for=[
        {
            EN: "kola nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Kolanuts.jpeg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/48/Kolanuts.jpeg",
                author="Azekhoria benjamin",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cola_acuminata-masc-fem.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Cola_acuminata-masc-fem.jpg",
        author="M. A. P. Accardo Filho",
        license=License.CC_BY_SA_3_0,
    ),
)
M_SYLVESTRIS = Species(
    name="Malva sylvestris",
    local_names={PL: "ślaz dziki", EN: "common mallow"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mallow_January_2008-1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Mallow_January_2008-1.jpg",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)
H_SABDARIFFA = Species(
    name="Hibiscus sabdariffa",
    local_names={EN: "roselle", PL: "ketmia szczawiowa"},
    known_for=[
        {
            EN: "hibiscus tea",
            PL: "herbata z hibiskusa (częsta baza herbat owocowych)",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Hibiscus_tea.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/3c/Hibiscus_tea.jpg",
                author="Emna Mizouni",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hibiscus_sabdariffa_kz01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Hibiscus_sabdariffa_kz01.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
A_ROSEA = Species(
    name="Alcea rosea",
    local_names={EN: "common hollyhock", PL: "malwa różowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Alcea_rosea_131902114.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0d/Alcea_rosea_131902114.jpg",
        author="librarianlea",
        license=License.CC_BY_SA_4_0,
    ),
)
A_DIGITATA = Species(
    name="Adansonia digitata",
    local_names={EN: "African baobab", PL: "baobab afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Baobab_and_elephant,_Tanzania.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Baobab_and_elephant%2C_Tanzania.jpg",
        author="Ferdinand Reus from Arnhem, Holland",
        license=License.CC_BY_SA_2_0,
    ),
)
G_HIRSUTUM = Species(
    name="Gossypium hirsutum",
    local_names={EN: "upland cotton", PL: "bawełna kosmata"},
    known_for=[{EN: "95% of all cotton production"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kappus_(Konkani-_%E0%A4%95%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%AA%E0%A5%81%E0%A4%B8)_(3538039119).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f0/Kappus_%28Konkani-_%E0%A4%95%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%AA%E0%A5%81%E0%A4%B8%29_%283538039119%29.jpg",
        author="Dinesh Valke from Thane, India",
        license=License.CC_BY_SA_2_0,
    ),
)
D_ZIBETHINUS = Species(
    name="Durio zibethinus",
    local_names={EN: "durian", PL: "durian właściwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Durio_zibethinus_(6980662120).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Durio_zibethinus_%286980662120%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
A_OFFICINALIS = Species(
    name="Althaea officinalis",
    local_names={EN: "marsh mallow", PL: "prawoślaz lekarski"},
    known_for=[{EN: "archetype of modern marshmallows"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Althaea_officinalis_Prawo%C5%9Blaz_lekarski_2019-08-09_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Althaea_officinalis_Prawo%C5%9Blaz_lekarski_2019-08-09_03.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
C_OLITORIUS = Species(
    name="Corchorus olitorius",
    local_names={EN: "jute mallow, nalta jute", PL: "juta warzywna"},
    known_for=[
        {
            EN: "jute fiber",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Yute_-_Sacos.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Yute_-_Sacos.jpg",
                author="Tamorlan",
                license=License.CC_BY_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%22Arya%22_molokhia_Corchorus_olitorius_Pilangsari_2019_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/%22Arya%22_molokhia_Corchorus_olitorius_Pilangsari_2019_3.jpg",
        author="Aris riyanto",
        license=License.CC_BY_SA_4_0,
    ),
)

OCHROMA = Genus(name="Ochroma", children=[O_PYRAMIDALE])
TILIA = Genus(name="Tilia", children=[T_EUROPAEA])
THEOBROMA = Genus(name="Theobroma", children=[T_CACAO])
COLA = Genus(name="Cola", children=[C_ACUMINATA])
MALVA = Genus(name="Malva", children=[M_SYLVESTRIS])
HIBISCUS = Genus(name="Hibiscus", children=[H_SABDARIFFA])
ALCEA = Genus(name="Alcea", children=[A_ROSEA])
ADANSONIA = Genus(name="Adansonia", children=[A_DIGITATA])
GOSSYPIUM = Genus(name="Gossypium", children=[G_HIRSUTUM])
DURIO = Genus(name="Durio", children=[D_ZIBETHINUS])
ALTHAEA = Genus(name="Althaea", children=[A_OFFICINALIS])
CORCHORUS = Genus(name="Corchorus", children=[C_OLITORIUS])

# https://www.semanticscholar.org/paper/Systematics-ofLavatera-andMalva-(Malvaceae%2C-new-Ray/798729552b867e7dcbe84471d3161ba731442bfe
MALVEAE_A = Clade(children=[ALCEA, ALTHAEA])

MALVEAE = Tribe(name="Malveae", children=[MALVA, MALVEAE_A])
HIBISCEAE = Tribe(name="Hibisceae", children=[HIBISCUS])
GOSSYPIEAE = Tribe(name="Gossypieae", children=[GOSSYPIUM])
DURIONEAE = Tribe(name="Durioneae", children=[DURIO])

BOMBACOIDEAE = Subfamily(name="Bombacoideae", children=[OCHROMA, ADANSONIA])
TILIOIDEAE = Subfamily(name="Tilioideae", children=[TILIA])
BYTTNERIOIDEAE = Subfamily(name="Byttnerioideae", children=[THEOBROMA])
STERCULIOIDEAE = Subfamily(name="Sterculioideae", children=[COLA])
MALVOIDEAE = Subfamily(name="Malvoideae", children=[MALVEAE, HIBISCEAE, GOSSYPIEAE])
HELICTEROIDEAE = Subfamily(name="Helicteroideae", children=[DURIONEAE])
GREWIOIDEAE = Subfamily(name="Grewioideae", children=[CORCHORUS])

MALVOIDEAE_BOMBACOIDEAE = Clade(children=[MALVOIDEAE, BOMBACOIDEAE])
MALVACEAE_A = Clade(
    children=[MALVOIDEAE_BOMBACOIDEAE, TILIOIDEAE, STERCULIOIDEAE, HELICTEROIDEAE]
)
BYTTNERIOIDEAE_GREWIOIDEAE = Clade(children=[BYTTNERIOIDEAE, GREWIOIDEAE])

MALVACEAE = Family(name="Malvaceae", children=[MALVACEAE_A, BYTTNERIOIDEAE_GREWIOIDEAE])

MALVALES = Order(name="Malvales", children=[MALVACEAE])
