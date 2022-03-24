from clade import Clade, Genus, Species, Subfamily, Tribe
from constants import EN, PL

O_MOSCHATUS = Species(
    name="Ovibos moschatus",
    local_names={EN: "muskox", PL: "wół piżmowy, piżmowół arktyczny"},
)
O_ARIES = Species(
    name="Ovis aries", local_names={EN: "domestic sheep", PL: "owca domowa"}
)
O_GMELINI = Species(
    name="Ovis gmelini", local_names={EN: "mouflon", PL: "muflon, urial armeński"}
)
R_RUPICAPRA = Species(
    name="Rupicapra rupicapra", local_names={EN: "chamois", PL: "kozica północna"}
)
O_AMERICANUS = Species(
    name="Oreamnos americanus",
    local_names={EN: "mountain goat", PL: "koza śnieżna, kozioł śnieżny"},
)
C_HIRCUS = Species(name="Capra hircus", local_names={EN: "goat", PL: "koza domowa"})
C_IBEX = Species(
    name="Capra ibex", local_names={EN: "alpine ibex", PL: "koziorożec alpejski"}
)
E_THOMSONII = Species(
    name="Eudorcas thomsonii",
    local_names={EN: "Thomson's gazelle", PL: "gazelopka sawannowa"},
)
K_KOB = Species(name="Kobus kob", local_names={EN: "kob", PL: "kob żółty"})

OVIBOS = Genus(name="Ovibos", children=[O_MOSCHATUS])
OVIS = Genus(name="Ovis", children=[O_ARIES, O_GMELINI])
RUPICAPRA = Genus(name="Rupicapra", children=[R_RUPICAPRA])
OREAMNOS = Genus(name="Oreamnos", children=[O_AMERICANUS])
CAPRA = Genus(name="Capra", children=[C_HIRCUS, C_IBEX])
EUDORCAS = Genus(name="Eudorcas", children=[E_THOMSONII])
KOBUS = Genus(name="Kobus", children=[K_KOB])

CAPRINI_B = Clade(children=[RUPICAPRA, OREAMNOS])
CAPRINI_A = Clade(children=[CAPRINI_B, CAPRA])

OVIBOVINI = Tribe(name="Ovibovini", children=[OVIBOS])
CAPRINI = Tribe(name="Caprini", children=[OVIS, CAPRINI_A])

CAPRINAE = Subfamily(name="Caprinae", children=[OVIBOVINI, CAPRINI])
ANTILOPINAE = Subfamily(name="Antilopinae", children=[EUDORCAS])
REDUNCINAE = Subfamily(name="Reduncinae", children=[KOBUS])

AEGODONTIA_A = Clade(children=[REDUNCINAE, CAPRINAE])
AEGODONTIA = Clade(name="Aegodontia", children=[ANTILOPINAE, AEGODONTIA_A])
