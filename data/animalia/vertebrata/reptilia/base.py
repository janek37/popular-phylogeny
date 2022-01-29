from clade import Class, Family, Genus, Order, Species, Superorder
from constants import EN, PL

from .squamata import SQUAMATA

S_PUNCTATUS = Species(
    name="Sphenodon punctatus",
    local_names={EN: "tuatara", PL: "hatteria, tuatara, łupkoząb"},
)

SPHENODON = Genus(name="Sphenodon", children=[S_PUNCTATUS])

SPHENODONTIDAE = Family(name="Sphenodontidae", children=[SPHENODON])

RHYNCHOCEPHALIA = Order(name="Rhynchocephalia", children=[SPHENODONTIDAE])

LEPIDOSAURIA = Superorder(name="Lepidosauria", children=[RHYNCHOCEPHALIA, SQUAMATA])

REPTILIA = Class(name="Reptilia", children=[LEPIDOSAURIA])
