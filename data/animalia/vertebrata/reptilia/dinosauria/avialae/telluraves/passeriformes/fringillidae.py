from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, PL

F_COELEBS = Species(
    name="Fringilla coelebs",
    local_names={EN: "common chaffinch", PL: "zięba zwyczajna"},
)
P_PYRRHULA = Species(
    name="Pyrrhula pyrrhula",
    local_names={EN: "Eurasian bullfinch", PL: "gil zwyczajny"},
)
L_CANNABINA = Species(
    name="Linaria cannabina",
    local_names={EN: "common linnet", PL: "makolągwa zwyczajna"},
)
C_CARDUELIS = Species(
    name="Carduelis carduelis", local_names={EN: "European goldfinch", PL: "szczygieł"}
)
S_CANARIA = Species(
    name="Serinus canaria",
    local_names={EN: "wild cannary, common cannary, Atlantic cannary", PL: "kanarek"},
)
S_SPINUS = Species(
    name="Spinus spinus",
    local_names={EN: "Eurasian siskin, common siskin", PL: "czyżyk, czyż zwyczajny"},
)
S_TRISTIS = Species(
    name="Spinus tristis", local_names={EN: "American goldfinch", PL: "czyż złotawy"}
)

FRINGILLA = Genus(name="Fringilla", children=[F_COELEBS])
PYRRHULA = Genus(name="Pyrrhula", children=[P_PYRRHULA])
LINARIA = Genus(name="Linaria", children=[L_CANNABINA])
CARDUELIS = Genus(name="Carduelis", children=[C_CARDUELIS])
SERINUS = Genus(name="Serinus", children=[S_CANARIA])
SPINUS = Genus(name="Spinus", children=[S_SPINUS, S_TRISTIS])

CARDUELINAE_A = Clade(children=[SERINUS, SPINUS])
CARDUELINAE_B = Clade(children=[CARDUELIS, CARDUELINAE_A])
CARDUELINAE_C = Clade(children=[LINARIA, CARDUELINAE_B])

FRINGILLINAE = Subfamily(name="Fringillinae", children=[FRINGILLA])
CARDUELINAE = Subfamily(name="Carduelinae", children=[PYRRHULA, CARDUELINAE_C])

FRINGILLIDAE = Family(name="Fringillidae", children=[FRINGILLINAE, CARDUELINAE])
