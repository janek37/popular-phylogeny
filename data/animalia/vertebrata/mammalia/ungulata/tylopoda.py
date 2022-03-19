from clade import Family, Genus, Species, Suborder
from constants import EN, PL

C_BACTRIANUS = Species(
    name="Camelus bactrianus",
    local_names={EN: "Bactrian camel", PL: "baktrian, wielbłąd dwugarbny"},
)
C_DROMEDARIUS = Species(
    name="Camelus dromedarius",
    local_names={EN: "dromedary, Arabian camel", PL: "dromader, wielbłąd jednogarbny"},
)
L_GLAMA = Species(name="Lama glama", local_names={EN: "llama", PL: "lama andyjska"})
L_PACOS = Species(name="Lama pacos", local_names={EN: "alpaca", PL: "alpaka"})

CAMELUS = Genus(name="Camelus", children=[C_BACTRIANUS, C_DROMEDARIUS])
LAMA = Genus(name="Lama", children=[L_GLAMA, L_PACOS])

CAMELIDAE = Family(name="Camelidae", children=[CAMELUS, LAMA])

TYLOPODA = Suborder(name="Tylopoda", children=[CAMELIDAE])
