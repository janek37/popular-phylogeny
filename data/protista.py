from clade import Phylum, Class, Order, Family, Genus, Species, Clade, Superphylum
from constants import EN, PL

P_MALARIAE = Species(name='Plasmodium malariae', known_for=[{EN: 'malaria'}])
P_CAUDATUM = Species(name='Paramecium caudatum', local_names={PL: 'Pantofelek'})
T_VAGINALIS = Species(name='Trichomonas vaginalis', local_names={PL: 'Rzęsistek pochwowy'})
A_PROTEUS = Species(name='Amoeba proteus')
F_SEPTICA = Species(name='Fuligo septica', local_names={EN: 'dog vomit slime mold'})
P_POLYCEPHALUM = Species(
    name='Physarum polycephalum',
    local_names={EN: 'the blob'},
    known_for=[{EN: 'can solve the shortest path problem'}],
)
P_CHROMATOPHORA = Species(
    name='Paulinella chromatophora',
    known_for=[{EN: 'photosyntetic plastids unrelated to chloroplasts'}],
)

PLASMODIUM = Genus(name='Plasmodium', children=[P_MALARIAE])
PARAMECIUM = Genus(name='Paramecium', children=[P_CAUDATUM])
TRICHOMONAS = Genus(name='Trichomonas', children=[T_VAGINALIS])
AMOEBA = Genus(name='Amoeba', children=[A_PROTEUS])
FULIGO = Genus(name='Fuligo', children=[F_SEPTICA])
PHYSARUM = Genus(name='Physarum', children=[P_POLYCEPHALUM])
PAULINELLA = Genus(name='Paulinella', children=[P_CHROMATOPHORA])

PLASMODIIDAE = Family(name='Plasmodiidae', children=[PLASMODIUM])
PARAMECIIDAE = Family(name='Parameciidae', children=[PARAMECIUM])
TRICHOMONADIDAE = Family(name='Trichomonadidae', children=[TRICHOMONAS])
AMOEBIDAE = Family(name='Amoebidae', children=[AMOEBA])
PHYSARACEAE = Family(name='Physaraceae', children=[FULIGO, PHYSARUM])
PAULINELLIDAE = Family(name='Paulinellidae', children=[PAULINELLA])

HAEMOSPORORIDA = Order(name='Haemospororida', children=[PLASMODIIDAE])
PENICULIDA = Order(name='Peniculida', children=[PARAMECIIDAE])
TRICHOMONADIDA = Order(name='Trichomonadida', children=[TRICHOMONADIDAE])
TUBULINIDA = Order(name='Tubulinida', children=[AMOEBIDAE])
PHYSARALES = Order(name='Physarales', children=[PHYSARACEAE])
EUGLYPHIDA = Order(name='Euglyphida', children=[PAULINELLIDAE])

ACONOIDASIDA = Class(name='Aconoidasida', children=[HAEMOSPORORIDA])
OLIGOHYMENOPHOREA = Class(name='Oligohymenophorea', children=[PENICULIDA])
TUBULINEA = Class(name='Tubulinea', children=[TUBULINIDA])
MYXOGASTRIA = Class(name='Myxogastria', children=[PHYSARALES])
IMBRICATEA = Class(name='Imbricatea', children=[EUGLYPHIDA])

CILIOPHORA = Phylum(name='Ciliphora', children=[OLIGOHYMENOPHOREA])
APICOMPLEXA = Phylum(name='Apicomplexa', children=[ACONOIDASIDA])
METAMONADA = Phylum(name='Metamonada', children=[TRICHOMONADIDA])
AMOEBOZOA = Phylum(name="Amoebozoa", children=[TUBULINEA, MYXOGASTRIA])
CERCOZOA = Phylum(name='Cercozoa', children=[IMBRICATEA])

ALVEOLATA = Superphylum(name='Alveolata', children=[CILIOPHORA, APICOMPLEXA])

SAR = Clade(name='SAR', children=[ALVEOLATA, CERCOZOA])
