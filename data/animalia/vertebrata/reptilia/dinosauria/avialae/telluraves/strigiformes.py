from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

B_BUBO = Species(
    name="Bubo bubo", local_names={EN: "eurasian eagle-owl", PL: "puchacz zwyczajny"}
)
B_VIRGINIANUS = Species(
    name="Bubo virginianus",
    local_names={EN: "great horned owl, tiger owl", PL: "puchacz wirginijski"},
)
B_SCANDIACUS = Species(
    name="Bubo scandiacus",
    local_names={EN: "snowy owl", PL: "sowa śnieżna, puchacz śnieżny"},
)
S_ALUCO = Species(
    name="Strix aluco",
    local_names={EN: "tawny owl, brown owl", PL: "puszczyk zwyczajny"},
)
A_NOCTUA = Species(
    name="Athene noctua",
    local_names={EN: "little owl", PL: "pójdźka zwyczajna"},
    known_for=[{EN: "owl of Athena/Minerva"}],
)
A_OTUS = Species(
    name="Asio otus",
    local_names={EN: "long-eared owl, cat owl", PL: "uszatka zwyczajna"},
)
T_ALBA = Species(
    name="Tyto alba", local_names={EN: "barn owl", PL: "płomykówka zwyczajna"}
)

# https://www.sciencedirect.com/science/article/abs/pii/S1055790312004642
BUBO_A = Clade(children=[B_VIRGINIANUS, B_SCANDIACUS])

BUBO = Genus(name="Bubo", children=[B_BUBO, BUBO_A])
STRIX = Genus(name="Strix", children=[S_ALUCO])
ATHENE = Genus(name="Athene", children=[A_NOCTUA])
ASIO = Genus(name="Asio", children=[A_OTUS])
TYTO = Genus(name="Tyto", children=[T_ALBA])

STRIGIDAE_A = Clade(children=[BUBO, STRIX])
STRIGIDAE_B = Clade(children=[STRIGIDAE_A, ASIO])

STRIGIDAE = Family(name="Strigidae", children=[STRIGIDAE_B, ATHENE])
TYTONIDAE = Family(name="Tytonidae", children=[TYTO])

STRIGIFORMES = Order(name="Strigiformes", children=[STRIGIDAE, TYTONIDAE])
