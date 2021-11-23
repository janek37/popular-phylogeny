from clade import Clade, Species, Genus, Family, Order, Subfamily
from constants import EN, PL

S_ALBA = Species(name='Salix alba', local_names={EN: 'white willow', PL: 'wierzba biała'})
S_BABYLONICA = Species(
    name='Salix babylonica',
    local_names={EN: 'weeping willow', PL: 'wierzba płacząca, wierzba babilońska'},
)
P_TREMULA = Species(name='Populus tremula', local_names={PL: 'osika', EN: 'aspen'})
P_ALBA = Species(name='Populus alba', local_names={PL: 'topola biała', EN: 'silver poplar'})
P_EDULIS = Species(name='Passiflora edulis', local_names={EN: 'passion fruit', PL: 'marakuja, męczennica jadalna'})
P_INCARNATA = Species(
    name='Passiflora incarnata',
    local_names={EN: 'maypop', PL: 'kwiat Męki Pańskiej, męczennica cielista'},
)
R_ARNOLDII = Species(
    name='Rafflesia arnoldii',
    local_names={EN: 'giant padma', PL: 'bukietnica Arnolda'},
    known_for=[{EN: 'giant flowers imitating rotting flesh'}],
)
E_PULCHERRIMA = Species(
    name='Euphorbia pulcherrima',
    local_names={EN: 'poinsettia', PL: 'gwiazda betlejemska, wilczomlecz nadobny'},
)
E_ESULA = Species(name='Euphorbia esula', local_names={PL: 'wilczomlecz lancetowaty', EN: 'leafy spurge'})
H_BRASILIENSIS = Species(
    name='Hevea brasiliensis',
    local_names={EN: 'rubber tree', PL: 'kauczukowiec brazylijski'},
    known_for={EN: 'rubber', PL: 'kauczuk'},
)
V_ODORATA = Species(name='Viola odorata', local_names={PL: 'fiołek wonny', EN: 'wood violet'})
V_WITTROCKIANA = Species(
    name='Viola × wittrockiana',
    local_names={PL: 'bratek ogrodowy, fiołek ogrodowy', EN: 'garden pansy'},
)
H_PERFORATUM = Species(
    name='Hypericum perforatum',
    local_names={PL: 'dziurawiec zwyczajny', EN: "perforate St John's-wort"},
)
E_COCA = Species(
    name='Erythroxylum coca', local_names={PL: 'Krasnodrzew pospolity', EN: 'coca'},
    known_for=[{EN: 'cocaine', PL: 'kokaina'}, {EN: 'Coca-Cola'}],
)
M_ESCULENTA = Species(
    name='Manihot esculenta',
    local_names={PL: 'maniok jadalny', EN: 'cassava'},
    known_for=[{PL: 'tapioka', EN: 'tapioca'}],
)
R_COMMUNIS = Species(
    name='Ricinus communis',
    local_names={PL: 'rącznik pospolity', EN: 'castor bean'},
    known_for=[{PL: 'rycyna', EN: 'ricin'}, {PL: 'olej rycynowy', EN: 'castor oil'}],
)
L_USITATISSIMUM = Species(
    name='Linum usitatissimum',
    local_names={PL: 'len zwyczajny', EN: 'flax, linseed'},
    known_for=[{EN: 'linen'}, {EN: 'linseed oil', PL: 'olej lniany'}],
)

SALIX = Genus(name='Salix', children=[S_ALBA, S_BABYLONICA])
POPULUS = Genus(name='Populus', children=[P_TREMULA, P_ALBA])
PASSIFLORA = Genus(name='Passiflora', children=[P_EDULIS, P_INCARNATA])
RAFFLESIA = Genus(name='Rafflesia', children=[R_ARNOLDII])
EUPHORBIA = Genus(name='Euphorbia', children=[E_PULCHERRIMA])
HEVEA = Genus(name='Hevea', children=[H_BRASILIENSIS])
VIOLA = Genus(name='Viola', children=[V_ODORATA, V_WITTROCKIANA])
HYPERICUM = Genus(name='Hypericum', children=[H_PERFORATUM])
ERYTHROXYLUM = Genus(name='Erythroxylum', children=[E_COCA])
MANIHOT = Genus(name='Manihot', children=[M_ESCULENTA])
LINUM = Genus(name='Linum', children=[L_USITATISSIMUM])

CROTONOIDEAE = Subfamily(name='Crotonoideae', children=[HEVEA, MANIHOT])

SALICACEAE = Family(name='Salicaceae', children=[SALIX, POPULUS])
PASSIFLORACEAE = Family(name='Passifloraceae', children=[PASSIFLORA])
RAFFLESIACEAE = Family(name='Rafflesiaceae', children=[RAFFLESIA])
EUPHORBIACEAE = Family(name='Euphorbiaceae', children=[EUPHORBIA, CROTONOIDEAE])
VIOLACEAE = Family(name='Violaceae', children=[VIOLA])
HYPERICACEAE = Family(name='Hypericaceae', children=[HYPERICUM])
ERYTHROXYLACEAE = Family(name='Erythroxylaceae', children=[ERYTHROXYLUM])
LINACEAE = Family(name='Linaceae', children=[LINUM])

SALICOIDS = Clade(name='salicoids', children=[SALICACEAE, PASSIFLORACEAE])
RAFFLESIACEAE_EUPHORBIACEAE = Clade(children=[RAFFLESIACEAE, EUPHORBIACEAE])
EUPHORBIOIDS = Clade(name='euphorbioids', children=[RAFFLESIACEAE_EUPHORBIACEAE, LINACEAE])
PARIETAL_CLADE = Clade(name='parietal clade', children=[SALICOIDS, VIOLACEAE])

MALPIGHIALES_A = Clade(children=[PARIETAL_CLADE, EUPHORBIOIDS])
MALPIGHIALES_B = Clade(children=[HYPERICACEAE, ERYTHROXYLACEAE])

MALPIGHIALES = Order(name='Malpighiales', children=[MALPIGHIALES_A, MALPIGHIALES_B])
