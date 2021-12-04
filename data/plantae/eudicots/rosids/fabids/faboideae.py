from clade import Clade, Genus, Species, Subfamily, Tribe
from constants import EN, PL

P_SATIVUM = Species(
    name="Pisum sativum", local_names={EN: "pea", PL: "groch zwyczajny"}
)
L_ODORATUS = Species(
    name="Lathyrus odoratus", local_names={EN: "sweat pea", PL: "groszek pachnący"}
)
R_PSEUDOACACIA = Species(
    name="Robinia pseudoacacia",
    local_names={EN: "black locust, false acacia", PL: "robinia akacjowa"},
)
A_LINEARIS = Species(
    name="Aspalathus linearis",
    local_names={EN: "rooibos", PL: "aspalat prosty"},
    known_for={EN: "rooibos herbal tea"},
)
L_ALBUS = Species(
    name="Lupinus albus", local_names={EN: "white lupin", PL: "łubin biały"}
)
A_HYPOGAEA = Species(
    name="Arachis hypogaea",
    local_names={
        EN: "peanut",
        PL: "orzech ziemny, orzech arachidowy, orzacha podziemna",
    },
    known_for={EN: "peanuts", PL: "orzeszki ziemne, fistaszki"},
)
C_ARIETINUM = Species(
    name="Cicer arietinum",
    local_names={EN: "chickpea", PL: "cieciorka, ciecierzyca pospolita"},
    known_for=[{EN: "falafel"}, {EN: "hummus"}, {EN: "chana masala"}],
)
G_MAX = Species(name="Glycine max", local_names={EN: "soybean", PL: "soja"})
P_VULGARIS = Species(
    name="Phaseolus vulgaris",
    local_names={EN: "common bean", PL: "fasola zwykła"},
    known_for=[{EN: "green beans, string beans", PL: "fasolka szparagowa"}],
)
T_PRATENSE = Species(
    name="Trifolium pratense", local_names={EN: "red clover", PL: "koniczyna łąkowa"}
)
T_REPENS = Species(
    name="Trifolium repens", local_names={EN: "white clover", PL: "koniczyna biała"}
)
V_FABA = Species(name="Vicia faba", local_names={EN: "broad bean", PL: "wyka bób"})
L_CULINARIS = Species(
    name="Lens culinaris", local_names={EN: "lentil", PL: "soczewica jadalna"}
)
G_GLABRA = Species(
    name="Glycyrrhiza glabra",
    local_names={EN: "liquorice, licorice", PL: "lukrecja gładka"},
)
T_FOENUM_GRAECUM = Species(
    name="Trigonella foenum-graecum",
    local_names={EN: "fenugreek", PL: "kozieradka pospolita"},
)

PISUM = Genus(name="Pisum", children=[P_SATIVUM])
LATHYRUS = Genus(name="Lathyrus", children=[L_ODORATUS])
ROBINIA = Genus(name="Robinia", children=[R_PSEUDOACACIA])
ASPALATHUS = Genus(name="Aspalathus", children=[A_LINEARIS])
LUPINUS = Genus(name="Lupinus", children=[L_ALBUS])
ARACHIS = Genus(name="Arachis", children=[A_HYPOGAEA])
CICER = Genus(name="Cicer", children=[C_ARIETINUM])
GLYCINE = Genus(name="Glycine", children=[G_MAX])
PHASEOLUS = Genus(name="Phaseolus", children=[P_VULGARIS])
TRIFOLIUM = Genus(name="Trifolium", children=[T_PRATENSE, T_REPENS])
VICIA = Genus(name="Vicia", children=[V_FABA])
LENS = Genus(name="Lens", children=[L_CULINARIS])
GLYCYRRHIZA = Genus(name="Glycyrrhiza", children=[G_GLABRA])
TRIGONELLA = Genus(name="Trigonella", children=[T_FOENUM_GRAECUM])

# https://www.researchgate.net/publication/233989057_Systematics_biogeography_and_character_evolution_of_the_legume_tribe_Fabeae_with_special_focus_on_the_middle-Atlantic_island_lineages
PISUM_LATHYRUS = Clade(children=[PISUM, LATHYRUS])
VICIA_LENS = Clade(children=[VICIA, LENS])

FABEAE = Tribe(name="Fabeae", children=[PISUM_LATHYRUS, VICIA_LENS])
ROBINIEAE = Tribe(name="Robinieae", children=[ROBINIA])
CROTALARIEAE = Tribe(name="Crotalarieae", children=[ASPALATHUS])
GENISTEAE = Tribe(name="Genisteae", children=[LUPINUS])
CICEREAE = Tribe(name="Cicereae", children=[CICER])
PHASEOLEAE = Tribe(name="Phaseoleae", children=[GLYCINE, PHASEOLUS])
TRIFOLIEAE = Tribe(name="Trifolieae", children=[TRIFOLIUM, TRIGONELLA])
GLYCYRRHIZEAE = Tribe(name="Glycyrrhizeae", children=[GLYCYRRHIZA])

GENISTOIDS = Clade(name="Genistoids", children=[CROTALARIEAE, GENISTEAE])

# http://tolweb.org/IRLC_(Inverted_Repeat-lacking_clade)/60358
FABEAE_TRIFOLIAE = Clade(children=[FABEAE, TRIFOLIEAE])
VICIOIDS = Clade(name="vicioids", children=[FABEAE_TRIFOLIAE, CICEREAE])
IRLC = Clade(name="inverted repeat-lacking clade", children=[VICIOIDS, GLYCYRRHIZEAE])

HOLOGALEGINA = Clade(name="Hologalegina", children=[IRLC, ROBINIEAE])

NPAAA_CLADE = Clade(
    name="non-protein amino acid-accumulating clade",
    children=[HOLOGALEGINA, PHASEOLEAE],
)

FABOIDEAE = Subfamily(name="Faboideae", children=[NPAAA_CLADE, GENISTOIDS, ARACHIS])
