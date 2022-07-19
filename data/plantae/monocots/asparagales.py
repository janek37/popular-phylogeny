from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, IMAGE, PL
from image import Image, License

O_MILITARIS = Species(
    name="Orchis militaris",
    local_names={EN: "military orchid", PL: "storczyk kukawka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Orchis_militaris_193071253.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/de/Orchis_militaris_193071253.jpg",
        author="carabus123",
        license=License.CC_BY_4_0,
    ),
)
V_PLANIFOLIA = Species(
    name="Vanilla planifolia",
    local_names={EN: "flat-leaved vanilla", PL: "wanilia płaskolistna"},
    known_for=[
        {
            EN: "vanilla flavouring",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Vanilla_6beans.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Vanilla_6beans.JPG",
                author="B.navez",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vanilla_planifolia_(6998639597).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Vanilla_planifolia_%286998639597%29.jpg",
        author="Malcolm Manners from Lakeland FL, USA",
        license=License.CC_BY_2_0,
    ),
)
O_APIFERA = Species(
    name="Ophrys apifera",
    local_names={EN: "bee orchid", PL: "dwulistnik pszczeli"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bee_Orchid_(Ophrys_apifera)_(14374841786)_-_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Bee_Orchid_%28Ophrys_apifera%29_%2814374841786%29_-_cropped.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
C_CALCEOLUS = Species(
    name="Cypripedium calceolus",
    local_names={EN: "lady's-slipper orchid", PL: "obuwik pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cypripedium_calceolus_03-09.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Cypripedium_calceolus_03-09.jpg",
        author="Johan Neegers",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
I_SIBIRICA = Species(
    name="Iris sibirica",
    local_names={EN: "Siberian iris", PL: "kosaciec syberyjski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Iris_Sibirica_in_Matschels_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/Iris_Sibirica_in_Matschels_01.jpg",
        author="Reinhard Müller",
        license=License.CC_BY_SA_4_0,
    ),
)
C_SATIVUS = Species(
    name="Crocus sativus",
    local_names={EN: "saffron crocus", PL: "szafran uprawny"},
    known_for=[
        {
            EN: "saffron",
            PL: "szafran (przyprawa)",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Iran_saffron_threads.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Iran_saffron_threads.jpg",
                author="Rainer Zenz",
                license=License.PUBLIC_DOMAIN_USER,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crocus_sativus_-_Saffron_crocus_-_Safran_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Crocus_sativus_-_Saffron_crocus_-_Safran_01.JPG",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
C_VERNUS = Species(
    name="Crocus vernus",
    local_names={EN: "spring crocus", PL: "krokus/szafran wiosenny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crocus_vernus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Crocus_vernus.jpg",
        author="Smihael",
        license=License.CC_BY_SA_3_0,
    ),
)
A_OFFICINALIS = Species(
    name="Asparagus officinalis",
    local_names={EN: "garden asparagus", PL: "szparag lekarski"},
    known_for=[{EN: "edible shoots", PL: "jadalne pędy"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Asparagus_officinalis_(Asperge)_-_Noordwijk,_South_Holland,_NL_v2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Asparagus_officinalis_%28Asperge%29_-_Noordwijk%2C_South_Holland%2C_NL_v2.jpg",
        author="Rudolphous",
        license=License.CC_BY_SA_4_0,
    ),
)
A_AMERICANA = Species(
    name="Agave americana",
    local_names={EN: "century plant, maguey", PL: "agawa amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Agave_americana_a-m.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4a/Agave_americana_a-m.jpg",
        author="Stan Shebs",
        license=License.CC_BY_SA_3_0,
    ),
)
A_TEQUILANA = Species(
    name="Agave tequilana",
    local_names={EN: "blue agave", PL: "agawa niebieska"},
    known_for=[
        {
            EN: "tequila",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Tequilas.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Tequilas.JPG",
                author="Photomag",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Agave_tequilana_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Agave_tequilana_1.jpg",
        author="Stan Shebs",
        license=License.CC_BY_SA_3_0,
    ),
)
C_MAJALIS = Species(
    name="Convallaria majalis",
    local_names={EN: "lily of the valley", PL: "konwalia majowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lily_of_the_valley,_Convallaria_majalis,_Mo%D0%BC%D0%B8%D0%BD%D0%B0_%D1%81%D1%8A%D0%BB%D0%B7%D0%B0.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/72/Lily_of_the_valley%2C_Convallaria_majalis%2C_Mo%D0%BC%D0%B8%D0%BD%D0%B0_%D1%81%D1%8A%D0%BB%D0%B7%D0%B0.jpg",
        author="TodorBelomorski",
        license=License.CC_BY_SA_4_0,
    ),
)
H_ORIENTALIS = Species(
    name="Hyacinthus orientalis",
    local_names={EN: "common hyacinth", PL: "hiacynt wschodni"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hyacinthus_orientalis_124796495.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Hyacinthus_orientalis_124796495.jpg",
        author="Steve DeGrace",
        license=License.CC_BY_4_0,
    ),
)
A_VERA = Species(
    name="Aloe vera",
    local_names={PL: "aloes zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_011104-0040_Aloe_vera.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Starr_011104-0040_Aloe_vera.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
A_CEPA = Species(
    name="Allium cepa",
    local_names={PL: "cebula", EN: "onion"},
    known_for=[
        {
            EN: "edible bulb",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Mixed_onions.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/Mixed_onions.jpg",
                author="Colin",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allium_cepa,_Amol.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Allium_cepa%2C_Amol.jpg",
        author="Mehdi",
        license=License.CC_BY_SA_3_0,
    ),
)
A_SATIVUM = Species(
    name="Allium sativum",
    local_names={PL: "czosnek", EN: "garlic"},
    known_for=[
        {
            EN: "edible buds (cloves)",
            PL: "jadalne pąki (ząbki)",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Garlic.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Garlic.jpg",
                author="Donovan Govan",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allium_sativum_02.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Allium_sativum_02.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_3_0,
    ),
)
A_AMPELOPRASUM = Species(
    name="Allium ampeloprasum",
    known_for=[
        {
            EN: "leek",
            PL: "por",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Prei_met_knobbel_(Leek).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Prei_met_knobbel_%28Leek%29.jpg",
                author="Rasbak",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "elephant garlic",
            PL: "czosnek słoniowy",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Ackerknoblauch_(Allium_ampeloprasum).JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Ackerknoblauch_%28Allium_ampeloprasum%29.JPG",
                author="Own work",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        },
        {
            EN: "pearl onion",
            PL: "cebulka perłowa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Silberzwiebeln_(9373-75).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Silberzwiebeln_%289373-75%29.jpg",
                author="Raimond Spekking",
                license=License.CC_BY_SA_4_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allium_ampeloprasum_inflorescence.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Allium_ampeloprasum_inflorescence.jpg",
        author="Hüseyin Cahid Doğan",
        license=License.CC_BY_SA_4_0,
    ),
)
A_SCHOENOPRASUM = Species(
    name="Allium schoenoprasum",
    local_names={EN: "chives", PL: "szczypiorek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allium_schoenoprasum_L..JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Allium_schoenoprasum_L..JPG",
        author="Kagor",
        license=License.CC_BY_SA_3_0,
    ),
)
A_URSINUM = Species(
    name="Allium ursinum",
    local_names={PL: "czosnek niedźwiedzi", EN: "wild garlic"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allium_ursinum_2_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Allium_ursinum_2_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
N_POETICUS = Species(
    name="Narcissus poeticus",
    local_names={PL: "narcyz biały", EN: "poet's daffodil"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Narcissus_poeticus_%27Recurvus%2706.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Narcissus_poeticus_%27Recurvus%2706.jpg",
        author="Meneerke bloem",
        license=License.CC_BY_SA_3_0,
    ),
)
N_JONQUILLA = Species(
    name="Narcissus jonquilla",
    local_names={PL: "narcyz żonkil", EN: "jonquil, rush daffodil"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Narcissus_jonquilla_Trevithian_4zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Narcissus_jonquilla_Trevithian_4zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
G_NIVALIS = Species(
    name="Galanthus nivalis",
    local_names={PL: "snieżyczka przebiśnieg", EN: "common snowdrop"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Galanthus_nivalis_close-up_aka.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Galanthus_nivalis_close-up_aka.jpg",
        author="André Karwath aka Aka",
        license=License.CC_BY_SA_2_5,
    ),
)

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2958792/
ALLIUM_A = Clade(children=[A_CEPA, A_SCHOENOPRASUM])
ALLIUM_B = Clade(children=[A_SATIVUM, A_AMPELOPRASUM])
ALLIUM_C = Clade(children=[ALLIUM_A, ALLIUM_B])

ORCHIS = Genus(name="Orchis", children=[O_MILITARIS])
VANILLA = Genus(name="Vanilla", children=[V_PLANIFOLIA])
OPHRYS = Genus(name="Ophrys", children=[O_APIFERA])
CYPRIPEDIUM = Genus(name="Cypripedium", children=[C_CALCEOLUS])
IRIS = Genus(name="Iris", children=[I_SIBIRICA])
CROCUS = Genus(name="Crocus", children=[C_SATIVUS, C_VERNUS])
ASPARAGUS = Genus(name="Asparagus", children=[A_OFFICINALIS])
AGAVE = Genus(name="Agave", children=[A_AMERICANA, A_TEQUILANA])
CONVALLARIA = Genus(name="Convallaria", children=[C_MAJALIS])
HYACINTHUS = Genus(name="Hyacinthus", children=[H_ORIENTALIS])
ALOE = Genus(name="Aloe", children=[A_VERA])
ALLIUM = Genus(name="Allium", children=[ALLIUM_C, A_URSINUM])
NARCISSUS = Genus(name="Narcissus", children=[N_POETICUS, N_JONQUILLA])
GALANTHUS = Genus(name="Galanthus", children=[G_NIVALIS])

ORCHIDOIDEAE = Subfamily(name="Orchidoideae", children=[ORCHIS, OPHRYS])
VANILLOIDEAE = Subfamily(name="Vanilloideae", children=[VANILLA])
CYPRIPEDIOIDEAE = Subfamily(name="Cypripedioideae", children=[CYPRIPEDIUM])
ASPARAGOIDEAE = Subfamily(name="Asparagoideae", children=[ASPARAGUS])
AGAVOIDEAE = Subfamily(name="Agavoideae", children=[AGAVE])
NOLINOIDEAE = Subfamily(name="Nolinoideae", children=[CONVALLARIA])
SCILLOIDEAE = Subfamily(name="Scilloideae", children=[HYACINTHUS])
ALLIOIDEAE = Subfamily(name="Allioideae", children=[ALLIUM])
AMARYLLIDOIDEAE = Subfamily(name="Amaryllidoideae", children=[NARCISSUS, GALANTHUS])

ASPARAGOIDEAE_NOLINOIDEAE = Clade(children=[ASPARAGOIDEAE, NOLINOIDEAE])
AGAVOIDEAE_SCILLOIDEAE = Clade(children=[AGAVOIDEAE, SCILLOIDEAE])
ORCHIDEACEAE_A = Clade(children=[ORCHIDOIDEAE, CYPRIPEDIOIDEAE])

ORCHIDEACEAE = Family(name="Orchideaceae", children=[ORCHIDEACEAE_A, VANILLOIDEAE])
IRIDACEAE = Family(name="Iridaceae", children=[IRIS, CROCUS])
ASPARAGACEAE = Family(
    name="Asparagaceae", children=[ASPARAGOIDEAE_NOLINOIDEAE, AGAVOIDEAE_SCILLOIDEAE]
)
ASPHODELACEAE = Family(name="Asphodelaceae", children=[ALOE])
AMARYLLIDACEAE = Family(name="Amaryllidaceae", children=[ALLIOIDEAE, AMARYLLIDOIDEAE])

ASPARAGACEAE_AMARYLLIDACEAE = Clade(children=[ASPARAGACEAE, AMARYLLIDACEAE])
ASPARAGALES_B = Clade(children=[ASPARAGACEAE_AMARYLLIDACEAE, ASPHODELACEAE])
ASPARAGALES_A = Clade(children=[IRIDACEAE, ASPARAGALES_B])

ASPARAGALES = Order(name="Asparagales", children=[ORCHIDEACEAE, ASPARAGALES_A])
