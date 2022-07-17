from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, IMAGE, PL
from image import Image, License

F_SYLVATICA = Species(
    name="Fagus sylvatica",
    local_names={EN: "European beech", PL: "buk zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fagus_sylvatica,_TCW_2020-09-19.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/72/Fagus_sylvatica%2C_TCW_2020-09-19.jpg",
        author="User:Kilom691",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
Q_ROBUR = Species(
    name="Quercus robur",
    local_names={EN: "common oak", PL: "dąb szypułkowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Quercus_robur_3_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Quercus_robur_3_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
Q_ALBA = Species(
    name="Quercus alba",
    local_names={EN: "white oak", PL: "dąb biały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:NAS-001g_Quercus_alba.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/NAS-001g_Quercus_alba.png",
        author="François André Michaux (book author), Pierre Joseph  Redouté (illustrator), Bessin (engraver)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
Q_SUBER = Species(
    name="Quercus suber",
    local_names={EN: "cork oak", PL: "dąb korkowy"},
    known_for=[
        {
            EN: "cork (material)",
            PL: "korek (surowiec)",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cork_closeup.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Cork_closeup.jpg",
                author="Buzzabuzza",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Quercus_suber_c.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Quercus_suber_c.JPG",
        author="Xemenendura",
        license=License.CC_BY_3_0,
    ),
)
C_SATIVA = Species(
    name="Castanea sativa",
    local_names={EN: "sweet chestnut", PL: "kasztan jadalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%C3%9Cberlingen_Goldbach_-_Castanea_sativa_03_ies.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/%C3%9Cberlingen_Goldbach_-_Castanea_sativa_03_ies.jpg",
        author="Frank Vincentz",
        license=License.CC_BY_SA_3_0,
    ),
)
J_REGIA = Species(
    name="Juglans regia",
    local_names={EN: "Persian/English/common walnut", PL: "orzech włoski"},
    known_for=[
        {
            EN: "walnuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Walnuts_-_whole_and_open_with_halved_kernel.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Walnuts_-_whole_and_open_with_halved_kernel.jpg",
                author="Ivar Leidus",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Juglans_regia_2009_G2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/Juglans_regia_2009_G2.jpg",
        author="George Chernilevsky",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
C_ILLINOINENSIS = Species(
    name="Carya illinoinensis",
    local_names={EN: "pecan", PL: "pekan, orzesznik jadalny"},
    known_for=[
        {
            EN: "pecan nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:2_pecan_nut_halves.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/2_pecan_nut_halves.jpg",
                author="Markus Brunner, Germany",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carya_illinoinensis_kz1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Carya_illinoinensis_kz1.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
B_PENDULA = Species(
    name="Betula pendula",
    local_names={EN: "silver birch", PL: "brzoza brodawkowata"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20191119Betula_pendula3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e5/20191119Betula_pendula3.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
A_GLUTINOSA = Species(
    name="Alnus glutinosa",
    local_names={EN: "common alder", PL: "olcha/olsza czarna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leaves_Alnus_glutinosa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Leaves_Alnus_glutinosa.jpg",
        author="Giovanni Caudullo",
        license=License.CC_BY_4_0,
    ),
)
C_AVELLANA = Species(
    name="Corylus avellana",
    local_names={EN: "common hazel", PL: "leszczyna pospolita"},
    known_for=[
        {
            EN: "hazel nuts",
            PL: "orzechy laskowe",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Corylus_avellana_0008.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Corylus_avellana_0008.JPG",
                author="H. Zell",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Corylus_avellana_(Russia)_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Corylus_avellana_%28Russia%29_4.jpg",
        author="Евгений Катышев",
        license=License.CC_BY_SA_3_0,
    ),
)
C_BETULUS = Species(
    name="Carpinus betulus",
    local_names={EN: "European hornbeam", PL: "grab pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carpinus_betulus_Grab_pospolity_2018-04-15_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Carpinus_betulus_Grab_pospolity_2018-04-15_01.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)

QUERCUS_SECTION_QUERCUS = Clade(
    name="Quercus sect. Quercus", children=[Q_ROBUR, Q_ALBA]
)  # Section
QUERCUS_SECTION_CERRIS = Clade(
    name="Quercus sect. Cerris", children=[Q_SUBER]
)  # Section

FAGUS = Genus(name="Fagus", children=[F_SYLVATICA])
QUERCUS = Genus(
    name="Quercus", children=[QUERCUS_SECTION_QUERCUS, QUERCUS_SECTION_CERRIS]
)
CASTANEA = Genus(name="Castanea", children=[C_SATIVA])
JUGLANS = Genus(name="Juglans", children=[J_REGIA])
CARYA = Genus(name="Carya", children=[C_ILLINOINENSIS])
BETULA = Genus(name="Betula", children=[B_PENDULA])
ALNUS = Genus(name="Alnus", children=[A_GLUTINOSA])
CORYLUS = Genus(name="Corylus", children=[C_AVELLANA])
CARPINUS = Genus(name="Carpinus", children=[C_BETULUS])

FAGOIDEAE = Subfamily(name="Fagoideae", children=[FAGUS])
QUERCOIDEAE = Subfamily(name="Quercoideae", children=[QUERCUS, CASTANEA])
BETULOIDEAE = Subfamily(name="Betuloideae", children=[BETULA, ALNUS])
CORYLOIDEAE = Subfamily(name="Coryloideae", children=[CORYLUS, CARPINUS])

FAGACEAE = Family(name="Fagaceae", children=[FAGOIDEAE, QUERCOIDEAE])
JUGLANDACEAE = Family(name="Juglandaceae", children=[JUGLANS, CARYA])
BETULACEAE = Family(name="Betulaceae", children=[BETULOIDEAE, CORYLOIDEAE])

FAGALES_A = Clade(children=[JUGLANDACEAE, BETULACEAE])
FAGALES = Order(name="Fagales", children=[FAGACEAE, FAGALES_A])
