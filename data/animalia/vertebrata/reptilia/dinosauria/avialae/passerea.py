from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .aequornithes import AEQUORNITHES
from .telluraves import TELLURAVES

C_CANORUS = Species(
    name="Cuculus canorus", local_names={EN: "common cuckoo", PL: "kukułka zwyczajna"}
)
G_CALIFORNIANUS = Species(
    name="Geococcyx californianus",
    local_names={EN: "greater roadrunner", PL: "kukawka kalifornijska"},
    known_for=[{EN: "Road Runner from Warner Bros cartoons", PL: "Struś Pędziwiatr"}],
)
G_JAPONENSIS = Species(
    name="Grus japonensis",
    local_names={EN: "red-crowned crane, Japanese crane", PL: "żuraw mandżurski"},
    known_for=[{EN: "a symbol of longevity in East Asia"}],
)
L_CANUS = Species(name="Larus canus", local_names={EN: "common gull", PL: "mewa siwa"})
S_HIRUNDO = Species(
    name="Sterna hirundo",
    local_names={EN: "common tern", PL: "rybitwa zwyczajna, rybitwa rzeczna"},
)
G_GALLINAGO = Species(
    name="Gallinago gallinago", local_names={EN: "common snipe", PL: "bekas kszyk"}
)
V_VANELLUS = Species(
    name="Vanellus vanellus",
    local_names={
        EN: "peewit, tuit, green plover, northern lapwing",
        PL: "czajka zwyczajna",
    },
)
A_COLUBRIS = Species(
    name="Archilochus colubris",
    local_names={EN: "ruby-throated hummingbird", PL: "koliberek rubinobrody"},
)
M_HELENAE = Species(
    name="Mellisuga helenae",
    local_names={EN: "bee hummingbird", PL: "koliberek hawański"},
    known_for=[{EN: "the world's smallest bird"}],
)
A_APUS = Species(
    name="Apus apus", local_names={EN: "common swift", PL: "jerzyk zwyczajny"}
)
C_EUROPAEUS = Species(
    name="Caprimulgus europaeus",
    local_names={
        EN: "European nightjar, common goatsucker",
        PL: "lelek kozodój, lelek zwyczajny",
    },
)

CUCULUS = Genus(name="Cuculus", children=[C_CANORUS])
GEOCOCCYX = Genus(name="Geococcyx", children=[G_CALIFORNIANUS])
GRUS = Genus(name="Grus", children=[G_JAPONENSIS])
LARUS = Genus(name="Larus", children=[L_CANUS])
STERNA = Genus(name="Sterna", children=[S_HIRUNDO])
GALLINAGO = Genus(name="Gallinago", children=[G_GALLINAGO])
VANELLUS = Genus(name="Vanellus", children=[V_VANELLUS])
ARCHILOCHUS = Genus(name="Archilochus", children=[A_COLUBRIS])
MELLISUGA = Genus(name="Mellisuga", children=[M_HELENAE])
APUS = Genus(name="Apus", children=[A_APUS])
CAPRIMULGUS = Genus(name="Caprimulgus", children=[C_EUROPAEUS])

CUCULIDAE = Family(name="Cuculidae", children=[CUCULUS, GEOCOCCYX])
GRUIDAE = Family(name="Gruidae", children=[GRUS])
LARIDAE = Family(name="Laridae", children=[LARUS, STERNA])
SCOLOPACIDAE = Family(name="Scolopacidae", children=[GALLINAGO])
CHARADRIIDAE = Family(name="Charadriidae", children=[VANELLUS])
TROCHILIDAE = Family(name="Trochilidae", children=[ARCHILOCHUS, MELLISUGA])
APODIDAE = Family(name="Apodidae", children=[APUS])
CAPRIMULGIDAE = Family(name="Caprimulgidae", children=[CAPRIMULGUS])

CHARADRIFORMES_A = Clade(children=[LARIDAE, SCOLOPACIDAE])

CUCULIFORMES = Order(name="Cuculiformes", children=[CUCULIDAE])
GRUIFORMES = Order(name="Gruiformes", children=[GRUIDAE])
CHARADRIIFORMES = Order(
    name="Charadriiformes", children=[CHARADRIFORMES_A, CHARADRIIDAE]
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
