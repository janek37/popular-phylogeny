from clade import Clade, Family, Genus, Order, Species, Subfamily
from constants import EN, IMAGE, PL
from image import Image, License

from .solanoideae import SOLANOIDEAE

C_ARVENSIS = Species(
    name="Convolvulus arvensis",
    local_names={EN: "field bindweed", PL: "powój polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%C3%85kervinda_Convolvulus_arvensis_Torslunda_%C3%96land_0558.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/%C3%85kervinda_Convolvulus_arvensis_Torslunda_%C3%96land_0558.JPG",
        author="Gunnar Creutz",
        license=License.CC_BY_SA_3_0,
    ),
)
I_BATATAS = Species(
    name="Ipomoea batatas",
    local_names={EN: "sweet potato", PL: "batat, wilec ziemniaczany"},
    known_for=[
        {
            EN: "edible tubers",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Ipomoea_batatas_-_Tubers.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Ipomoea_batatas_-_Tubers.jpg",
                author="Filo gèn'",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ipomoea_batatas_(Purple_Sweet_Potato_Variety)_Flower.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Ipomoea_batatas_%28Purple_Sweet_Potato_Variety%29_Flower.JPG",
        author="Earth100",
        license=License.CC_BY_SA_3_0,
    ),
)
P_ATKINSIANA = Species(
    name="Petunia × atkinsiana",
    local_names={EN: "garden petunia", PL: "petunia ogrodowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Petunia_%C3%97_atkinsiana_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a8/Petunia_%C3%97_atkinsiana_%282%29.jpg",
        author="Prenn",
        license=License.CC_BY_SA_3_0,
    ),
)
N_TABACUM = Species(
    name="Nicotiana tabacum",
    local_names={EN: "cultivated tobacco", PL: "tytoń szlachetny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nicotiana_tabacum_004.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6b/Nicotiana_tabacum_004.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)

CONVOLVULUS = Genus(name="Convolvulus", children=[C_ARVENSIS])
IPOMOEA = Genus(name="Ipomoea", children=[I_BATATAS])
PETUNIA = Genus(name="Petunia", children=[P_ATKINSIANA])
NICOTIANA = Genus(name="Nicotiana", children=[N_TABACUM])

PETUNIOIDEAE = Subfamily(name="Petunioideae", children=[PETUNIA])
NICOTIANOIDEAE = Subfamily(name="Nicotianoideae", children=[NICOTIANA])

# https://www.researchgate.net/publication/257251395_Discovery_of_novel_plastid_phenylalanine_trnF_pseudogenes_defines_a_distinctive_clade_in_Solanaceae
SOLANACEAE_A = Clade(children=[NICOTIANOIDEAE, SOLANOIDEAE])

CONVOLVULACEAE = Family(name="Convolvulaceae", children=[CONVOLVULUS, IPOMOEA])
SOLANACEAE = Family(name="Solanaceae", children=[PETUNIOIDEAE, SOLANACEAE_A])

SOLANALES = Order(name="Solanales", children=[CONVOLVULACEAE, SOLANACEAE])
