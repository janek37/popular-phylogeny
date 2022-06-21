from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL, URL
from image import Image, License

from .pelecaniformes import PELECANIFORMES

G_IMMER = Species(
    name="Gavia immer",
    local_names={EN: "common loon", PL: "nur lodowiec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gavia_immer_-Minocqua,_Wisconsin,_USA_-swimming-8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Gavia_immer_-Minocqua%2C_Wisconsin%2C_USA_-swimming-8.jpg",
        author="John Picken from Chicago, USA",
        license=License.CC_BY_2_0,
    ),
)
D_EXULANS = Species(
    name="Diomedea exulans",
    local_names={EN: "wandering albatross, snowy albatross", PL: "albatros wędrowny"},
    known_for=[{EN: "the longest wingspan of all birds"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wandering_Albatross-_east_of_the_Tasman_Peninsula.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Wandering_Albatross-_east_of_the_Tasman_Peninsula.jpg",
        author="JJ Harrison",
        license=License.CC_BY_SA_3_0,
    ),
)
A_FORSTERI = Species(
    name="Aptenodytes forsteri",
    local_names={EN: "emperor penguin", PL: "pingwin cesarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Emperor_Penguin_Manchot_empereur.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Emperor_Penguin_Manchot_empereur.jpg",
        author="Samuel Blanc",
        license=License.CC_BY_SA_3_0,
    ),
)
P_ADELIAE = Species(
    name="Pygoscelis adeliae",
    local_names={EN: "Adélie penguin", PL: "pingwin Adeli, pingwin białooki"},
    known_for=[
        {
            EN: "penguins from Madagascar franchise",
            URL: "https://madagascar.fandom.com/wiki/Category:Penguins",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Manchot_Ad%C3%A9lie_-_Adelie_Penguin.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Manchot_Ad%C3%A9lie_-_Adelie_Penguin.jpg",
        author="Samuel Blanc",
        license=License.CC_BY_SA_3_0,
    ),
)
P_PAPUA = Species(
    name="Pygoscelis papua",
    local_names={EN: "Gentoo penguin", PL: "pingwin białobrewy"},
    known_for=[{EN: "Gentoo Linux"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pygoscelis_papua_11(js).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Pygoscelis_papua_11%28js%29.jpg",
        author="Jerzy Strzelecki",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CICONIA = Species(
    name="Ciconia ciconia",
    local_names={EN: "white stork", PL: "bocian biały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:White_Stork_(Ciconia_ciconia)_(6).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/White_Stork_%28Ciconia_ciconia%29_%286%29.jpg",
        author="Ken Billington",
        license=License.CC_BY_SA_3_0,
    ),
)
L_CRUMENIFER = Species(
    name="Leptoptilos crumenifer",
    local_names={EN: "marabou stork", PL: "marabut afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Marabou_Stork_(Leptoptilos_crumenifer)_(51873772498).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Marabou_Stork_%28Leptoptilos_crumenifer%29_%2851873772498%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
M_BASSANUS = Species(
    name="Morus bassanus",
    local_names={EN: "northern gannet", PL: "głuptak biały, głuptak zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Northern_gannet_in_flight,_Lummenfelsen,_Heligoland,_Germany.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Northern_gannet_in_flight%2C_Lummenfelsen%2C_Heligoland%2C_Germany.jpg",
        author="Carsten Steger",
        license=License.CC_BY_SA_4_0,
    ),
)
S_LEUCOGASTER = Species(
    name="Sula leucogaster",
    local_names={EN: "brown booby", PL: "głuptak białobrzuchy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brown_booby_(Sula_leucogaster_leucogaster)_Principe_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/05/Brown_booby_%28Sula_leucogaster_leucogaster%29_Principe_3.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
P_CARBO = Species(
    name="Phalacrocorax carbo",
    local_names={EN: "great cormorant", PL: "kormoran czarny, kormoran zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cormorant_(Phalacrocorax_carbo)_(17).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Cormorant_%28Phalacrocorax_carbo%29_%2817%29.JPG",
        author="Ken Billington",
        license=License.CC_BY_SA_3_0,
    ),
)

GAVIA = Genus(name="Gavia", children=[G_IMMER])
DIOMEDEA = Genus(name="Diomedea", children=[D_EXULANS])
APTENODYTES = Genus(name="Aptenodytes", children=[A_FORSTERI])
PYGOSCELIS = Genus(name="Pygoscelis", children=[P_ADELIAE, P_PAPUA])
CICONIA = Genus(name="Ciconia", children=[C_CICONIA])
LEPTOPTILOS = Genus(name="Leptoptilos", children=[L_CRUMENIFER])
MORUS = Genus(name="Morus", children=[M_BASSANUS])
SULA = Genus(name="Sula", children=[S_LEUCOGASTER])
PHALACROCORAX = Genus(name="Phalacrocorax", children=[P_CARBO])

GAVIIDAE = Family(name="Gaviidae", children=[GAVIA])
DIOMEDEIDAE = Family(name="Diomedeidae", children=[DIOMEDEA])
SPHENISCIDAE = Family(name="Spheniscidae", children=[APTENODYTES, PYGOSCELIS])
CICONIIDAE = Family(name="Ciconiidae", children=[CICONIA, LEPTOPTILOS])
SULIDAE = Family(name="Sulidae", children=[MORUS, SULA])
PHALACROCORACIDAE = Family(name="Phalacrocoracidae", children=[PHALACROCORAX])

GAVIIFORMES = Order(name="Gaviiformes", children=[GAVIIDAE])
PROCELLARIIFORMES = Order(name="Procellariiformes", children=[DIOMEDEIDAE])
SPHENISCIFORMES = Order(name="Sphenisciformes", children=[SPHENISCIDAE])
CICONIIFORMES = Order(name="Ciconiiformes", children=[CICONIIDAE])
SULIFORMES = Order(name="Suliformes", children=[SULIDAE, PHALACROCORACIDAE])

PELECANIMORPHAE_A = Clade(children=[SULIFORMES, PELECANIFORMES])

AUSTRODYPTORNITHES = Clade(
    name="Austrodyptornithes", children=[PROCELLARIIFORMES, SPHENISCIFORMES]
)
PELECANIMORPHAE = Clade(
    name="Pelecanimorphae", children=[CICONIIFORMES, PELECANIMORPHAE_A]
)

FERAEQUORNITHES = Clade(
    name="Feraequornithes", children=[AUSTRODYPTORNITHES, PELECANIMORPHAE]
)

AEQUORNITHES = Clade(name="Aequornithes", children=[GAVIIFORMES, FERAEQUORNITHES])
