from clade import Clade, Genus, Species, Subfamily, Supertribe, Tribe
from constants import EN, PL

M_CHAMOMILLA = Species(
    name="Matricaria chamomilla",
    local_names={EN: "German chamomile", PL: "rumianek pospolity"},
)
C_NOBILE = Species(
    name="Chamaemelum nobile", local_names={EN: "Roman chamomile", PL: "rumian rzymski"}
)
A_ABSINTHIUM = Species(
    name="Artemisia absinthium",
    local_names={EN: "wormwood", PL: "bylica piołun"},
    known_for=[{EN: "absinthe", PL: "absynt"}],
)
A_DRACUNCULUS = Species(
    name="Artemisia dracunculus",
    local_names={EN: "tarragon, estragon", PL: "estragon, bylica draganek"},
)
C_MORIFOLIUM = Species(
    name="Chrysanthemum × morifolium",
    local_names={
        EN: "'florist's daisy, hardy garden mum'",
        PL: "chryzantema, złocień chiński",
    },
)
D_PINNATA = Species(
    name="Dahlia pinnata",
    local_names={EN: "garden dahlia", PL: "dalia ogrodowa, dalia zmienna"},
)
H_ANNUUS = Species(
    name="Helianthus annuus",
    local_names={EN: "common sunflower", PL: "słonecznik zwyczajny"},
)
H_TUBEROSUS = Species(
    name="Helianthus tuberosus",
    local_names={
        EN: "Jerusalem artichoke, sunroot",
        PL: "topinambur, słonecznik bulwiasty",
    },
)
C_OFFICINALIS = Species(
    name="Calendula officinalis",
    local_names={EN: "pot marigold", PL: "nagietek lekarski"},
)
A_AMELLUS = Species(
    name="Aster amellus",
    local_names={EN: "European Michaelmas daisy, Italian aster", PL: "aster gawędka"},
)
S_CANADENSIS = Species(
    name="Solidago canadensis",
    local_names={EN: "Canada goldenrod", PL: "nawłoć kanadyjska"},
)
L_NIVALE = Species(
    name="Leontopodium nivale", local_names={EN: "edelweiss", PL: "szarotka alpejska"}
)
T_FARFARA = Species(
    name="Tussilago farfara", local_names={EN: "coltsfoot", PL: "podbiał pospolity"}
)
S_REBAUDIANA = Species(
    name="Stevia rebaudiana",
    local_names={EN: "candyleaf", PL: "stewia"},
    known_for=[{EN: "sweetener"}],
)
A_MILLEFOLIUM = Species(
    name="Achillea millefolium",
    local_names={EN: "common yarrow", PL: "krwarwnik pospolity"},
)
B_PERENNIS = Species(
    name="Bellis perennis", local_names={EN: "common daisy", PL: "stokrotka pospolita"}
)
T_ERECTA = Species(
    name="Tagetes erecta",
    local_names={
        EN: "Aztec marigold, Mexican marigold, big marigold",
        PL: "aksamitka wzniesiona",
    },
)
A_MONTANA = Species(
    name="Arnica montana",
    local_names={
        EN: "wolf's bane, leopard's bane, mountain tobacco, mountain arnica",
        PL: "arnika górska",
    },
)

MATRICARIA = Genus(name="Matricaria", children=[M_CHAMOMILLA])
CHAMAEMELUM = Genus(name="Chamaemelum", children=[C_NOBILE])
ARTEMISIA = Genus(name="Artemisia", children=[A_ABSINTHIUM, A_DRACUNCULUS])
CHRYSANTHEMUM = Genus(name="Chrysanthemum", children=[C_MORIFOLIUM])
DAHLIA = Genus(name="Dahlia", children=[D_PINNATA])
HELIANTHUS = Genus(name="Helianthus", children=[H_ANNUUS, H_TUBEROSUS])
CALENDULA = Genus(name="Calendula", children=[C_OFFICINALIS])
ASTER = Genus(name="Aster", children=[A_AMELLUS])
SOLIDAGO = Genus(name="Solidago", children=[S_CANADENSIS])
LEONTOPODIUM = Genus(name="Leontopodium", children=[L_NIVALE])
TUSSILAGO = Genus(name="Tussilago", children=[T_FARFARA])
STEVIA = Genus(name="Stevia", children=[S_REBAUDIANA])
ACHILLEA = Genus(name="Achillea", children=[A_MILLEFOLIUM])
BELLIS = Genus(name="Bellis", children=[B_PERENNIS])
TAGETES = Genus(name="Tagetes", children=[T_ERECTA])
ARNICA = Genus(name="Arnica", children=[A_MONTANA])

# https://www.semanticscholar.org/paper/Molecular-phylogeny-of-Chrysanthemum,-Ajania-and-as-Zhao-Chen/1557e307fcb57f30f51615b3e3d9aceaa8d21a34
ANTHEMIDEAE_C = Clade(children=[MATRICARIA, ACHILLEA])
ANTHEMIDEAE_A = Clade(children=[ANTHEMIDEAE_C, CHAMAEMELUM])
ANTHEMIDEAE_B = Clade(children=[ARTEMISIA, CHRYSANTHEMUM])

# https://www.researchgate.net/publication/330620543_Convergent_origin_of_the_narrowly_lanceolate_leaf_in_the_genus_Aster-with_special_reference_to_an_unexpected_discovery_of_a_new_Aster_species_from_East_China
ASTEREAE_A = Clade(children=[ASTER, SOLIDAGO])

ANTHEMIDEAE = Tribe(name="Anthemideae", children=[ANTHEMIDEAE_A, ANTHEMIDEAE_B])
COREOPSIDEAE = Tribe(name="Coreopsideae", children=[DAHLIA])
HELIANTHEAE = Tribe(name="Heliantheae", children=[HELIANTHUS])
CALENDULEAE = Tribe(name="Calenduleae", children=[CALENDULA])
ASTEREAE = Tribe(name="Astereae", children=[ASTEREAE_A, BELLIS])
GNAPHALIEAE = Tribe(name="Gnaphalieae", children=[LEONTOPODIUM])
SENECIONEAE = Tribe(name="Senecioneae", children=[TUSSILAGO])
EUPATORIEAE = Tribe(name="Eupatorieae", children=[STEVIA])
TAGETEAE = Tribe(name="Tageteae", children=[TAGETES])
MADIEAE = Tribe(name="Madieae", children=[ARNICA])

# https://www.researchgate.net/publication/276250002_Cuticular_Patterns_on_Stylar_Hairs_in_Asteraceae_a_New_Micromorphological_Feature
ANTHEMIDEAE_ASTEREAE = Clade(children=[ANTHEMIDEAE, ASTEREAE])
ASTERODAE_A = Clade(children=[ANTHEMIDEAE_ASTEREAE, GNAPHALIEAE])
HELIANTHODAE_C = Clade(children=[EUPATORIEAE, MADIEAE])
HELIANTHODAE_A = Clade(children=[HELIANTHEAE, HELIANTHODAE_C])
HELIANTHODAE_B = Clade(children=[HELIANTHODAE_A, TAGETEAE])

ASTERODAE = Supertribe(name="Asterodae", children=[ASTERODAE_A, CALENDULEAE])
HELIANTHODAE = Supertribe(name="Helianthodae", children=[COREOPSIDEAE, HELIANTHODAE_B])
SENECIONODAE = Supertribe(name="Senecionodae", children=[SENECIONEAE])

# unresolved for now
ASTEROIDEAE = Subfamily(
    name="Asteroideae", children=[ASTERODAE, HELIANTHODAE, SENECIONODAE]
)
