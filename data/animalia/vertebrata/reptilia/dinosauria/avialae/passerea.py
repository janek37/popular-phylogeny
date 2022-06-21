from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL, URL
from image import Image, License

from .aequornithes import AEQUORNITHES
from .telluraves import TELLURAVES

C_CANORUS = Species(
    name="Cuculus canorus",
    local_names={EN: "common cuckoo", PL: "kukułka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cuculus_canorus,_kukavica_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bf/Cuculus_canorus%2C_kukavica_%28cropped%29.jpg",
        author="Medenica Ivan",
        license=License.CC_BY_SA_4_0,
    ),
)
G_CALIFORNIANUS = Species(
    name="Geococcyx californianus",
    local_names={EN: "greater roadrunner", PL: "kukawka kalifornijska"},
    known_for=[
        {
            EN: "Road Runner from Warner Bros cartoons",
            PL: "Struś Pędziwiatr",
            URL: "https://looneytunes.fandom.com/wiki/Road_Runner",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Geococcyx_californianus_Albuquerque_(4815685925).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Geococcyx_californianus_Albuquerque_%284815685925%29.jpg",
        author="John Fowler from Placitas, NM, USA",
        license=License.CC_BY_2_0,
    ),
)
G_JAPONENSIS = Species(
    name="Grus japonensis",
    local_names={EN: "red-crowned crane, Japanese crane", PL: "żuraw mandżurski"},
    known_for=[{EN: "a symbol of longevity in East Asia"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Grus_japonensis_-Marwell_Wildlife,_Hampshire,_England-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Grus_japonensis_-Marwell_Wildlife%2C_Hampshire%2C_England-8a.jpg",
        author="Charles Miller from Basingstoke, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)
G_VIRGO = Species(
    name="Grus virgo",
    local_names={EN: "demoiselle crane", PL: "żuraw stepowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Demoiselle_Crane_(Grus_virgo)_(51191573249).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Demoiselle_Crane_%28Grus_virgo%29_%2851191573249%29.jpg",
        author="Imran Shah from Islamabad, Pakistan",
        license=License.CC_BY_SA_2_0,
    ),
)
L_CANUS = Species(
    name="Larus canus",
    local_names={EN: "common gull", PL: "mewa siwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Larus_canus_Common_Gull_in_Norway.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Larus_canus_Common_Gull_in_Norway.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
S_HIRUNDO = Species(
    name="Sterna hirundo",
    local_names={EN: "common tern", PL: "rybitwa zwyczajna, rybitwa rzeczna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_tern_2022_04_05_04.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/96/Common_tern_2022_04_05_04.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)
G_GALLINAGO = Species(
    name="Gallinago gallinago",
    local_names={EN: "common snipe", PL: "bekas kszyk"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gallinago-delicata-002.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Gallinago-delicata-002.jpg",
        author="Mdf",
        license=License.CC_BY_SA_3_0,
    ),
)
V_VANELLUS = Species(
    name="Vanellus vanellus",
    local_names={
        EN: "peewit, tuit, green plover, northern lapwing",
        PL: "czajka zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Northern-Lapwing-Vanellus-vanellus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Northern-Lapwing-Vanellus-vanellus.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
F_ARCTICA = Species(
    name="Fratercula arctica",
    local_names={EN: "Atlantic puffin, common puffin", PL: "maskonur zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Puffin_(Fratercula_arctica).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Puffin_%28Fratercula_arctica%29.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
A_COLUBRIS = Species(
    name="Archilochus colubris",
    local_names={EN: "ruby-throated hummingbird", PL: "koliberek rubinobrody"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Juvenile_Male_Ruby-throated_Hummingbird.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Juvenile_Male_Ruby-throated_Hummingbird.jpg",
        author="Pslawinski",
        license=License.CC_BY_SA_3_0,
    ),
)
M_HELENAE = Species(
    name="Mellisuga helenae",
    local_names={EN: "bee hummingbird", PL: "koliberek hawański"},
    known_for=[{EN: "the world's smallest bird"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bee_hummingbird_(Mellisuga_helenae)_adult_male_in_flight.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Bee_hummingbird_%28Mellisuga_helenae%29_adult_male_in_flight.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
A_APUS = Species(
    name="Apus apus",
    local_names={EN: "common swift", PL: "jerzyk zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apus_apus_flying_(transparent_background).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Apus_apus_flying_%28transparent_background%29.png",
        author="Original: pau.artigasPNG (transparent background): Paolo Villa",
        license=License.CC_BY_SA_2_0,
    ),
)
C_EUROPAEUS = Species(
    name="Caprimulgus europaeus",
    local_names={
        EN: "European nightjar, common goatsucker",
        PL: "lelek kozodój, lelek zwyczajny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Caprimulgus_europaeus_Keulemans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Caprimulgus_europaeus_Keulemans.jpg",
        author="John Gerrard Keulemans",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
F_ATRA = Species(
    name="Fulica atra",
    local_names={
        EN: "Eurasian coot, common coot, Australian coot",
        PL: "łyska zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fulica_atra_(walking).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3c/Fulica_atra_%28walking%29.jpg",
        author="Alpsdake",
        license=License.CC_BY_SA_4_0,
    ),
)

CUCULUS = Genus(name="Cuculus", children=[C_CANORUS])
GEOCOCCYX = Genus(name="Geococcyx", children=[G_CALIFORNIANUS])
GRUS = Genus(name="Grus", children=[G_JAPONENSIS, G_VIRGO])
LARUS = Genus(name="Larus", children=[L_CANUS])
STERNA = Genus(name="Sterna", children=[S_HIRUNDO])
GALLINAGO = Genus(name="Gallinago", children=[G_GALLINAGO])
VANELLUS = Genus(name="Vanellus", children=[V_VANELLUS])
FRATERCULA = Genus(name="Fratercula", children=[F_ARCTICA])
ARCHILOCHUS = Genus(name="Archilochus", children=[A_COLUBRIS])
MELLISUGA = Genus(name="Mellisuga", children=[M_HELENAE])
APUS = Genus(name="Apus", children=[A_APUS])
CAPRIMULGUS = Genus(name="Caprimulgus", children=[C_EUROPAEUS])
FULICA = Genus(name="Fulica", children=[F_ATRA])

CUCULIDAE = Family(name="Cuculidae", children=[CUCULUS, GEOCOCCYX])
GRUIDAE = Family(name="Gruidae", children=[GRUS])
LARIDAE = Family(name="Laridae", children=[LARUS, STERNA])
SCOLOPACIDAE = Family(name="Scolopacidae", children=[GALLINAGO])
CHARADRIIDAE = Family(name="Charadriidae", children=[VANELLUS])
ALCIDAE = Family(name="Alcidae", children=[FRATERCULA])
TROCHILIDAE = Family(name="Trochilidae", children=[ARCHILOCHUS, MELLISUGA])
APODIDAE = Family(name="Apodidae", children=[APUS])
CAPRIMULGIDAE = Family(name="Caprimulgidae", children=[CAPRIMULGUS])
RALLIDAE = Family(name="Rallidae", children=[FULICA])

CHARADRIIFORMES_B = Clade(children=[LARIDAE, ALCIDAE])
CHARADRIIFORMES_A = Clade(children=[CHARADRIIFORMES_B, SCOLOPACIDAE])

CUCULIFORMES = Order(name="Cuculiformes", children=[CUCULIDAE])
GRUIFORMES = Order(name="Gruiformes", children=[GRUIDAE, RALLIDAE])
CHARADRIIFORMES = Order(
    name="Charadriiformes", children=[CHARADRIIFORMES_A, CHARADRIIDAE]
)
APODIFORMES = Order(name="Apodiformes", children=[TROCHILIDAE, APODIDAE])
CAPRIMULGIFORMES = Order(name="Caprimulgiformes", children=[CAPRIMULGIDAE])

STISORES = Clade(name="Stisores", children=[APODIFORMES, CAPRIMULGIFORMES])

# currently unresolved
PASSEREA = Clade(
    name="Passerea",
    children=[
        CUCULIFORMES,
        GRUIFORMES,
        CHARADRIIFORMES,
        STISORES,
        AEQUORNITHES,
        TELLURAVES,
    ],
)
