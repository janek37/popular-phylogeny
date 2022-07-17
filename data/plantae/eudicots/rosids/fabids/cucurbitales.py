from clade import Family, Genus, Order, Species, Subfamily, Subtribe, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

L_SICERARIA = Species(
    name="Lagenaria siceraria",
    local_names={EN: "calabash, bottle gourd", PL: "tykwa pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Calabash_(Lagenaria_siceraria)_in_Seoul.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Calabash_%28Lagenaria_siceraria%29_in_Seoul.jpg",
        author="Hyunjung Kim",
        license=License.CC0,
    ),
)
C_LANATUS = Species(
    name="Citrullus lanatus",
    local_names={EN: "watermelon", PL: "arbuz zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Citrullus_lanatus_(Thunb.)_Cucurbitaceae_(7174523558).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Citrullus_lanatus_%28Thunb.%29_Cucurbitaceae_%287174523558%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
C_SATIVUS = Species(
    name="Cucumis sativus",
    local_names={EN: "cucumber", PL: "ogórek siewny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cucumis_sativus20090812_497.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/93/Cucumis_sativus20090812_497.jpg",
        author="Bff",
        license=License.CC_BY_SA_3_0,
    ),
)
C_MELO = Species(
    name="Cucumis melo",
    local_names={EN: "melon, muskmelon", PL: "melon cukrowy, ogórek melon"},
    known_for=[
        {
            EN: "cantaloupe",
            PL: "kantalupa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cantaloupes.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Cantaloupes.jpg",
                author="USDA photo by Scott Bauer. Image Number K7355-11.",
                license=License.USDA,
            ),
        },
        {
            EN: "honeydew",
            PL: "melon spadziowy",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Honeydew.Melon.2.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Honeydew.Melon.2.jpg",
                author="Church of emacs",
                license=License.CC_BY_SA_4_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cucumis_melo_34.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Cucumis_melo_34.jpg",
        author="Wilfredor",
        license=License.CC0,
    ),
)
C_PEPO = Species(
    name="Cucurbita pepo",
    local_names={PL: "dynia zwyczajna"},
    known_for=[
        {
            EN: "pumpkin",
            PL: "dynia",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pumpkin.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/f7/Pumpkin.jpg",
                author="Fredde 99",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "pattypan squash, scallop squash",
            PL: "patison",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pattypan_squash_J3.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/Pattypan_squash_J3.JPG",
                author="Jamain",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "zucchini, courgette",
            PL: "cukinia, kabaczek",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Zucchini_(20221106509).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Zucchini_%2820221106509%29.jpg",
                author="Willis Lam",
                license=License.CC_BY_SA_2_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_080815-9759_Cucurbita_pepo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Starr_080815-9759_Cucurbita_pepo.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
C_MOSCHATA = Species(
    name="Cucurbita moschata",
    local_names={PL: "dynia piżmowa"},
    known_for=[
        {
            EN: "butternut squash",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cucurbita_moschata_Butternut_2012_G2.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Cucurbita_moschata_Butternut_2012_G2.jpg",
                author="George Chernilevsky",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cucurbita_moschata_(zapallo_espont%C3%A1neo)_flor_masculina_M09_M10_antesis_vista_lateral_orientaci%C3%B3n.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Cucurbita_moschata_%28zapallo_espont%C3%A1neo%29_flor_masculina_M09_M10_antesis_vista_lateral_orientaci%C3%B3n.JPG",
        author="RoRo",
        license=License.CC0,
    ),
)
B_TUBERHYBRIDA = Species(
    name="Begonia × tuberhybrida",
    local_names={PL: "begonia bulwiasta", EN: "tuberous begonia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Begonia_%C3%97_tuberhybrida_-_Kew_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Begonia_%C3%97_tuberhybrida_-_Kew_1.jpg",
        author="Emőke Dénes",
        license=License.CC_BY_SA_4_0,
    ),
)

LAGENARIA = Genus(name="Lagenaria", children=[L_SICERARIA])
CITRULLUS = Genus(name="Citrullus", children=[C_LANATUS])
CUCUMIS = Genus(name="Cucumis", children=[C_SATIVUS, C_MELO])
CUCURBITA = Genus(name="Cucurbita", children=[C_PEPO, C_MOSCHATA])
BEGONIA = Genus(name="Begonia", children=[B_TUBERHYBRIDA])

BENINCASINAE = Subtribe(name="Benincasinae", children=[LAGENARIA, CITRULLUS])

BENINCASEAE = Tribe(name="Benincaseae", children=[BENINCASINAE, CUCUMIS])
CUCURBITEAE = Tribe(name="Cucurbiteae", children=[CUCURBITA])

CUCURBITOIDEAE = Subfamily(name="Cucurbitoideae", children=[BENINCASEAE])

CUCURBITACEAE = Family(name="Cucurbitaceae", children=[CUCURBITOIDEAE, CUCURBITEAE])
BEGONIACEAE = Family(name="Begoniaceae", children=[BEGONIA])

CUCURBITALES = Order(name="Cucurbitales", children=[CUCURBITACEAE, BEGONIACEAE])
