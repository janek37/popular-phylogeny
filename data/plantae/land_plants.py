from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subclass
from constants import EN, PL
from image import Image, License

from .angiospermae import ANGIOSPERMAE
from .gymnospermae import GYMNOSPERMAE

P_COMMUNE = Species(
    name="Polytrichum commune",
    local_names={EN: "common haircap moss", PL: "płonnik pospolity"},
    known_for=[{EN: "one of the most common mosses"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Polytrichum_commune_.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Polytrichum_commune_.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
L_GLAUCUM = Species(
    name="Leucobryum glaucum",
    local_names={EN: "pin cusion moss", PL: "bielistka siwa"},
    known_for=[{EN: "one of the most common mosses"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leucobryum_glaucum_148778151.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Leucobryum_glaucum_148778151.jpg",
        author="Tomas Pocius",
        license=License.CC0,
    ),
)
P_AQUILINUM = Species(
    name="Pteridium aquilinum",
    local_names={EN: "common bracken, eagle fern", PL: "orlica pospolita"},
    known_for=[{EN: "one of the most common ferns"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pteridium_aquilinum_176152491.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Pteridium_aquilinum_176152491.jpg",
        author="Tom Scavo",
        license=License.CC_BY_SA_4_0,
    ),
)
A_AUSTRALIS = Species(name="Alsophila australis", local_names={EN: "rough tree fern"})
M_QUADRIFOLIA = Species(
    name="Marsilea quadrifolia",
    local_names={EN: "four leaf clover", PL: "marsylia czterolistna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Marsilea_quadrifolia_kz13.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/da/Marsilea_quadrifolia_kz13.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
L_CLAVATUM = Species(
    name="Lycopodium clavatum",
    local_names={EN: "common club moss, stag's-horn clubmoss", PL: "widłak goździsty"},
    known_for=[
        {EN: "one of the most common lycophytes", PL: "jeden z najczęstszych widłaków"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:LycopodiumClavatum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/LycopodiumClavatum.jpg",
        author="Christian Fischer",
        license=License.CC_BY_SA_3_0,
    ),
)
L_LYCOPODIOIDES = Species(
    name="Lepidodendron lycopodioides",
    known_for=[
        {
            EN: "extinct giant club moss (scale tree)",
            PL: "jeden z wymarłych ogromnych widłaków",
        }
    ],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stigmaria_Heimans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Stigmaria_Heimans.jpg",
        author="Eli Heimans",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_ARVENSE = Species(
    name="Equisetum arvense",
    local_names={EN: "field horsetail", PL: "skrzyp polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Equisetum_arvense_117578468.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Equisetum_arvense_117578468.jpg",
        author="Oleg Kosterin",
        license=License.CC_BY_4_0,
    ),
)
C_SUCKOWII = Species(
    name="Calamites suckowii",
    known_for=[
        {EN: "extinct giant horsetail", PL: "jeden z wymarłych ogromnych skrzypów"}
    ],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Calamites_reconstrucci%C3%B3n.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Calamites_reconstrucci%C3%B3n.png",
        author="Falconaumanni",
        license=License.CC_BY_SA_3_0,
    ),
)

POLYTRICHUM = Genus(name="Polytrichum", children=[P_COMMUNE])
LEUCOBRYUM = Genus(name="Leucobryum", children=[L_GLAUCUM])
PTERIDIUM = Genus(name="Pteridium", children=[P_AQUILINUM])
ALSOPHILA = Genus(name="Alsophila", children=[A_AUSTRALIS])
MARSILEA = Genus(name="Marsilea", children=[M_QUADRIFOLIA])
LYCOPODIUM = Genus(name="Lycopodium", children=[L_CLAVATUM])
LEPIDODENDRON = Genus(name="Lepidodendron", children=[L_LYCOPODIOIDES])
EQUISETUM = Genus(name="Equisetum", children=[E_ARVENSE])
CALAMITES = Genus(name="Calamites", children=[C_SUCKOWII])

POLYTRICHACEAE = Family(name="Polytrichaceae", children=[POLYTRICHUM])
LEUCOBRYACEAE = Family(name="Leucobryaceae", children=[LEUCOBRYUM])
DENNSTAEDTIACEAE = Family(name="Dennstaedtiaceae", children=[PTERIDIUM])
CYATHEACEAE = Family(name="Cyatheaceae", children=[ALSOPHILA])
MARSILEACEAE = Family(name="Marsileaceae", children=[MARSILEA])
LYCOPODIACEAE = Family(name="Lycopodiaceae", children=[LYCOPODIUM])
LEPIDODENDRACEAE = Family(name="Lepidodendraceae", children=[LEPIDODENDRON])
EQUISETACEAE = Family(name="Equisetaceae", children=[EQUISETUM])
CALAMITACEAE = Family(name="Calamitaceae", children=[CALAMITES])

POLYTRICHALES = Order(name="Polytrichales", children=[POLYTRICHACEAE])
DICRANALES = Order(name="Dicranales", children=[LEUCOBRYACEAE])
POLYPODIALES = Order(name="Polypodiales", children=[DENNSTAEDTIACEAE])
CYATHEALES = Order(name="Cyatheales", children=[CYATHEACEAE])
SALVINIALES = Order(name="Salviniales", children=[MARSILEACEAE])
LYCOPODIALES = Order(name="Lycopodiales", children=[LYCOPODIACEAE])
LEPIDODENDRALES = Order(name="Lepidodendrales", children=[LEPIDODENDRACEAE])
EQUISETALES = Order(name="Equisetales", children=[EQUISETACEAE, CALAMITACEAE])

POLYPODIALES_CYATHEALES = Clade(children=[POLYPODIALES, CYATHEALES])

POLYPODIIDAE = Subclass(
    name="Polypodiidae", children=[POLYPODIALES_CYATHEALES, SALVINIALES]
)
EQUISETIDAE = Subclass(name="Equisetidae", children=[EQUISETALES])

POLYTRICHOPSIDA = Class(name="Polytrichopsida", children=[POLYTRICHALES])
BRYOPSIDA = Class(name="Bryopsida", children=[DICRANALES])
POLYPODIOPSIDA = Class(name="Polypodiopsida", children=[POLYPODIIDAE, EQUISETIDAE])
LYCOPODIOPSIDA = Class(name="Lycopodiopsida", children=[LYCOPODIALES, LEPIDODENDRALES])

BRYOPHYTA = Phylum(name="Bryophyta", children=[POLYTRICHOPSIDA, BRYOPSIDA])
POLYPODIOPHYTA = Phylum(name="Polypodiophyta", children=[POLYPODIOPSIDA])
LYCOPHYTES = Phylum(name="Lycophytes", children=[LYCOPODIOPSIDA])

SPERMATOPHYTA = Clade(name="Spermatophyta", children=[GYMNOSPERMAE, ANGIOSPERMAE])
MEGAPHYLLS = Clade(name="Megaphylls", children=[POLYPODIOPHYTA, SPERMATOPHYTA])
TRACHEOPHYTES = Clade(name="Tracheophytes", children=[MEGAPHYLLS, LYCOPHYTES])

EMBRYOPHYTA = Clade(name="Embryophyta", children=[BRYOPHYTA, TRACHEOPHYTES])
