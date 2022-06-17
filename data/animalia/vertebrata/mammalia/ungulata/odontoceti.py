from clade import Clade, Family, Genus, Parvorder, Species, Subfamily, Superfamily
from constants import EN, PL, URL
from image import Image, License

P_MACROCEPHALUS = Species(
    name="Physeter macrocephalus",
    local_names={EN: "sperm whale, cachalot", PL: "kaszalot spermacetowy"},
    known_for=[{EN: "Moby Dick", URL: "https://en.wikipedia.org/wiki/Moby-Dick"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Physeter_macrocephalus_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/41/Physeter_macrocephalus_NOAA.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
)
P_PHOCOENA = Species(
    name="Phocoena phocoena",
    local_names={EN: "harbour porpoise", PL: "morświn zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ecomare_-_bruinvis_Berend_(berend3).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/26/Ecomare_-_bruinvis_Berend_%28berend3%29.jpg",
        author="Ecomare/Salko de Wolf     Den Hoorn Texel",
        license=License.CC_BY_SA_4_0,
    ),
)
D_LEUCAS = Species(
    name="Delphinapterus leucas",
    local_names={EN: "beluga whale, white whale", PL: "wal biały, białucha arktyczna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oceanogr%C3%A0fic_29102004.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Oceanogr%C3%A0fic_29102004.jpg",
        author="Javier Yaya Tur / CIUDAD DE LAS ARTES Y LAS CIENCIAS from Valencia, España",
        license=License.CC_BY_2_0,
    ),
)
M_MONOCEROS = Species(
    name="Monodon monoceros",
    local_names={EN: "narwhal", PL: "narwal jednozębny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Monodon_monoceros_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c2/Monodon_monoceros_NOAA.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
)
O_ORCA = Species(
    name="Orcinus orca",
    local_names={EN: "orca, killer whale", PL: "orka oceaniczna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Orcinus_orca_NOAA_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Orcinus_orca_NOAA_2.jpg",
        author="NOAA United States. National Marine Fisheries Service",
        license=License.NOAA,
    ),
)
D_DELPHIS = Species(
    name="Delphinus delphis",
    local_names={EN: "common dolphin", PL: "delfin zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leap_For_It_(27359678360).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/Leap_For_It_%2827359678360%29.jpg",
        author="incidencematrix",
        license=License.CC_BY_2_0,
    ),
)
T_TRUNCATUS = Species(
    name="Tursiops truncatus",
    local_names={
        EN: "common bottlenose dolphin",
        PL: "delfin butlonosy, butlonos zwyczajny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tursiops_truncatus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Tursiops_truncatus.png",
        author="Mith",
        license=License.CC_BY_SA_3_0,
    ),
)

PHYSETER = Genus(name="Physeter", children=[P_MACROCEPHALUS])
PHOCOENA = Genus(name="Phocoena", children=[P_PHOCOENA])
DELPHINAPTERUS = Genus(name="Delphinapterus", children=[D_LEUCAS])
MONODON = Genus(name="Monodon", children=[M_MONOCEROS])
ORCINUS = Genus(name="Orcinus", children=[O_ORCA])
DELPHINUS = Genus(name="Delphinus", children=[D_DELPHIS])
TURSIOPS = Genus(name="Tursiops", children=[T_TRUNCATUS])

ORCININAE = Subfamily(name="Orcininae", children=[ORCINUS])
DELPHININAE = Subfamily(name="Delphininae", children=[DELPHINUS, TURSIOPS])

PHYSETERIDAE = Family(name="Physeteridae", children=[PHYSETER])
PHOCOENIDAE = Family(name="Phocoenidae", children=[PHOCOENA])
MONODONTIDAE = Family(name="Monodontidae", children=[DELPHINAPTERUS, MONODON])
DELPHINIDAE = Family(name="Delphinidae", children=[ORCININAE, DELPHININAE])

DELPHINOIDEA_A = Clade(children=[PHOCOENIDAE, MONODONTIDAE])

PHYSETEROIDEA = Superfamily(name="Physeteroidea", children=[PHYSETERIDAE])
DELPHINOIDEA = Superfamily(name="Delphinoidea", children=[DELPHINOIDEA_A, DELPHINIDAE])

ODONTOCETI = Parvorder(name="Odontoceti", children=[PHYSETEROIDEA, DELPHINOIDEA])
