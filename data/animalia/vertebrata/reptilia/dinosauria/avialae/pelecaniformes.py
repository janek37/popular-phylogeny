from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

P_ONOCROTALUS = Species(
    name="Pelecanus onocrotalus",
    local_names={EN: "great white pelican", PL: "pelikan różowy"},
)
A_CINEREA = Species(
    name="Ardea cinerea", local_names={EN: "grey heron", PL: "czapla siwa"}
)
N_NYCTICORAX = Species(
    name="Nycticorax nycticorax",
    local_names={EN: "black-crowned night heron", PL: "ślepowron zwyczajny"},
)
T_AETHIOPICUS = Species(
    name="Threskiornis aethiopicus",
    local_names={EN: "African sacred ibis", PL: "ibis czczony"},
)
B_REX = Species(
    name="Balaeniceps rex", local_names={EN: "shoebill, whalehead", PL: "trzewikodziób"}
)

PELECANUS = Genus(name="Pelecanus", children=[P_ONOCROTALUS])
ARDEA = Genus(name="Ardea", children=[A_CINEREA])
NYCTICORAX = Genus(name="Nycticorax", children=[N_NYCTICORAX])
THRESKIORNIS = Genus(name="Threskiornis", children=[T_AETHIOPICUS])
BALAENICEPS = Genus(name="Balaeniceps", children=[B_REX])

PELECANIDAE = Family(name="Pelecanidae", children=[PELECANUS])
ARDEIDAE = Family(name="Ardeidae", children=[ARDEA, NYCTICORAX])
THRESKIORNITHIDAE = Family(name="Threskiornithidae", children=[THRESKIORNIS])
BALAENICIPITIDAE = Family(name="Balaenicipitidae", children=[BALAENICEPS])

PELECANIFORMES_A = Clade(children=[PELECANIDAE, BALAENICIPITIDAE])
PELECANIFORMES_B = Clade(children=[PELECANIFORMES_A, ARDEIDAE])
PELECANIFORMES = Order(
    name="Pelecaniformes", children=[PELECANIFORMES_B, THRESKIORNITHIDAE]
)
