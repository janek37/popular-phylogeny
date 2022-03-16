from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

T_EUROPAEA = Species(
    name="Talpa europaea",
    local_names={EN: "European mole, common mole", PL: "kret europejski"},
)
E_EUROPAEUS = Species(
    name="Erinaceus europaeus", local_names={EN: "European hedgehog, common hedgehog"}
)
S_ARANEUS = Species(
    name="Sorex araneus",
    local_names={EN: "common shrew, Eurasian shrew", PL: "ryjówka aksamitna"},
)

TALPA = Genus(name="Talpa", children=[T_EUROPAEA])
ERINACEUS = Genus(name="Erinaceus", children=[E_EUROPAEUS])
SOREX = Genus(name="Sorex", children=[S_ARANEUS])

TALPIDAE = Family(name="Talpidae", children=[TALPA])
ERINACEIDAE = Family(name="Erinaceidae", children=[ERINACEUS])
SORICIDAE = Family(name="Soricidae", children=[SOREX])

EULIPOTYPHLA_A = Clade(children=[ERINACEIDAE, SORICIDAE])

EULIPOTYPHLA = Order(name="Eulipotyphla", children=[TALPIDAE, EULIPOTYPHLA_A])
