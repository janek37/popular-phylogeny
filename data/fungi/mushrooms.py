from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Subclass
from constants import EN, IT, JP, PL
from image import Image, License

from .agaricales import AGARICALES

G_FRONDOSA = Species(
    name="Grifola frondosa",
    local_names={EN: "hen-of-the-woods", JP: "maitake"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Grifola_frondosa_(29381622514).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Grifola_frondosa_%2829381622514%29.jpg",
        author="Lukas from London, England",
        license=License.CC_BY_SA_2_0,
    ),
)
H_REPANDUM = Species(
    name="Hydnum repandum",
    local_names={EN: "hedgehog mushroom"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Semmel-Stoppelpilz_Semmelgelber_Stacheling_Hydnum_repandum.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/31/Semmel-Stoppelpilz_Semmelgelber_Stacheling_Hydnum_repandum.JPG",
        author="Holger Krisp",
        license=License.CC_BY_3_0,
    ),
)
B_EDULIS = Species(
    name="Boletus edulis",
    local_names={IT: "fungo porcino", PL: "borowik szlachetny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Boletus_edulis_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/75/Boletus_edulis_1.jpg",
        author="Michael Wood",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CIBARIUS = Species(
    name="Cantharellus cibarius",
    local_names={EN: "chantarelle", PL: "kurka, pieprznik jadalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cantharellus_cibarius_60028898.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Cantharellus_cibarius_60028898.jpg",
        author="Nina Filippova",
        license=License.CC_BY_4_0,
    ),
)
L_SULPHUREUS = Species(
    name="Laetiporus sulphureus",
    local_names={EN: "chicken-of-the-woods"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Laetiporus_sulphureus_in_Lutsk,_2020.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Laetiporus_sulphureus_in_Lutsk%2C_2020.jpg",
        author="Віщун",
        license=License.CC_BY_SA_4_0,
    ),
)
R_SATANAS = Species(
    name="Rubroboletus satanas",
    local_names={PL: "borowik szatański", EN: "Satan's bolete"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Park_grzybowy_w_Pilce_(boletus_satanas).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Park_grzybowy_w_Pilce_%28boletus_satanas%29.JPG",
        author="MOs810",
        license=License.CC_BY_SA_4_0,
    ),
)
L_DELICIOSUS = Species(
    name="Lactarius deliciosus",
    local_names={PL: "mleczaj rydz", EN: "saffron milk cap"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lactarius-deliciosus-Finland.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Lactarius-deliciosus-Finland.jpg",
        author="Petritap",
        license=License.CC_BY_SA_3_0,
    ),
)
P_INDUSIATUS = Species(
    name="Phallus indusiatus",
    local_names={EN: "bamboo mushroom, bridal veil stinkhorn"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phallus_indusiatus_87771437.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Phallus_indusiatus_87771437.jpg",
        author="葉子",
        license=License.CC_BY_4_0,
    ),
)
P_IMPUDICUS = Species(
    name="Phallus impudicus",
    local_names={
        EN: "common stinkhorn",
        PL: "sromotnik bezwstydny, sromotnik smrodliwy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phallus_impudicus_82122614.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Phallus_impudicus_82122614.jpg",
        author="silvan95",
        license=License.CC_BY_4_0,
    ),
)
H_PECKII = Species(
    name="Hydnellum peckii",
    local_names={EN: "Devil's tooth"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hydnellum_peckii2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Hydnellum_peckii2.jpg",
        author="Bernypisa",
        license=License.CC_BY_SA_3_0,
    ),
)
R_VESCA = Species(
    name="Russula vesca",
    local_names={EN: "bare-toothed Russula", PL: "gołąbek wyborny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Russula_vesca.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Russula_vesca.jpg",
        author="Walter J. Pilsak, Waldsassen",
        license=License.CC_BY_SA_3_0,
    ),
)
S_LUTEUS = Species(
    name="Suillus luteus",
    local_names={EN: "slippery jack, sticky bun", PL: "maślak zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Suillus_luteus_113280.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Suillus_luteus_113280.jpg",
        author="Tim Sage (T. Sage)",
        license=License.CC_BY_SA_3_0,
    ),
)

GRIFOLA = Genus(name="Grifola", children=[G_FRONDOSA])
HYDNUM = Genus(name="Hydnum", children=[H_REPANDUM])
BOLETUS = Genus(name="Boletus", children=[B_EDULIS])
CANTHARELLUS = Genus(name="Cantharellus", children=[C_CIBARIUS])
LAETIPORUS = Genus(name="Laetiporus", children=[L_SULPHUREUS])
RUBROBOLETUS = Genus(name="Rubroboletus", children=[R_SATANAS])
LACTORIUS = Genus(name="Lactorius", children=[L_DELICIOSUS])
PHALLUS = Genus(name="Phallus", children=[P_INDUSIATUS, P_IMPUDICUS])
HYDNELLUM = Genus(name="Hydnellum", children=[H_PECKII])
RUSSULA = Genus(name="Russula", children=[R_VESCA])
SUILLUS = Genus(name="Suillus", children=[S_LUTEUS])

MERIPILACEAE = Family(name="Meripilaceae", children=[GRIFOLA])
HYDNACEAE = Family(name="Hydnaceae", children=[HYDNUM])
BOLETACEAE = Family(name="Boletaceae", children=[BOLETUS, RUBROBOLETUS])
CANTHARELLACEAE = Family(name="Cantharellaceae", children=[CANTHARELLUS])
POLYPORACEAE = Family(name="Polyporaceae", children=[LAETIPORUS])
RUSSULACEAE = Family(name="Russulaceae", children=[LACTORIUS, RUSSULA])
PHALLACEAE = Family(name="Phallaceae", children=[PHALLUS])
BANKERACEAE = Family(name="Bankeraceae", children=[HYDNELLUM])
SUILLACEAE = Family(name="Suillaceae", children=[SUILLUS])

POLYPORALES = Order(name="Polyporales", children=[MERIPILACEAE, POLYPORACEAE])
CANTHARELLALES = Order(name="Cantharellales", children=[HYDNACEAE, CANTHARELLACEAE])
BOLETALES = Order(name="Boletales", children=[BOLETACEAE, SUILLACEAE])
RUSSULALES = Order(name="Russulales", children=[RUSSULACEAE])
PHALLALES = Order(name="Phallales", children=[PHALLACEAE])
THELEPHORALES = Order(name="Thelephorales", children=[BANKERACEAE])

AGARICOMYCETIDAE = Subclass(name="Agaricomycetidae", children=[AGARICALES, BOLETALES])
POLYPORALES_THELEPHORALES = Clade(children=[POLYPORALES, THELEPHORALES])

AGARICOMYCETES_A = Clade(children=[AGARICOMYCETIDAE, RUSSULALES])
AGARICOMYCETES_B = Clade(children=[AGARICOMYCETES_A, POLYPORALES_THELEPHORALES])
AGARICOMYCETES_C = Clade(children=[AGARICOMYCETES_B, PHALLALES])

AGARICOMYCETES = Class(
    name="Agaricomycetes", children=[AGARICOMYCETES_C, CANTHARELLALES]
)

BASIDIOMYCOTA = Phylum(name="Basidiomycota", children=[AGARICOMYCETES])
