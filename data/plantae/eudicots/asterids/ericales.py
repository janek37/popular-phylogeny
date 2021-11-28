from clade import Clade, Family, Genus, Order, Species, Subfamily, Subgenus, Tribe
from constants import EN, PL

B_EXCELSA = Species(
    name="Bertholletia excelsa",
    local_names={EN: "Brazil nut", PL: "orzesznica brazylijska, orzesznica wyniosła"},
    known_for=[{PL: "orzechy brazylijskie", EN: "edible nuts"}],
)
D_EBENUM = Species(
    name="Diospyros ebenum",
    local_names={EN: "Ceylon ebony", PL: "hebanowe drzewo, hurma hebanowa"},
    known_for=[{EN: "ebony, black wood", PL: "heban"}],
)
D_KAKI = Species(
    name="Diospyros kaki",
    local_names={EN: "Oriental persimmon", PL: "heban wiśniówka, hurma wschodnia"},
    known_for=[{EN: "kaki fruit", PL: "owoc kaki"}],
)
P_VULGARIS = Species(
    name="Primula vulgaris",
    local_names={EN: "common primrose", PL: "pierwiosnek bezłodygowy"},
)
C_SINENSIS = Species(
    name="Camellia sinensis",
    local_names={EN: "tea plant", PL: "herbata chińska"},
    known_for=[{EN: "tea", PL: "herbata"}],
)
C_JAPONICA = Species(
    name="Camellia japonica",
    local_names={EN: "common camellia", PL: "kamelia japońska"},
)
S_RUBRA = Species(
    name="Sarracenia rubra", local_names={EN: "sweet pitcherplant", PL: "kapturnica"}
)
A_DELICIOSA = Species(
    name="Actinidia deliciosa",
    local_names={EN: "fuzzy kiwifruit", PL: "aktinidia smakowita"},
    known_for=[{PL: "owoce kiwi"}],
)
C_VULGARIS = Species(
    name="Calluna vulgaris", local_names={EN: "common heather", PL: "wrzos zwyczajny"}
)
V_VITIS_IDAEA = Species(
    name="Vaccinium vitis-idaea",
    local_names={EN: "lingonberry, cowberry", PL: "borówka brusznica"},
)
V_OXYCOCCOS = Species(
    name="Vaccinium oxycoccos",
    local_names={EN: "small/common cranberry", PL: "żurawina błotna"},
)
V_MACROCARPON = Species(
    name="Vaccinium macrocarpon",
    local_names={EN: "large/American cranberry", PL: "żurawina wielkoowocowa"},
)
V_MYRTILLUS = Species(
    name="Vaccinium myrtillus",
    local_names={
        EN: "European blueberry, bilberry",
        PL: "czarna jagoda, czernica, borówka czarna",
    },
)
V_CORYMBOSUM = Species(
    name="Vaccinium corymbosum",
    local_names={
        EN: "northern highbush blueberry",
        PL: "borówka amerykańska, borówka wysoka",
    },
)
R_NOVA_ZEMBLA = Species(
    name="Rhododendron Nova Zembla",
    local_names={PL: "rododendron, różanecznik wielkokwiatowy Nova Zembla"},
)

# possibly vitis-idaea should be closest to macrocarpon? conflicting data
VACCINIUM_SUBGENUS_OXYCOCCUS = Subgenus(
    name="Vaccinium subg. Oxycoccus", children=[V_OXYCOCCOS, V_MACROCARPON]
)
VACCINIUM_SUBGENUS_VACCINIUM = Subgenus(
    name="Vaccinium subg. Vaccinium",
    children=[V_VITIS_IDAEA, V_MYRTILLUS, V_CORYMBOSUM],
)

BERTHOLLETIA = Genus(name="Bertholletia", children=[B_EXCELSA])
DIOSPYROS = Genus(name="Diospyros", children=[D_EBENUM, D_KAKI])
PRIMULA = Genus(name="Primula", children=[P_VULGARIS])
CAMELLIA = Genus(name="Camelia", children=[C_SINENSIS, C_JAPONICA])
SARRACENIA = Genus(name="Sarracenia", children=[S_RUBRA])
ACTINIDIA = Genus(name="Actinidia", children=[A_DELICIOSA])
CALLUNA = Genus(name="Calluna", children=[C_VULGARIS])
VACCINIUM = Genus(
    name="Vaccinium",
    children=[VACCINIUM_SUBGENUS_VACCINIUM, VACCINIUM_SUBGENUS_OXYCOCCUS],
)
RHODODENDRON = Genus(name="Rhododendron", children=[R_NOVA_ZEMBLA])

ERICEAE = Tribe(name="Ericeae", children=[CALLUNA])
VACCINIEAE = Tribe(name="Vaccinieae", children=[V_VITIS_IDAEA])
RHODOREAE = Tribe(name="Rhodoreae", children=[RHODODENDRON])

LECYTHIDOIDEAE = Subfamily(name="Lecythidoideae", children=[BERTHOLLETIA])
PRIMULOIDEAE = Subfamily(name="Primuloideae", children=[PRIMULA])
ERICOIDEAE = Subfamily(name="Ericoideae", children=[ERICEAE, RHODOREAE])
VACCINIOIDEAE = Subfamily(name="Vaccinioideae", children=[VACCINIEAE])

LECYTHIDACEAE = Family(name="Lecythidaceae", children=[LECYTHIDOIDEAE])
EBANACEAE = Family(name="Ebanaceae", children=[DIOSPYROS])
PRIMULACEAE = Family(name="Primulaceae", children=[PRIMULOIDEAE])
THEACEAE = Family(name="Theaceae", children=[CAMELLIA])
SARRACENIACEAE = Family(name="Sarraceniaceae", children=[SARRACENIA])
ACTINIDIACEAE = Family(name="Actinidiaceae", children=[ACTINIDIA])
ERICACEAE = Family(name="Ericaceae", children=[ERICOIDEAE, VACCINIOIDEAE])

PRIMULOIDS = Clade(name="primuloids", children=[EBANACEAE, PRIMULACEAE])
SARRACENIOIDS = Clade(name="sarracenioids", children=[SARRACENIACEAE, ACTINIDIACEAE])

ERICALES_A = Clade(children=[ERICACEAE, SARRACENIOIDS])
ERICALES_B = Clade(children=[ERICALES_A, THEACEAE])
ERICALES_C = Clade(children=[ERICALES_B, PRIMULOIDS])

ERICALES = Order(name="Ericales", children=[LECYTHIDACEAE, ERICALES_C])
