from clade import Clade, Family, Genus, Order, Species, Subfamily, Superfamily, Tribe
from constants import EN, LA, PL

N_MELEAGRIS = Species(
    name="Numida meleagris",
    local_names={EN: "helmeted guineafowl", PL: "perliczka, perlica zwyczajna"},
)
C_VIRGINIANUS = Species(
    name="Colinus virginianus",
    local_names={EN: "northern bobwhite, Virginia quail", PL: "przepiór wirginijski"},
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
)
B_UMBELLUS = Species(
    name="Bonasa umbellus", local_names={EN: "ruffed grouse", PL: "cieciornik"}
)
T_UROGALLUS = Species(
    name="Tetrao urogallus",
    local_names={
        EN: "western capercaillie, wood grouse, heather cock",
        PL: "głuszec zwyczajny",
    },
)
P_PERDIX = Species(
    name="Perdix perdix", local_names={EN: "grey partridge", PL: "kuropatwa zwyczajna"}
)
P_COLCHICUS = Species(
    name="Phasianus colchicus",
    local_names={EN: "common pheasant", PL: "bażant zwyczajny"},
)
C_PICTUS = Species(
    name="Chrysolophus pictus",
    local_names={
        EN: "golden pheasant, Chinese/rainbow pheasant",
        PL: "bażant złocisty",
    },
    known_for=[{EN: "famous Slovak beer brand Zlatý Bažant"}],
)
C_COTURNIX = Species(
    name="Coturnix coturnix",
    local_names={EN: "common quail, European quail", PL: "przepiórka zwyczajna"},
)
G_GALLUS = Species(
    name="Gallus gallus",
    local_names={EN: "red junglefowl", PL: "kur bankiwa"},
    known_for=[{LA: "Gallus gallus domesticus", EN: "chicken", PL: "kura domowa"}],
)
P_CRISTATUS = Species(
    name="Pavo cristatus",
    local_names={
        EN: "Indian peafowl, common peafowl, blue peafowl",
        PL: "paw zwyczajny, paw niebieski, paw indyjski",
    },
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
