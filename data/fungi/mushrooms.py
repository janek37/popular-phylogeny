from clade import Clade, Class, Family, Genus, Order, Phylum, Species
from constants import EN, IT, JP, PL

from .agaricales import AGARICALES

G_FRONDOSA = Species(
    name="Grifola frondosa",
    local_names={EN: "hen-of-the-woods", JP: "maitake"},
)
H_REPANDUM = Species(name="Hydnum repandum", local_names={EN: "hedgehog mushroom"})
B_EDULIS = Species(
    name="Boletus edulis", local_names={IT: "fungo porcino", PL: "borowik szlachetny"}
)
C_CIBARIUS = Species(
    name="Cantharellus cibarius",
    local_names={EN: "chantarelle", PL: "kurka, pieprznik jadalny"},
)
L_SULPHUREUS = Species(
    name="Laetiporus sulphureus", local_names={EN: "chicken-of-the-woods"}
)
R_SATANAS = Species(
    name="Rubroboletus satanas",
    local_names={PL: "borowik szatański", EN: "Satan's bolete"},
)
L_DELICIOSUS = Species(
    name="Lactarius deliciosus",
    local_names={PL: "mleczaj rydz", EN: "saffron milk cap"},
)
P_INDUSIATUS = Species(name="Phallus indusiatus", local_names={EN: "bamboo mushroom"})
H_PECKII = Species(name="Hydnellum peckii", local_names={EN: "Devil's tooth"})

GRIFOLA = Genus(name="Grifola", children=[G_FRONDOSA])
HYDNUM = Genus(name="Hydnum", children=[H_REPANDUM])
BOLETUS = Genus(name="Boletus", children=[B_EDULIS])
CANTHARELLUS = Genus(name="Cantharellus", children=[C_CIBARIUS])
LAETIPORUS = Genus(name="Laetiporus", children=[L_SULPHUREUS])
RUBROBOLETUS = Genus(name="Rubroboletus", children=[R_SATANAS])
LACTORIUS = Genus(name="Lactorius", children=[L_DELICIOSUS])
PHALLUS = Genus(name="Phallus", children=[P_INDUSIATUS])
HYDNELLUM = Genus(name="Hydnellum", children=[H_PECKII])

MERIPILACEAE = Family(name="Meripilaceae", children=[GRIFOLA])
HYDNACEAE = Family(name="Hydnaceae", children=[HYDNUM])
BOLETACEAE = Family(name="Boletaceae", children=[BOLETUS, RUBROBOLETUS])
CANTHARELLACEAE = Family(name="Cantharellaceae", children=[CANTHARELLUS])
POLYPORACEAE = Family(name="Polyporaceae", children=[LAETIPORUS])
RUSSULACEAE = Family(name="Russulaceae", children=[LACTORIUS])
PHALLACEAE = Family(name="Phallaceae", children=[PHALLUS])
BANKERACEAE = Family(name="Bankeraceae", children=[HYDNELLUM])

POLYPORALES = Order(name="Polyporales", children=[MERIPILACEAE, POLYPORACEAE])
CANTHARELLALES = Order(name="Cantharellales", children=[HYDNACEAE, CANTHARELLACEAE])
BOLETALES = Order(name="Boletales", children=[BOLETACEAE])
RUSSULALES = Order(name="Russulales", children=[RUSSULACEAE])
PHALLALES = Order(name="Phallales", children=[PHALLACEAE])
THELEPHORALES = Order(name="Thelephorales", children=[BANKERACEAE])

AGARICOMYCETIDAE = Clade(
    name="Agaricomycetidae", children=[AGARICALES, BOLETALES]
)  # Subclass
POLYPORALES_THELEPHORALES = Clade(children=[POLYPORALES, THELEPHORALES])

AGARICOMYCETES_A = Clade(children=[AGARICOMYCETIDAE, RUSSULALES])
AGARICOMYCETES_B = Clade(children=[AGARICOMYCETES_A, POLYPORALES_THELEPHORALES])
AGARICOMYCETES_C = Clade(children=[AGARICOMYCETES_B, PHALLALES])

AGARICOMYCETES = Class(
    name="Agaricomycetes", children=[AGARICOMYCETES_C, CANTHARELLALES]
)

BASIDIOMYCOTA = Phylum(name="Basidiomycota", children=[AGARICOMYCETES])
