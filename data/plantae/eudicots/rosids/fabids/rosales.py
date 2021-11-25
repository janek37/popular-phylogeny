from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL

from .amygdaloideae import AMYGDALOIDEAE
from .rosoideae import ROSOIDEAE

C_SATIVA = Species(
    name="Cannabis sativa",
    local_names={PL: "konopie siewne"},
    known_for=[
        {EN: "THC"},
        {EN: "marijuana"},
        {EN: "hashish", PL: "haszysz"},
        {EN: "hemp"},
    ],
)
C_INDICA = Species(
    name="Cannabis indica",
    local_names={PL: "konopie indyjskie"},
    known_for=[
        {EN: "marijuana"},
        {EN: "hashish", PL: "haszysz"},
        {EN: "higher concentrations of THC"},
    ],
)
H_LUPULUS = Species(
    name="Humulus lupulus",
    local_names={PL: "chmiel zwyczajny", EN: "common hop, hops"},
    known_for={EN: "beer", PL: "piwo"},
)
F_CARICA = Species(
    name="Ficus carica",
    local_names={PL: "figowiec pospolity"},
    known_for=[{EN: "fig", PL: "figa"}],
)
F_BENJAMINA = Species(
    name="Ficus benjamina",
    local_names={EN: "weeping fig, ficus tree", PL: "fikus, figowiec benjamina"},
)
F_RELIGIOSA = Species(
    name="Ficus religiosa",
    local_names={EN: "sacred fig", PL: "figowiec pagodowy"},
    known_for=[{EN: "significant in Hinduism, Buddhism and Jaininsm"}],
)
A_ALTILIS = Species(
    name="Artocarpus altilis", local_names={EN: "breadfruit", PL: "chlebowiec właściwy"}
)
A_HETEROPHYLLUS = Species(
    name="Artocarpus heterophyllus",
    local_names={
        EN: "jackfruit",
        PL: "drzewo bochenkowe, dżakfrut, chlebowiec różnolistny",
    },
)
M_ALBA = Species(
    name="Morus alba", local_names={EN: "white mulberry", PL: "morwa biała"}
)
U_DIOICA = Species(
    name="Urtica dioica", local_names={EN: "common nettle", PL: "pokrzywa zwyczajna"}
)

CANNABIS = Genus(name="Cannabbis", children=[C_SATIVA, C_INDICA])
HUMULUS = Genus(name="Humulus", children=[H_LUPULUS])
FICUS = Genus(name="Ficus", children=[F_CARICA, F_BENJAMINA, F_RELIGIOSA])
ARTOCARPUS = Genus(name="Artocarpus", children=[A_ALTILIS, A_HETEROPHYLLUS])
MORUS = Genus(name="Morus", children=[M_ALBA])
URTICA = Genus(name="Urtica", children=[U_DIOICA])

FICEAE = Tribe(name="Ficeae", children=[FICUS])
ARTOCARPEAE = Tribe(name="Artocarpeae", children=[ARTOCARPUS])
MOREAE = Tribe(name="Moreae", children=[MORUS])

ARTOCARPEAE_MOREAE = Clade(children=[ARTOCARPEAE, MOREAE])

CANNABACEAE = Family(name="Cannabaceae", children=[CANNABIS, HUMULUS])
MORACEAE = Family(name="Moraceae", children=[FICEAE, ARTOCARPEAE_MOREAE])
URTICACEAE = Family(name="Urticaceae", children=[URTICA])
ROSACEAE = Family(name="Rosaceae", children=[AMYGDALOIDEAE, ROSOIDEAE])

MORACEAE_URTICACEAE = Clade(children=[MORACEAE, URTICACEAE])

URTICALEAN_ROSIDS = Clade(
    name="urticalean rosids", children=[CANNABACEAE, MORACEAE_URTICACEAE]
)

ROSALES = Order(name="Rosales", children=[URTICALEAN_ROSIDS, ROSACEAE])
