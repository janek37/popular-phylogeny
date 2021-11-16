from clade import Clade, Species, Genus, Family, Order
from constants import EN, PL
from .rosids import ROSIDS

R_ACRIS = Species(name='Ranunculus acris', local_names={EN: 'meadow buttercup', PL: 'jaskier ostry'})
P_RHOEAS = Species(name='Papaver rhoeas', local_names={EN: 'common poppy', PL: 'mak polny'})
P_SOMNIFERUM = Species(
    name='Papaver somniferum',
    local_names={EN: 'opium poppy', PL: 'mak lekarski'},
    known_for=[{EN: 'opiates: morphine, codeine, heroin'}, {EN: 'edible poppy seeds'}],
)
A_NAPELLUS = Species(
    name='Aconitum napellus',
    local_names={EN: 'wolfsbane', PL: 'tojad mocny'},
    known_for=[{EN: 'extremely poisonous'}],
)
N_NUCIFERA = Species(
    name='Nelumbo nucifera',
    local_names={PL: 'lotos orzechodajny', EN: 'Indian lotus, sacred lotus'},
    known_for=[{EN: 'trypohobia-inducing fruit'}],
)
M_INTEGRIFOLIA = Species(name='Macadamia integrifolia', local_names={PL: 'makadamia', EN: 'macadamia'})
P_ACERIFOLIA = Species(name='Platanus × acerifolia', local_names={PL: 'platan klonolistny', EN: 'London plane'})
P_OFFICINALIS = Species(name='Paeonia officinalis', local_names={EN: 'common peony', PL: 'peonia/piwonia lekarska'})
R_UVA_CRISPA = Species(name='Ribes uva-crispa', local_names={EN: 'European gooseberry', PL: 'agrest, porzeczka agrest'})
R_NIGRUM = Species(name='Ribes nigrum', local_names={EN: 'blackcurrant', PL: 'czarna porzeczka'})
R_RUBRUM = Species(name='Ribes rubrum', local_names={EN: 'redcurrant', PL: 'czerwona porzeczka'})
C_OVATA = Species(
    name='Crassula ovata',
    local_names={EN: 'jade tree, money tree', PL: 'drzewko szczęścia, grubosz jajowaty'},
)

RIBES_SUBGENUS_RIBES = Clade(children=[R_NIGRUM, R_RUBRUM])  # Subgenus

RANUNCULUS = Genus(name='Ranunculus', children=[R_ACRIS])
PAPAVER = Genus(name='Papaver', children=[P_RHOEAS, P_SOMNIFERUM])
ACONITUM = Genus(name='Aconitum', children=[A_NAPELLUS])
NELUMBO = Genus(name='Nelumbo', children=[N_NUCIFERA])
MACADAMIA = Genus(name='Macadamia', children=[M_INTEGRIFOLIA])
PLATANUS = Genus(name='Platanus', children=[P_ACERIFOLIA])
PAEONIA = Genus(name='Paeonia', children=[P_OFFICINALIS])
RIBES = Genus(name='Ribes', children=[R_UVA_CRISPA, RIBES_SUBGENUS_RIBES])
CRASSULA = Genus(name='Crassula', children=[C_OVATA])

RANUNCULACEAE = Family(name='Ranunculaceae', children=[RANUNCULUS, ACONITUM])
PAPAVERACEAE = Family(name='Papaveraceae', children=[PAPAVER])
PAEONIACEAE = Family(name='Paeoniaceae', children=[PAEONIA])
GROSSULARIACEAE = Family(name='Grossulariaceae', children=[RIBES])
CRASSULACEAE = Family(name='Crassulaceae', children=[CRASSULA])
NELUMBONACEAE = Family(name='Nelumbonaceae', children=[NELUMBO])
PROTEACEAE = Family(name='Proteaceae', children=[MACADAMIA])
PLATANACEAE = Family(name='Platanaceae', children=[PLATANUS])

GROSSULARIACEAE_CRASSULACEAE = Clade(children=[GROSSULARIACEAE, CRASSULACEAE])
PLATANACEAE_PROTEACEAE = Clade(children=[PLATANACEAE, PROTEACEAE])

RANUNCULALES = Order(name='Ranunculales', children=[RANUNCULACEAE, PAPAVERACEAE])
PROTEALES = Order(name='Proteales', children=[NELUMBONACEAE, PLATANACEAE_PROTEACEAE])
SAXIFRAGALES = Order(name='Saxifragales', children=[PAEONIACEAE, GROSSULARIACEAE_CRASSULACEAE])

SUPERROSIDS = Clade(name='superrosids', children=[SAXIFRAGALES, ROSIDS])

PENTAPETALAE = Clade(name='Pentapetalae', children=[SUPERROSIDS])

EUDICOTYLEDONES_A = Clade(children=[PROTEALES, PENTAPETALAE])
EUDICOTYLEDONES = Clade(
    name="Eudicotyledones",
    local_names={EN: 'eudicots', PL: 'dwuliścienne'},
    children=[RANUNCULALES, EUDICOTYLEDONES_A],
)
