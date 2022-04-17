from clade import Clade, Family, Genus, Parvorder, Species, Superfamily
from constants import EN, PL

B_GARRULUS = Species(
    name="Bombycilla garrulus",
    local_names={EN: "Bohemian waxwing", PL: "jemiołuszka zwyczajna"},
)
E_RUBECULA = Species(
    name="Erithacus rubecula", local_names={EN: "European robin", PL: "rudzik"}
)
L_MEGARHYNCHOS = Species(
    name="Luscinia megarhynchos",
    local_names={EN: "common nightingale", PL: "słowik rdzawy"},
)
S_SIALIS = Species(
    name="Sialia sialis",
    local_names={EN: "eastern bluebird", PL: "błękitnik rudogardły"},
)
T_PHILOMELOS = Species(
    name="Turdus philomelos", local_names={EN: "song thrush", PL: "drozd śpiewak"}
)
T_VISCIVORUS = Species(
    name="Turdus viscivorus", local_names={EN: "mistle thrush", PL: "paszkot"}
)
T_MIGRATORIUS = Species(
    name="Turdus migratorius", local_names={EN: "American robin", PL: "drozd wędrowny"}
)
T_MERULA = Species(
    name="Turdus merula", local_names={EN: "common blackbird", PL: "kos"}
)
S_VULGARIS = Species(
    name="Sturnus vulgaris", local_names={EN: "common starling", PL: "szpak zwyczajny"}
)
M_POLYGLOTTOS = Species(
    name="Mimus polyglottos",
    local_names={EN: "northern mockingbird", PL: "przedrzeźniacz północny"},
    known_for=[{EN: "To Kill a Mockingbird"}],
)
R_REGULUS = Species(
    name="Regulus regulus", local_names={EN: "goldcrest", PL: "mysikrólik zwyczajny"}
)
S_EUROPAEA = Species(
    name="Sitta europaea",
    local_names={EN: "Eurasian nuthatch, wood nuthatch", PL: "kowalik zwyczajny"},
)
T_TROGLODYTES = Species(
    name="Troglodytes troglodytes",
    local_names={EN: "Eurasian wren", PL: "strzyżyk zwyczajny"},
)

# https://royalsocietypublishing.org/doi/10.1098/rspb.2019.2400
TURDUS_A = Clade(children=[T_MIGRATORIUS, T_MERULA])
TURDUS_B = Clade(children=[T_VISCIVORUS, TURDUS_A])

BOMBYCILLA = Genus(name="Bombycilla", children=[B_GARRULUS])
ERITHACUS = Genus(name="Erithacus", children=[E_RUBECULA])
LUSCINIA = Genus(name="Luscinia", children=[L_MEGARHYNCHOS])
SIALIA = Genus(name="Sialia", children=[S_SIALIS])
TURDUS = Genus(name="Turdus", children=[T_PHILOMELOS, TURDUS_B])
STURNUS = Genus(name="Sturnus", children=[S_VULGARIS])
MIMUS = Genus(name="Mimus", children=[M_POLYGLOTTOS])
REGULUS = Genus(name="Regulus", children=[R_REGULUS])
SITTA = Genus(name="Sitta", children=[S_EUROPAEA])
TROGLODYTES = Genus(name="Troglodytes", children=[T_TROGLODYTES])

BOMBYCILLIDAE = Family(name="Bombycillidae", children=[BOMBYCILLA])
MUSCICAPIDAE = Family(name="Muscicapidae", children=[ERITHACUS, LUSCINIA])
TURDIDAE = Family(name="Turdidae", children=[SIALIA, TURDUS])
STURNIDAE = Family(name="Sturnidae", children=[STURNUS])
MIMIDAE = Family(name="Mimidae", children=[MIMUS])
REGULIDAE = Family(name="Regulidae", children=[REGULUS])
SITTIDAE = Family(name="Sittidae", children=[SITTA])
TROGLODYTIDAE = Family(name="Troglodytidae", children=[TROGLODYTES])

MUSCICAPOIDEA_A = Clade(children=[MUSCICAPIDAE, TURDIDAE])
MUSCICAPOIDEA_B = Clade(children=[STURNIDAE, MIMIDAE])

BOMBYCILLOIDEA = Superfamily(name="Bombycilloidea", children=[BOMBYCILLIDAE])
MUSCICAPOIDEA = Superfamily(
    name="Muscicapoidea", children=[MUSCICAPOIDEA_A, MUSCICAPOIDEA_B]
)
CERTHIOIDEA = Superfamily(name="Certhioidea", children=[SITTIDAE, TROGLODYTIDAE])

MUSCICAPIDA_A = Clade(children=[REGULIDAE, CERTHIOIDEA])
MUSCICAPIDA_B = Clade(children=[MUSCICAPOIDEA, MUSCICAPIDA_A])

MUSCICAPIDA = Parvorder(name="Muscicapida", children=[BOMBYCILLOIDEA, MUSCICAPIDA_B])
