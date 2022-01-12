from clade import Clade, Family, Genus, Order, Species, Subfamily, Subtribe, Tribe
from constants import EN, PL

D_CARYOPHYLLUS = Species(
    name="Dianthus caryophyllus",
    local_names={EN: "carnation, clove pink", PL: "goździk ogrodowy"},
)
A_GITHAGO = Species(
    name="Agrostemma githago", local_names={EN: "common corn-cockle", PL: "kąkol polny"}
)
B_VULGARIS = Species(
    name="Beta vulgaris",
    local_names={EN: "beet", PL: "burak zwyczajny"},
    known_for=[
        {EN: "sugar beet", PL: "burak cukrowy"},
        {EN: "Mangelwurzel", PL: "burak pastweny"},
        {EN: "chard", PL: "boćwina, burak liściowy"},
    ],
)
D_ROTUNDIFOLIA = Species(
    name="Drosera rotundifolia",
    local_names={EN: "round-leaved sundew", PL: "rosiczka okrągłolistna"},
)
D_MUSCIPULA = Species(
    name="Dionaea muscipula",
    local_names={EN: "Venus flytrap", PL: "muchołówka amerykańska"},
)
N_MIRABILIS = Species(
    name="Nepenthes mirabilis",
    local_names={EN: "common swamp pitcher-plant", PL: "dzbanecznik przedziwny"},
)
S_OLERACEA = Species(
    name="Spinacia oleracea", local_names={EN: "spinach", PL: "szpinak warzywny"}
)
R_HYBRIDUM = Species(
    name="Rheum × hybridum", local_names={EN: "rhubarb", PL: "rabarbar"}
)
C_QUINOA = Species(
    name="Chenopodium quinoa", local_names={EN: "quinoa", PL: "komosa ryżowa"}
)
K_TRAGUS = Species(
    name="Kali tragus",
    local_names={EN: "tumbleweed, prickly Russian thistle"},
    known_for=[{EN: "most common tumbleweed plant"}],
)
F_ESCULENTUM = Species(
    name="Fagopyrum esculentum", local_names={EN: "buckwheat", PL: "gryka zwyczajna"}
)
R_ACETOSA = Species(
    name="Rumex acetosa", local_names={EN: "sorrel", PL: "szczaw zwyczajny"}
)
S_BUCKLEYI = Species(
    name="Schlumbergera × buckleyi",
    local_names={EN: "Christmas cactus", PL: "szlumbergera, kaktus bożonarodzeniowy"},
)
S_UNDATUS = Species(
    name="Selenicereus undatus",
    local_names={EN: "white-fleshed pitahaya", PL: "pitaja"},
)
M_HAHNIANA = Species(
    name="Mammillaria hahniana",
    local_names={EN: "old lady cactus", PL: "wymion, mamilaria"},
)
O_MICRODASYS = Species(
    name="Opuntia microdasys",
    local_names={EN: "bunny ear cactus", PL: "opuncja drobnokolczasta"},
)
L_WILLIAMSII = Species(
    name="Lophophora williamsii",
    local_names={EN: "peyote", PL: "pejotl, jazgrza Williamsa"},
    known_for=[{EN: "psychoactive mescaline"}],
)
A_ASTERIAS = Species(
    name="Astrophytum asterias", local_names={EN: "sand dollar cactus"}
)
E_GRUSONII = Species(
    name="Echinocactus grusonii",
    local_names={
        EN: "golden barrel cactus, mother in law's cushion",
        PL: "złota beczka, poduszka/fotel teściowej",
    },
)
C_GIGANTEA = Species(
    name="Carnegiea gigantea", local_names={EN: "saguaro", PL: "karnegia olbrzymia"}
)
P_AVICULARE = Species(
    name="Polygonum aviculare",
    local_names={EN: "common knotgrass", PL: "rdest zwyczajny"},
)

DIANTHUS = Genus(name="Dianthus", children=[D_CARYOPHYLLUS])
AGROSTEMMA = Genus(name="Agrostemma", children=[A_GITHAGO])
BETA = Genus(name="Beta", children=[B_VULGARIS])
DROSERA = Genus(name="Drosera", children=[D_ROTUNDIFOLIA])
DIONAEA = Genus(name="Dionaea", children=[D_MUSCIPULA])
NEPENTHES = Genus(name="Nepenthes", children=[N_MIRABILIS])
SPINACIA = Genus(name="Spinacia", children=[S_OLERACEA])
RHEUM = Genus(name="Rheum", children=[R_HYBRIDUM])
CHENOPODIUM = Genus(name="Chenopodium", children=[C_QUINOA])
KALI = Genus(name="Kali", children=[K_TRAGUS])
FAGOPYRUM = Genus(name="Fagopyrum", children=[F_ESCULENTUM])
RUMEX = Genus(name="Rumex", children=[R_ACETOSA])
SCHLUMBERGERA = Genus(name="Schlumbergera", children=[S_BUCKLEYI])
SELENICEREUS = Genus(name="Selenicereus", children=[S_UNDATUS])
MAMMILARIA = Genus(name="Mammilaria", children=[M_HAHNIANA])
OPUNTIA = Genus(name="Opuntia", children=[O_MICRODASYS])
LOPHOMORA = Genus(name="Lophomora", children=[L_WILLIAMSII])
ASTROPHYTUM = Genus(name="Astrophytum", children=[A_ASTERIAS])
ECHINOCACTUS = Genus(name="Echinocactus", children=[E_GRUSONII])
CARNEGIEA = Genus(name="Carnegiea", children=[C_GIGANTEA])
POLYGONUM = Genus(name="Polygonum", children=[P_AVICULARE])

CACTINAE = Subtribe(name="Cactinae", children=[MAMMILARIA])

# https://www.semanticscholar.org/paper/Phylogenetic-relationships-and-evolution-of-growth-Hernández-Hernández-Hernández
CACTEAE_A = Clade(children=[CACTINAE, LOPHOMORA])
CACTEAE_B = Clade(children=[ASTROPHYTUM, ECHINOCACTUS])

BETEAE = Tribe(name="Beta", children=[BETA])
FAGOPYREAE = Tribe(name="Fagopyreae", children=[FAGOPYRUM])
RUMICEAE = Tribe(name="Rumiceae", children=[RHEUM, RUMEX])
SALSOLEAE = Tribe(name="Salsoleae", children=[KALI])
CACTEAE = Tribe(name="Cacteae", children=[CACTEAE_A, CACTEAE_B])
RHIPSALIDEAE = Tribe(name="Rhipsalideae", children=[SCHLUMBERGERA])
HYLOCEREEAE = Tribe(name="Hylocereeae", children=[SELENICEREUS])
ECHINOCEREEAE = Tribe(name="Echinocereeae", children=[CARNEGIEA])
POLYGONEAE = Tribe(name="Polygoneae", children=[POLYGONUM])

# https://www.semanticscholar.org/paper/Phylogeny-and-evolution-of-the-epiphytic-(-)-Korotkova/4b7d67f2043a8fcd0f2797fa5b76c5a35e92273a
PHYLLOCACTEAE = Clade(name="Phyllocacteae", children=[HYLOCEREEAE, ECHINOCEREEAE])
CACTOIDEAE_A = Clade(children=[RHIPSALIDEAE, PHYLLOCACTEAE])

# https://www.researchgate.net/publication/351448060_The_complete_chloroplast_genome_of_the_medicinal_plant_Polygonum_cuspidatum_Polygonaceae_and_its_phylogenetic_implications_within_the_subfamily_Polygonoideae
POLYGONOIDEAE_A = Clade(children=[RUMICEAE, POLYGONEAE])

CHENOPODIOIDEAE = Subfamily(name="Chenopodioideae", children=[SPINACIA, CHENOPODIUM])
CACTOIDEAE = Subfamily(name="Cactoideae", children=[CACTEAE, CACTOIDEAE_A])
OPUNTIOIDEAE = Subfamily(name="Opuntioideae", children=[OPUNTIA])
BETOIDEAE = Subfamily(name="Betoideae", children=[BETEAE])
SALSOLOIDEAE = Subfamily(name="Salsoloideae", children=[SALSOLEAE])
POLYGONOIDEAE = Subfamily(name="Polygonoideae", children=[POLYGONOIDEAE_A, FAGOPYREAE])

AMARANTHACEAE_A = Clade(children=[BETOIDEAE, CHENOPODIOIDEAE])

CARYOPHYLLACEAE = Family(name="Caryophyllaceae", children=[DIANTHUS, AGROSTEMMA])
AMARANTHACEAE = Family(name="Amaranthaceae", children=[AMARANTHACEAE_A, SALSOLOIDEAE])
DROSERACEAE = Family(name="Droseraceae", children=[DROSERA, DIONAEA])
NEPENTHACEAE = Family(name="Nepenthaceae", children=[NEPENTHES])
POLYGONACEAE = Family(name="Polygonaceae", children=[POLYGONOIDEAE])
CACTACEAE = Family(name="Cactaceae", children=[CACTOIDEAE, OPUNTIOIDEAE])

# https://www.researchgate.net/publication/225486253_The_distribution_of_ester-linked_ferulic_acid_in_the_cell_walls_of_angiosperms
CARYOPHYLLACEAE_AMARANTHACEAE = Clade(children=[CARYOPHYLLACEAE, AMARANTHACEAE])
DROSERACEAE_NEPENTHACEAE = Clade(children=[DROSERACEAE, NEPENTHACEAE])
CARYOPHYLLALES_A = Clade(children=[CARYOPHYLLACEAE_AMARANTHACEAE, CACTACEAE])
CARYOPHYLLALES_B = Clade(children=[DROSERACEAE_NEPENTHACEAE, POLYGONACEAE])

CARYOPHYLLALES = Order(
    name="Caryophyllales", children=[CARYOPHYLLALES_A, CARYOPHYLLALES_B]
)
