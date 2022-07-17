from clade import Clade, Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL
from image import Image, License

S_AUCUPARIA = Species(
    name="Sorbus aucuparia",
    local_names={EN: "rowan, mountain-ash", PL: "jarzębina, jarząb pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20130921Sorbus_aucuparia1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/20130921Sorbus_aucuparia1.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
A_MELANOCARPA = Species(
    name="Aronia melanocarpa",
    local_names={EN: "black chokeberry", PL: "aronia czarna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aronia_melanocarpa_cv_Rubina_P1020524.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Aronia_melanocarpa_cv_Rubina_P1020524.JPG",
        author="manfred.sause@volloeko.de",
        license=License.CC_BY_SA_3_0,
    ),
)
M_DOMESTICA = Species(
    name="Malus domestica",
    local_names={EN: "apple tree", PL: "jabłoń domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Malus_domestica_unriped_fruit.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Malus_domestica_unriped_fruit.jpg",
        author="Dinnye",
        license=License.CC_BY_SA_3_0,
    ),
)
M_SYLVESTRIS = Species(
    name="Malus sylvestris",
    local_names={EN: "European crab apple", PL: "jabłoń dzika"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Malus_sylvestris_(Crab-apple),_July,_Stewarton,_East_Ayrshire,_Scotland.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Malus_sylvestris_%28Crab-apple%29%2C_July%2C_Stewarton%2C_East_Ayrshire%2C_Scotland.jpg",
        author="Rosser1954",
        license=License.CC_BY_SA_4_0,
    ),
)
P_COMMUNIS = Species(
    name="Pyrus communis",
    local_names={EN: "common pear", PL: "grusza pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pyrus_communis._Peral.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fd/Pyrus_communis._Peral.jpg",
        author="SABENCIA Bertu Ordiales",
        license=License.CC_BY_SA_4_0,
    ),
)
C_MONOGYNA = Species(
    name="Crataegus monogyna",
    local_names={EN: "common hawthorn", PL: "głóg jednoszyjkowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crataegus_monogyna_G%C5%82%C3%B3g_jednoszyjkowy_2020-10-25_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Crataegus_monogyna_G%C5%82%C3%B3g_jednoszyjkowy_2020-10-25_01.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
P_DOMESTICA = Species(
    name="Prunus domestica",
    local_names={EN: "European plum", PL: "śliwa domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prunus_domestica_105047037.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Prunus_domestica_105047037.jpg",
        author="Kai Löhr",
        license=License.CC_BY_4_0,
    ),
)
P_AVIUM = Species(
    name="Prunus avium",
    local_names={EN: "wild cherry, sweet cherry", PL: "czereśnia, wiśnia ptasia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nature_forest_wild_cherry_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Nature_forest_wild_cherry_02.jpg",
        author="Jan Helebrant",
        license=License.CC0,
    ),
)
P_CERASUS = Species(
    name="Prunus cerasus",
    local_names={EN: "sour cherry", PL: "wiśnia pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sauerkirschenfrucht_Prunus_cerasus_2.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2d/Sauerkirschenfrucht_Prunus_cerasus_2.JPG",
        author="böhringer friedrich",
        license=License.CC_BY_SA_2_5,
    ),
)
P_PERSICA = Species(
    name="Prunus persica",
    local_names={EN: "peach", PL: "brzoskwinia zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prunus_persica_-_Peach_Hungary.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Prunus_persica_-_Peach_Hungary.jpg",
        author="Takkk",
        license=License.CC_BY_SA_3_0,
    ),
)
P_ARMENIACA = Species(
    name="Prunus armeniaca",
    local_names={EN: "common apricot", PL: "morela pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ripened_Apricot_Fruit_(Prunus_armeniaca).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Ripened_Apricot_Fruit_%28Prunus_armeniaca%29.jpg",
        author="Rehmat Alam",
        license=License.CC_BY_SA_3_0,
    ),
)
P_AMYGDALUS = Species(
    name="Prunus amygdalus",
    local_names={EN: "almond", PL: "migdał, migdałowiec pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prunus_dulcis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-250.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/Prunus_dulcis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-250.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_SPINOSA = Species(
    name="Prunus spinosa",
    local_names={EN: "blackthorn", PL: "śliwa tarnina"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Steinfr%C3%BCchte_des_Schlehdorns,_Prunus_spinosa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Steinfr%C3%BCchte_des_Schlehdorns%2C_Prunus_spinosa.jpg",
        author="Georg Buzin",
        license=License.CC_BY_SA_4_0,
    ),
)
C_OBLONGA = Species(
    name="Cydonia oblonga",
    local_names={EN: "quince", PL: "pigwa pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Illustration_Cydonia_oblonga0_-_clean.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/75/Illustration_Cydonia_oblonga0_-_clean.jpg",
        author="Otto Wilhelm Thomé",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

PRUNUS_SECTION_PRUNUS = Clade(
    name="Prunus sect. Prunus", children=[P_DOMESTICA, P_SPINOSA]
)
PRUNUS_SECTION_ARMENIACA = Clade(name="Prunus sect. Armeniaca", children=[P_ARMENIACA])

PRUNUS_SUBGENUS_PRUNUS = Subgenus(
    name="Prunus subg. Prunus",
    children=[PRUNUS_SECTION_PRUNUS, PRUNUS_SECTION_ARMENIACA],
)
PRUNUS_SUBGENUS_CERASUS = Subgenus(
    name="Prunus subg. Cerasus", children=[P_AVIUM, P_CERASUS]
)
PRUNUS_SUBGENUS_AMYGDALUS = Subgenus(
    name="Prunus subg. Amygdalus", children=[P_PERSICA, P_AMYGDALUS]
)

# https://www.researchgate.net/publication/255954651_Phylogeny_and_Classification_of_Prunus_sensu_lato_Rosaceae
AMYGDALUS_PRUNUS = Clade(children=[PRUNUS_SUBGENUS_PRUNUS, PRUNUS_SUBGENUS_AMYGDALUS])

SORBUS = Genus(name="Sorbus", children=[S_AUCUPARIA])
ARONIA = Genus(name="Aronia", children=[A_MELANOCARPA])
MALUS = Genus(name="Malus", children=[M_DOMESTICA, M_SYLVESTRIS])
PYRUS = Genus(name="Pyrus", children=[P_COMMUNIS])
CRATAEGUS = Genus(name="Crataegus", children=[C_MONOGYNA])
PRUNUS = Genus(name="Prunus", children=[AMYGDALUS_PRUNUS, PRUNUS_SUBGENUS_CERASUS])
CYDONIA = Genus(name="Cydonia", children=[C_OBLONGA])

# https://www.hindawi.com/journals/bmri/2018/7627191/
# but could be wrong, to be checked later?
MALINAE_A = Clade(children=[ARONIA, MALUS])
MALINAE_B = Clade(children=[SORBUS, PYRUS])
MALINAE_C = Clade(children=[MALINAE_A, MALINAE_B])
MALINAE_D = Clade(children=[CRATAEGUS, CYDONIA])

MALINAE = Subtribe(name="Malinae", children=[MALINAE_C, MALINAE_D])

MALEAE = Tribe(name="Maleae", children=[MALINAE])
AMYGDALEAE = Tribe(name="Amygdaleae", children=[PRUNUS])

AMYGDALOIDEAE = Subfamily(name="Amygdaloideae", children=[MALEAE, AMYGDALEAE])
