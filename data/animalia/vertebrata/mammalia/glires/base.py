from clade import Clade, Family, Genus, Order, Species, Suborder
from constants import EN, PL

from .hystricomorpha import HYSTRICOMORPHA
from .myomorpha import MYOMORPHA
from .sciuromorpha import SCIUROMORPHA

O_PRINCEPS = Species(
    name="Ochotona princeps",
    local_names={EN: "American pika", PL: "szczekuszka amerykańska"},
)
L_EUROPAEUS = Species(
    name="Lepus europaeus", local_names={EN: "European hare", PL: "zając szarak"}
)
O_CUNICULUS = Species(
    name="Oryctolagus cuniculus",
    local_names={EN: "European rabbit", PL: "królik europejski"},
    known_for=[
        {EN: "domestic rabbit, bunny rabbit", PL: "królik domowy"},
        {EN: "dwarf rabbit", PL: "królik miniaturowy"},
    ],
)
C_FIBER = Species(
    name="Castor fiber", local_names={EN: "European beaver", PL: "bóbr europejski"}
)
G_BURSARIUS = Species(
    name="Geomys bursarius",
    local_names={EN: "plains pocket gopher", PL: "goffer równinny"},
    known_for=[{EN: "Disney's Winnie-the-Pooh"}],
)

OCHOTONA = Genus(name="Ochotona", children=[O_PRINCEPS])
LEPUS = Genus(name="Lepus", children=[L_EUROPAEUS])
ORYCTOLAGUS = Genus(name="Oryctolagus", children=[O_CUNICULUS])
CASTOR = Genus(name="Castor", children=[C_FIBER])
GEOMYS = Genus(name="Geomys", children=[G_BURSARIUS])

OCHOTONIDAE = Family(name="Ochotonidae", children=[OCHOTONA])
LEPORIDAE = Family(name="Leporidae", children=[LEPUS, ORYCTOLAGUS])
CASTORIDAE = Family(name="Castoridae", children=[CASTOR])
GEOMYIDAE = Family(name="Geomyidae", children=[GEOMYS])

CASTORIMORPHA = Suborder(name="Castorimorpha", children=[CASTORIDAE, GEOMYIDAE])

RODENTIA_A = Clade(children=[CASTORIMORPHA, MYOMORPHA])
RODENTIA_B = Clade(children=[HYSTRICOMORPHA, RODENTIA_A])

LAGOMORPHA = Order(name="Lagomorpha", children=[LEPORIDAE, OCHOTONIDAE])
RODENTIA = Order(name="Rodentia", children=[SCIUROMORPHA, RODENTIA_B])

GLIRES = Clade(name="Glires", children=[LAGOMORPHA, RODENTIA])
