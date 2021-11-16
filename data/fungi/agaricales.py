from clade import Order, Clade, Family, Genus, Species
from constants import EN, PL, JP

A_BISPORUS = Species(
    name='Agaricus bisporus',
    local_names={EN: 'button/cremini/portobello mushroom', PL: 'pieczarka dwuzarodnikowa'},
)
L_EDODES = Species(name='Lentinula edodes', local_names={JP: 'shiitake'})
F_VELUTIPES = Species(name='Flammulina velutipes', local_names={EN: 'enoki', JP: 'enokitake'})
H_TESSELLATUS = Species(name='Hypsizygus tessellatus', local_names={EN: 'beech/clamshell mushroom'})
P_OSTREATUS = Species(name='Pleurotus ostreatus', local_names={EN: 'oyster mushroom', PL: 'boczniak ostrygowaty'})
P_ERYNGII = Species(name='Pleurotus eryngii', local_names={EN: 'king oyster mushroom', PL: 'boczniak mikołajkowy'})
P_SEMILANCEATA = Species(
    name='Psilocybe semilanceata',
    local_names={EN: 'liberty cap'},
    known_for=[{EN: 'psychoactive psylocybin'}],
)
A_MUSCARIA = Species(name='Amanita muscaria', local_names={PL: 'muchomor czerwony', EN: 'fly agaric'})
A_PHALLOIDES = Species(name='Amanita phalloides', local_names={PL: 'muchomor sromotnikowy', EN: 'death cap'})
M_PROCERA = Species(name='Macrolepiota procera', local_names={PL: 'czubajka kania', EN: 'parasol mushroom'})
A_OSTOYAE = Species(
    name='Armillaria ostoyae',
    local_names={EN: 'honey agaric', PL: 'opieńka ciemna'},
    known_for=[{EN: 'possibly the largest living organism on Earth (humungous fungus)'}],
)
C_GIGANTEA = Species(name='Calvatia gigantea', local_names={PL: 'purchawka olbrzymia', EN: 'giant pufflball'})

AGARICUS = Genus(name='Agaricus', children=[A_BISPORUS])
LENTINULA = Genus(name='Lentinula', children=[L_EDODES])
FLAMMULINA = Genus(name='Flammulina', children=[F_VELUTIPES])
HYPSIZYGUS = Genus(name='Hypsizygus', children=[H_TESSELLATUS])
PLEUROTUS = Genus(name='Pleurotus', children=[P_OSTREATUS, P_ERYNGII])
PSILOCYBE = Genus(name='Psilocybe', children=[P_SEMILANCEATA])
AMANITA = Genus(name='Amanita', children=[A_MUSCARIA])
MACROLEPIOTA = Genus(name='Macrolepiota', children=[M_PROCERA])
ARMILLARIA = Genus(name='Armillaria', children=[A_OSTOYAE])
CALVATIA = Genus(name='Calvatia', children=[C_GIGANTEA])

# based on https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00019285/Gube/Dissertation.pdf
# unsure
AGARICACEAE_A = Clade(children=[AGARICUS, MACROLEPIOTA])

AGARICACEAE = Family(name='Agaricaceae', children=[AGARICACEAE_A, CALVATIA])
OMPHALOTACEAE = Family(name='Omphalotaceae', children=[LENTINULA])
PHYSALACRIACEAE = Family(name='Physalacriaceae', children=[FLAMMULINA, ARMILLARIA])
LYOPHYLLACEAE = Family(name='Lyophyllaceae', children=[HYPSIZYGUS])
PLEUROTACEAE = Family(name='Pleurotaceae', children=[PLEUROTUS])
HYMENOGASTRACEAE = Family(name='Hymenogastraceae', children=[PSILOCYBE])
AMANITACEAE = Family(name='Amanitaceae', children=[AMANITA])

MIRASMOID_CLADE = Clade(name='Mirasmoid clade', children=[OMPHALOTACEAE, PHYSALACRIACEAE])
AGARICOID_CLADE = Clade(name='Agaricoid clade', children=[AGARICACEAE, HYMENOGASTRACEAE])
PLUTEOID_CLADE = Clade(name='Pluteoid clade', children=[PLEUROTACEAE, AMANITACEAE])
# source: http://tolweb.org/Agaricales/20551
AGARICOID_TRICHOLOMATOID = Clade(children=[AGARICOID_CLADE, LYOPHYLLACEAE])

AGARICALES = Order(name='Agaricales', children=[AGARICOID_TRICHOLOMATOID, MIRASMOID_CLADE, PLUTEOID_CLADE])
