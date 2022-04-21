from clade import Clade, Class, Family, Genus, Order, Species, Subphylum
from constants import EN, PL
from image import Image, License

O_SABULOSUS = Species(
    name="Ommatoiulus sabulosus",
    local_names={EN: "striped millipede", PL: "krocionóg piaskowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ommatoiulus_sabulosus_06.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Ommatoiulus_sabulosus_06.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
S_COLEOPTRATA = Species(
    name="Scutigera coleoptrata",
    local_names={EN: "house centipede"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Scutigera_coleoptrata_MHNT.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Scutigera_coleoptrata_MHNT.jpg",
        author="Muséum de Toulouse",
        license=License.CC_BY_SA_4_0,
    ),
)
L_FORFICATUS = Species(
    name="Lithobius forficatus",
    local_names={EN: "brown/stone centipede", PL: "drewniak widełkowiec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lithobius_forficatus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2e/Lithobius_forficatus.jpg",
        author="Palica",
        license=License.CC_BY_SA_3_0,
    ),
)
S_CINGULATA = Species(
    name="Scolopendra cingulata",
    local_names={EN: "Megarian banded centipede", PL: "skolopendra paskowana"},
    known_for=[
        {EN: "the most common scolopendromorph species in the Mediterranean area"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Scolopendra_cingulata_-_D7-08-2291.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Scolopendra_cingulata_-_D7-08-2291.JPG",
        author="Eran Finkle",
        license=License.CC_BY_SA_3_0,
    ),
)
A_ARMATA = Species(
    name="Arthropleura armata",
    known_for=[{EN: "largest known arthropod (extinct)"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arthropleura_NT_small.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Arthropleura_NT_small.jpg",
        author="Nobu Tamura",
        license=License.CC_BY_SA_4_0,
    ),
)

OMMATOIULUS = Genus(name="Ommatoiulus", children=[O_SABULOSUS])
SCUTIGERA = Genus(name="Scutigera", children=[S_COLEOPTRATA])
LITHOBIUS = Genus(name="Lithobius", children=[L_FORFICATUS])
SCOLOPENDRA = Genus(name="Scolopendra", children=[S_CINGULATA])
ARTHROPLEURA = Genus(name="Arthropleura", children=[A_ARMATA])

JULIDAE = Family(name="Julidae", children=[OMMATOIULUS])
SCUTIGERIDAE = Family(name="Scutigeridae", children=[SCUTIGERA])
LITHOBIIDAE = Family(name="Lithobiidae", children=[LITHOBIUS])
SCOLOPENDRIDAE = Family(name="Scolopendridae", children=[SCOLOPENDRA])
ARTHROPLEURIDAE = Family(name="Arthropleuridae", children=[ARTHROPLEURA])

JULIDA = Order(name="Julida", children=[JULIDAE])
SCUTIGEROMORPHA = Order(name="Scutigeromorpha", children=[SCUTIGERIDAE])
LITHOBIOMORPHA = Order(name="Lithobiomorpha", children=[LITHOBIIDAE])
SCOLOPENDROMORPHA = Order(name="Scolopendromorpha", children=[SCOLOPENDRIDAE])
ARTHROPLEURIDA = Order(name="Arthropleurida", children=[ARTHROPLEURIDAE])

CHILOPODA_A = Clade(children=[LITHOBIOMORPHA, SCOLOPENDROMORPHA])

DIPLOPODA = Class(name="Diplopoda", children=[JULIDA, ARTHROPLEURIDA])
CHILOPODA = Class(name="Chilopoda", children=[SCUTIGEROMORPHA, CHILOPODA_A])

MYRIAPODA = Subphylum(
    name="Myriapoda", children=[DIPLOPODA, CHILOPODA], local_names={PL: "wije"}
)
