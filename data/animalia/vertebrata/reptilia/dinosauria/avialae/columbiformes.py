from clade import Family, Genus, Order, Species, Subfamily
from constants import EN, PL

C_LIVIA = Species(
    name="Columba livia",
    local_names={EN: "rock dove, rock pigeon, common pigeon", PL: "gołąb skalny"},
    known_for=[
        {EN: "domestic pigeon"},
        {EN: "homing pigeon", PL: "gołąb pocztowy"},
        {EN: "ciy pigeon, feral pigeon", PL: "gołąb miejski"},
    ],
)
R_CUCULLATUS = Species(
    name="Raphus cucullatus", local_names={EN: "dodo", PL: "dront dodo"}
)
S_DECAOCTO = Species(
    name="Streptopelia decaocto",
    local_names={EN: "Eurasian collared dove", PL: "synogarlica turecka, sierpówka"},
)
S_TURTUR = Species(
    name="Streptopelia turtur",
    local_names={EN: "European turtle dove", PL: "turkawka zwyczajna"},
)

COLUMBA = Genus(name="Columba", children=[C_LIVIA])
RAPHUS = Genus(name="Raphus", children=[R_CUCULLATUS])
STREPTOPELIA = Genus(name="Streptopelia", children=[S_DECAOCTO, S_TURTUR])

COLUMBINAE = Subfamily(name="Columbinae", children=[COLUMBA, STREPTOPELIA])
RAPHINAE = Subfamily(name="Raphinae", children=[RAPHUS])

COLUMBIDAE = Family(name="Columbidae", children=[COLUMBINAE, RAPHINAE])

COLUMBIFORMES = Order(name="Columbiformes", children=[COLUMBIDAE])
