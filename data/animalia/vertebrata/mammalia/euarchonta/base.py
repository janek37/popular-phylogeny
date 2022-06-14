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
from image import Image, License

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
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Die_S%C3%A4ugthiere_in_Abbildungen_nach_der_Natur,_mit_Beschreibungen_(Plate_34)_(white_background).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Die_S%C3%A4ugthiere_in_Abbildungen_nach_der_Natur%2C_mit_Beschreibungen_%28Plate_34%29_%28white_background%29.jpg",
        author="Goldfuss, Georg August; Schreber, Johann Christian Daniel; Wagner, Andreas Johann",
        license=License.CC_BY_2_0,
    ),
)
C_VOLANS = Species(
    name="Cynocephalus volans",
    local_names={
        EN: "Philippine flying lemur, Philippine colugo",
        PL: "lotokot filipiński",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cynocephalus_volans_Brehm1883.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bc/Cynocephalus_volans_Brehm1883.jpg",
        author="Unknown",
        license=License.PUBLIC_DOMAIN,
    ),
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
