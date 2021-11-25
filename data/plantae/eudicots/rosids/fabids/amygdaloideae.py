from clade import Clade, Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL

S_AUCUPARIA = Species(
    name="Sorbus aucuparia",
    local_names={EN: "rowan, mountain-ash", PL: "jarzębina, jarząb pospolity"},
)
A_MELANOCARPA = Species(
    name="Aronia melanocarpa", local_names={EN: "black chokeberry", PL: "aronia czarna"}
)
M_DOMESTICA = Species(
    name="Malus domestica", local_names={EN: "apple tree", PL: "jabłoń domowa"}
)
M_SYLVESTRIS = Species(
    name="Malus sylvestris", local_names={EN: "European crab apple", PL: "jabłoń dzika"}
)
P_COMMUNIS = Species(
    name="Pyrus communis", local_names={EN: "common pear", PL: "grusza pospolita"}
)
C_MONOGYNA = Species(
    name="Crataegus monogyna",
    local_names={EN: "common hawthorn", PL: "głóg jednoszyjkowy"},
)
P_DOMESTICA = Species(
    name="Prunus domestica", local_names={EN: "European plum", PL: "śliwa domowa"}
)
P_AVIUM = Species(
    name="Prunus avium",
    local_names={EN: "wild cherry, sweet cherry", PL: "czereśnia, wiśnia ptasia"},
)
P_CERASUS = Species(
    name="Prunus cerasus", local_names={EN: "sour cherry", PL: "wiśnia pospolita"}
)
P_PERSICA = Species(
    name="Prunus persica", local_names={EN: "peach", PL: "brzoskwinia zwyczajna"}
)
P_ARMENIACA = Species(
    name="Prunus armeniaca", local_names={EN: "common apricot", PL: "morela pospolita"}
)
P_AMYGDALUS = Species(
    name="Prunus amygdalus",
    local_names={EN: "almond", PL: "migdał, migdałowiec pospolity"},
)

PRUNUS_SUBGENUS_PRUNUS = Subgenus(
    name="Prunus subg. Prunus", children=[P_DOMESTICA, P_ARMENIACA]
)
PRUNUS_SUBGENUS_CERASUS = Subgenus(
    name="Prunus subg. Cerasus", children=[P_AVIUM, P_CERASUS]
)
PRUNUS_SUBGENUS_AMYGDALUS = Subgenus(
    name="Prunus subg. Amygdalus", children=[P_PERSICA, P_AMYGDALUS]
)

# https://www.researchgate.net/publication/255954651_Phylogeny_and_Classification_of_Prunus_sensu_lato_Rosaceae
AMYGDALUS_PRUNUS = Clade(children=[PRUNUS_SUBGENUS_PRUNUS, PRUNUS_SUBGENUS_AMYGDALUS])

SORBUS = Genus(name="Sorbus", children=[S_AUCUPARIA])
ARONIA = Genus(name="Aronia", children=[A_MELANOCARPA])
MALUS = Genus(name="Malus", children=[M_DOMESTICA, M_SYLVESTRIS])
PYRUS = Genus(name="Pyrus", children=[P_COMMUNIS])
CRATAEGUS = Genus(name="Crataegus", children=[C_MONOGYNA])
PRUNUS = Genus(name="Prunus", children=[AMYGDALUS_PRUNUS, PRUNUS_SUBGENUS_CERASUS])

# https://www.hindawi.com/journals/bmri/2018/7627191/
# but could be wrong, to be checked later?
MALINAE_A = Clade(children=[ARONIA, MALUS])
MALINAE_B = Clade(children=[SORBUS, PYRUS])
MALINAE_C = Clade(children=[MALINAE_A, MALINAE_B])

MALINAE = Subtribe(name="Malinae", children=[MALINAE_C, CRATAEGUS])

MALEAE = Tribe(name="Maleae", children=[MALINAE])
AMYGDALEAE = Tribe(name="Amygdaleae", children=[PRUNUS])

AMYGDALOIDEAE = Subfamily(name="Amygdaloideae", children=[MALEAE, AMYGDALEAE])
