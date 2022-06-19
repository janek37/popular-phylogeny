from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily
from constants import EN, PL, URL
from image import Image, License

P_MOLURUS = Species(
    name="Python molurus",
    local_names={EN: "Indian python", PL: "pyton tygrysi"},
    known_for=[
        {EN: "Kaa from The Jungle Book", URL: "https://en.wikipedia.org/wiki/Kaa"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Python,_IIT_Bombay.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Python%2C_IIT_Bombay.JPG",
        author="Sobarwiki",
        license=License.PUBLIC_DOMAIN_LINK,
    ),
)
P_REGIUS = Species(
    name="Python regius",
    local_names={EN: "ball python, royal python", PL: "pyton królewski"},
    known_for=[{EN: "most common pet snake"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ball_python_lucy.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Ball_python_lucy.JPG",
        author="Mokele (talk)",
        license=License.CC_BY_SA_3_0,
    ),
)
B_CONSTRICTOR = Species(
    name="Boa constrictor",
    local_names={EN: "boa constrictor", PL: "boa dusiciel"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:B._constrictor.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/B._constrictor.jpg",
        author="Luis Alejandro Rodriguez J.",
        license=License.CC_BY_SA_4_0,
    ),
)
E_MURINUS = Species(
    name="Eunectes murinus",
    local_names={EN: "green anaconda", PL: "anakonda zielona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sucuri_verde.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Sucuri_verde.jpg",
        author="MKAMPIS",
        license=License.CC_BY_SA_4_0,
    ),
)
E_NOTAEUS = Species(
    name="Eunectes notaeus",
    local_names={EN: "yellow anaconda", PL: "anakonda żółta"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zoo_Ohrada,_anakonda_%C5%BElut%C3%A1_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Zoo_Ohrada%2C_anakonda_%C5%BElut%C3%A1_01.jpg",
        author="Czeva",
        license=License.CC_BY_SA_3_0,
    ),
)
V_BERUS = Species(
    name="Vipera berus",
    local_names={
        EN: "black adder, common European adder/viper",
        PL: "żmija zygzakowata",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vipera_berus_7434.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Vipera_berus_7434.jpg",
        author="wikipedysta Astrum (Mirella Liszka)",
        license=License.CC_BY_SA_2_5,
    ),
)
C_VIRIDIS = Species(
    name="Crotalus viridis",
    local_names={EN: "prairie rattlesnake", PL: "grzechotnik preriowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crotalus_viridis_02_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/02/Crotalus_viridis_02_%28cropped%29.jpg",
        author="Gary M. Stolz, U.S. Fish and Wildlife Service",
        license=License.FWS,
    ),
)
P_GUTTATUS = Species(
    name="Pantherophis guttatus",
    local_names={EN: "corn snake", PL: "wąż zbożowy"},
    known_for=[{EN: "second most common pet snake"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Corn_Snake_Adult.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Corn_Snake_Adult.jpg",
        author="Glenn Bartolotti",
        license=License.CC_BY_SA_4_0,
    ),
)
Z_LONGISSIMUS = Species(
    name="Zamenis longissimus",
    local_names={EN: "Aesculapian snake", PL: "wąż Eskulapa"},
    known_for=[{EN: "Rod of Asclepius", PL: "laska Eskulapa"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zamenis_longissimus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Zamenis_longissimus.jpg",
        author="FelixReimann",
        license=License.CC_BY_SA_3_0,
    ),
)
N_NATRIX = Species(
    name="Natrix natrix",
    local_names={EN: "grass snake, rigged snake", PL: "zaskroniec zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nastik_-_Grass_snake_-_Natrix_natrix_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Nastik_-_Grass_snake_-_Natrix_natrix_%282%29.jpg",
        author="Kristian Pikner",
        license=License.CC_BY_SA_4_0,
    ),
)
N_NAJA = Species(
    name="Naja naja",
    local_names={EN: "Indian cobra, spectacled cobra", PL: "okularnik, kobra indyjska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Indian_Cobra_Naja_naja_by_Dr_Raju_Kasambe_DSCN4991_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Indian_Cobra_Naja_naja_by_Dr_Raju_Kasambe_DSCN4991_%282%29.jpg",
        author="Dr. Raju Kasambe",
        license=License.CC_BY_SA_4_0,
    ),
)
M_FULVIUS = Species(
    name="Micrurus fulvius",
    local_names={
        EN: "eastern coral snake, common coral snake",
        PL: "wąż koralowy arlekin, koralówka arlekin",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Micrurus_fulviusHolbrookV3P10AA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Micrurus_fulviusHolbrookV3P10AA.jpg",
        author="Holbrook, John Edwards, 1794-1871 (English Wikipedia)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
O_HANNAH = Species(
    name="Ophiophagus hannah",
    local_names={EN: "king cobra", PL: "kobra królewska"},
    known_for=[{EN: "the longest venomous snake"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:12_-_The_Mystical_King_Cobra_and_Coffee_Forests.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/12_-_The_Mystical_King_Cobra_and_Coffee_Forests.jpg",
        author="Michael Allen Smith from Seattle, USA",
        license=License.CC_BY_SA_2_0,
    ),
)
D_POLYLEPIS = Species(
    name="Dendroaspis polylepis",
    local_names={EN: "black mamba", PL: "mamba czarna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dendroaspis_polylepis_(6).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Dendroaspis_polylepis_%286%29.jpg",
        author="TimVickers",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)

PYTHON = Genus(name="Python", children=[P_MOLURUS, P_REGIUS])
BOA = Genus(name="Boa", children=[B_CONSTRICTOR])
EUNECTES = Genus(name="Eunectes", children=[E_MURINUS, E_NOTAEUS])
VIPERA = Genus(name="Vipera", children=[V_BERUS])
CROTALUS = Genus(name="Crotalus", children=[C_VIRIDIS])
PANTHEROPHIS = Genus(name="Pantherophis", children=[P_GUTTATUS])
ZAMENIS = Genus(name="Zamenis", children=[Z_LONGISSIMUS])
NATRIX = Genus(name="Natrix", children=[N_NATRIX])
NAJA = Genus(name="Naja", children=[N_NAJA])
MICRURUS = Genus(name="Micrurus", children=[M_FULVIUS])
OPHIOPHAGUS = Genus(name="Ophiophagus", children=[O_HANNAH])
DENDROASPIS = Genus(name="Dendroaspis", children=[D_POLYLEPIS])

COLUBRINAE = Subfamily(name="Colubrinae", children=[PANTHEROPHIS, ZAMENIS])
NATRICINAE = Subfamily(name="Natricinae", children=[NATRIX])

PYTHONIDAE = Family(name="Pythonidae", children=[PYTHON])
BOIDAE = Family(name="Boidae", children=[BOA, EUNECTES])
VIPERIDAE = Family(name="Viperidae", children=[VIPERA, CROTALUS])
COLUBRIDAE = Family(name="Colubridae", children=[COLUBRINAE, NATRICINAE])
# unresolved for now
ELAPIDAE = Family(name="Elapidae", children=[NAJA, MICRURUS, OPHIOPHAGUS, DENDROASPIS])

PROTEROGLYPHA = Clade(name="Proteroglypha", children=[COLUBRIDAE, ELAPIDAE])

BOOIDEA = Superfamily(name="Booidea", children=[PYTHONIDAE, BOIDAE])
COLUBROIDEA = Superfamily(name="Colubroidea", children=[VIPERIDAE, PROTEROGLYPHA])

SERPENTES = Suborder(name="Serpentes", children=[BOOIDEA, COLUBROIDEA])
