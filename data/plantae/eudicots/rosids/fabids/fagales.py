from clade import Clade, Species, Genus, Family, Order, Subfamily
from constants import EN, PL

F_SYLVATICA = Species(name='Fagus sylvatica', local_names={EN: 'European beech', PL: 'buk zwyczajny'})
Q_ROBUR = Species(name='Quercus robur', local_names={EN: 'common oak', PL: 'dąb szypułkowy'})
C_SATIVA = Species(name='Castanea satica', local_names={EN: 'sweet chestnut', PL: 'kasztan jadalny'})
J_REGIA = Species(name='Juglans regia', local_names={EN: 'Persian/English/common walnut', PL: 'orzech włoski'})
C_ILLINOINENSIS = Species(name='Carya illinoinensis', local_names={EN: 'pecan', PL: 'pekan, orzesznik jadalny'})
B_PENDULA = Species(name='Betula pendula', local_names={EN: 'silver birch', PL: 'brzoza brodawkowata'})
A_GLUTINOSA = Species(name='Alnus glutinosa', local_names={EN: 'common alder', PL: 'olcha/olsza czarna'})
C_AVELLANA = Species(name='Corylus avellana', local_names={EN: 'common hazel', PL: 'leszczyna pospolita'})
C_BETULUS = Species(name='Carpinus betulus', local_names={EN: 'European hornbeam', PL: 'grab pospolity'})

FAGUS = Genus(name='Fagus', children=[F_SYLVATICA])
QUERCUS = Genus(name='Quercus', children=[Q_ROBUR])
CASTANEA = Genus(name='Castanea', children=[C_SATIVA])
JUGLANS = Genus(name='Juglans', children=[J_REGIA])
CARYA = Genus(name='Carya', children=[C_ILLINOINENSIS])
BETULA = Genus(name='Betula', children=[B_PENDULA])
ALNUS = Genus(name='Alnus', children=[A_GLUTINOSA])
CORYLUS = Genus(name='Corylus', children=[C_AVELLANA])
CARPINUS = Genus(name='Carpinus', children=[C_BETULUS])

FAGOIDEAE = Subfamily(name='Fagoideae', children=[FAGUS])
QUERCOIDEAE = Subfamily(name='Quercoideae', children=[QUERCUS, CASTANEA])
BETULOIDEAE = Subfamily(name='Betuloideae', children=[BETULA, ALNUS])
CORYLOIDEAE = Subfamily(name='Coryloideae', children=[CORYLUS, CARPINUS])

FAGACEAE = Family(name='Fagaceae', children=[FAGOIDEAE, QUERCOIDEAE])
JUGLANDACEAE = Family(name='Juglandaceae', children=[JUGLANS, CARYA])
BETULACEAE = Family(name='Betulaceae', children=[BETULOIDEAE, CORYLOIDEAE])

FAGALES_A = Clade(children=[JUGLANDACEAE, BETULACEAE])
FAGALES = Order(name='Fagales', children=[FAGACEAE, FAGALES_A])
