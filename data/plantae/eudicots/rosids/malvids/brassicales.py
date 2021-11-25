from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL

S_ALBA = Species(
    name="Sinapis alba",
    local_names={EN: "white mustard", PL: "gorczyca biała"},
    known_for=[{EN: "yellow table mustard", PL: "musztarda stołowa"}],
)
E_VESICARIA = Species(
    name="Eruca vesicaria", local_names={EN: "rocket, arugola", PL: "rukola"}
)
L_SATIVUM = Species(
    name="Lepidium sativum",
    local_names={EN: "garden cress", PL: "rzeżucha, pieprzyca siewna"},
)
B_JUNCEA = Species(
    name="Brassica juncea",
    local_names={EN: "brown mustard", PL: "gorczyca sarepska, kapusta sitowata"},
    known_for=[{EN: "brown mustard", PL: "musztarda sarepska"}],
)
B_OLERACEA = Species(
    name="Brassica oleracea",
    local_names={PL: "kapusta warzywna"},
    known_for=[
        {EN: "cabbage", PL: "kapusta"},
        {EN: "broccoli", PL: "brokuł"},
        {EN: "cauliflower", PL: "kalafior"},
        {EN: "kale", PL: "jarmuż"},
        {EN: "Brussels sprouts", PL: "brukselka"},
        {EN: "kohlrabi, German turnip", PL: "kalarepa"},
    ],
)
B_RAPA = Species(
    name="Brassica rapa",
    local_names={PL: "kapusta właściwa"},
    known_for=[
        {EN: "turnip", PL: "rzepa"},
        {EN: "Napa cabbage", PL: "kapusta pekińska"},
        {EN: "bok choy", PL: "kapusta chińska"},
    ],
)
B_NAPUS = Species(
    name="Brassica napus",
    local_names={EN: "rapeseed", PL: "kapusta rzepak"},
    known_for=[{PL: "brukiew", EN: "rutabaga, swede"}],
)
R_RAPHANISTRUM = Species(
    name="Raphanus raphanistrum", local_names={EN: "radish", PL: "rzodkiew zwyczajna"}
)
A_RUSTICANA = Species(
    name="Armoracia rusticana", local_names={EN: "horseradish", PL: "chrzan pospolity"}
)
E_JAPONICUM = Species(
    name="Eutrema japonicum", local_names={EN: "wasabi", PL: "wasabi, chrzan japoński"}
)
C_PAPAYA = Species(
    name="Carica papaya", local_names={EN: "papaya", PL: "papaja, melonowiec właściwy"}
)
R_ODORATA = Species(
    name="Reseda odorata", local_names={EN: "garden mignonette", PL: "rezeda wonna"}
)
T_MAJUS = Species(
    name="Tropaeolum majus",
    local_names={EN: "garden nasturtium", PL: "nasturcja większa"},
)
C_SPINOSA = Species(
    name="Capparis spinosa", local_names={EN: "caper", PL: "kapary cierniste"}
)

SINAPIS = Genus(name="Sinapis", children=[S_ALBA])
ERUCA = Genus(name="Eruca", children=[E_VESICARIA])
LEPIDIUM = Genus(name="Lepidium", children=[L_SATIVUM])
# research returned conflicting phylogenies of Brassica species
BRASSICA = Genus(name="Brassica", children=[B_JUNCEA, B_OLERACEA, B_RAPA, B_NAPUS])
RAPHANUS = Genus(name="Raphanus", children=[R_RAPHANISTRUM])
ARMORACIA = Genus(name="Armoracia", children=[A_RUSTICANA])
EUTREMA = Genus(name="Eutrema", children=[E_JAPONICUM])
CARICA = Genus(name="Carica", children=[C_PAPAYA])
RESEDA = Genus(name="Reseda", children=[R_ODORATA])
TROPAEOLUM = Genus(name="Tropaeolum", children=[T_MAJUS])
CAPPARIS = Genus(name="Capparis", children=[C_SPINOSA])

# https://www.researchgate.net/publication/283890506_Genetic_Differentiation_Molecular_Phylogenetic_Analysis_and_Ethnobotanical_Study_of_Eutrema_japonicum_and_E_tenue_in_Japan_and_E_yunnanense_in_China
BRASSICEAE_A = Clade(children=[BRASSICA, RAPHANUS])
BRASSICEAE_B = Clade(children=[BRASSICEAE_A, ERUCA])

BRASSICEAE = Tribe(name="Brassiceae", children=[SINAPIS, BRASSICEAE_B])
LEPIDIEAE = Tribe(name="Lepidieae", children=[LEPIDIUM])
CARDAMINEAE = Tribe(name="Cardamineae", children=[ARMORACIA])
EUTREMEAE = Tribe(name="Eutremeae", children=[EUTREMA])

BRASSICACEAE_A = Clade(children=[BRASSICEAE, EUTREMEAE])
BRASSICACEAE_B = Clade(children=[LEPIDIEAE, CARDAMINEAE])

BRASSICACEAE = Family(name="Brassicaceae", children=[BRASSICACEAE_A, BRASSICACEAE_B])
CARICACEAE = Family(name="Caricaceae", children=[CARICA])
RESEDACEAE = Family(name="Resedaceae", children=[RESEDA])
TROPAEOLACEAE = Family(name="Tropaeolaceae", children=[TROPAEOLUM])
CAPPARACEAE = Family(name="Capparaceae", children=[CAPPARIS])

# https://www.researchgate.net/publication/51179989_Embryology_of_Koeberlinia_Koeberliniaceae_Evidence_for_core-Brassicalean_affinities
BRASSICALES_A = Clade(children=[BRASSICACEAE, CAPPARACEAE])
BRASSICALES_B = Clade(children=[BRASSICALES_A, RESEDACEAE])
BRASSICALES_C = Clade(children=[BRASSICALES_B, CARICACEAE])

BRASSICALES = Order(name="Brassicales", children=[BRASSICALES_C, TROPAEOLACEAE])
