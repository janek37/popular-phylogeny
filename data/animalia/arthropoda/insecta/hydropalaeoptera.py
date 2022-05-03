from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder, Superorder
from constants import EN, PL
from image import Image, License

E_DANICA = Species(
    name="Ephemera danica",
    local_names={EN: "green drake mayfly", PL: "jętka duńska, jętka górska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ephemera_danica01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Ephemera_danica01.jpg",
        author="Jeffdelonge",
        license=License.CC_BY_SA_3_0,
    ),
)
M_PERMIANA = Species(
    name="Meganeuropsis permiana",
    local_names={EN: "griffinfly"},
    known_for=[{EN: "the largest prehistoric insect"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Meganeuropsis_W.Kraus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/Meganeuropsis_W.Kraus.jpg",
        author="Werner Kraus",
        license=License.CC_BY_SA_4_0,
    ),
)
P_FLAVESCENS = Species(
    name="Pantala flavescens",
    local_names={EN: "globe skimmer, globe wanderer", PL: "nomadka żółtawa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wandering_Glider_(Pantala_flavescens)_(37845645704).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5f/Wandering_Glider_%28Pantala_flavescens%29_%2837845645704%29.jpg",
        author="Rison Thumboor from Thrissur, India",
        license=License.CC_BY_2_0,
    ),
)
E_CYATHIGERUM = Species(
    name="Enallagma cyathigerum",
    local_names={EN: "common blue damselfly", PL: "nimfa stawowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Enallagma_cyathigerum_8(loz).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Enallagma_cyathigerum_8%28loz%29.jpg",
        author="Loz (L. B. Tettenborn)",
        license=License.CC_BY_SA_3_0,
    ),
)

EPHEMERA = Genus(name="Ephemera", children=[E_DANICA])
MEGANEUROPSIS = Genus(name="Meganeuropsis", children=[M_PERMIANA])
PANTALA = Genus(name="Pantala", children=[P_FLAVESCENS])
ENALLAGMA = Genus(name="Enallagma", children=[E_CYATHIGERUM])

EPHEMERIDAE = Family(name="Ephemeridae", children=[EPHEMERA])
MEGANEURIDAE = Family(name="Meganeuridae", children=[MEGANEUROPSIS])
LIBELLULIDAE = Family(name="Libellulidae", children=[PANTALA])
COENAGRIONIDAE = Family(name="Coenagrionidae", children=[ENALLAGMA])

ANISOPTERA = Infraorder(name="Anisoptera", children=[LIBELLULIDAE])

ZYGOPTERA = Suborder(name="Zygoptera", children=[COENAGRIONIDAE])

EPHEMEROPTERA = Order(name="Ephemeroptera", children=[EPHEMERIDAE])
MEGANISOPTERA = Order(name="Meganisoptera", children=[MEGANEURIDAE])
ODONATA = Order(name="Odonata", children=[ANISOPTERA, ZYGOPTERA])

ODONATOPTERA = Superorder(name="Odonatoptera", children=[MEGANISOPTERA, ODONATA])

HYDROPALAEOPTERA = Clade(
    name="Hydropalaeoptera", children=[EPHEMEROPTERA, ODONATOPTERA]
)
