from clade import Family, Genus, Order, Species, Subfamily
from constants import EN, IMAGE, NAME, PL, URL
from image import Image, License

A_PLATYRHYNCHOS = Species(
    name="Anas platyrhynchos",
    local_names={EN: "mallard", PL: "kaczka krzyżówka"},
    known_for=[
        {
            NAME: "Anas platyrhynchos domesticus",
            EN: "domestic duck",
            PL: "kaczka domowa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Anas_platyrhynchos_domesticus_EM1B1109_(48969709537).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Anas_platyrhynchos_domesticus_EM1B1109_%2848969709537%29.jpg",
                author="Bengt Nyman from Vaxholm, Sweden",
                license=License.CC_BY_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anas_platyrhynchos_(Male)_in_Locarno_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Anas_platyrhynchos_%28Male%29_in_Locarno_4.jpg",
        author="Commonists",
        license=License.CC_BY_SA_4_0,
    ),
)
A_RUBRIPES = Species(
    name="Anas rubripes",
    local_names={EN: "American black duck", PL: "brązówka"},
    known_for=[
        {EN: "Daffy Duck", URL: "https://looneytunes.fandom.com/wiki/Daffy_Duck"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anas_rubripes.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Anas_rubripes.jpg",
        author="DickDaniels  (https://carolinabirds.org/)",
        license=License.CC_BY_SA_3_0,
    ),
)
A_GALERICULATA = Species(
    name="Aix galericulata",
    local_names={EN: "mandarin duck", PL: "kaczka mandarynka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mandarin_duck_(Aix_galericulata)_Franconville_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2d/Mandarin_duck_%28Aix_galericulata%29_Franconville_03.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)
A_SPONSA = Species(
    name="Aix sponsa",
    local_names={EN: "wood duck, Carolina duck", PL: "karolinka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wood_Duck_(Aix_sponsa),_Parc_du_Rouge-Clo%C3%AEtre,_Brussels.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Wood_Duck_%28Aix_sponsa%29%2C_Parc_du_Rouge-Clo%C3%AEtre%2C_Brussels.jpg",
        author="Frank Vassen",
        license=License.CC_BY_2_0,
    ),
)
A_ANSER = Species(
    name="Anser anser",
    local_names={EN: "greylag goose", PL: "gęś gęgawa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anser_anser_1_(Piotr_Kuczynski).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/Anser_anser_1_%28Piotr_Kuczynski%29.jpg",
        author="Piotr Kuczynski",
        license=License.CC_BY_SA_3_0,
    ),
)
C_OLOR = Species(
    name="Cygnus olor",
    local_names={EN: "mute swan", PL: "łabędź niemy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mute_swan_Vrhnika.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/35/Mute_swan_Vrhnika.jpg",
        author="Yerpo",
        license=License.CC_BY_SA_3_0,
    ),
)

ANAS = Genus(name="Anas", children=[A_PLATYRHYNCHOS, A_RUBRIPES])
AIX = Genus(name="Aix", children=[A_GALERICULATA, A_SPONSA])
ANSER = Genus(name="Anser", children=[A_ANSER])
CYGNUS = Genus(name="Cygnus", children=[C_OLOR])

ANATINAE = Subfamily(name="Anatinae", children=[ANAS, AIX])
ANSERINAE = Subfamily(name="Anserinae", children=[ANSER, CYGNUS])

ANATIDAE = Family(name="Anatidae", children=[ANATINAE, ANSERINAE])

ANSERIFORMES = Order(name="Anseriformes", children=[ANATIDAE])
