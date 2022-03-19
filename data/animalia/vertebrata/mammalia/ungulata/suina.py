from clade import Family, Genus, Species, Suborder
from constants import EN, PL

S_DOMESTICUS = Species(
    name="Sus domesticus", local_names={EN: "domestic pig", PL: "świnia domowa"}
)
S_SCROFA = Species(
    name="Sus scrofa", local_names={EN: "wild boar", PL: "dzik euroazjatycki"}
)
P_AFRICANUS = Species(
    name="Phacochoerus africanus",
    local_names={EN: "common warthog", PL: "guziec zwyczajny"},
    known_for=[{EN: "Pumbaa from The Lion King"}],
)

SUS = Genus(name="Sus", children=[S_DOMESTICUS, S_SCROFA])
PHACOCHOERUS = Genus(name="Phacochoerus", children=[P_AFRICANUS])

SUIDAE = Family(name="Suidae", children=[SUS, PHACOCHOERUS])

SUINA = Suborder(name="Suina", children=[SUIDAE])
