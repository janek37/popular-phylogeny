from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, PL

P_DIOICA = Species(
    name="Pimenta dioica",
    local_names={EN: "allspice", PL: "ziele angielskie, korzennik lekarski"},
)
F_MAGELLANICA = Species(
    name="Fuchsia magellanica",
    local_names={EN: "hummingbird fuchsia", PL: "fuksja magellańska"},
)
S_AROMATICUM = Species(
    name="Syzygium aromaticum",
    local_names={EN: "clove", PL: "goździkowiec korzenny, czapetka pachnąca"},
    known_for=[{PL: "goździki (przyprawa)", EN: "cloves"}],
)
E_CAMALDULENSIS = Species(
    name="Eucalyptus camaldulensis",
    local_names={EN: "river red gum", PL: "eukaliptus kamaldulski"},
)
P_GRANATUM = Species(
    name="Punica granatum", local_names={EN: "pomegranate", PL: "granat właściwy"}
)
P_GUAJAVA = Species(
    name="Psidium guajava", local_names={EN: "common guava", PL: "gujawa pospolita"}
)

PIMENTA = Genus(name="Pimenta", children=[P_DIOICA])
FUCHSIA = Genus(name="Fuchsia", children=[F_MAGELLANICA])
SYZYGIUM = Genus(name="Syzygium", children=[S_AROMATICUM])
EUCALYPTUS = Genus(name="Eucalyptus", children=[E_CAMALDULENSIS])
PUNICA = Genus(name="Punica", children=[P_GRANATUM])
PSIDIUM = Genus(name="Psidium", children=[P_GUAJAVA])

MYRTEAE = Tribe(name="Myrteae", children=[PIMENTA, PSIDIUM])
SYZYGIEAE = Tribe(name="Syzygieae", children=[SYZYGIUM])

# https://www.researchgate.net/publication/258164894_The_evolution_of_foliar_terpene_diversity_in_Myrtaceae
MYRTACEAE_A = Clade(children=[MYRTEAE, SYZYGIEAE])

MYRTACEAE = Family(name="Myrtaceae", children=[MYRTACEAE_A, EUCALYPTUS])
ONAGRACEAE = Family(name="Onagraceae", children=[FUCHSIA])
LYTHRACEAE = Family(name="Lythraceae", children=[PUNICA])

# https://www.researchgate.net/publication/321640262_A_continuous_morphological_approach_to_study_the_evolution_of_pollen_in_a_phylogenetic_context_An_example_with_the_order_Myrtales
LYTHRACEAE_ONAGRACEAE = Clade(children=[LYTHRACEAE, ONAGRACEAE])

MYRTALES = Order(name="Myrtales", children=[MYRTACEAE, LYTHRACEAE_ONAGRACEAE])
