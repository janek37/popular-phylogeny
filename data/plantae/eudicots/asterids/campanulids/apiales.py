from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, PL

P_ANISUM = Species(
    name="Pimpinella anisum",
    local_names={EN: "anise, aniseed", PL: "anyżek, biedrzeniec anyż"},
)
T_AMMI = Species(
    name="Trachyspermum ammi",
    local_names={EN: "ajwain, ajowan", PL: "indyjski kminek, chropawiec wonny"},
)
C_MACULATUM = Species(
    name="Conium maculatum",
    local_names={EN: "poison hemlock", PL: "szczwół plamisty"},
    known_for=[{EN: "the death of Socrates"}],
)
C_SATIVUM = Species(
    name="Coriandrum sativum", local_names={EN: "coriander", PL: "kolendra siewna"}
)
P_SATIVA = Species(
    name="Pastinaca sativa", local_names={EN: "parsnip", PL: "pasternak zwyczajny"}
)
C_CARVI = Species(
    name="Carum carvi",
    local_names={EN: "caraway, meridian fennel, Persian cumin", PL: "kminek zwyczajny"},
)
A_PODAGRARIA = Species(
    name="Aegopodium podagraria",
    local_names={EN: "ground elder", PL: "podagrycznik pospolity"},
)
A_CYNAPIUM = Species(
    name="Aethusa cynapium", local_names={EN: "fool's parsley", PL: "blekot pospolity"}
)
O_CROCATA = Species(
    name="Oenanthe crocata",
    local_names={
        EN: "hemlock water-dropwort, dead man's fingers",
        PL: "kropidło szafranowe",
    },
    known_for=[{EN: "sardonic smile", PL: "uśmiech sardoniczny"}],
)
L_OFFICINALE = Species(
    name="Levisticum officinale", local_names={EN: "lovage", PL: "lubczyk ogrodowy"}
)
ANETHUM_GRAVEOLENS = Species(
    name="Anethum graveolens", local_names={EN: "dill", PL: "koper ogrodowy"}
)
F_VULGARE = Species(
    name="Foeniculum vulgare",
    local_names={EN: "fennel", PL: "koper włoski, fenkuł włoski"},
)
APIUM_GRAVEOLENS = Species(
    name="Apium graveolens",
    local_names={EN: "celery, celeriac", PL: "seler zwyczajny, selery zwyczajne"},
)
E_MARITIMUM = Species(
    name="Eryngium maritimum",
    local_names={EN: "sea holly, seaside eryngo", PL: "mikołajek nadmorski"},
)
D_CAROTA = Species(
    name="Daucus carota",
    local_names={EN: "carrot, wild carrot", PL: "marchew uprawna, marchew zwyczajna"},
)
H_SOSNOWSKYI = Species(
    name="Heracleum sosnowskyi",
    local_names={EN: "Sosnowsky's hogweed", PL: "barszcz Sosnowskiego"},
)
P_CRISPUM = Species(
    name="Petroselinum crispum",
    local_names={EN: "common parsley", PL: "pietruszka zwyczajna"},
)
C_VIROSA = Species(
    name="Cicuta virosa",
    local_names={EN: "cowbane, northern water hemlock", PL: "szalej jadowity"},
)
H_HELIX = Species(
    name="Hedera helix", local_names={EN: "common ivy", PL: "bluszcz pospolity"}
)
P_GINSENG = Species(
    name="Panax ginseng", local_names={EN: "ginseng", PL: "wszechlek żeń-szeń"}
)
C_CYMINUM = Species(
    name="Cuminum cyminum", local_names={EN: "cumin", PL: "kmin rzymski"}
)

PIMPINELLA = Genus(name="Pimpinella", children=[P_ANISUM])
TRACHYSPERMUM = Genus(name="Trachyspermum", children=[T_AMMI])
CONIUM = Genus(name="Conium", children=[C_MACULATUM])
CORIANDRUM = Genus(name="Coriandrum", children=[C_SATIVUM])
PASTINACA = Genus(name="Pastinaca", children=[P_SATIVA])
CARUM = Genus(name="Carum", children=[C_CARVI])
AEGOPODIUM = Genus(name="Aegopodium", children=[A_PODAGRARIA])
AETHUSA = Genus(name="Aethusa", children=[A_CYNAPIUM])
OENANTHE = Genus(name="Oenanthe", children=[O_CROCATA])
LEVISTICUM = Genus(name="Levisticum", children=[L_OFFICINALE])  # incertia sedis
ANETHUM = Genus(name="Anethum", children=[ANETHUM_GRAVEOLENS])
FOENICULUM = Genus(name="Foeniculum", children=[F_VULGARE])
APIUM = Genus(name="Apium", children=[APIUM_GRAVEOLENS])
ERYNGIUM = Genus(name="Eryngium", children=[E_MARITIMUM])
DAUCUS = Genus(name="Daucus", children=[D_CAROTA])
HERACLEUM = Genus(name="Heracleum", children=[H_SOSNOWSKYI])
PETROSELINUM = Genus(name="Petroselinum", children=[P_CRISPUM])
CICUTA = Genus(name="Cicuta", children=[C_VIROSA])
HEDERA = Genus(name="Hedera", children=[H_HELIX])
PANAX = Genus(name="Panax", children=[P_GINSENG])
CUMINUM = Genus(name="Cuminum", children=[C_CYMINUM])

# https://www.researchgate.net/publication/275771656_Taxonomy_of_the_tribe_Apieae_Apiaceae_revisited_as_revealed_by_molecular_phylogenies_and_morphological_characters
APIEAE_A = Clade(children=[ANETHUM, FOENICULUM])
APIEAE_B = Clade(children=[APIUM, PETROSELINUM])

PIMPINELLEAE = Tribe(name="Pimpinelleae", children=[PIMPINELLA])
PYRAMIDOPTEREAE = Tribe(name="Pyramidoptereae", children=[TRACHYSPERMUM])
CORIANDREAE = Tribe(name="Coriandreae", children=[CORIANDRUM])
TORDYLIEAE = Tribe(name="Tordylieae", children=[PASTINACA, HERACLEUM])
CAREAE = Tribe(name="Careae", children=[CARUM, AEGOPODIUM])
# https://www.researchgate.net/publication/263393806_Identification_of_species_and_materia_medica_within_Angelica_L_Umbelliferae_based_on_phylogeny_inferred_from_DNA_barcodes
# evidence for Levisticum in Selineae
SELINEAE = Tribe(name="Selineae", children=[AETHUSA, LEVISTICUM])
OENANTHEAE = Tribe(name="Oenantheae", children=[OENANTHE, CICUTA])
SANICULEAE = Tribe(name="Saniculeae", children=[ERYNGIUM])
APIEAE = Tribe(name="Apieae", children=[APIEAE_A, APIEAE_B])
SCANDICEAE = Tribe(name="Scandiceae", children=[DAUCUS, CUMINUM])

# https://www.semanticscholar.org/paper/Major-clades-within-Apiaceae-subfamily-Apioideae-as-Downie-Spalik/135ee9257c5e624b9ba06523c228a77b2d2c32f5
# couldn't resolve better using available sources (many conflicts)
# probably there is at least [TORDYLIEAE, SELINEAE, CORIANDREAE, CONIUM]
# and maybe [PYRAMIDOPTEREAE, CAREAE]
APIOIDEAE_A = Clade(
    children=[
        TORDYLIEAE,
        SELINEAE,
        CORIANDREAE,
        CONIUM,
        APIEAE,
        PIMPINELLEAE,
        PYRAMIDOPTEREAE,
        CAREAE,
    ]
)
APIOIDEAE_B = Clade(children=[APIOIDEAE_A, SCANDICEAE])

APIOIDEAE = Subfamily(name="Apioideae", children=[APIOIDEAE_B, OENANTHEAE])
SANICULOIDEAE = Subfamily(name="Saniculoideae", children=[SANICULEAE])

APIACEAE = Family(name="Apiaceae", children=[APIOIDEAE, SANICULOIDEAE])
ARALIACEAE = Family(name="Araliaceae", children=[HEDERA, PANAX])

APIALES = Order(name="Apiales", children=[APIACEAE, ARALIACEAE])
