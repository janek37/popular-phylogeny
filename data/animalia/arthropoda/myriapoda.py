from clade import Clade, Class, Family, Genus, Order, Species, Subphylum
from constants import EN, PL

O_SABULOSUS = Species(
    name="Ommatoiulus sabulosus",
    local_names={EN: "striped millipede", PL: "krocionóg piaskowy"},
)
S_COLEOPTRATA = Species(
    name="Scutigera coleoptrata", local_names={EN: "house centipede"}
)
L_FORFICATUS = Species(
    name="Lithobius forficatus",
    local_names={EN: "brown/stone centipede", PL: "drewniak widełkowiec"},
)
S_CINGULATA = Species(
    name="Scolopendra cingulata",
    local_names={EN: "Megarian banded centipede", PL: "skolopendra paskowana"},
    known_for=[
        {EN: "the most common scolopendromorph species in the Mediterranean area"}
    ],
)

OMMATOIULUS = Genus(name="Ommatoiulus", children=[O_SABULOSUS])
SCUTIGERA = Genus(name="Scutigera", children=[S_COLEOPTRATA])
LITHOBIUS = Genus(name="Lithobius", children=[L_FORFICATUS])
SCOLOPENDRA = Genus(name="Scolopendra", children=[S_CINGULATA])

JULIDAE = Family(name="Julidae", children=[OMMATOIULUS])
SCUTIGERIDAE = Family(name="Scutigeridae", children=[SCUTIGERA])
LITHOBIIDAE = Family(name="Lithobiidae", children=[LITHOBIUS])
SCOLOPENDRIDAE = Family(name="Scolopendridae", children=[SCOLOPENDRA])

JULIDA = Order(name="Julida", children=[JULIDAE])
SCUTIGEROMORPHA = Order(name="Scutigeromorpha", children=[SCUTIGERIDAE])
LITHOBIOMORPHA = Order(name="Lithobiomorpha", children=[LITHOBIIDAE])
SCOLOPENDROMORPHA = Order(name="Scolopendromorpha", children=[SCOLOPENDRIDAE])

CHILOPODA_A = Clade(children=[LITHOBIOMORPHA, SCOLOPENDROMORPHA])

DIPLOPODA = Class(name="Diplopoda", children=[JULIDA])
CHILOPODA = Class(name="Chilopoda", children=[SCUTIGEROMORPHA, CHILOPODA_A])

MYRIAPODA = Subphylum(
    name="Myriapoda", children=[DIPLOPODA, CHILOPODA], local_names={PL: "wije"}
)
