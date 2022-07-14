from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .lamiales import LAMIALES
from .solanales import SOLANALES

M_SYLVATICA = Species(
    name="Myosotis sylvatica",
    local_names={EN: "forget-me-not", PL: "niezapominajka leśna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myosotis_sylvatica_%27Bluesylva%27_Niezapominajka_le%C5%9Bna_2019-04-06_05.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Myosotis_sylvatica_%27Bluesylva%27_Niezapominajka_le%C5%9Bna_2019-04-06_05.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
S_OFFICINALE = Species(
    name="Symphytum officinale",
    local_names={EN: "common comfrey", PL: "żywokost lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Symphytum_officinale_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Symphytum_officinale_02.jpg",
        author="Agnieszka Kwiecień (Nova)",
        license=License.CC_BY_SA_3_0,
    ),
)
B_OFFICINALIS = Species(
    name="Borago officinalis",
    local_names={EN: "borage, starflower", PL: "ogórecznik lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Borago_officinalis_-_Fior_di_Borraggine.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/01/Borago_officinalis_-_Fior_di_Borraggine.jpg",
        author="PROPOLI87",
        license=License.CC_BY_SA_4_0,
    ),
)
C_ARABICA = Species(
    name="Coffea arabica",
    local_names={EN: "Arabian coffee", PL: "kawa arabska"},
    known_for=[
        {
            EN: "arabica coffee",
            PL: "kawa arabica",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Roasted_arabica_coffee_beans_Minca.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/Roasted_arabica_coffee_beans_Minca.jpg",
                author="Roger Burger",
                license=License.CC0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20210529_Coffea_arabica_blossom_011.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/20210529_Coffea_arabica_blossom_011.jpg",
        author="Zinnmann",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CANEPHORA = Species(
    name="Coffea canephora",
    local_names={EN: "robusta coffee", PL: "robusta, kawa kongijska"},
    known_for=[
        {
            EN: "the second most popular coffee species",
            PL: "kawa robusta",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Coffea_canephora-Mus%C3%A9e_botanique_de_Berlin.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/7e/Coffea_canephora-Mus%C3%A9e_botanique_de_Berlin.jpg",
                author="Ji-Elle",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coffea_canephora_6.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Coffea_canephora_6.JPG",
        author="Vinayaraj",
        license=License.CC_BY_SA_3_0,
    ),
)
C_OFFICINALIS = Species(
    name="Cinchona officinalis",
    local_names={PL: "chinowiec lekarski"},
    known_for=[
        {
            PL: "chinina",
            EN: "quinine",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:QuinineBKchemSVG.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/QuinineBKchemSVG.svg",
                author="Darkness3560",
                license=License.CC0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cinchona_officinalis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-180.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/Cinchona_officinalis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-180.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_NUX_VOMICA = Species(
    name="Strychnos nux-vomica",
    local_names={PL: "kulczyba wronie oko", EN: "strychnine tree"},
    known_for=[
        {
            EN: "strychnine",
            PL: "strychnina",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Strychnine2.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/41/Strychnine2.svg",
                author="Calvero.",
                license=License.PUBLIC_DOMAIN_INELIGIBLE,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Strychnos_nux-vomica_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-266.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Strychnos_nux-vomica_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-266.jpg",
        author="Franz Eugen Köhler",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
N_OLEANDER = Species(
    name="Nerium oleander",
    local_names={EN: "oleander, nerium", PL: "oleander pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nerium_oleander_flowers_leaves.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cc/Nerium_oleander_flowers_leaves.jpg",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)

MYOSOTIS = Genus(name="Myosotis", children=[M_SYLVATICA])
SYMPHYTUM = Genus(name="Symphytum", children=[S_OFFICINALE])
BORAGO = Genus(name="Borago", children=[B_OFFICINALIS])
COFFEA = Genus(name="Coffea", children=[C_ARABICA, C_CANEPHORA])
CINCHONA = Genus(name="Cinchona", children=[C_OFFICINALIS])
STRYCHNOS = Genus(name="Strychnos", children=[S_NUX_VOMICA])
NERIUM = Genus(name="Nerium", children=[N_OLEANDER])

ERITRICHIEAE = Tribe(name="Eritrichieae", children=[MYOSOTIS])
BORAGINEAE = Tribe(name="Boragineae", children=[SYMPHYTUM, BORAGO])

BORAGINACEAE = Family(name="Boraginaceae", children=[ERITRICHIEAE, BORAGINEAE])
RUBIACEAE = Family(name="Rubiaceae", children=[COFFEA, CINCHONA])
LOGANIACEAE = Family(name="Loganiaceae", children=[STRYCHNOS])
APOCYNACEAE = Family(name="Apocynaceae", children=[NERIUM])

GENTIANALES_A = Clade(children=[LOGANIACEAE, APOCYNACEAE])

BORAGINALES = Order(name="Boraginales", children=[BORAGINACEAE])
GENTIANALES = Order(name="Gentianales", children=[RUBIACEAE, GENTIANALES_A])

# Boraginales and Lamiales may be sisters, but the evidence is weak so far
LAMIIDS = Clade(
    name="lamiids", children=[BORAGINALES, GENTIANALES, LAMIALES, SOLANALES]
)
