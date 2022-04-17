from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Superphylum
from constants import EN, PL

P_MALARIAE = Species(name="Plasmodium malariae", known_for=[{EN: "malaria"}])
P_CAUDATUM = Species(name="Paramecium caudatum", local_names={PL: "Pantofelek"})
T_VAGINALIS = Species(
    name="Trichomonas vaginalis", local_names={PL: "Rzęsistek pochwowy"}
)
A_PROTEUS = Species(name="Amoeba proteus")
F_SEPTICA = Species(name="Fuligo septica", local_names={EN: "dog vomit slime mold"})
P_POLYCEPHALUM = Species(
    name="Physarum polycephalum",
    local_names={EN: "the blob"},
    known_for=[{EN: "can solve the shortest path problem"}],
)
P_CHROMATOPHORA = Species(
    name="Paulinella chromatophora",
    known_for=[{EN: "photosyntetic plastids unrelated to chloroplasts"}],
)
F_VESICULOSUS = Species(
    name="Fucus vesiculosus",
    local_names={EN: "bladder wrack", PL: "morszczyn pęcherzykowaty"},
)
U_PINNATIFIDA = Species(name="Undaria pinnatifida", local_names={EN: "wakame"})
M_PYRIFERA = Species(
    name="Macrocystis pyrifera",
    local_names={EN: "giant kelp, bladder kelp", PL: "wielkomorszcz gruszkonośny"},
)
B_PAXILLIFER = Species(
    name="Bacillaria paxillifer",
    known_for=[{EN: "one of the thousands of diatom species"}],
)
T_PSEUDONANA = Species(
    name="Thalassiosira pseudonana",
    known_for=[{EN: "the first marine phytoplankton to have its genome sequenced"}],
)
T_BRUCEI = Species(
    name="Trypanosoma brucei",
    local_names={PL: "świdrowiec nagany"},
    known_for=[{EN: "African sleeping sickness", PL: "śpiączka afrykańska"}],
)

PLASMODIUM = Genus(name="Plasmodium", children=[P_MALARIAE])
PARAMECIUM = Genus(name="Paramecium", children=[P_CAUDATUM])
TRICHOMONAS = Genus(name="Trichomonas", children=[T_VAGINALIS])
AMOEBA = Genus(name="Amoeba", children=[A_PROTEUS])
FULIGO = Genus(name="Fuligo", children=[F_SEPTICA])
PHYSARUM = Genus(name="Physarum", children=[P_POLYCEPHALUM])
PAULINELLA = Genus(name="Paulinella", children=[P_CHROMATOPHORA])
FUCUS = Genus(name="Fucus", children=[F_VESICULOSUS])
UNDARIA = Genus(name="Undaria", children=[U_PINNATIFIDA])
MACROCYSTIS = Genus(name="Macrocystis", children=[M_PYRIFERA])
BACILLARIA = Genus(name="Bacillaria", children=[B_PAXILLIFER])
THALASSIOSIRA = Genus(name="Thalassiosira", children=[T_PSEUDONANA])
TRYPANOSOMA = Genus(name="Trypanosoma", children=[T_BRUCEI])

PLASMODIIDAE = Family(name="Plasmodiidae", children=[PLASMODIUM])
PARAMECIIDAE = Family(name="Parameciidae", children=[PARAMECIUM])
TRICHOMONADIDAE = Family(name="Trichomonadidae", children=[TRICHOMONAS])
AMOEBIDAE = Family(name="Amoebidae", children=[AMOEBA])
PHYSARACEAE = Family(name="Physaraceae", children=[FULIGO, PHYSARUM])
PAULINELLIDAE = Family(name="Paulinellidae", children=[PAULINELLA])
FUCACEAE = Family(name="Fucaceae", children=[FUCUS])
ALARIACEAE = Family(name="Alariaceae", children=[UNDARIA])
LAMINARIACEAE = Family(name="Laminariaceae", children=[MACROCYSTIS])
BACILLARIACEAE = Family(name="Bacillariaceae", children=[BACILLARIA])
THALASSIOSIRACEAE = Family(name="Thalassiosiraceae", children=[THALASSIOSIRA])
TRYPANOSOMATIDAE = Family(name="Trypanosomatidae", children=[TRYPANOSOMA])

HAEMOSPORORIDA = Order(name="Haemospororida", children=[PLASMODIIDAE])
PENICULIDA = Order(name="Peniculida", children=[PARAMECIIDAE])
TRICHOMONADIDA = Order(name="Trichomonadida", children=[TRICHOMONADIDAE])
TUBULINIDA = Order(name="Tubulinida", children=[AMOEBIDAE])
PHYSARALES = Order(name="Physarales", children=[PHYSARACEAE])
EUGLYPHIDA = Order(name="Euglyphida", children=[PAULINELLIDAE])
FUCALES = Order(name="Fucales", children=[FUCACEAE])
LAMINARIALES = Order(name="Laminariales", children=[ALARIACEAE, LAMINARIACEAE])
BACILLARIALES = Order(name="Bacillariales", children=[BACILLARIACEAE])
THALASSIOSIRALES = Order(name="Thalassiosirales", children=[THALASSIOSIRACEAE])
TRYPANOSOMATIDA = Order(name="Trypanosomatida", children=[TRYPANOSOMATIDAE])

ACONOIDASIDA = Class(name="Aconoidasida", children=[HAEMOSPORORIDA])
OLIGOHYMENOPHOREA = Class(name="Oligohymenophorea", children=[PENICULIDA])
TUBULINEA = Class(name="Tubulinea", children=[TUBULINIDA])
MYXOGASTRIA = Class(name="Myxogastria", children=[PHYSARALES])
IMBRICATEA = Class(name="Imbricatea", children=[EUGLYPHIDA])
PHAEOPHYCEAE = Class(name="Phaeophyceae", children=[FUCALES, LAMINARIALES])
BACILLARIAPHYCEAE = Class(
    name="Bacillariaphyceae", children=[BACILLARIALES, THALASSIOSIRALES]
)
KINETOPLASTEA = Class(name="Kinetoplastea", children=[TRYPANOSOMATIDA])

CILIOPHORA = Phylum(name="Ciliophora", children=[OLIGOHYMENOPHOREA])
APICOMPLEXA = Phylum(name="Apicomplexa", children=[ACONOIDASIDA])
METAMONADA = Phylum(name="Metamonada", children=[TRICHOMONADIDA])
AMOEBOZOA = Phylum(name="Amoebozoa", children=[TUBULINEA, MYXOGASTRIA])
CERCOZOA = Phylum(name="Cercozoa", children=[IMBRICATEA])
OCHROPHYTA = Phylum(name="Ochrophyta", children=[PHAEOPHYCEAE, BACILLARIAPHYCEAE])
EUGLENOZOA = Phylum(name="Euglenozoa", children=[KINETOPLASTEA])

ALVEOLATA = Superphylum(name="Alveolata", children=[CILIOPHORA, APICOMPLEXA])
DISCICRISTATA = Superphylum(name="Discicristata", children=[EUGLENOZOA])

SAR_A = Clade(children=[ALVEOLATA, OCHROPHYTA])
SAR = Clade(name="SAR", children=[SAR_A, CERCOZOA])
