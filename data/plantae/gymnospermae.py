from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subfamily
from constants import EN, IMAGE, PL
from image import Image, License

A_ALBA = Species(
    name="Abies alba",
    local_names={EN: "silver fir", PL: "jodła pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Abies_alba.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0c/Abies_alba.png",
        author="Lisa Nicvert",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SYLVESTRIS = Species(
    name="Pinus sylvestris",
    local_names={EN: "European red pine", PL: "sosna zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20160819Pinus_sylvestris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/20160819Pinus_sylvestris.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
P_PINEA = Species(
    name="Pinus pinea",
    local_names={EN: "stone pine, umbrella pine", PL: "sosna pinia"},
    known_for=[
        {
            EN: "pine nuts",
            PL: "orzeszki piniowe",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Shelled_pine_nuts.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Shelled_pine_nuts.jpg",
                author="Paul Goyette",
                license=License.CC_BY_SA_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pinus_pinea_-_cone_-_Flickr_-_S._Rae.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/14/Pinus_pinea_-_cone_-_Flickr_-_S._Rae.jpg",
        author="S. Rae from Scotland, UK",
        license=License.CC_BY_2_0,
    ),
)
P_ABIES = Species(
    name="Picea abies",
    local_names={EN: "European spruce", PL: "świerk pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Norway_Spruce_cones_(Picea_abies).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Norway_Spruce_cones_%28Picea_abies%29.jpg",
        author="MrPanyGoff",
        license=License.CC_BY_SA_3_0,
    ),
)
L_DECIDUA = Species(
    name="Larix decidua",
    local_names={EN: "European larch", PL: "modrzew europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Larix_decidua_002.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f2/Larix_decidua_002.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
C_LIBANI = Species(
    name="Cedrus libani",
    local_names={EN: "Lebanese cedar", PL: "cedr libański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pinaceae_Cedrus_libani_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Pinaceae_Cedrus_libani_2.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
C_SEMPERVIRENS = Species(
    name="Cupressus sempervirens",
    local_names={EN: "Mediterranean cypress", PL: "cyprys wiecznie zielony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fresh_Cupressus_sempervirens_cones.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Fresh_Cupressus_sempervirens_cones.jpg",
        author="Rosendahl",
        license=License.PUBLIC_DOMAIN_AUTHOR,
    ),
)
T_OCCIDENTALIS = Species(
    name="Thuja occidentalis",
    local_names={EN: "northen white cedar", PL: "tuja, żywotnik zachodni"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Thuja_occidentalis_%27Warean_Lutescens%27_%C5%BBywotnik_zachodni_2019-10-26_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Thuja_occidentalis_%27Warean_Lutescens%27_%C5%BBywotnik_zachodni_2019-10-26_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
J_COMMUNIS = Species(
    name="Juniperus communis",
    local_names={PL: "jałowiec pospolity", EN: "common juniper"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Juniperus_communis,_Xinebru_alp%C3%ADn.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Juniperus_communis%2C_Xinebru_alp%C3%ADn.jpg",
        author="SABENCIA Guillermo César Ruiz",
        license=License.CC_BY_SA_4_0,
    ),
)
S_GIGANTEUM = Species(
    name="Sequoiadendron giganteum",
    local_names={PL: "sekwoja olbrzymia, mamutowiec olbrzymi", EN: "giant sequoia"},
    known_for=[{EN: "the most massive trees on Earth"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:GreenSeedConesSequoiadendronGiganteum.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/GreenSeedConesSequoiadendronGiganteum.JPG",
        author="Thereidshome",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
T_BACCATA = Species(
    name="Taxus baccata",
    local_names={PL: "cis pospolity", EN: "common yew"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Taxus_baccata,_el_tejo_com%C3%BAn,_tejo_negro_(10).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Taxus_baccata%2C_el_tejo_com%C3%BAn%2C_tejo_negro_%2810%29.jpg",
        author="M. Martin Vicente",
        license=License.CC_BY_SA_4_0,
    ),
)
G_BILOBA = Species(
    name="Ginkgo biloba",
    local_names={PL: "miłorząb dwuklapowy", EN: "ginkgo"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ginkgo_biloba_Mi%C5%82orz%C4%85b_dwuklapowy_2007-08-11_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/Ginkgo_biloba_Mi%C5%82orz%C4%85b_dwuklapowy_2007-08-11_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
T_HETEROPHYLLA = Species(
    name="Tsuga heterophylla",
    local_names={EN: "western hemlock", PL: "choina zachodnia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hemlock_foliage_and_cone.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Hemlock_foliage_and_cone.jpg",
        author="Ebustad",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)

ABIES = Genus(name="Abies", children=[A_ALBA])
PINUS = Genus(name="Pinus", children=[P_SYLVESTRIS, P_PINEA])
PICEA = Genus(name="Picea", children=[P_ABIES])
LARIX = Genus(name="Larix", children=[L_DECIDUA])
CEDRUS = Genus(name="Cedrus", children=[C_LIBANI])
CUPRESSUS = Genus(name="Cupressus", children=[C_SEMPERVIRENS])
THUJA = Genus(name="Thuja", children=[T_OCCIDENTALIS])
JUNIPERUS = Genus(name="Juniperus", children=[J_COMMUNIS])
SEQUOIADENDRON = Genus(name="Sequoiadendron", children=[S_GIGANTEUM])
TAXUS = Genus(name="Taxus", children=[T_BACCATA])
GINKGO = Genus(name="Ginkgo", children=[G_BILOBA])
TSUGA = Genus(name="Tsuga", children=[T_HETEROPHYLLA])

CUPRESSUS_JUNIPERUS = Clade(children=[CUPRESSUS, JUNIPERUS])
ABIETOIDEAE_A = Clade(children=[ABIES, TSUGA])

ABIETOIDEAE = Subfamily(name="Abietoideae", children=[ABIETOIDEAE_A, CEDRUS])
CUPRESSOIDEAE = Subfamily(name="Cupressoideae", children=[CUPRESSUS_JUNIPERUS, THUJA])

PINUS_PICEA = Clade(children=[PINUS, PICEA])
PINACEAE_A = Clade(children=[PINUS_PICEA, LARIX])

PINACEAE = Family(name="Pinaceae", children=[ABIETOIDEAE, PINACEAE_A])
CUPRESSACEAE = Family(name="Cupressaceae", children=[CUPRESSOIDEAE, SEQUOIADENDRON])
TAXACEAE = Family(name="Taxaceae", children=[TAXUS])
GINKGOACEAE = Family(name="Ginkgoaceae", children=[GINKGO])

CUPRESSALES = Clade(
    name="Cupressales", children=[CUPRESSACEAE, TAXACEAE]
)  # former Order

PINALES = Order(name="Pinales", children=[PINACEAE, CUPRESSALES])
GINKGOALES = Order(name="Ginkgoales", children=[GINKGOACEAE])

PINOPSIDA = Class(name="Pinopsida", children=[PINALES])
GINKGOOPSIDA = Class(name="Ginkgoopsida", children=[GINKGOALES])

PINOPHYTA = Phylum(name="Pinophyta", children=[PINOPSIDA])
GINKGOPHYTA = Phylum(name="Ginkgophyta", children=[GINKGOOPSIDA])

GYMNOSPERMAE = Clade(name="Gymnospermae", children=[PINOPHYTA, GINKGOPHYTA])
