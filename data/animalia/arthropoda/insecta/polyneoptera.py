from clade import Clade, Cohort, Family, Genus, Order, Species, Superorder
from constants import EN, PL
from image import Image, License

from .blattodea import BLATTODEA
from .orthoptera import ORTHOPTERA

F_AURICULARIA = Species(
    name="Forficula auricularia",
    local_names={EN: "common earwig", PL: "skorek pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Forficula_auricularia_Piazzo_04.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Forficula_auricularia_Piazzo_04.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
M_RELIGIOSA = Species(
    name="Mantis religiosa",
    local_names={EN: "praying mantis, European mantis", PL: "modliszka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:European_mantis_(female)_watercolour.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/European_mantis_%28female%29_watercolour.png",
        author="Lisa Nicvert",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SIPYLUS = Species(
    name="Sipyloidea sipylus",
    local_names={EN: "pink winged stick insect", PL: "patyczak skrzydlaty"},
    known_for=[{EN: "the most widespread walking stick in the world"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sipyloidea_sipylus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/Sipyloidea_sipylus.jpg",
        author="Drägüs",
        license=License.CC_BY_SA_3_0,
    ),
)

FORFICULA = Genus(name="Forficula", children=[F_AURICULARIA])
MANTIS = Genus(name="Mantis", children=[M_RELIGIOSA])
SIPYLOIDEA = Genus(name="Sipyloidea", children=[S_SIPYLUS])

FORFICULIDAE = Family(name="Forficulidae", children=[FORFICULA])
MANTIDAE = Family(name="Mantidae", children=[MANTIS])
LONCHODIDAE = Family(name="Lonchodidae", children=[SIPYLOIDEA])

DERMAPTERA = Order(name="Dermaptera", children=[FORFICULIDAE])
MANTODEA = Order(name="Mantodea", children=[MANTIDAE])
PHASMATODEA = Order(name="Phasmatodea", children=[LONCHODIDAE])

DICTYOPTERA = Superorder(name="Dictyoptera", children=[MANTODEA, BLATTODEA])

POLYNEOPTERA_B = Clade(children=[DICTYOPTERA, PHASMATODEA])
POLYNEOPTERA_A = Clade(children=[ORTHOPTERA, POLYNEOPTERA_B])

POLYNEOPTERA = Cohort(
    name="Polyneoptera", children=[DERMAPTERA, POLYNEOPTERA_A]
)  # or Subdivision?
