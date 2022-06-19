from clade import Clade, Class, Family, Genus, Order, Species, Superorder
from constants import EN, PL
from image import Image, License

from .crocodilia import CROCODILIA
from .dinosauria import DINOSAURIA
from .pterosauria import PTEROSAURIA
from .squamata import SQUAMATA
from .testudines import TESTUDINES

S_PUNCTATUS = Species(
    name="Sphenodon punctatus",
    local_names={EN: "tuatara", PL: "hatteria, tuatara, łupkoząb"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sphenodon_punctatus_white_background.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Sphenodon_punctatus_white_background.jpg",
        author="TimVickers",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
I_COMMUNIS = Species(
    name="Ichthyosaurus communis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202006_Ichthyosaurus_communis.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/202006_Ichthyosaurus_communis.png",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
P_DOLICHODEIRUS = Species(
    name="Plesiosaurus dolichodeirus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202006_Plesiosaurus_dolichodeirus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/202006_Plesiosaurus_dolichodeirus.png",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)

SPHENODON = Genus(name="Sphenodon", children=[S_PUNCTATUS])
ICHTHYOSAURUS = Genus(name="Ichthyosaurus", children=[I_COMMUNIS])
PLESIOSAURUS = Genus(name="Plesiosaurus", children=[P_DOLICHODEIRUS])

SPHENODONTIDAE = Family(name="Sphenodontidae", children=[SPHENODON])
ICHTHYOSAURIDAE = Family(name="Ichthyosauridae", children=[ICHTHYOSAURUS])
PLESIOSAURIDAE = Family(name="Plesiosauridae", children=[PLESIOSAURUS])

RHYNCHOCEPHALIA = Order(name="Rhynchocephalia", children=[SPHENODONTIDAE])
ICHTHYOSAURIA = Order(name="Ichthyosauria", children=[ICHTHYOSAURIDAE])
PLESIOSAURIA = Order(name="Plesiosauria", children=[PLESIOSAURIDAE])

LEPIDOSAURIA = Superorder(name="Lepidosauria", children=[RHYNCHOCEPHALIA, SQUAMATA])
ICHTHYOPTERYGIA = Superorder(name="Ichthyopterygia", children=[ICHTHYOSAURIA])

AVEMETATARSALIA = Clade(name="Avemetatarsalia", children=[PTEROSAURIA, DINOSAURIA])

PANTESTUDINES = Clade(name="Pantestudines", children=[PLESIOSAURIA, TESTUDINES])
ARCHOSAURIA = Clade(name="Archosauria", children=[CROCODILIA, AVEMETATARSALIA])

ARCHOSAURIFORMES = Clade(name="Archosauriformes", children=[ARCHOSAURIA])

ARCHELOSAURIA = Clade(name="Archelosauria", children=[PANTESTUDINES, ARCHOSAURIFORMES])

REPTILIA_A = Clade(children=[LEPIDOSAURIA, ARCHELOSAURIA])
# not sure about ichthyo-
REPTILIA = Class(name="Reptilia", children=[REPTILIA_A, ICHTHYOPTERYGIA])
