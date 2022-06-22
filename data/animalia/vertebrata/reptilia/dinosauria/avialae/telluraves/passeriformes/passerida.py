from clade import Clade, Family, Genus, Parvorder, Species, Superfamily
from constants import EN, PL
from image import Image, License

from .fringillidae import FRINGILLIDAE

P_DOMESTICUS = Species(
    name="Passer domesticus",
    local_names={EN: "house sparrow", PL: "wróbel zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Passer_domesticus_-_House_sparrow_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Passer_domesticus_-_House_sparrow_02.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
M_ALBA = Species(
    name="Motacilla alba",
    local_names={EN: "white wagtail, pied wagtail, water wagtail", PL: "pliszka siwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Motacilla_Alba_Oulu_20200501_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Motacilla_Alba_Oulu_20200501_01.jpg",
        author="Estormiz",
        license=License.CC0,
    ),
)
M_CINEREA = Species(
    name="Motacilla cinerea",
    local_names={EN: "grey wagtail", PL: "pliszka górska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Grey_Wagtail_Motacilla_cinerea,_Nepal_19_cm.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Grey_Wagtail_Motacilla_cinerea%2C_Nepal_19_cm.jpg",
        author="Nrik kiran",
        license=License.CC_BY_SA_4_0,
    ),
)
E_CITRINELLA = Species(
    name="Emberiza citrinella",
    local_names={EN: "yellowhammer", PL: "trznadel zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Goldammer_Emberiza_citrinella_(cropped,_mirrored_and_retouched).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Goldammer_Emberiza_citrinella_%28cropped%2C_mirrored_and_retouched%29.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
G_MAGNIROSTRIS = Species(
    name="Geospiza magnirostris",
    local_names={EN: "large ground finch", PL: "darwinka wielkodzioba"},
    known_for=[{EN: "one of Darwin's finches"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Large_ground_finch_(4229035966).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Large_ground_finch_%284229035966%29.jpg",
        author="Peter Wilton",
        license=License.CC_BY_2_0,
    ),
)
C_PARVULUS = Species(
    name="Camarhynchus parvulus",
    local_names={EN: "small tree finch", PL: "kłowacz mały"},
    known_for=[{EN: "one of Darwin's finches"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Geospiza_parvula.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/53/Geospiza_parvula.jpg",
        author="John Gould",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_OLIVACEA = Species(
    name="Certhidea olivacea",
    local_names={EN: "green warbler-finch", PL: "owadziarka zielona"},
    known_for=[{EN: "one of Darwin's finches"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Certhidea_olivacea_-_Green_Wabler_Finch.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Certhidea_olivacea_-_Green_Wabler_Finch.jpg",
        author="2000 - Paul McFarling, Charles Darwin Foundation",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CARDINALIS = Species(
    name="Cardinalis cardinalis",
    local_names={EN: "northern cardinal", PL: "kardynał szkarłatny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cardinalis_cardinalis_(Northern_Cardinal)_11.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Cardinalis_cardinalis_%28Northern_Cardinal%29_11.jpg",
        author="gary_leavens",
        license=License.CC_BY_SA_2_0,
    ),
)
S_NEGLECTA = Species(
    name="Sturnella neglecta",
    local_names={EN: "western meadowlark", PL: "wojak żółtogardły"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Western_Meadowlark_(Sturnella_neglecta)_(7063379033)_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Western_Meadowlark_%28Sturnella_neglecta%29_%287063379033%29_%28cropped%29.jpg",
        author="Steve Berardi from Long Beach, CA, United States",
        license=License.CC_BY_SA_2_0,
    ),
)

PASSER = Genus(name="Passer", children=[P_DOMESTICUS])
MOTACILLA = Genus(name="Motacilla", children=[M_ALBA, M_CINEREA])
EMBERIZA = Genus(name="Emberiza", children=[E_CITRINELLA])
GEOSPIZA = Genus(name="Geospiza", children=[G_MAGNIROSTRIS])
CAMARHYNCHUS = Genus(name="Camarhynchus", children=[C_PARVULUS])
CERTHIDEA = Genus(name="Certhidea", children=[C_OLIVACEA])
CARDINALIS = Genus(name="Cardinalis", children=[C_CARDINALIS])
STURNELLA = Genus(name="Sturnella", children=[S_NEGLECTA])

THAUPIDAE_A = Clade(children=[GEOSPIZA, CAMARHYNCHUS])

PASSERIDAE = Family(name="Passeridae", children=[PASSER])
MOTACILLIDAE = Family(name="Motacillidae", children=[MOTACILLA])
EMBERIZIDAE = Family(name="Emberizidae", children=[EMBERIZA])
THRAUPIDAE = Family(name="Thraupidae", children=[THAUPIDAE_A, CERTHIDEA])
CARDINALIDAE = Family(name="Cardinalidae", children=[CARDINALIS])
ICTERIDAE = Family(name="Icteridae", children=[STURNELLA])

EMBERIZOIDEA_B = Clade(children=[THRAUPIDAE, CARDINALIDAE])
EMBERIZOIDEA_A = Clade(children=[ICTERIDAE, EMBERIZOIDEA_B])

EMBERIZOIDEA = Superfamily(name="Emberizoidea", children=[EMBERIZIDAE, EMBERIZOIDEA_A])

PASSERIDA_A = Clade(children=[FRINGILLIDAE, EMBERIZOIDEA])
PASSERIDA_B = Clade(children=[MOTACILLIDAE, PASSERIDA_A])

PASSERIDA = Parvorder(name="Passerida", children=[PASSERIDAE, PASSERIDA_B])
