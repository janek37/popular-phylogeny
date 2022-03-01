from clade import Clade, Family, Genus, Order, Species, Suborder, Superorder
from constants import EN, PL

from .proboscidea import PROBOSCIDEA

O_AFER = Species(
    name="Orycteropus afer", local_names={EN: "aardvark", PL: "mrównik afrykański"}
)
R_PETERSI = Species(
    name="Rhynchocyon petersi",
    local_names={
        EN: "black and rufous elephant shrew, black and rufous sengi",
        PL: "sorkonos czarno-rdzawy",
    },
)
C_ASIATICA = Species(
    name="Chrysochloris asiatica",
    local_names={EN: "Cape golden mole", PL: "złotokret zwyczajny"},
)
T_ECAUDATUS = Species(
    name="Tenrec ecaudatus",
    local_names={EN: "tailless tenrec, common tenrec", PL: "tenrek zwyczajny"},
)
S_SETOSUS = Species(
    name="Setifer setosus",
    local_names={
        EN: "greater hedgehog tenrec, large Madagaskar hedgehog",
        PL: "jeżokret kłujący",
    },
)
P_CAPENSIS = Species(
    name="Procavia capensis",
    local_names={EN: "rock hyrax, dassie, rock rabbit", PL: "góralek skalny"},
)
T_MANATUS = Species(
    name="Trichechus manatus",
    local_names={
        EN: "North American manatee, West Indian manatee",
        PL: "manat karaibski",
    },
)

ORYCTEROPUS = Genus(name="Orycteropus", children=[O_AFER])
RHYNCHOCYON = Genus(name="Rhynchocyon", children=[R_PETERSI])
CHRYSOCHLORIS = Genus(name="Chrysochloris", children=[C_ASIATICA])
TENREC = Genus(name="Tenrec", children=[T_ECAUDATUS])
SETIFER = Genus(name="Setifer", children=[S_SETOSUS])
PROCAVIA = Genus(name="Procavia", children=[P_CAPENSIS])
TRICHECHUS = Genus(name="Trichechus", children=[T_MANATUS])

ORYCTEROPODIDAE = Family(name="Orycteropodidae", children=[ORYCTEROPUS])
MACROSCELIDIDAE = Family(name="Macroscelididae", children=[RHYNCHOCYON])
CHRYSOCHLORIDAE = Family(name="Chrysochloridae", children=[CHRYSOCHLORIS])
TENRECIDAE = Family(name="Tenrecidae", children=[TENREC, SETIFER])
PROCAVIIDAE = Family(name="Procaviidae", children=[PROCAVIA])
TRICHECHIDAE = Family(name="Trichechidae", children=[TRICHECHUS])

TENRECOMORPHA = Suborder(name="Tenrecomorpha", children=[TENRECIDAE])

TUBULIDENTATA = Order(name="Tubulidentata", children=[ORYCTEROPODIDAE])
MACROSCELIDEA = Order(name="Macroscelidea", children=[MACROSCELIDIDAE])
AFROSORICIDA = Order(name="Afrosoricida", children=[CHRYSOCHLORIDAE, TENRECOMORPHA])
HYRACOIDEA = Order(name="Hyracoidea", children=[PROCAVIIDAE])
SIRENIA = Order(name="Sirenia", children=[TRICHECHIDAE])

AFROINSECTIVORA = Clade(name="Afroinsectivora", children=[MACROSCELIDEA, AFROSORICIDA])
TETHYTHERIA = Clade(name="Tethytheria", children=[SIRENIA, PROBOSCIDEA])

AFROINSECTIPHILIA = Clade(
    name="Afroinsectiphilia", children=[TUBULIDENTATA, AFROINSECTIVORA]
)
PAENUNGULATA = Clade(name="Paenungulata", children=[HYRACOIDEA, TETHYTHERIA])

AFROTHERIA = Superorder(name="Afrotheria", children=[AFROINSECTIPHILIA, PAENUNGULATA])
