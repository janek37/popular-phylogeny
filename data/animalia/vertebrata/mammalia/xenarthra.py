from clade import Family, Genus, Order, Species, Suborder, Superorder
from constants import EN, PL
from image import Image, License

D_NOVEMCINCTUS = Species(
    name="Dasypus novemcinctus",
    local_names={
        EN: "nine-banded armadillo",
        PL: "pancernik długoogonowy, pancernik dziewięciopaskowy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nine-banded_Armadillo_(Dasypus_novemcinctus)_(37649606094).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/64/Nine-banded_Armadillo_%28Dasypus_novemcinctus%29_%2837649606094%29.jpg",
        author="gailhampshire from Cradley, Malvern, U.K",
        license=License.CC_BY_2_0,
    ),
)
M_TRIDACTYLA = Species(
    name="Myrmecophaga tridactyla",
    local_names={EN: "giant anteater, ant bear", PL: "mrówkojad wielki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Giant_anteater_-_Oso_hormiguero_(Myrmecophaga_tridactyla)_(8697863742).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Giant_anteater_-_Oso_hormiguero_%28Myrmecophaga_tridactyla%29_%288697863742%29.jpg",
        author="Fernando Flores from Caracas, Venezuela",
        license=License.CC_BY_SA_2_0,
    ),
)
M_AMERICANUM = Species(
    name="Megatherium americanum",
    local_names={EN: "giant ground sloth, megathere"},
    known_for=[{EN: "one of the largest land mammals"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Megatherium_americanum_by_sphenaphinae.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Megatherium_americanum_by_sphenaphinae.png",
        author="Sphenaphinae",
        license=License.CC_BY_SA_4_0,
    ),
)
B_VARIEGATUS = Species(
    name="Bradypus variegatus",
    local_names={EN: "brown-throated sloth", PL: "leniwiec pstry"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bicho-pregui%C3%A7a_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/be/Bicho-pregui%C3%A7a_3.jpg",
        author="Daniella Maraschiello",
        license=License.CC_BY_SA_4_0,
    ),
)

DASYPUS = Genus(name="Dasypus", children=[D_NOVEMCINCTUS])
MYRMECOPHAGA = Genus(name="Myrmecophaga", children=[M_TRIDACTYLA])
MEGATHERIUM = Genus(name="Megatherium", children=[M_AMERICANUM])
BRADYPUS = Genus(name="Bradypus", children=[B_VARIEGATUS])

DASYPODIDAE = Family(name="Dasypodidae", children=[DASYPUS])
MYRMECOPHAGIDAE = Family(name="Myrmecophagidae", children=[MYRMECOPHAGA])
MEGATHERIIDAE = Family(name="Megatheriidae", children=[MEGATHERIUM])
BRADYPODIDAE = Family(name="Bradypodidae", children=[BRADYPUS])

VERMILINGUA = Suborder(name="Vermilingua", children=[MYRMECOPHAGIDAE])
FOLIVORA = Suborder(name="Folivora", children=[MEGATHERIIDAE, BRADYPODIDAE])

CINGULATA = Order(name="Cingulata", children=[DASYPODIDAE])
PILOSA = Order(name="Pilosa", children=[VERMILINGUA, FOLIVORA])

XENARTHRA = Superorder(name="Xenarthra", children=[CINGULATA, PILOSA])
