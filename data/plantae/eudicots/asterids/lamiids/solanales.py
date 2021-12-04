from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, PL

from .solanoideae import SOLANOIDEAE

C_ARVENSIS = Species(
    name="Convolvulus arvensis", local_names={EN: "field bindweed", PL: "powój polny"}
)
I_BATATAS = Species(
    name="Ipomoea batatas",
    local_names={EN: "sweet potato", PL: "batat, wilec ziemniaczany"},
)
P_ATKINSIANA = Species(
    name="Petunia × atkinsiana",
    local_names={EN: "garden petunia", PL: "petunia ogrodowa"},
)
N_TABACUM = Species(
    name="Nicotiana tabacum",
    local_names={EN: "cultivated tobacco", PL: "tytoń szlachetny"},
)

CONVOLVULUS = Genus(name="Convolvulus", children=[C_ARVENSIS])
IPOMOEA = Genus(name="Ipomoea", children=[I_BATATAS])
PETUNIA = Genus(name="Petunia", children=[P_ATKINSIANA])
NICOTIANA = Genus(name="Nicotiana", children=[N_TABACUM])

PETUNIOIDEAE = Subfamily(name="Petunioideae", children=[PETUNIA])
NICOTIANOIDEAE = Subfamily(name="Nicotianoideae", children=[NICOTIANA])

# https://www.researchgate.net/publication/257251395_Discovery_of_novel_plastid_phenylalanine_trnF_pseudogenes_defines_a_distinctive_clade_in_Solanaceae
SOLANACEAE_A = Clade(children=[NICOTIANOIDEAE, SOLANOIDEAE])

CONVOLVULACEAE = Family(name="Convolvulaceae", children=[CONVOLVULUS, IPOMOEA])
SOLANACEAE = Family(name="Solanaceae", children=[PETUNIOIDEAE, SOLANACEAE_A])

SOLANALES = Order(name="Solanales", children=[CONVOLVULACEAE, SOLANACEAE])
