from clade import Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

F_PEREGRINUS = Species(
    name="Falco peregrinus",
    local_names={EN: "peregrine falcon", PL: "sokół wędrowny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Falco_peregrinus_-_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/21/Falco_peregrinus_-_01.jpg",
        author="Carlos Delgado",
        license=License.CC_BY_SA_4_0,
    ),
)
F_TINNUNCULUS = Species(
    name="Falco tinnunculus",
    local_names={EN: "common kestrel, European kestrel", PL: "pustułka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_kestrel_falco_tinnunculus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Common_kestrel_falco_tinnunculus.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
F_SPARVERIUS = Species(
    name="Falco sparverius",
    local_names={EN: "American kestrel, sparrow hawk", PL: "pustułka amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:AmericanKestrel02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/AmericanKestrel02.jpg",
        author="Photo by Greg Hume (Greg5030)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_PLANCUS = Species(
    name="Caracara plancus",
    local_names={EN: "crested caracara", PL: "karakara czubata"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Southern_Crested_Caracara_(Caracara_plancus)_(8077678188).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Southern_Crested_Caracara_%28Caracara_plancus%29_%288077678188%29.jpg",
        author="Ron Knight from Seaford, East Sussex, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)

# unresolved
FALCO = Genus(name="Falco", children=[F_PEREGRINUS, F_TINNUNCULUS, F_SPARVERIUS])
CARACARA = Genus(name="Caracara", children=[C_PLANCUS])

FALCONIDAE = Family(name="Falconidae", children=[FALCO, CARACARA])

FALCONIFORMES = Order(name="Falconiformes", children=[FALCONIDAE])
