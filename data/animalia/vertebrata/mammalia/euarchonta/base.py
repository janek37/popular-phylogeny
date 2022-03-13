from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL

from .platyrrhini import PLATYRRHINI
from .strepsirrhini import STREPSIRRHINI

T_GLIS = Species(
    name="Tupaia glis",
    local_names={
        EN: "common treeshrew",
        PL: "wiewiórecznik pospolity, tupaja pospolita",
    },
)
C_VOLANS = Species(
    name="Cynocephalus volans",
    local_names={
        EN: "Philippine flying lemur, Philippine colugo",
        PL: "lotokot filipiński",
    },
)

TUPAIA = Genus(name="Tupaia", children=[T_GLIS])
CYNOCEPHALUS = Genus(name="Cynocephalus", children=[C_VOLANS])

TUPAIIDAE = Family(name="Tupaiidae", children=[TUPAIA])
CYNOCEPHALIDAE = Family(name="Cynocephalidae", children=[CYNOCEPHALUS])

SIMIIFORMES = Infraorder(name="Simiiformes", children=[PLATYRRHINI])

HAPLORHINI = Suborder(name="Haplorhini", children=[SIMIIFORMES])

SCANDENTIA = Order(name="Scandentia", children=[TUPAIIDAE])
DERMOPTERA = Order(name="Dermoptera", children=[CYNOCEPHALIDAE])
PRIMATES = Order(name="Primates", children=[STREPSIRRHINI, HAPLORHINI])

PRIMATOMORPHA = Clade(name="Primatomorpha", children=[DERMOPTERA, PRIMATES])  # Mirorder

EUARCHONTA = Clade(
    name="Euarchonta", children=[SCANDENTIA, PRIMATOMORPHA]
)  # Grandorder
