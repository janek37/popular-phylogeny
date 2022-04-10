from clade import Clade, Family, Genus, Order, Species, Subgenus, Tribe
from constants import EN, PL

from .asterids import ASTERIDS
from .caryophyllales import CARYOPHYLLALES
from .rosids import ROSIDS

R_ACRIS = Species(
    name="Ranunculus acris", local_names={EN: "meadow buttercup", PL: "jaskier ostry"}
)
P_RHOEAS = Species(
    name="Papaver rhoeas", local_names={EN: "common poppy", PL: "mak polny"}
)
P_SOMNIFERUM = Species(
    name="Papaver somniferum",
    local_names={EN: "opium poppy", PL: "mak lekarski"},
    known_for=[{EN: "opiates: morphine, codeine, heroin"}, {EN: "edible poppy seeds"}],
)
A_NAPELLUS = Species(
    name="Aconitum napellus",
    local_names={EN: "wolfsbane", PL: "tojad mocny"},
    known_for=[{EN: "extremely poisonous"}],
)
N_NUCIFERA = Species(
    name="Nelumbo nucifera",
    local_names={PL: "lotos orzechodajny", EN: "Indian lotus, sacred lotus"},
    known_for=[{EN: "trypohobia-inducing fruit"}],
)
M_INTEGRIFOLIA = Species(
    name="Macadamia integrifolia", local_names={PL: "makadamia", EN: "macadamia"}
)
P_ACERIFOLIA = Species(
    name="Platanus × acerifolia",
    local_names={PL: "platan klonolistny", EN: "London plane"},
)
P_OFFICINALIS = Species(
    name="Paeonia officinalis",
    local_names={EN: "common peony", PL: "peonia/piwonia lekarska"},
)
R_UVA_CRISPA = Species(
    name="Ribes uva-crispa",
    local_names={EN: "European gooseberry", PL: "agrest, porzeczka agrest"},
)
R_NIGRUM = Species(
    name="Ribes nigrum", local_names={EN: "blackcurrant", PL: "czarna porzeczka"}
)
R_RUBRUM = Species(
    name="Ribes rubrum", local_names={EN: "redcurrant", PL: "czerwona porzeczka"}
)
C_OVATA = Species(
    name="Crassula ovata",
    local_names={
        EN: "jade tree, money tree",
        PL: "drzewko szczęścia, grubosz jajowaty",
    },
)
V_ALBUM = Species(
    name="Viscum album", local_names={EN: "European mistletoe", PL: "jemioła pospolita"}
)
S_ALBUM = Species(
    name="Santalum album",
    local_names={EN: "Indian sandalwood", PL: "sandałowiec biały"},
)
P_VULGARIS = Species(
    name="Pulsatilla vulgaris",
    local_names={EN: "European pasqueflower", PL: "sasanka zwyczajna"},
)
A_CORONARIA = Species(
    name="Anemone coronaria", local_names={EN: "poppy anemone", PL: "zawilec wieńcowy"}
)
B_SEMPERVIRENS = Species(
    name="Buxus sempervirens", local_names={EN: "common box", PL: "bukszpan zwyczajny"}
)

RIBES_SUBGENUS_RIBES = Subgenus(name="Ribes subg. Ribes", children=[R_NIGRUM, R_RUBRUM])

RANUNCULUS = Genus(name="Ranunculus", children=[R_ACRIS])
PAPAVER = Genus(name="Papaver", children=[P_RHOEAS, P_SOMNIFERUM])
ACONITUM = Genus(name="Aconitum", children=[A_NAPELLUS])
NELUMBO = Genus(name="Nelumbo", children=[N_NUCIFERA])
MACADAMIA = Genus(name="Macadamia", children=[M_INTEGRIFOLIA])
PLATANUS = Genus(name="Platanus", children=[P_ACERIFOLIA])
PAEONIA = Genus(name="Paeonia", children=[P_OFFICINALIS])
RIBES = Genus(name="Ribes", children=[R_UVA_CRISPA, RIBES_SUBGENUS_RIBES])
CRASSULA = Genus(name="Crassula", children=[C_OVATA])
VISCUM = Genus(name="Viscum", children=[V_ALBUM])
SANTALUM = Genus(name="Santalum", children=[S_ALBUM])
PULSATILLA = Genus(name="Pulsatilla", children=[P_VULGARIS])
ANEMONE = Genus(name="Anemone", children=[A_CORONARIA])
BUXUS = Genus(name="Buxus", children=[B_SEMPERVIRENS])

RANUNCULEAE = Tribe(name="Ranunculeae", children=[RANUNCULUS])
DELPHINIEAE = Tribe(name="Delphinieae", children=[ACONITUM])
ANEMONEAE = Tribe(name="Anemoneae", children=[PULSATILLA, ANEMONE])

# https://www.researchgate.net/publication/339299453_Ranunculaceae_Phylogeny_Poster_RanPP_2020V3a
RANUNCULEAE_ANEMONEAE = Clade(children=[RANUNCULEAE, ANEMONEAE])

RANUNCULACEAE = Family(
    name="Ranunculaceae", children=[RANUNCULEAE_ANEMONEAE, DELPHINIEAE]
)
PAPAVERACEAE = Family(name="Papaveraceae", children=[PAPAVER])
PAEONIACEAE = Family(name="Paeoniaceae", children=[PAEONIA])
GROSSULARIACEAE = Family(name="Grossulariaceae", children=[RIBES])
CRASSULACEAE = Family(name="Crassulaceae", children=[CRASSULA])
NELUMBONACEAE = Family(name="Nelumbonaceae", children=[NELUMBO])
PROTEACEAE = Family(name="Proteaceae", children=[MACADAMIA])
PLATANACEAE = Family(name="Platanaceae", children=[PLATANUS])
SANTALACEAE = Family(name="Santalaceae", children=[VISCUM, SANTALUM])
BUXACEAE = Family(name="Buxaceae", children=[BUXUS])

GROSSULARIACEAE_CRASSULACEAE = Clade(children=[GROSSULARIACEAE, CRASSULACEAE])
PLATANACEAE_PROTEACEAE = Clade(children=[PLATANACEAE, PROTEACEAE])

RANUNCULALES = Order(name="Ranunculales", children=[RANUNCULACEAE, PAPAVERACEAE])
PROTEALES = Order(name="Proteales", children=[NELUMBONACEAE, PLATANACEAE_PROTEACEAE])
SAXIFRAGALES = Order(
    name="Saxifragales", children=[PAEONIACEAE, GROSSULARIACEAE_CRASSULACEAE]
)
SANTALALES = Order(name="Santalales", children=[SANTALACEAE])
BUXALES = Order(name="Buxales", children=[BUXACEAE])

SUPERASTERIDS_A = Clade(children=[CARYOPHYLLALES, ASTERIDS])

SUPERROSIDS = Clade(name="superrosids", children=[SAXIFRAGALES, ROSIDS])
SUPERASTERIDS = Clade(name="superasterids", children=[SANTALALES, SUPERASTERIDS_A])

PENTAPETALAE = Clade(name="Pentapetalae", children=[SUPERROSIDS, SUPERASTERIDS])

EUDICOTYLEDONES_B = Clade(children=[BUXALES, PENTAPETALAE])
EUDICOTYLEDONES_A = Clade(children=[PROTEALES, EUDICOTYLEDONES_B])
EUDICOTYLEDONES = Clade(
    name="Eudicotyledones",
    local_names={EN: "eudicots", PL: "dwuliścienne"},
    children=[RANUNCULALES, EUDICOTYLEDONES_A],
)
