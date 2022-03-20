from clade import Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL

S_CAFFER = Species(
    name="Syncerus caffer", local_names={EN: "African buffalo", PL: "bawół afrykański"}
)
B_ARNEE = Species(
    name="Bubalus arnee",
    local_names={EN: "wild water buffalo", PL: "bawół indyjski, arni azjatycki"},
)
B_BUBALIS = Species(
    name="Bubalus bubalis",
    local_names={EN: "domestic water buffalo", PL: "wół domowy"},
    known_for=[{EN: "mozzarella"}],
)
B_BONASUS = Species(
    name="Bison bonasus",
    local_names={EN: "European bison, wisent, zubr", PL: "żubr europejski"},
)
B_BISON = Species(
    name="Bison bison", local_names={EN: "American bison", PL: "bizon amerykański"}
)
B_GRUNNIENS = Species(
    name="Bos grunniens", local_names={EN: "domestic yak", PL: "jak udomowiony"}
)
B_PRIMIGENIUS = Species(
    name="Bos primigenius", local_names={EN: "aurochs", PL: "tur leśny"}, extinct=True
)
B_TAURUS = Species(name="Bos taurus", local_names={EN: "cattle", PL: "bydło domowe"})
B_INDICUS = Species(
    name="Bos indicus",
    local_names={
        EN: "zebu, indicine cattle, humped cattle",
        PL: "bydło domowe garbaty, zebu indyjskie",
    },
    known_for=[
        {EN: "venerated within the Hindu religion", PL: "święte krowy w hinduizmie"}
    ],
)

BISON = Subgenus(name="Bison", children=[B_BONASUS, B_BISON])
BOS_SUBGENUS_POEPHAGUS = Subgenus(name="Bos subg. Poephagus", children=[B_GRUNNIENS])
# unresolved
BOS_SUBGENUS_BOS = Subgenus(
    name="Bos subg. Bos", children=[B_PRIMIGENIUS, B_TAURUS, B_INDICUS]
)

SYNCERUS = Genus(name="Syncerus", children=[S_CAFFER])
BUBALUS = Genus(name="Bubalus", children=[B_ARNEE, B_BUBALIS])
# unresolved
BOS = Genus(name="Bos", children=[BISON, BOS_SUBGENUS_POEPHAGUS, BOS_SUBGENUS_BOS])

BUBALINA = Subtribe(name="Bubalina", children=[SYNCERUS, BUBALUS])
BOVINA = Subtribe(name="Bovina", children=[BISON, BOS])

BOVINI = Tribe(name="Bovini", children=[BUBALINA, BOVINA])

BOVINAE = Subfamily(name="Bovinae", children=[BOVINI])
