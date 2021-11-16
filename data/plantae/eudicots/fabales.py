from clade import Clade, Species, Genus, Family, Order, Tribe, Subfamily
from constants import EN, PL
from .faboideae import FABOIDEAE

T_INDICA = Species(name='Tamarindus indica', local_names={EN: 'tamarind', PL: 'tamaryndowiec indyjski'})
M_PUDICA = Species(name='Mimosa pudica', local_names={PL: 'mimoza wstydliwa', EN: 'sensitive plant, touch-me-not'})
V_TORTILIS = Species(
    name='Vachellia tortilis',
    local_names={PL: 'akacja', EN: 'umbrella thorn acacia'},
    known_for=[{EN: 'biblical mentions'}, {EN: 'Tree of Ténéré, formerly the loneliest tree'}]
)
S_SENEGAL = Species(
    name='Senegalia senegal',
    local_names={EN: 'gum acacia, gum arabic tree', PL: 'akacja senegalska'},
    known_for=[{EN: 'gum arabic', PL: 'guma arabska'}]
)
C_SILIQUA = Species(
    name='Ceratonia siliqua',
    local_names={EN: 'carob, locust tree', PL: 'drzewo karobowe, szarańczyn strąkowy'},
    known_for=[{EN: "St John's bread", PL: 'chleb świętojański'}],
)

TAMARINDUS = Genus(name='Tamarindus', children=[T_INDICA])
MIMOSA = Genus(name='Mimosa', children=[M_PUDICA])
VACHELLIA = Genus(name='Vachellia', children=[V_TORTILIS])
SENEGALIA = Genus(name='Senegalia', children=[S_SENEGAL])
CERATONIA = Genus(name='Ceratonia', children=[C_SILIQUA])

AMHERSTIEAE = Tribe(name='Amherstieae', children=[TAMARINDUS])

MIMOSOIDEAE_A = Clade(children=[MIMOSA, SENEGALIA])
MIMOSOIDEAE = Clade(name='Mimosoideae', children=[MIMOSOIDEAE_A, VACHELLIA])

DETARIOIDEAE = Subfamily(name='Detarioideae', children=[AMHERSTIEAE])
CAESALPINIOIDEAE = Subfamily(name='Caesalpinioideae', children=[MIMOSOIDEAE, CERATONIA])

CAESALPINIOIDEAE_FABOIDEAE = Clade(children=[CAESALPINIOIDEAE, FABOIDEAE])
FABACEAE = Family(name='Fabaceae', children=[DETARIOIDEAE, CAESALPINIOIDEAE_FABOIDEAE])

FABALES = Order(name='Fabales', children=[FABACEAE])
