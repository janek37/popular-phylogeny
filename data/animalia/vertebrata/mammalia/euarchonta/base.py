from clade import (
    Family,
    Genus,
    Grandorder,
    Infraorder,
    Mirorder,
    Order,
    Parvorder,
    Species,
    Suborder,
)
from constants import EN, PL

from .cercopithecoidea import CERCOPITHECOIDEA
from .hominoidea import HOMINOIDEA
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

CATARRHINI = Parvorder(name="Catarrhini", children=[CERCOPITHECOIDEA, HOMINOIDEA])

SIMIIFORMES = Infraorder(name="Simiiformes", children=[PLATYRRHINI, CATARRHINI])

HAPLORHINI = Suborder(name="Haplorhini", children=[SIMIIFORMES])

SCANDENTIA = Order(name="Scandentia", children=[TUPAIIDAE])
DERMOPTERA = Order(name="Dermoptera", children=[CYNOCEPHALIDAE])
PRIMATES = Order(name="Primates", children=[STREPSIRRHINI, HAPLORHINI])

PRIMATOMORPHA = Mirorder(name="Primatomorpha", children=[DERMOPTERA, PRIMATES])

EUARCHONTA = Grandorder(name="Euarchonta", children=[SCANDENTIA, PRIMATOMORPHA])
