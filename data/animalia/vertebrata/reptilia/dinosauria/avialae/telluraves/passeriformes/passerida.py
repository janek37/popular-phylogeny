from clade import Clade, Family, Genus, Parvorder, Species
from constants import EN, PL

from .fringillidae import FRINGILLIDAE

P_DOMESTICUS = Species(
    name="Passer domesticus", local_names={EN: "house sparrow", PL: "wróbel zwyczajny"}
)
M_ALBA = Species(
    name="Motacilla alba",
    local_names={EN: "white wagtail, pied wagtail, water wagtail", PL: "pliszka siwa"},
)
M_CINEREA = Species(
    name="Motacilla cinerea", local_names={EN: "grey wagtail", PL: "pliszka górska"}
)

PASSER = Genus(name="Passer", children=[P_DOMESTICUS])
MOTACILLA = Genus(name="Motacilla", children=[M_ALBA, M_CINEREA])

PASSERIDAE = Family(name="Passeridae", children=[PASSER])
MOTACILLIDAE = Family(name="Motacillidae", children=[MOTACILLA])

PASSERIDA_A = Clade(children=[MOTACILLIDAE, FRINGILLIDAE])

PASSERIDA = Parvorder(name="Passerida", children=[PASSERIDAE, PASSERIDA_A])
