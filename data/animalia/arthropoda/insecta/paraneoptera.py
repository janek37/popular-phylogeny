from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, LA, PL

P_HUMANUS = Species(
    name="Pediculus humanus",
    local_names={PL: "wesz ludzka"},
    known_for=[
        {LA: "pediculus humanus humanus", EN: "body louse", PL: "wesz odzieżowa"},
        {LA: "pediculus humanus capitis", EN: "head louse", PL: "wesz głowowa"},
    ],
)
P_PUBIS = Species(
    name="Pthirus pubis",
    local_names={EN: "crab louse, pubic louse", PL: "menda, wesz łonowa"},
)
M_PERSICAE = Species(
    name="Myzus persicae",
    local_names={
        EN: "green peach aphid, greenfly",
        PL: "mszyca brzoskwiniowo-ziemniaczana",
    },
)
P_POLONICA = Species(
    name="Porphyrophora polonica",
    local_names={EN: "Polish cochineal", PL: "czerwiec polski"},
)
G_LACUSTRIS = Species(
    name="Gerris lacustris",
    local_names={EN: "common pond skater, common water strider", PL: "nartnik duży"},
)
C_LECTULARIUS = Species(
    name="Cimex lectularius", local_names={EN: "common bed bug", PL: "pluskwa domowa"}
)
P_APTERUS = Species(
    name="Pyrrhocoris apterus",
    local_names={EN: "firebug", PL: "tramwajarz, kowal bezskrzydły"},
)
P_PRASINA = Species(
    name="Palomena prasina",
    local_names={EN: "green shield bug", PL: "odorek zieleniak"},
)
C_VIRIDIS = Species(name="Cicadella viridis", local_names={EN: "green leafhopper"})
M_SEPTENDECIM = Species(
    name="Magicicada septendecim",
    local_names={EN: "Pharaoh cicada, 17-year locust", PL: "17-letnia cykada"},
)

PEDICULUS = Genus(name="Pediculus", children=[P_HUMANUS])
PTHIRUS = Genus(name="Pthirus", children=[P_PUBIS])
MYZUS = Genus(name="Myzus", children=[M_PERSICAE])
PORPHYROPHORA = Genus(name="Porphyrophora", children=[P_POLONICA])
GERRIS = Genus(name="Gerris", children=[G_LACUSTRIS])
CIMEX = Genus(name="Cimex", children=[C_LECTULARIUS])
PYRRHOCORIS = Genus(name="Pyrrhocoris", children=[P_APTERUS])
PALOMENA = Genus(name="Palomena", children=[P_PRASINA])
CICADELLA = Genus(name="Cicadella", children=[C_VIRIDIS])
MAGICICADA = Genus(name="Magicicada", children=[M_SEPTENDECIM])

PEDICULIDAE = Family(name="Pediculidae", children=[PEDICULUS])
PTHIRIDAE = Family(name="Pthiridae", children=[PTHIRUS])
APHIDIDAE = Family(name="Aphididae", children=[MYZUS])
MARGARODIDAE = Family(name="Margarodidae", children=[PORPHYROPHORA])
GERRIDAE = Family(name="Gerridae", children=[GERRIS])
CIMICIDAE = Family(name="Cimicidae", children=[CIMEX])
PYRRHOCORIDAE = Family(name="Pyrrhocoridae", children=[PYRRHOCORIS])
PENTATOMIDAE = Family(name="Pentatomidae", children=[PALOMENA])
CICADELLIDAE = Family(name="Cicadellidae", children=[CICADELLA])
CICADIDAE = Family(name="Cicadidae", children=[MAGICICADA])

GERROMORPHA = Infraorder(name="Gerromorpha", children=[GERRIDAE])
CIMICOMORPHA = Infraorder(name="Cimicomorpha", children=[CIMICIDAE])
PENTATOMOMORPHA = Infraorder(
    name="Pentatomomorpha", children=[PYRRHOCORIDAE, PENTATOMIDAE]
)
CICADOMORPHA = Infraorder(name="Cicadomorpha", children=[CICADELLIDAE, CICADIDAE])

# https://www.researchgate.net/publication/227525359_Phylogeny_of_the_true_water_bugs_Nepomorpha_Hemiptera-Heteroptera_based_on_16S_and_28S_rDNA_and_morphology
HETEROPTERA_A = Clade(children=[CIMICOMORPHA, PENTATOMOMORPHA])

STERNORRHYNCHA = Suborder(name="Sternorrhyncha", children=[APHIDIDAE, MARGARODIDAE])
HETEROPTERA = Suborder(name="Heteroptera", children=[GERROMORPHA, HETEROPTERA_A])
AUCHENORRHYNCHA = Suborder(name="Auchenorrhyncha", children=[CICADOMORPHA])

HEMIPTERA_A = Clade(children=[HETEROPTERA, AUCHENORRHYNCHA])

PSOCODEA = Order(name="Psocodea", children=[PEDICULIDAE, PTHIRIDAE])
HEMIPTERA = Order(name="Hemiptera", children=[STERNORRHYNCHA, HEMIPTERA_A])

PARANEOPTERA = Clade(name="Paraneoptera", children=[PSOCODEA, HEMIPTERA])  # Superorder?
