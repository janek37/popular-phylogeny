from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

from .piciformes import PICIFORMES

U_EPOPS = Species(
    name="Upupa epops", local_names={EN: "Eurasian hoopoe", PL: "dudek zwyczajny"}
)
B_BICORNIS = Species(
    name="Buceros bicornis",
    local_names={EN: "great hornbill", PL: "dzioborożec wielki"},
)
T_ERYTHRORHYNCHUS = Species(
    name="Tockus rufirostris",
    local_names={EN: "southern red-billed hornbill", PL: "toko białogrzbiety"},
    known_for=[{EN: "Zazu from The Lion King"}],
)
A_ATTHIS = Species(
    name="Alcedo atthis",
    local_names={EN: "common kingfisher", PL: "zimorodek zwyczajny"},
)
C_GARRULUS = Species(
    name="Coracias garrulus",
    local_names={EN: "European roller", PL: "kraska zwyczajna"},
)

UPUPA = Genus(name="Upupa", children=[U_EPOPS])
BUCEROS = Genus(name="Buceros", children=[B_BICORNIS])
TOCKUS = Genus(name="Tockus", children=[T_ERYTHRORHYNCHUS])
ALCEDO = Genus(name="Alcedo", children=[A_ATTHIS])
CORACIAS = Genus(name="Coracias", children=[C_GARRULUS])

UPUPIDAE = Family(name="Upupidae", children=[UPUPA])
BUCEROTIDAE = Family(name="Bucerotidae", children=[BUCEROS, TOCKUS])
ALCEDINIDAE = Family(name="Alcedinidae", children=[ALCEDO])
CORACIIDAE = Family(name="Coraciidae", children=[CORACIAS])

BUCEROTIFORMES = Order(name="Bucerotiformes", children=[UPUPIDAE, BUCEROTIDAE])
CORACIIFORMES = Order(name="Coraciiformes", children=[ALCEDINIDAE, CORACIIDAE])

PICODYNASTORNITHES = Clade(
    name="Picodynastornithes", children=[CORACIIFORMES, PICIFORMES]
)

CORACIIMORPHAE = Clade(
    name="Coraciimorphae", children=[BUCEROTIFORMES, PICODYNASTORNITHES]
)
