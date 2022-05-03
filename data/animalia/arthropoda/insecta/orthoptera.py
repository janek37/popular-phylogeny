from clade import Family, Genus, Infraorder, Order, Species, Subfamily, Suborder
from constants import EN, PL
from image import Image, License

L_MIGRATORIA = Species(
    name="Locusta migratoria",
    local_names={EN: "migratory locust", PL: "szarańcza wędrowna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202203_migratory_locust_gregarious_phase.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/202203_migratory_locust_gregarious_phase.svg",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
C_BIGUTTULUS = Species(
    name="Chorthippus biguttulus",
    local_names={EN: "bow-winged grasshopper", PL: "konik pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chorthippus_biguttulus_f_8835.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Chorthippus_biguttulus_f_8835.jpg",
        author="G.-U. Tolkiehn",
        license=License.CC_BY_SA_3_0,
    ),
)
G_GRYLLOTALPA = Species(
    name="Gryllotalpa gryllotalpa",
    local_names={EN: "European mole cricket", PL: "turkuć podjadek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Grillotalpa_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Grillotalpa_02.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
G_CAMPESTRIS = Species(
    name="Gryllus campestris",
    local_names={EN: "European field cricket", PL: "świerszcz polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gryllus_campestris_(35634613106).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Gryllus_campestris_%2835634613106%29.jpg",
        author="xulescu_g",
        license=License.CC_BY_SA_2_0,
    ),
)
A_DOMESTICUS = Species(
    name="Acheta domesticus",
    local_names={EN: "house cricket", PL: "świerszcz domowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acheta_domesticus_male_9243.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ae/Acheta_domesticus_male_9243.jpg",
        author="G.-U. Tolkiehn",
        license=License.CC_BY_SA_3_0,
    ),
)
T_VIRIDISSIMA = Species(
    name="Tettigonia viridissima",
    local_names={EN: "great green bush-cricket", PL: "pasikonik zielony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dixi-Tettigonia_Viridissima.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Dixi-Tettigonia_Viridissima.jpg",
        author="Monika Betley",
        license=License.CC_BY_SA_3_0,
    ),
)
P_GRISEOAPTERA = Species(
    name="Pholidoptera griseoaptera",
    local_names={EN: "dark bush-cricket", PL: "podkrzewin szary"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pholidoptera_griseoaptera-ms.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Pholidoptera_griseoaptera-ms.jpg",
        author="Magnefl",
        license=License.CC_BY_SA_3_0,
    ),
)
D_HETERACANTHA = Species(
    name="Deinacrida heteracantha",
    local_names={EN: "wetapunga, Little Barrier giant wētā"},
    known_for=[{EN: "the heaviest known insect"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wetapunga.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Wetapunga.jpg",
        author="Dinobass",
        license=License.CC_BY_SA_4_0,
    ),
)

LOCUSTA = Genus(name="Locusta", children=[L_MIGRATORIA])
CHORTHIPPUS = Genus(name="Chorthippus", children=[C_BIGUTTULUS])
GRYLLOTALPA = Genus(name="Gryllotalpa", children=[G_GRYLLOTALPA])
GRYLLUS = Genus(name="Gryllus", children=[G_CAMPESTRIS])
ACHETA = Genus(name="Acheta", children=[A_DOMESTICUS])
TETTIGONIA = Genus(name="Tettigonia", children=[T_VIRIDISSIMA])
PHOLIDOPTERA = Genus(name="Pholidoptera", children=[P_GRISEOAPTERA])
DEINACRIDA = Genus(name="Deinacrida", children=[D_HETERACANTHA])

OEDIPODINAE = Subfamily(name="Oedipodinae", children=[LOCUSTA])
GOMPHOCERINAE = Subfamily(name="Gomphocerinae", children=[CHORTHIPPUS])
GRYLLINAE = Subfamily(name="Gryllinae", children=[GRYLLUS, ACHETA])

ACRIDIDAE = Family(name="Acrididae", children=[OEDIPODINAE, GOMPHOCERINAE])
GRYLLOTALPIDAE = Family(name="Gryllotalpidae", children=[GRYLLOTALPA])
GRYLLIDAE = Family(name="Gryllidae", children=[GRYLLINAE])
TETTIGONIIDAE = Family(name="Tettigoniidae", children=[TETTIGONIA, PHOLIDOPTERA])
ANOSTOSTOMATIDAE = Family(name="Anostostomatidae", children=[DEINACRIDA])

GRYLLIDEA = Infraorder(name="Gryllidea", children=[GRYLLOTALPIDAE, GRYLLIDAE])
TETTIGONIIDEA = Infraorder(
    name="Tettigoniidea", children=[TETTIGONIIDAE, ANOSTOSTOMATIDAE]
)

CAELIFERA = Suborder(name="Caelifera", children=[ACRIDIDAE])
ENSIFERA = Suborder(name="Ensifera", children=[GRYLLIDEA, TETTIGONIIDEA])

ORTHOPTERA = Order(name="Orthoptera", children=[CAELIFERA, ENSIFERA])
