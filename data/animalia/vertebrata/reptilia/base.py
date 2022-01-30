from clade import Class, Family, Genus, Order, Species, Superorder
from constants import EN, PL

from .squamata import SQUAMATA

S_PUNCTATUS = Species(
    name="Sphenodon punctatus",
    local_names={EN: "tuatara", PL: "hatteria, tuatara, łupkoząb"},
)
I_COMMUNIS = Species(name="Ichthyosaurus communis")

SPHENODON = Genus(name="Sphenodon", children=[S_PUNCTATUS])
ICHTHYOSAURUS = Genus(name="Ichthyosaurus", children=[I_COMMUNIS])

SPHENODONTIDAE = Family(name="Sphenodontidae", children=[SPHENODON])
ICHTHYOSAURIDAE = Family(name="Ichthyosauridae", children=[ICHTHYOSAURUS])

RHYNCHOCEPHALIA = Order(name="Rhynchocephalia", children=[SPHENODONTIDAE])
ICHTHYOSAURIA = Order(name="Ichthyosauria", children=[ICHTHYOSAURIDAE])

LEPIDOSAURIA = Superorder(name="Lepidosauria", children=[RHYNCHOCEPHALIA, SQUAMATA])
ICHTHYOPTERYGIA = Superorder(name="Ichthyopterygia", children=[ICHTHYOSAURIA])

REPTILIA = Class(name="Reptilia", children=[LEPIDOSAURIA, ICHTHYOPTERYGIA])
