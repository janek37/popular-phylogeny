from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, IMAGE, PL, URL
from image import Image, License

D_LEUCOTOS = Species(
    name="Dendrocopos leucotos",
    local_names={EN: "white-backed woodpecker", PL: "dzięcioł białogrzbiety"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dzieciol_bialogrzbiety_samiec.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Dzieciol_bialogrzbiety_samiec.jpg",
        author="Joanna Jasek",
        license=License.CC_BY_SA_4_0,
    ),
)
D_MARTIUS = Species(
    name="Dryocopus martius",
    local_names={EN: "black woodpecker", PL: "dzięcioł czarny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Black_woodpecker_(Dryocopus_martius).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Black_woodpecker_%28Dryocopus_martius%29.jpg",
        author="Clément Bardot",
        license=License.CC_BY_SA_4_0,
    ),
)
D_PILEATUS = Species(
    name="Dryocopus pileatus",
    local_names={EN: "pileated woodpecker", PL: "dzięcioł smugoszyi"},
    known_for=[
        {EN: "Woody Woodpecker", URL: "https://en.wikipedia.org/wiki/Woody_Woodpecker"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pileated_Woodpecker_(male),_Dryocopus_pileatus_(7036840047).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7e/Pileated_Woodpecker_%28male%29%2C_Dryocopus_pileatus_%287036840047%29.jpg",
        author="tsaiproject from Canada",
        license=License.CC_BY_2_0,
    ),
)
M_FORMICIVORUS = Species(
    name="Melanerpes formicivorus",
    local_names={EN: "acorn woodpecker", PL: "dzięciur żołędziowy"},
    known_for=[
        {
            EN: "trypophobia-triggering granary trees",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Melanerpes_formicivorus-Acorn_Storage-6.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Melanerpes_formicivorus-Acorn_Storage-6.jpg",
                author="Eugene Zelenko",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "probable inspiration for Woody Woodpecker's signature laugh",
            URL: "https://www.youtube.com/watch?v=A_IDGrKZ0Rs",
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Melanerpes_formicivorus_-San_Luis_Obispo,_California,_USA_-male-8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Melanerpes_formicivorus_-San_Luis_Obispo%2C_California%2C_USA_-male-8.jpg",
        author="marlin harms",
        license=License.CC_BY_2_0,
    ),
)
D_PUBESCENS = Species(
    name="Dryobates pubescens",
    local_names={EN: "downy woodpecker", PL: "dzięcioł kosmaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Downy_Woodpecker01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Downy_Woodpecker01.jpg",
        author="Wolfgang Wander",
        license=License.CC_BY_SA_3_0,
    ),
)
P_VIRIDIS = Species(
    name="Picus viridis",
    local_names={EN: "European green woodpecker", PL: "dzięcioł zielony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%D0%96%D0%BE%D0%B2%D0%BD%D0%B0_%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B0_(Picus_viridis).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/%D0%96%D0%BE%D0%B2%D0%BD%D0%B0_%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B0_%28Picus_viridis%29.jpg",
        author="Ryzhkov Sergey",
        license=License.CC_BY_SA_4_0,
    ),
)
R_TOCO = Species(
    name="Ramphastos toco",
    local_names={
        EN: "toco toucan, common toucan, giant toucan",
        PL: "tukan toko, tukan wielki",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ramphastos_toco_-Birdworld,_Farnham,_Surrey,_England-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Ramphastos_toco_-Birdworld%2C_Farnham%2C_Surrey%2C_England-8a.jpg",
        author="Chris Parfitt from East Grinstead, West Sussex, England",
        license=License.CC_BY_2_0,
    ),
)

DENDROCOPOS = Genus(name="Dendrocopos", children=[D_LEUCOTOS])
DRYOCOPUS = Genus(name="Dryocopus", children=[D_MARTIUS, D_PILEATUS])
MELANERPES = Genus(name="Melanerpes", children=[M_FORMICIVORUS])
DRYOBATES = Genus(name="Dryobates", children=[D_PUBESCENS])
PICUS = Genus(name="Picus", children=[P_VIRIDIS])
RAMPHASTOS = Genus(name="Ramphastos", children=[R_TOCO])

# https://en.wikipedia.org/wiki/Picinae
MELANERPINI_A = Clade(children=[DENDROCOPOS, DRYOBATES])

MELANERPINI = Tribe(name="Melanerpini", children=[MELANERPINI_A, MELANERPES])
PICINI = Tribe(name="Picini", children=[DRYOCOPUS, PICUS])

PICINAE = Subfamily(name="Picinae", children=[MELANERPINI, PICINI])

PICIDAE = Family(name="Picidae", children=[PICINAE])
RAMPHASTIDAE = Family(name="Ramphastidae", children=[RAMPHASTOS])

PICIFORMES = Order(name="Piciformes", children=[PICIDAE, RAMPHASTIDAE])
