from clade import Clade, Species, Genus, Family, Order, Subfamily, Tribe
from constants import EN, PL

O_PYRAMIDALE = Species(name='Ochroma pyramidale', local_names={EN: 'balsa tree', PL: 'balsa, ogorzałka wełnista'})
T_EUROPAEA = Species(name='Tilia × europaea', local_names={EN: 'common lime, common linden', PL: 'lipa holenderska'})
T_CACAO = Species(name='Theobroma cacao', local_names={EN: 'cacao/cocoa tree', PL: 'kakaowiec właściwy'})
C_ACUMINATA = Species(name='Cola acuminata', local_names={PL: 'kola zaostrzona'}, known_for=[{EN: 'kola nuts'}])
M_SYLVESTRIS = Species(name='Malva sylvestris', local_names={PL: 'ślaz dziki', EN: 'common mallow'})
H_SABDARIFFA = Species(
    name='Hibiscus sabdariffa',
    local_names={EN: 'roselle', PL: 'ketmia szczawiowa'},
    known_for=[{EN: 'hibiscus tea', PL: 'herbata z hibiskusa (częsta baza herbat owocowych)'}],
)
A_ROSEA = Species(name='Alcea rosea', local_names={EN: 'common hollyhock', PL: 'malwa różowa'})
A_DIGITATA = Species(name='Adansonia digitata', local_names={EN: 'African baobab', PL: 'baobab afrykański'})
G_HIRSUTUM = Species(
    name='Gossypium hirsutum',
    local_names={EN: 'upland cotton', PL: 'bawełna kosmata'},
    known_for=[{EN: '95% of all cotton production'}],
)
D_ZIBETHINUS = Species(name='Durio zibethinus', local_names={EN: 'durian', PL: 'durian właściwy'})
A_OFFICINALIS = Species(
    name='Althaea officinalis',
    local_names={EN: 'marsh mallow', PL: 'prawoślaz lekarski'},
    known_for=[{EN: 'archetype of modern marshmallows'}],
)

OCHROMA = Genus(name='Ochroma', children=[O_PYRAMIDALE])
TILIA = Genus(name='Tilia', children=[T_EUROPAEA])
THEOBROMA = Genus(name='Theobroma', children=[T_CACAO])
COLA = Genus(name='Cola', children=[C_ACUMINATA])
MALVA = Genus(name='Malva', children=[M_SYLVESTRIS])
HIBISCUS = Genus(name='Hibiscus', children=[H_SABDARIFFA])
ALCEA = Genus(name='Alcea', children=[A_ROSEA])
ADANSONIA = Genus(name='Adansonia', children=[A_DIGITATA])
GOSSYPIUM = Genus(name='Gossypium', children=[G_HIRSUTUM])
DURIO = Genus(name='Durio', children=[D_ZIBETHINUS])

MALVEAE = Tribe(name='Malveae', children=[MALVA])
HIBISCEAE = Tribe(name='Hibisceae', children=[HIBISCUS])
GOSSYPIEAE = Tribe(name='Gossypieae', children=[GOSSYPIUM])
DURIONEAE = Tribe(name='Durioneae', children=[DURIO])

BOMBACOIDEAE = Subfamily(name='Bombacoideae', children=[OCHROMA, ADANSONIA])
TILIOIDEAE = Subfamily(name='Tilioideae', children=[TILIA])
BYTTNERIOIDEAE = Subfamily(name='Byttnerioideae', children=[THEOBROMA])
STERCULIOIDEAE = Subfamily(name='Sterculioideae', children=[COLA])
MALVOIDEAE = Subfamily(name='Malvoideae', children=[MALVEAE, HIBISCEAE, GOSSYPIEAE])
HELICTEROIDEAE = Subfamily(name='Helicteroideae', children=[DURIONEAE])

MALVOIDEAE_BOMBACOIDEAE = Clade(children=[MALVOIDEAE, BOMBACOIDEAE])
MALVACEAE_A = Clade(children=[MALVOIDEAE_BOMBACOIDEAE, TILIOIDEAE, STERCULIOIDEAE, HELICTEROIDEAE])

MALVACEAE = Family(name='Malvaceae', children=[MALVACEAE_A, BYTTNERIOIDEAE])

MALVALES = Order(name='Malvales', children=[MALVACEAE])
