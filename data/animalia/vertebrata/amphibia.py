from clade import Clade, Class, Family, Genus, Order, Species, Suborder
from constants import EN, PL

L_VULGARIS = Species(
    name="Lissotriton vulgaris",
    local_names={
        EN: "European newt, northern smooth newt, common newt",
        PL: "traszka zwyczajna",
    },
)
S_SALAMANDRA = Species(
    name="Salamandra salamandra",
    local_names={EN: "fire salamander", PL: "salamandra plamista"},
)
A_MEXICANUM = Species(
    name="Ambystoma mexicanum",
    local_names={EN: "axolotl", PL: "aksolotl meksykański, ambystoma meksykańska"},
)
P_ANGUINUS = Species(
    name="Proteus anguinus", local_names={EN: "olm", PL: "odmieniec jaskiniowy"}
)
A_SLIGOI = Species(
    name="Andrias sligoi",
    local_names={EN: "South China giant salamander"},
    known_for=[{EN: "the largest living amphibian"}],
)
B_BUFO = Species(
    name="Bufo bufo",
    local_names={
        EN: "common toad, European toad",
        PL: "ropucha szara, ropucha zwyczajna",
    },
)
L_CATESBEIANUS = Species(
    name="Lithobates catesbeianus",
    local_names={EN: "American bullfrog", PL: "żaba rycząca, żaba byk"},
)
R_TEMPORARIA = Species(
    name="Rana temporaria", local_names={EN: "European common frog", PL: "żaba trawna"}
)
P_ESCULENTUS = Species(
    name="Pelophylax kl. esculentus",
    local_names={EN: "edible frog, common water frog", PL: "żaba wodna"},
)
H_ARBOREA = Species(
    name="Hyla arborea", local_names={EN: "European tree frog", PL: "rzekotka drzewna"}
)
A_CALLIDRYAS = Species(
    name="Agalychnis callidryas",
    local_names={
        EN: "red-eyed tree frog",
        PL: "rzekotka czerwonooka, chwytnica kolorowa",
    },
)
P_TERRIBILIS = Species(
    name="Phyllobates terribilis",
    local_names={EN: "golden poison frog", PL: "liściołaz żółty"},
    known_for=[{EN: "the most poisonous amphibian"}],
)
R_NIGROPALMATUS = Species(
    name="Rhacophorus nigropalmatus",
    local_names={EN: "Wallace's flying frog", PL: "nogolotka czarnostopa"},
)

LISSOTRITON = Genus(name="Lissotriton", children=[L_VULGARIS])
SALAMANDRA = Genus(name="Salamandra", children=[S_SALAMANDRA])
AMBYSTOMA = Genus(name="Ambystoma", children=[A_MEXICANUM])
PROTEUS = Genus(name="Proteus", children=[P_ANGUINUS])
ANDRIAS = Genus(name="Andrias", children=[A_SLIGOI])
BUFO = Genus(name="Bufo", children=[B_BUFO])
LITHOBATES = Genus(name="Lithobates", children=[L_CATESBEIANUS])
RANA = Genus(name="Rana", children=[R_TEMPORARIA])
PELOPHYLAX = Genus(name="Pelophylax", children=[P_ESCULENTUS])
HYLA = Genus(name="Hyla", children=[H_ARBOREA])
AGALYCHNIS = Genus(name="Agalychnis", children=[A_CALLIDRYAS])
PHYLLOBATES = Genus(name="Phyllobates", children=[P_TERRIBILIS])
RHACOPHORUS = Genus(name="Rhacophorus", children=[R_NIGROPALMATUS])

SALAMANDRIDAE = Family(name="Salamandridae", children=[LISSOTRITON, SALAMANDRA])
AMBYSTOMATIDAE = Family(name="Ambystomatidae", children=[AMBYSTOMA])
PROTEIDAE = Family(name="Proteidae", children=[PROTEUS])
CRYPTOBRANCHIDAE = Family(name="Cryptobranchidae", children=[ANDRIAS])
BUFONIDAE = Family(name="Bufonidae", children=[BUFO])
RANIDAE = Family(name="Ranidae", children=[LITHOBATES, RANA, PELOPHYLAX])
HYLIDAE = Family(name="Hylidae", children=[HYLA])
PHYLLOMEDUSIDAE = Family(name="Phyllomedusidae", children=[AGALYCHNIS])
DENDROBATIDAE = Family(name="Dendrobatidae", children=[PHYLLOBATES])
RHACOPHORIDAE = Family(name="Rhacophoridae", children=[RHACOPHORUS])

AGASTOROPHRYNIA = Clade(name="Agastorophrynia", children=[BUFONIDAE, DENDROBATIDAE])

# https://en.wikipedia.org/wiki/Phyllomedusidae
ATHESPHATANURA_A = Clade(children=[HYLIDAE, PHYLLOMEDUSIDAE])

ATHESPHATANURA = Clade(
    name="Athesphatanura", children=[AGASTOROPHRYNIA, ATHESPHATANURA_A]
)
RANOIDEA = Clade(name="Ranoidea", children=[RANIDAE, RHACOPHORIDAE])

# https://www.researchgate.net/publication/324584163_Restudy_of_Regalerpeton_weichangensis_Amphibia_Urodela_from_the_Lower_Cretaceous_of_Hebei_China
SALAMANDROIDEA_A = Clade(children=[SALAMANDRIDAE, AMBYSTOMATIDAE])

SALAMANDROIDEA = Suborder(name="Salamandroidea", children=[SALAMANDROIDEA_A, PROTEIDAE])
CRYPTOBRANCHOIDEA = Suborder(name="Cryptobranchoidea", children=[CRYPTOBRANCHIDAE])

URODELA = Order(name="Urodela", children=[SALAMANDROIDEA, CRYPTOBRANCHOIDEA])
ANURA = Order(name="Anura", children=[ATHESPHATANURA, RANOIDEA])

AMPHIBIA = Class(name="Amphibia", children=[URODELA, ANURA])
