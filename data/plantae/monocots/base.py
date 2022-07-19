from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, IMAGE, PL, URL
from image import Image, License

from .asparagales import ASPARAGALES
from .poales import POALES

A_CALAMUS = Species(
    name="Acorus calamus",
    local_names={EN: "sweet flag", PL: "tatarak zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acorus_calamus1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Acorus_calamus1.jpg",
        author="J.F. Gaffard, Autoreille, France",
        license=License.CC_BY_SA_3_0,
    ),
)
Z_MARINA = Species(
    name="Zostera marina",
    local_names={EN: "eelgrass", PL: "trawa morska, zostera morska"},
    known_for=[{EN: "one of the most common species of seagrass"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zostera_marina_Shikoku_Aquarium.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/Zostera_marina_Shikoku_Aquarium.jpg",
        author="Totti",
        license=License.CC_BY_SA_4_0,
    ),
)
L_MINOR = Species(
    name="Lemna minor",
    local_names={EN: "common duckweed", PL: "rzęsa wodna, rzęsa drobna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lemna_minor-floating_on_water.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/43/Lemna_minor-floating_on_water.jpg",
        author="Abrimaal at Polish Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
L_CANDIDUM = Species(
    name="Lilium candidum",
    local_names={EN: "Madonna lily", PL: "lilia biała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lilium_candidum_(14434339854).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Lilium_candidum_%2814434339854%29.jpg",
        author="peganum from Henfield, England",
        license=License.CC_BY_SA_2_0,
    ),
)
L_LANCIFOLIUM = Species(
    name="Lilium lancifolium",
    local_names={EN: "tiger lily", PL: "lilia tygrysia"},
    known_for=[
        {
            EN: "chief's daughter in Peter Pan",
            URL: "https://en.wikipedia.org/wiki/Tiger_Lily_(Peter_Pan)",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lilium_lancifolium_002.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Lilium_lancifolium_002.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
T_GESNERIANA = Species(
    name="Tulipa gesneriana",
    local_names={EN: "garden tulip", PL: "tulipan ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tulpan_(Tulipa_gesneriana))003.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Tulpan_%28Tulipa_gesneriana%29%29003.jpg",
        author="Bernt Fransson",
        license=License.CC_BY_SA_4_0,
    ),
)
C_NUCIFERA = Species(
    name="Cocos nucifera",
    local_names={EN: "coconut palm", PL: "palma kokosowa, kokos właściwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cocos_nucifera_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-187.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Cocos_nucifera_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-187.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_GUINEENSIS = Species(
    name="Elaeis guineensis",
    local_names={EN: "oil palm", PL: "palma olejowa, olejowiec gwinejski"},
    known_for=[{EN: "palm oil", PL: "olej palmowy"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elaeis_guineensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-056.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6e/Elaeis_guineensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-056.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_OLERACEA = Species(
    name="Euterpe oleracea",
    local_names={EN: "açaí palm", PL: "euterpa warzywna"},
    known_for=[
        {
            EN: "açaí berries",
            PL: "jagody açaí",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:A%C3%A7a%C3%AD_debulhado.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/5/5e/A%C3%A7a%C3%AD_debulhado.jpg",
                author="Marajonida",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:A%C3%A7aizeiro_no_pal%C3%A1cio.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/A%C3%A7aizeiro_no_pal%C3%A1cio.JPG",
        author="User:Arouck",
        license=License.PUBLIC_DOMAIN_AUTHOR,
    ),
)
P_DACTYLIFERA = Species(
    name="Phoenix dactylifera",
    local_names={EN: "date palm", PL: "palma daktylowa, daktylowiec właściwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phoenix_dactylifera2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c0/Phoenix_dactylifera2.jpg",
        author="No machine-readable author provided. MPF assumed (based on copyright claims).",
        license=License.CC_BY_SA_3_0,
    ),
)
A_MERRILLII = Species(
    name="Adonidia merrillii",
    local_names={EN: "Manila palm, Christmas palm", PL: "palma bożonarodzeniowa"},
    known_for=[{EN: "commonly placed in hotels, casinos and shopping malls"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_070123-3594_Veitchia_merrillii.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Starr_070123-3594_Veitchia_merrillii.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
M_PARADISIACA = Species(
    name="Musa × paradisiaca",
    local_names={EN: "banana", PL: "banan zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Musa_paradisiaca_Blanco1.88.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0d/Musa_paradisiaca_Blanco1.88.png",
        author="Francisco Manuel Blanco (O.S.A.)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
Z_OFFICINALE = Species(
    name="Zingiber officinale",
    local_names={EN: "ginger", PL: "imbir lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Koeh-146-no_text.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Koeh-146-no_text.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_CARDAMOMUM = Species(
    name="Elettaria cardamomum",
    local_names={EN: "green cardamom", PL: "kardamon malabarski"},
    known_for=[
        {
            EN: "edible seeds used as a spice",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Elettaria_cardamomum_Capsules_and_seeds.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/2c/Elettaria_cardamomum_Capsules_and_seeds.jpg",
                author="Didier Descouens",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elettaria_cardamomum_0zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Elettaria_cardamomum_0zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
C_LONGA = Species(
    name="Curcuma longa",
    local_names={EN: "turmeric", PL: "kurkuma, ostryż długi"},
    known_for=[
        {
            EN: "edible rhizome used for seasoning",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Curcuma_longa_roots.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Curcuma_longa_roots.jpg",
                author="Simon A. Eugster",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Curcuma_longa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/47/Curcuma_longa.jpg",
        author="Lucien Monfils",
        license=License.CC_BY_SA_3_0,
    ),
)

ACORUS = Genus(name="Acorus", children=[A_CALAMUS])
ZOSTERA = Genus(name="Zostera", children=[Z_MARINA])
LEMNA = Genus(name="Lemna", children=[L_MINOR])
LILIUM = Genus(name="Lilium", children=[L_CANDIDUM, L_LANCIFOLIUM])
TULIPA = Genus(name="Tulipa", children=[T_GESNERIANA])
COCOS = Genus(name="Cocos", children=[C_NUCIFERA])
ELAEIS = Genus(name="Elaeis", children=[E_GUINEENSIS])
EUTERPE = Genus(name="Euterpe", children=[E_OLERACEA])
PHOENIX = Genus(name="Phoenix", children=[P_DACTYLIFERA])
ADONIDIA = Genus(name="Adonidia", children=[A_MERRILLII])
MUSA = Genus(name="Musa", children=[M_PARADISIACA])
ZINGIBER = Genus(name="Zingiber", children=[Z_OFFICINALE])
ELETTARIA = Genus(name="Elettaria", children=[E_CARDAMOMUM])
CURCUMA = Genus(name="Curcuma", children=[C_LONGA])

COCOSEAE = Tribe(name="Cocoseae", children=[COCOS, ELAEIS])
EUTERPEAE = Tribe(name="Euterpeae", children=[EUTERPE])
PHOENICEAE = Tribe(name="Phoeniceae", children=[PHOENIX])
ARECAE = Tribe(name="Arecae", children=[ADONIDIA])
ZINGIBEREAE = Tribe(name="Zingibereae", children=[ZINGIBER, CURCUMA])
ALPINIEAE = Tribe(name="Alpinieae", children=[ELETTARIA])

# https://www.researchgate.net/publication/44651559_Complete_Generic-Level_Phylogenetic_Analyses_of_Palms_Arecaceae_with_Comparisons_of_Supertree_and_Supermatrix_Approaches/figures
ARECOIDEAE_A = Clade(children=[EUTERPEAE, ARECAE])

ARECOIDEAE = Subfamily(name="Arecoideae", children=[COCOSEAE, ARECOIDEAE_A])
CORYPHOIDEAE = Subfamily(name="Coryphoideae", children=[PHOENICEAE])

ACORACEAE = Family(name="Acoraceae", children=[ACORUS])
ZOSTERACEAE = Family(name="Zosteraceae", children=[ZOSTERA])
ARACEAE = Family(name="Araceae", children=[LEMNA])
LILIACEAE = Family(name="Liliaceae", children=[LILIUM, TULIPA])
ARECACEAE = Family(name="Arecaceae", children=[ARECOIDEAE, CORYPHOIDEAE])
MUSACEAE = Family(name="Musaceae", children=[MUSA])
ZINGIBERACEAE = Family(name="Zingiberaceae", children=[ZINGIBEREAE, ALPINIEAE])

ACORALES = Order(name="Acorales", children=[ACORACEAE])
ALISMATALES = Order(name="Alismatales", children=[ZOSTERACEAE, ARACEAE])
LILIALES = Order(name="Liliales", children=[LILIACEAE])
ARECALES = Order(name="Arecales", children=[ARECACEAE])
ZINGIBERALES = Order(name="Zingiberales", children=[MUSACEAE, ZINGIBERACEAE])

ZINGIBERALES_POALES = Clade(children=[ZINGIBERALES, POALES])
COMMELINIDAE = Clade(name="commelinidae", children=[ARECALES, ZINGIBERALES_POALES])

ASPARAGALES_COMMELINIDS = Clade(children=[ASPARAGALES, COMMELINIDAE])
MONOCOTYLEDONES_B = Clade(children=[LILIALES, ASPARAGALES_COMMELINIDS])
MONOCOTYLEDONES_A = Clade(children=[ALISMATALES, MONOCOTYLEDONES_B])

MONOCOTYLEDONES = Clade(
    name="monocotyledones",
    local_names={EN: "monocots", PL: "jednoliścienne"},
    children=[ACORALES, MONOCOTYLEDONES_A],
)
