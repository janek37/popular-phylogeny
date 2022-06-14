from clade import Clade, Family, Genus, Infraorder, Species, Suborder, Superfamily
from constants import EN, PL, URL
from image import Image, License

L_CATTA = Species(
    name="Lemur catta",
    local_names={EN: "ring-tailed lemur", PL: "lemur katta"},
    known_for=[
        {
            EN: "King Julien from Madagascar feanchise",
            URL: "https://madagascar.fandom.com/wiki/King_Julien",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lemur_catta_001.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Lemur_catta_001.jpg",
        author="Alex Dunkel (Maky)",
        license=License.CC_BY_3_0,
    ),
)
D_MADAGASCARIENSIS = Species(
    name="Daubentonia madagascariensis",
    local_names={EN: "aye-aye", PL: "palczak madagaskarski"},
    known_for=[
        {
            EN: "Maurice from Madagascar franchise",
            URL: "https://madagascar.fandom.com/wiki/Maurice",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Handbook_to_the_Primates_Plate_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Handbook_to_the_Primates_Plate_01.jpg",
        author="Henry Ogg Forbes (1851-1932). Species Plates by John Gerrard Keulemans (1842–1912).",
        license=License.PUBLIC_DOMAIN,
    ),
)
M_LEHILAHYTSARA = Species(
    name="Microcebus lehilahytsara",
    local_names={EN: "Goodman's mouse lemur", PL: "mikrusek kasztanowaty"},
    known_for=[
        {
            EN: "Mort from Madagascar franchise",
            URL: "https://madagascar.fandom.com/wiki/Mort",
        },
        {EN: "one of the smallest living primates"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mausmaki_Andasibe-Mantadia_National_Park_2019-10-16_(6).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/Mausmaki_Andasibe-Mantadia_National_Park_2019-10-16_%286%29.jpg",
        author="Z thomas",
        license=License.CC_BY_SA_4_0,
    ),
)

LEMUR = Genus(name="Lemur", children=[L_CATTA])
DAUBENTONIA = Genus(name="Daubentonia", children=[D_MADAGASCARIENSIS])
MICROCEBUS = Genus(name="Microcebus", children=[M_LEHILAHYTSARA])

LEMURIDAE = Family(name="Lemuridae", children=[LEMUR])
DAUBENTONIIDAE = Family(name="Daubentoniidae", children=[DAUBENTONIA])
CHEIROGALEIDAE = Family(name="Cheirogaleidae", children=[MICROCEBUS])

# https://en.wikipedia.org/wiki/Taxonomy_of_lemurs
LEMUROIDEA_A = Clade(children=[LEMURIDAE, CHEIROGALEIDAE])

LEMUROIDEA = Superfamily(name="Lemuroidea", children=[LEMUROIDEA_A, DAUBENTONIIDAE])

LEMURIFORMES = Infraorder(name="Lemuriformes", children=[LEMUROIDEA])

STREPSIRRHINI = Suborder(name="Strepsirrhini", children=[LEMURIFORMES])
