from clade import Clade, Family, Genus, Species, Subtribe, Tribe
from constants import EN, PL, URL
from image import Image, License

S_VULGARIS = Species(
    name="Syringa vulgaris",
    local_names={EN: "common lilac", PL: "lilak pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Syringa_vulgaris-Lilac-Chepan.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3c/Syringa_vulgaris-Lilac-Chepan.jpg",
        author="Нели Иванова - Сдружение за дива природа БАЛКАНИ",
        license=License.CC_BY_SA_4_0,
    ),
)
O_EUROPAEA = Species(
    name="Olea europaea",
    local_names={EN: "olive", PL: "oliwka europejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Olea_europaea_2830_olives.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Olea_europaea_2830_olives.jpg",
        author="Anna Anichkova",
        license=License.CC_BY_SA_3_0,
    ),
)
J_OFFICINALE = Species(
    name="Jasminum officinale",
    local_names={EN: "common jasmine", PL: "jaśmin lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Jasminum_officinale_2892.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Jasminum_officinale_2892.jpg",
        author="Vengolis",
        license=License.CC_BY_SA_4_0,
    ),
)
F_EXCELSIOR = Species(
    name="Fraxinus excelsior",
    local_names={EN: "European ash, common ash", PL: "jesion wyniosły"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fraxinus_excelsior_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Fraxinus_excelsior_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
L_VULGARE = Species(
    name="Ligustrum vulgare",
    local_names={EN: "common privet", PL: "ligustr pospolity"},
    known_for=[
        {
            EN: "4 Privet Drive, home of Dursleys from Harry Potter",
            URL: "https://harrypotter.fandom.com/wiki/4_Privet_Drive",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_Privet_(Ligustrum_vulgare)_-_Kitchener,_Ontario.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Common_Privet_%28Ligustrum_vulgare%29_-_Kitchener%2C_Ontario.jpg",
        author="Ryan Hodnett",
        license=License.CC_BY_SA_4_0,
    ),
)
F_INTERMEDIA = Species(
    name="Forsythia × intermedia",
    local_names={EN: "border forsythia", PL: "forsycja pośrednia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Forsythia_x_intermedia_Spectabilis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Forsythia_x_intermedia_Spectabilis.jpg",
        author="A. Barra",
        license=License.CC_BY_SA_4_0,
    ),
)

SYRINGA = Genus(name="Syringa", children=[S_VULGARIS])
LIGUSTRUM = Genus(name="Ligustrum", children=[L_VULGARE])
OLEA = Genus(name="Olea", children=[O_EUROPAEA])
JASMINUM = Genus(name="Jasminum", children=[J_OFFICINALE])
FRAXINUS = Genus(name="Fraxinus", children=[F_EXCELSIOR])
FORSYTHIA = Genus(name="Forsythia", children=[F_INTERMEDIA])

LIGUSTRINAE = Subtribe(name="Ligustrinae", children=[SYRINGA, LIGUSTRUM])
OLEINAE = Subtribe(name="Oleinae", children=[OLEA])
FRAXININAE = Subtribe(name="Fraxininae", children=[FRAXINUS])

# https://www.researchgate.net/publication/347381214_Resolving_the_Phylogeny_of_the_Olive_Family_Oleaceae_Confronting_Information_from_Organellar_and_Nuclear_Genomes
OLEEAE_A = Clade(children=[OLEINAE, FRAXININAE])

OLEEAE = Tribe(name="Oleeae", children=[LIGUSTRINAE, OLEEAE_A])
JASMINEAE = Tribe(name="Jasmineae", children=[JASMINUM])
FORSYTHIEAE = Tribe(name="Forsythieae", children=[FORSYTHIA])

# https://www.researchgate.net/publication/347381214_Resolving_the_Phylogeny_of_the_Olive_Family_Oleaceae_Confronting_Information_from_Organellar_and_Nuclear_Genomes
OLEACEAE_A = Clade(children=[OLEEAE, JASMINEAE])

OLEACEAE = Family(name="Oleaceae", children=[OLEACEAE_A, FORSYTHIEAE])
