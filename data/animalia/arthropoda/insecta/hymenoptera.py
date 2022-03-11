from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, PL

V_VULGARIS = Species(
    name="Vespula vulgaris",
    local_names={EN: "common wasp, common yellow-jacket", PL: "osa pospolita"},
)
V_CRABRO = Species(
    name="Vespa crabro", local_names={EN: "European hornet", PL: "szerszeń europejski"}
)
S_INVICTA = Species(
    name="Solenopsis invicta",
    local_names={EN: "red imported fire ant", PL: "mrówka ognista"},
)
L_NIGER = Species(
    name="Lasius niger",
    local_names={EN: "black garden ant, common black ant", PL: "hurtnica pospolita"},
)
M_RUBRA = Species(
    name="Myrmica rubra",
    local_names={EN: "European fire ant, common red ant", PL: "wścieklica zwyczajna"},
)
M_PHARAONIS = Species(
    name="Monomorium pharaonis", local_names={EN: "pharaoh ant", PL: "mrówka faraona"}
)
A_MELLIFERA = Species(
    name="Apis mellifera",
    local_names={EN: "western honey bee, European honey bee", PL: "pszczoła miodna"},
)
B_TERRESTRIS = Species(
    name="Bombus terrestris",
    local_names={
        EN: "buff-tailed bumblebee, large earth bumblebee",
        PL: "trzmiel ziemny",
    },
)

VESPULA = Genus(name="Vespula", children=[V_VULGARIS])
VESPA = Genus(name="Vespa", children=[V_CRABRO])
SOLENOPSIS = Genus(name="Solenopsis", children=[S_INVICTA])
LASIUS = Genus(name="Lasius", children=[L_NIGER])
MYRMICA = Genus(name="Myrmica", children=[M_RUBRA])
MONOMORIUM = Genus(name="Monomorium", children=[M_PHARAONIS])
APIS = Genus(name="Apis", children=[A_MELLIFERA])
BOMBUS = Genus(name="Bombus", children=[B_TERRESTRIS])

SOLENOPSIDINI = Tribe(name="Solenopsidini", children=[SOLENOPSIS, MONOMORIUM])
MYRMICINI = Tribe(name="Myrmicini", children=[MYRMICA])

MYRMICINAE = Subfamily(name="Myrmicinae", children=[SOLENOPSIDINI, MYRMICINI])
FORMICINAE = Subfamily(name="Formicinae", children=[LASIUS])

VESPIDAE = Family(name="Vespidae", children=[VESPULA, VESPA])
FORMICIDAE = Family(name="Formicidae", children=[MYRMICINAE, FORMICINAE])
APIDAE = Family(name="Apidae", children=[APIS, BOMBUS])

# Tree based on https://en.wikipedia.org/wiki/Apocrita
HYMENOPTERA_A = Clade(children=[FORMICIDAE, APIDAE])

HYMENOPTERA = Order(name="Hymenoptera", children=[VESPIDAE, HYMENOPTERA_A])
