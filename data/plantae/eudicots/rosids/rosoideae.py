from clade import Clade, Species, Genus, Tribe, Subfamily
from constants import EN, PL

F_VESCA = Species(name='Fragaria vesca', local_names={EN: 'wild strawberry', PL: 'poziomka pospolita'})
F_ANANASSA = Species(name='Fragaria × ananassa', local_names={EN: 'garden strawberry', PL: 'poziomka truskawka'})
R_CANINA = Species(
    name='Rosa canina',
    local_names={EN: 'dog rose', PL: 'róża dzika'},
    known_for=[{EN: 'jams', PL: 'dżemy'}, {EN: 'tea', PL: 'herbata'}],
)
R_MISTER_LINCOLN = Species(name="Rosa 'Mister Lincoln'", known_for={EN: 'one of the most popular red roses'})
R_IDAEUS = Species(name='Rubus idaeus', local_names={EN: 'red raspberry', PL: 'malina właściwa'})
R_PLICATUS = Species(name='Rubus plicatus', local_names={EN: 'European blackberry', PL: 'jeżyna fałdowana'})
R_CAESIUS = Species(name='Rubus caesius', local_names={EN: 'European dewberry', PL: 'jeżyna popielica'})

FRAGARIA = Genus(name='Fragaria', children=[F_VESCA])
ROSA = Genus(name='Rosa', children=[R_CANINA, R_MISTER_LINCOLN])
RUBUS = Genus(name='Rubus', children=[R_IDAEUS, R_PLICATUS, R_CAESIUS])

POTENTILLEAE = Tribe(name='Potentilleae', children=[FRAGARIA])
ROSEAE = Tribe(name='Roseae', children=[ROSA])
RUBEAE = Tribe(name='Rubeae', children=[RUBUS])

ROSOIDEAE_A = Clade(children=[POTENTILLEAE, ROSEAE])
ROSOIDEAE = Subfamily(name='Rosoideae', children=[ROSOIDEAE_A, RUBEAE])
