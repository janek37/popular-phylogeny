from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, PL

O_MILITARIS = Species(
    name="Orchis militaris", local_names={EN: "military orchid", PL: "storczyk kukawka"}
)
V_PLANIFOLIA = Species(
    name="Vanilla planifolia",
    local_names={EN: "flat-leaved vanilla", PL: "wanilia płaskolistna"},
    known_for=[{EN: "vanilla flavouring"}],
)
I_SIBIRICA = Species(
    name="Iris sibirica", local_names={EN: "Siberian iris", PL: "kosaciec syberyjski"}
)
C_SATIVUS = Species(
    name="Crocus sativus",
    local_names={EN: "saffron crocus", PL: "szafran uprawny"},
    known_for=[{EN: "saffron", PL: "szafran (przyprawa)"}],
)
C_VERNUS = Species(
    name="Crocus vernus",
    local_names={EN: "spring crocus", PL: "krokus/szafran wiosenny"},
)
A_OFFICINALIS = Species(
    name="Asparagus officinalis",
    local_names={EN: "garden asparagus", PL: "szparag lekarski"},
)
A_AMERICANA = Species(
    name="Agave americana",
    local_names={EN: "century plant, maguey", PL: "agawa amerykańska"},
)
A_TEQUILANA = Species(
    name="Agave tequilana",
    local_names={EN: "blue agave", PL: "agawa niebieska"},
    known_for=[{EN: "tequila"}],
)
C_MAJALIS = Species(
    name="Convallaria majalis",
    local_names={EN: "lily of the valley", PL: "konwalia majowa"},
)
H_ORIENTALIS = Species(
    name="Hyacinthus orientalis",
    local_names={EN: "common hyacinth", PL: "hiacynt wschodni"},
)
A_VERA = Species(name="Aloe vera", local_names={PL: "aloes zwyczajny"})
A_CEPA = Species(name="Allium cepa", local_names={PL: "cebula", EN: "onion"})
A_SATIVUM = Species(name="Allium sativum", local_names={PL: "czosnek", EN: "garlic"})
A_AMPELOPRASUM = Species(
    name="Allium ampeloprasum",
    known_for=[
        {EN: "leek", PL: "por"},
        {EN: "elephant garlic", PL: "czosnek słoniowy"},
        {EN: "pearl onion", PL: "cebulka perłowa"},
    ],
)
A_SCHOENOPRASUM = Species(
    name="Allium schoenoprasum", local_names={EN: "chives", PL: "szczypiorek"}
)
A_URSINUM = Species(
    name="Allium ursinum", local_names={PL: "czosnek niedźwiedzi", EN: "wild garlic"}
)
N_POETICUS = Species(
    name="Narcissus poeticus", local_names={PL: "narcyz biały", EN: "poet's daffodil"}
)
N_JONQUILLA = Species(
    name="Narcissus jonquilla",
    local_names={PL: "narcyz żonkil", EN: "jonquil, rush daffodil"},
)
G_NIVALIS = Species(
    name="Galanthus nivalis",
    local_names={PL: "snieżyczka przebiśnieg", EN: "common snowdrop"},
)

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2958792/
ALLIUM_A = Clade(children=[A_CEPA, A_SCHOENOPRASUM])
ALLIUM_B = Clade(children=[A_SATIVUM, A_AMPELOPRASUM])
ALLIUM_C = Clade(children=[ALLIUM_A, ALLIUM_B])

ORCHIS = Genus(name="Orchis", children=[O_MILITARIS])
VANILLA = Genus(name="Vanilla", children=[V_PLANIFOLIA])
IRIS = Genus(name="Iris", children=[I_SIBIRICA])
CROCUS = Genus(name="Crocus", children=[C_SATIVUS, C_VERNUS])
ASPARAGUS = Genus(name="Asparagus", children=[A_OFFICINALIS])
AGAVE = Genus(name="Agave", children=[A_AMERICANA, A_TEQUILANA])
CONVALLARIA = Genus(name="Convallaria", children=[C_MAJALIS])
HYACINTHUS = Genus(name="Hyacinthus", children=[H_ORIENTALIS])
ALOE = Genus(name="Aloe", children=[A_VERA])
ALLIUM = Genus(name="Allium", children=[ALLIUM_C, A_URSINUM])
NARCISSUS = Genus(name="Narcissus", children=[N_POETICUS, N_JONQUILLA])
GALANTHUS = Genus(name="Galanthus", children=[G_NIVALIS])

ASPARAGOIDEAE = Subfamily(name="Asparagoideae", children=[ASPARAGUS])
AGAVOIDEAE = Subfamily(name="Agavoideae", children=[AGAVE])
NOLINOIDEAE = Subfamily(name="Nolinoideae", children=[CONVALLARIA])
SCILLOIDEAE = Subfamily(name="Scilloideae", children=[HYACINTHUS])
ALLIOIDEAE = Subfamily(name="Allioideae", children=[ALLIUM])
AMARYLLIDOIDEAE = Subfamily(name="Amaryllidoideae", children=[NARCISSUS, GALANTHUS])

ASPARAGOIDEAE_NOLINOIDEAE = Clade(children=[ASPARAGOIDEAE, NOLINOIDEAE])
AGAVOIDEAE_SCILLOIDEAE = Clade(children=[AGAVOIDEAE, SCILLOIDEAE])

ORCHIDEACEAE = Family(name="Orchideaceae", children=[ORCHIS, VANILLA])
IRIDACEAE = Family(name="Iridaceae", children=[IRIS, CROCUS])
ASPARAGACEAE = Family(
    name="Asparagaceae", children=[ASPARAGOIDEAE_NOLINOIDEAE, AGAVOIDEAE_SCILLOIDEAE]
)
ASPHODELACEAE = Family(name="Asphodelaceae", children=[ALOE])
AMARYLLIDACEAE = Family(name="Amaryllidaceae", children=[ALLIOIDEAE, AMARYLLIDOIDEAE])

ASPARAGACEAE_AMARYLLIDACEAE = Clade(children=[ASPARAGACEAE, AMARYLLIDACEAE])
ASPARAGALES_B = Clade(children=[ASPARAGACEAE_AMARYLLIDACEAE, ASPHODELACEAE])
ASPARAGALES_A = Clade(children=[IRIDACEAE, ASPARAGALES_B])

ASPARAGALES = Order(name="Asparagales", children=[ORCHIDEACEAE, ASPARAGALES_A])
