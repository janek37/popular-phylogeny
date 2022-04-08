from clade import Clade, Family, Genus, Parvorder, Species, Superfamily
from constants import EN, PL

from .fringillidae import FRINGILLIDAE

P_DOMESTICUS = Species(
    name="Passer domesticus", local_names={EN: "house sparrow", PL: "wróbel zwyczajny"}
)
M_ALBA = Species(
    name="Motacilla alba",
    local_names={EN: "white wagtail, pied wagtail, water wagtail", PL: "pliszka siwa"},
)
M_CINEREA = Species(
    name="Motacilla cinerea", local_names={EN: "grey wagtail", PL: "pliszka górska"}
)
E_CITRINELLA = Species(
    name="Emberiza citrinella",
    local_names={EN: "yellowhammer", PL: "trznadel zwyczajny"},
)
G_MAGNIROSTRIS = Species(
    name="Geospiza magnirostris",
    local_names={EN: "large ground finch", PL: "darwinka wielkodzioba"},
    known_for=[{EN: "one of Darwin's finches"}],
)
C_PARVULUS = Species(
    name="Camarhynchus parvulus",
    local_names={EN: "small tree finch", PL: "kłowacz mały"},
    known_for=[{EN: "one of Darwin's finches"}],
)
C_OLIVACEA = Species(
    name="Certhidea olivacea",
    local_names={EN: "green warbler-finch", PL: "owadziarka zielona"},
    known_for=[{EN: "one of Darwin's finches"}],
)
C_CARDINALIS = Species(
    name="Cardinalis cardinalis",
    local_names={EN: "northern cardinal", PL: "kardynał szkarłatny"},
)
S_NEGLECTA = Species(
    name="Sturnella neglecta",
    local_names={EN: "western meadowlark", PL: "wojak żółtogardły"},
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
