from clade import Clade, Family, Genus, Order, Species, Subfamily, Superfamily, Tribe
from constants import EN, LA, PL
from image import Image, License

N_MELEAGRIS = Species(
    name="Numida meleagris",
    local_names={EN: "helmeted guineafowl", PL: "perliczka, perlica zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Helmeted_Guineafowl,_Numida_meleagris_at_Elephant_Sands_Lodge,_Botswana_(31892609040).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Helmeted_Guineafowl%2C_Numida_meleagris_at_Elephant_Sands_Lodge%2C_Botswana_%2831892609040%29.jpg",
        author="Derek Keats from Johannesburg, South Africa",
        license=License.CC_BY_2_0,
    ),
)
C_VIRGINIANUS = Species(
    name="Colinus virginianus",
    local_names={EN: "northern bobwhite, Virginia quail", PL: "przepiór wirginijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Colinus_virginianus_-_Bird_Walk.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Colinus_virginianus_-_Bird_Walk.jpg",
        author="JJ Harrison (https://www.jjharrison.com.au/)",
        license=License.CC_BY_SA_3_0,
    ),
)
M_GALLOPAVO = Species(
    name="Meleagris gallopavo",
    local_names={EN: "wild turkey", PL: "indyk zwyczajny"},
    known_for=[
        {
            LA: "Meleagris gallopavo domesticus",
            EN: "domestic turkey",
            PL: "indyk domowy",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Male_wild_turkey_(Meleagris_gallopavo)_strutting.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8a/Male_wild_turkey_%28Meleagris_gallopavo%29_strutting.jpg",
        author="Frank Schulenburg",
        license=License.CC_BY_SA_4_0,
    ),
)
B_UMBELLUS = Species(
    name="Bonasa umbellus",
    local_names={EN: "ruffed grouse", PL: "cieciornik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Reed-ruffed-grouse.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Reed-ruffed-grouse.png",
        author="Chester A. Reed",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_UROGALLUS = Species(
    name="Tetrao urogallus",
    local_names={
        EN: "western capercaillie, wood grouse, heather cock",
        PL: "głuszec zwyczajny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tetrao_urogallus_(mating_display)_(26738644457).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Tetrao_urogallus_%28mating_display%29_%2826738644457%29.jpg",
        author="Tero Laakso from Hyvinkää, Finland",
        license=License.CC_BY_2_0,
    ),
)
P_PERDIX = Species(
    name="Perdix perdix",
    local_names={EN: "grey partridge", PL: "kuropatwa zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phasianidae_Perdix_perdix_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Phasianidae_Perdix_perdix_2.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
P_COLCHICUS = Species(
    name="Phasianus colchicus",
    local_names={EN: "common pheasant", PL: "bażant zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pheasant_cock_(Phasianus_colchicus)_at_the_territorial_shout.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Pheasant_cock_%28Phasianus_colchicus%29_at_the_territorial_shout.jpg",
        author="ThomasLendt",
        license=License.CC_BY_SA_4_0,
    ),
)
C_PICTUS = Species(
    name="Chrysolophus pictus",
    local_names={
        EN: "golden pheasant, Chinese/rainbow pheasant",
        PL: "bażant złocisty",
    },
    known_for=[{EN: "famous Slovak beer brand Zlatý Bažant"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:ChrysolophusPictus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/ChrysolophusPictus.jpg",
        author="smartneddy",
        license=License.CC_BY_SA_2_0,
    ),
)
C_COTURNIX = Species(
    name="Coturnix coturnix",
    local_names={EN: "common quail, European quail", PL: "przepiórka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coturnix_coturnix_1873.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Coturnix_coturnix_1873.jpg",
        author="John Gerrard Keulemans",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
G_GALLUS = Species(
    name="Gallus gallus",
    local_names={EN: "red junglefowl", PL: "kur bankiwa"},
    known_for=[{LA: "Gallus gallus domesticus", EN: "chicken", PL: "kura domowa"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Junglefowl_on_tree.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Junglefowl_on_tree.jpg",
        author="Philip Pikart",
        license=License.CC_BY_SA_4_0,
    ),
)
P_CRISTATUS = Species(
    name="Pavo cristatus",
    local_names={
        EN: "Indian peafowl, common peafowl, blue peafowl",
        PL: "paw zwyczajny, paw niebieski, paw indyjski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Peacock,_East_Park,_Hull_-_panoramio.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/df/Peacock%2C_East_Park%2C_Hull_-_panoramio.jpg",
        author="Paul Lakin",
        license=License.CC_BY_3_0,
    ),
)

NUMIDA = Genus(name="Numida", children=[N_MELEAGRIS])
COLINUS = Genus(name="Colinus", children=[C_VIRGINIANUS])
MELEAGRIS = Genus(name="Meleagris", children=[M_GALLOPAVO])
BONASA = Genus(name="Bonasa", children=[B_UMBELLUS])
TETRAO = Genus(name="Tetrao", children=[T_UROGALLUS])
PERDIX = Genus(name="Perdix", children=[P_PERDIX])
PHASIANUS = Genus(name="Phasianus", children=[P_COLCHICUS])
CHRYSOLOPHUS = Genus(name="Chrysolophus", children=[C_PICTUS])
COTURNIX = Genus(name="Coturnix", children=[C_COTURNIX])
GALLUS = Genus(name="Gallus", children=[G_GALLUS])
PAVO = Genus(name="Pavo", children=[P_CRISTATUS])

TETRAONINI_A = Clade(children=[BONASA, TETRAO])
PHASIANINI_A = Clade(children=[PHASIANUS, CHRYSOLOPHUS])

TETRAONINI = Tribe(name="Tetraonini", children=[MELEAGRIS, TETRAONINI_A])
PHASIANINI = Tribe(name="Phasianini", children=[PERDIX, PHASIANINI_A])
COTURNICINI = Tribe(name="Coturnicini", children=[COTURNIX])
GALLINI = Tribe(name="Gallini", children=[GALLUS])
PAVONINI = Tribe(name="Pavonini", children=[PAVO])

PAVONINAE_A = Clade(children=[GALLINI, PAVONINI])

PHASIANINAE = Subfamily(name="Phasianinae", children=[TETRAONINI, PHASIANINI])
PAVONINAE = Subfamily(name="Pavoninae", children=[COTURNICINI, PAVONINAE_A])

NUMIDIDAE = Family(name="Numididae", children=[NUMIDA])
ODONTOPHORIDAE = Family(name="Odontophoridae", children=[COLINUS])
PHASIANIDAE = Family(name="Phasianidae", children=[PHASIANINAE, PAVONINAE])

PHASIANOIDEA = Superfamily(name="Phasianoidea", children=[ODONTOPHORIDAE, PHASIANIDAE])

GALLIFORMES = Order(name="Galliformes", children=[NUMIDIDAE, PHASIANOIDEA])
