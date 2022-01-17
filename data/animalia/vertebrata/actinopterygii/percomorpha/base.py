from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL

from .anabantiformes import ANABANTIFORMES
from .carangaria import CARANGARIA
from .ovalentaria import OVALENTARIA

S_SCOMBRUS = Species(
    name="Scomber scombrus",
    local_names={EN: "Atlantic mackarel", PL: "makrela atlantycka"},
)
T_THYNNUS = Species(
    name="Thunnus thynnus",
    local_names={EN: "Atlantic bluefin tuna", PL: "tuńczyk pospolity"},
)
T_ALBACARES = Species(
    name="Thunnus albacares",
    local_names={EN: "Yellowfin tuna", PL: "tuńczyk żółtopłetwy"},
)
K_PELAMIS = Species(
    name="Katsuwonus pelamis",
    local_names={EN: "skipjack tuna", PL: "tuńczyk pasiasty, bonito"},
)
H_HIPPOCAMPUS = Species(
    name="Hippocampus hippocampus",
    local_names={
        EN: "short-snouted seahorse",
        PL: "konik morski, pławikonik europejski",
    },
)
P_BARBARUS = Species(
    name="Periophthalmus barbarus",
    local_names={EN: "Atlantic mudskipper", PL: "mułoskoczek, poskoczek mułowy"},
)
P_MICROPS = Species(
    name="Pomatoschistus microps", local_names={EN: "common goby", PL: "babka piaskowa"}
)

SCOMBER = Genus(name="Scomber", children=[S_SCOMBRUS])
THUNNUS = Genus(name="Thunnus", children=[T_THYNNUS, T_ALBACARES])
KATSUWONUS = Genus(name="Katsuwonus", children=[K_PELAMIS])
HIPPOCAMPUS = Genus(name="Hippocampus", children=[H_HIPPOCAMPUS])
PERIOPHTHALMUS = Genus(name="Periophthalmus", children=[P_BARBARUS])
POMATOSCHISTUS = Genus(name="Pomatoschistus", children=[P_MICROPS])

THUNNINI = Tribe(name="Thunnini", children=[THUNNUS, KATSUWONUS])

SCOMBRIDAE = Family(name="Scombridae", children=[SCOMBER, THUNNINI])
SYNGNATHIDAE = Family(name="Syngnathidae", children=[HIPPOCAMPUS])
OXUDERCIDAE = Family(name="Oxudercidae", children=[PERIOPHTHALMUS])
GOBIIDAE = Family(name="Gobiidae", children=[POMATOSCHISTUS])

SCOMBRIFORMES = Order(name="Scombriformes", children=[SCOMBRIDAE])
SYNGNATHIFORMES = Order(name="Syngnathiformes", children=[SYNGNATHIDAE])
GOBIIFORMES = Order(name="Gobiiformes", children=[OXUDERCIDAE, GOBIIDAE])

PERCOMORPHA_A = Clade(children=[SCOMBRIFORMES, SYNGNATHIFORMES])
PERCOMORPHA_D = Clade(children=[ANABANTIFORMES, CARANGARIA])
PERCOMORPHA_E = Clade(children=[PERCOMORPHA_D, OVALENTARIA])
PERCOMORPHA_C = Clade(children=[GOBIIFORMES, PERCOMORPHA_E])
PERCOMORPHA_B = Clade(children=[PERCOMORPHA_A, PERCOMORPHA_C])
PERCOMORPHA = Clade(name="Percomorpha", children=[PERCOMORPHA_B])
