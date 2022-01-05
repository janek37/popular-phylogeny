from clade import Family, Genus, Order, Species, Subfamily, Subtribe, Tribe
from constants import EN, PL

L_SICERARIA = Species(
    name="Lagenaria siceraria",
    local_names={EN: "calabash, bottle gourd", PL: "tykwa pospolita"},
)
C_LANATUS = Species(
    name="Citrullus lanatus", local_names={EN: "watermelon", PL: "arbuz zwyczajny"}
)
C_SATIVUS = Species(
    name="Cucumis sativus", local_names={EN: "cucumber", PL: "ogórek siewny"}
)
C_MELO = Species(
    name="Cucumis melo",
    local_names={EN: "melon, muskmelon", PL: "melon cukrowy, ogórek melon"},
    known_for=[
        {EN: "cataloupe", PL: "kantalupa"},
        {EN: "honedew", PL: "melon spadziowy"},
    ],
)
C_PEPO = Species(
    name="Cucurbita pepo",
    local_names={PL: "dynia zwyczajna"},
    known_for=[
        {EN: "pumpkin", PL: "dynia"},
        {EN: "pattypan squash, scallop squash", PL: "patison"},
        {EN: "zucchini, courgette", PL: "cukinia, kabaczek"},
    ],
)
C_MOSCHATA = Species(
    name="Cucurbita moschata",
    local_names={PL: "dynia piżmowa"},
    known_for=[{EN: "butternut squash"}],
)
B_OBLIQUA = Species(
    name="Begonia × tuberhybrida",
    local_names={PL: "begonia bulwiasta", EN: "tuberous begonia"},
)

LAGENARIA = Genus(name="Lagenaria", children=[L_SICERARIA])
CITRULLUS = Genus(name="Citrullus", children=[C_LANATUS])
CUCUMIS = Genus(name="Cucumis", children=[C_SATIVUS, C_MELO])
CUCURBITA = Genus(name="Cucurbita", children=[C_PEPO, C_MOSCHATA])
BEGONIA = Genus(name="Begonia", children=[B_OBLIQUA])

BENINCASINAE = Subtribe(name="Benincasinae", children=[LAGENARIA, CITRULLUS])

BENINCASEAE = Tribe(name="Benincaseae", children=[BENINCASINAE, CUCUMIS])
CUCURBITEAE = Tribe(name="Cucurbiteae", children=[CUCURBITA])

CUCURBITOIDEAE = Subfamily(name="Cucurbitoideae", children=[BENINCASEAE])

CUCURBITACEAE = Family(name="Cucurbitaceae", children=[CUCURBITOIDEAE, CUCURBITEAE])
BEGONIACEAE = Family(name="Begoniaceae", children=[BEGONIA])

CUCURBITALES = Order(name="Cucurbitales", children=[CUCURBITACEAE, BEGONIACEAE])
