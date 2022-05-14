from clade import Clade, Class, Family, Genus, Order, Species, Suborder
from constants import EN, PL
from image import Image, License

L_VULGARIS = Species(
    name="Lissotriton vulgaris",
    local_names={
        EN: "European newt, northern smooth newt, common newt",
        PL: "traszka zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Smooth_Newt._Lissotriton_vulgaris_(33135962471).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Smooth_Newt._Lissotriton_vulgaris_%2833135962471%29.jpg",
        author="gailhampshire from Cradley, Malvern, U.K",
        license=License.CC_BY_2_0,
    ),
)
S_SALAMANDRA = Species(
    name="Salamandra salamandra",
    local_names={EN: "fire salamander", PL: "salamandra plamista"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salamandra_salamandra_MHNT_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/Salamandra_salamandra_MHNT_1.jpg",
        author="Didier Descouens",
        license=License.CC_BY_SA_4_0,
    ),
)
A_MEXICANUM = Species(
    name="Ambystoma mexicanum",
    local_names={EN: "axolotl", PL: "aksolotl meksykański, ambystoma meksykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ambystoma_mexicanum,_Pozna%C5%84_2020.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Ambystoma_mexicanum%2C_Pozna%C5%84_2020.jpg",
        author="Mateusz Giełczyński",
        license=License.CC_BY_SA_4_0,
    ),
)
P_ANGUINUS = Species(
    name="Proteus anguinus",
    local_names={EN: "olm", PL: "odmieniec jaskiniowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Covecija_ribica.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Covecija_ribica.jpg",
        author="Ranko",
        license=License.CC_BY_3_0,
    ),
)
A_JAPONICUS = Species(
    name="Andrias japonicus",
    local_names={EN: "Japanese giant salamander", PL: "salamandra olbrzymia japońska"},
    known_for=[{EN: "one of the largest living salamanders and amphibians"}],
    image=Image(
        url="https://en.wikipedia.org/wiki/File:Japanese_giant_salamander_in_Tottori_Prefecture,_Japan.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d8/Japanese_giant_salamander_in_Tottori_Prefecture%2C_Japan.jpg",
        author="Salamandra2021",
        license=License.CC_BY_SA_4_0,
    ),
)
B_BUFO = Species(
    name="Bufo bufo",
    local_names={
        EN: "common toad, European toad",
        PL: "ropucha szara, ropucha zwyczajna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bufo_bufo_03-clean.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/01/Bufo_bufo_03-clean.jpg",
        author="Kuebi = Armin Kübelbeck",
        license=License.CC_BY_SA_3_0,
    ),
)
L_CATESBEIANUS = Species(
    name="Lithobates catesbeianus",
    local_names={EN: "American bullfrog", PL: "żaba rycząca, żaba byk"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lithobates_catesbeianus.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Lithobates_catesbeianus.JPG",
        author="Alpsdake",
        license=License.CC_BY_SA_3_0,
    ),
)
R_TEMPORARIA = Species(
    name="Rana temporaria",
    local_names={EN: "European common frog", PL: "żaba trawna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:European_Common_Frog_Rana_temporaria.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/39/European_Common_Frog_Rana_temporaria.jpg",
        author="Richard Bartz, Munich aka Makro Freak",
        license=License.CC_BY_SA_2_5,
    ),
)
P_ESCULENTUS = Species(
    name="Pelophylax kl. esculentus",
    local_names={EN: "edible frog, common water frog", PL: "żaba wodna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bastaardkikker_Pelophylax_klepton_esculentus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9a/Bastaardkikker_Pelophylax_klepton_esculentus.jpg",
        author="Angela de Wild",
        license=License.CC_BY_SA_4_0,
    ),
)
H_ARBOREA = Species(
    name="Hyla arborea",
    local_names={EN: "European tree frog", PL: "rzekotka drzewna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hyla_arborea_-_rzekotka_drzewna2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Hyla_arborea_-_rzekotka_drzewna2.jpg",
        author="RobertC1301 at pl.wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
A_CALLIDRYAS = Species(
    name="Agalychnis callidryas",
    local_names={
        EN: "red-eyed tree frog",
        PL: "rzekotka czerwonooka, chwytnica kolorowa",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Red_eyed_tree_frog_edit2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/be/Red_eyed_tree_frog_edit2.jpg",
        author="Careyjamesbalboa at English Wikipedia (Eric De Vries)",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_TERRIBILIS = Species(
    name="Phyllobates terribilis",
    local_names={EN: "golden poison frog", PL: "liściołaz żółty"},
    known_for=[{EN: "the most poisonous amphibian"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phyllobates_terribilis_%22orange_blackfoot%22.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Phyllobates_terribilis_%22orange_blackfoot%22.jpg",
        author="crbonade",
        license=License.CC_BY_SA_4_0,
    ),
)
R_NIGROPALMATUS = Species(
    name="Rhacophorus nigropalmatus",
    local_names={EN: "Wallace's flying frog", PL: "nogolotka czarnostopa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhacophorus_nigropalmatus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/45/Rhacophorus_nigropalmatus.jpg",
        author="Rushenb",
        license=License.CC_BY_SA_4_0,
    ),
)

LISSOTRITON = Genus(name="Lissotriton", children=[L_VULGARIS])
SALAMANDRA = Genus(name="Salamandra", children=[S_SALAMANDRA])
AMBYSTOMA = Genus(name="Ambystoma", children=[A_MEXICANUM])
PROTEUS = Genus(name="Proteus", children=[P_ANGUINUS])
ANDRIAS = Genus(name="Andrias", children=[A_JAPONICUS])
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
