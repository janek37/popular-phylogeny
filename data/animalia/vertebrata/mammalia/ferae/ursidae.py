from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, NAME, PL, URL
from image import Image, License

A_MELANOLEUCA = Species(
    name="Ailuropoda melanoleuca",
    local_names={EN: "giant panda", PL: "panda wielka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ailuropoda_melanoleuca_Zhen_Zhen_220518e.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1a/Ailuropoda_melanoleuca_Zhen_Zhen_220518e.jpg",
        author="江戸村のとくぞう",
        license=License.CC_BY_SA_4_0,
    ),
)
T_ORNATUS = Species(
    name="Tremarctos ornatus",
    local_names={
        EN: "spectacled bear, Andean bear",
        PL: "niedźwiedź andyjski, niedźwiedź okularowy, andoniedźwiedź okularowy",
    },
    known_for=[{EN: "Paddington Bear", URL: "https://www.paddington.com"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tremarctos_ornatus_-Binghamton_Zoo-6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Tremarctos_ornatus_-Binghamton_Zoo-6.jpg",
        author="Alex Erde",
        license=License.CC_BY_2_0,
    ),
)
M_URSINUS = Species(
    name="Melursus ursinus",
    local_names={EN: "sloth bear", PL: "wargacz leniwy"},
    known_for=[
        {EN: "Baloo from The Jungle Book", URL: "https://en.wikipedia.org/wiki/Baloo"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flickr_-_Rainbirder_-_Sloth_Bear.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Flickr_-_Rainbirder_-_Sloth_Bear.jpg",
        author="Steve Garvie from Dunfermline, Fife, Scotland",
        license=License.CC_BY_SA_2_0,
    ),
)
U_AMERICANUS = Species(
    name="Ursus americanus",
    local_names={
        EN: "American black bear",
        PL: "baribal, niedźwiedż amerykański, niedźwiedź czarny",
    },
    known_for=[{EN: "Winnipeg, inspiration for Winnie-the-Pooh"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:American_black_bear_Gros_Morn%D0%B5_NFL.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/American_black_bear_Gros_Morn%D0%B5_NFL.jpg",
        author="Mykola Swarnyk",
        license=License.CC_BY_SA_3_0,
    ),
)
U_THIBETANUS = Species(
    name="Ursus thibetanus",
    local_names={
        EN: "Asian black bear, moon bear",
        PL: "niedźwiedź księżycowy, niedźwiedź himalajski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ursus_thibetanus_3_(Wroclaw_zoo).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b7/Ursus_thibetanus_3_%28Wroclaw_zoo%29.JPG",
        author="Guérin Nicolas",
        license=License.CC_BY_SA_3_0,
    ),
)
U_SPELAEUS = Species(
    name="Ursus spelaeus",
    local_names={EN: "cave bear", PL: "niedźwiedź jaskiniowy"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ursus_spelaeus_Sergiodlarosa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Ursus_spelaeus_Sergiodlarosa.jpg",
        author="Sergiodlarosa",
        license=License.CC_BY_SA_3_0,
    ),
)
U_ARCTOS = Species(
    name="Ursus arctos",
    local_names={EN: "brown bear", PL: "niedźwiedź brunatny"},
    known_for=[
        {NAME: "Ursus arctos horribilis", EN: "grizzly bear", PL: "niedźwiedź grizli"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kamchatka_Brown_Bear_near_Dvuhyurtochnoe_on_2015-07-23.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/Kamchatka_Brown_Bear_near_Dvuhyurtochnoe_on_2015-07-23.jpg",
        author="Robert F. Tobler",
        license=License.CC_BY_SA_4_0,
    ),
)
U_MARITIMUS = Species(
    name="Ursus maritimus",
    local_names={EN: "polar bear", PL: "niedźwiedź polarny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ursus_maritimus_10zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1f/Ursus_maritimus_10zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)

URSUS_A = Clade(children=[U_AMERICANUS, U_THIBETANUS])
URSUS_B = Clade(children=[U_ARCTOS, U_MARITIMUS])
# https://www.researchgate.net/publication/328232826_A_three-dimensional_analysis_of_tooth-root_morphology_in_living_bears_and_implications_for_feeding_behaviour_in_the_extinct_cave_bear
URSUS_C = Clade(children=[U_SPELAEUS, URSUS_B])

AILUROPODA = Genus(name="Ailuropoda", children=[A_MELANOLEUCA])
TREMARCTOS = Genus(name="Tremarctos", children=[T_ORNATUS])
MELURSUS = Genus(name="Melursus", children=[M_URSINUS])
URSUS = Genus(name="Ursus", children=[URSUS_A, URSUS_C])

AILUROPODINAE = Subfamily(name="Ailuropodinae", children=[AILUROPODA])
TREMARCTINAE = Subfamily(name="Tremarctinae", children=[TREMARCTOS])
URSINAE = Subfamily(name="Ursinae", children=[MELURSUS, URSUS])

URSIDAE_A = Clade(children=[TREMARCTINAE, URSINAE])
URSIDAE = Family(name="Ursidae", children=[AILUROPODINAE, URSIDAE_A])
