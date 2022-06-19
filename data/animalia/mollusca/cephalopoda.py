from clade import Clade, Class, Family, Genus, Order, Species, Subclass, Superorder
from constants import EN, PL
from image import Image, License

O_VULGARIS = Species(
    name="Octopus vulgaris",
    local_names={EN: "common octopus", PL: "ośmiornica zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Octopus_vulgaris_Merculiano.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Octopus_vulgaris_Merculiano.jpg",
        author="Comingio Merculiano (1845-1915)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
G_UMBELLATA = Species(
    name="Grimpoteuthis umbellata",
    local_names={EN: "dumbo octopus"},
    known_for=[{EN: "swims using ear-like fins"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dumbo-hires_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Dumbo-hires_%28cropped%29.jpg",
        author="NOAA Okeanos Explorer",
        license=License.NOAA,
    ),
)
V_INFERNALIS = Species(
    name="Vampyroteuthis infernalis",
    local_names={EN: "vampire squid", PL: "wampirnica, wampirzyca piekielna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vampyroteuthis_infernalis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/64/Vampyroteuthis_infernalis.jpg",
        author="Carl Chun  (1852–1914)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
L_VULGARIS = Species(
    name="Loligo vulgaris",
    local_names={EN: "European squid, common squid", PL: "kalmar pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Loligo_vulgaris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Loligo_vulgaris.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
A_DUX = Species(
    name="Architeuthis dux",
    local_names={EN: "giant squid", PL: "kałamarnica olbrzymia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Architeuthis_dux_specimen_F_88555.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Architeuthis_dux_specimen_F_88555.jpg",
        author="Rodney Start, Museums Victoria",
        license=License.CC_BY_4_0,
    ),
)
M_HAMILTONI = Species(
    name="Mesonychoteuthis hamiltoni",
    local_names={EN: "colossal squid", PL: "kałamarnica kolosalna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Colossalsquid.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Colossalsquid.png",
        author="Throast",
        license=License.CC_BY_SA_4_0,
    ),
)
D_GIGAS = Species(
    name="Dosidicus gigas",
    local_names={EN: "Humboldt squid", PL: "kałamarnica Humboldta"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dosidicus_gigas.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/92/Dosidicus_gigas.jpg",
        author="Image courtesy of NOAA/MBARI 2006",
        license=License.NOAA,
    ),
)
S_OFFICINALIS = Species(
    name="Sepia officinalis",
    local_names={EN: "common cuttlefish", PL: "mątwa zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sepia_officinalis_2648.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Sepia_officinalis_2648.jpg",
        author="Amada44",
        license=License.CC_BY_SA_3_0,
    ),
)
N_POMPILIUS = Species(
    name="Nautilus pompilius",
    local_names={EN: "chambered nautilus, pearly nautilus", PL: "łodzik piękny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nautilus_pompilius_photo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Nautilus_pompilius_photo.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SEPPENRADENSIS = Species(
    name="Parapuzosia seppenradensis",
    known_for=[{EN: "the largest known ammonite"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Parapusozia_seppenradensis_32.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Parapusozia_seppenradensis_32.JPG",
        author="Ghedoghedo",
        license=License.CC_BY_SA_3_0,
    ),
)

OCTOPUS = Genus(name="Octopus", children=[O_VULGARIS])
GRIMPOTEUTHIS = Genus(name="Grimpoteuthis", children=[G_UMBELLATA])
VAMPYROTEUTHIS = Genus(name="Vampyroteuthis", children=[V_INFERNALIS])
LOLIGO = Genus(name="Loligo", children=[L_VULGARIS])
ARCHITEUTHIS = Genus(name="Architeuthis", children=[A_DUX])
MESONYCHOTEUTHIS = Genus("Mesonychoteuthis", children=[M_HAMILTONI])
DOSIDICUS = Genus(name="Dosidicus", children=[D_GIGAS])
SEPIA = Genus(name="Sepia", children=[S_OFFICINALIS])
NAUTILUS = Genus(name="Nautilus", children=[N_POMPILIUS])
PARAPUZOSIA = Genus(name="Parapuzosia", children=[P_SEPPENRADENSIS])

OCTOPODIDAE = Family(name="Octopodidae", children=[OCTOPUS])
OPISTHOTEUTHIDAE = Family(name="Opisthoteuthidae", children=[GRIMPOTEUTHIS])
VAMPYROTEUTHIDAE = Family(name="Vampyroteuthidae", children=[VAMPYROTEUTHIS])
LOLIGINIDAE = Family(name="Loliginidae", children=[LOLIGO])
ARCHITEUTHIDAE = Family(name="Architeuthidae", children=[ARCHITEUTHIS])
CRANCHIIDAE = Family(name="Cranchiidae", children=[MESONYCHOTEUTHIS])
OMMASTREPHIDAE = Family(name="Ommastrephidae", children=[DOSIDICUS])
SEPIIDAE = Family(name="Sepiidae", children=[SEPIA])
NAUTILIDAE = Family(name="Nautilidae", children=[NAUTILUS])
DESMOCERATIDAE = Family(name="Desmoceratidae", children=[PARAPUZOSIA])

OCTOPODA = Order(name="Octopoda", children=[OCTOPODIDAE, OPISTHOTEUTHIDAE])
VAMPYROMORPHIDA = Order(name="Vampyromorphida", children=[VAMPYROTEUTHIDAE])
MYOPSIDA = Order(name="Myopsida", children=[LOLIGINIDAE])
NAUTILIDA = Order(name="Nautilida", children=[NAUTILIDAE])
AMMONITIDA = Order(name="Ammonitida", children=[DESMOCERATIDAE])

DECAPODIFORMES_A = Clade(children=[ARCHITEUTHIDAE, CRANCHIIDAE])
DECAPODIFORMES_B = Clade(children=[DECAPODIFORMES_A, OMMASTREPHIDAE])
DECAPODIFORMES_C = Clade(children=[MYOPSIDA, SEPIIDAE])

OCTOPODIFORMES = Superorder(name="Octopodiformes", children=[OCTOPODA, VAMPYROMORPHIDA])
DECAPODIFORMES = Superorder(
    name="Decapodiformes", children=[DECAPODIFORMES_C, DECAPODIFORMES_B]
)

COLEOIDEA = Subclass(name="Coleoidea", children=[OCTOPODIFORMES, DECAPODIFORMES])
NAUTILOIDEA = Subclass(name="Nautiloidea", children=[NAUTILIDA])
AMMONOIDEA = Subclass(name="Ammonoidea", children=[AMMONITIDA])

# https://www.digitalatlasofancientlife.org/learn/mollusca/cephalopoda/ammonoidea/
CEPHALOPODA_A = Clade(children=[COLEOIDEA, AMMONOIDEA])

CEPHALOPODA = Class(name="Cephalopoda", children=[CEPHALOPODA_A, NAUTILOIDEA])
