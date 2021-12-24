from clade import Family, Genus, Infraorder, Order, Species, Subfamily, Suborder
from constants import EN, PL

L_MIGRATORIA = Species(
    name="Locusta migratoria",
    local_names={EN: "migratory locust", PL: "szarańcza wędrowna"},
)
C_BIGUTTULUS = Species(
    name="Chorthippus biguttulus",
    local_names={EN: "bow-winged grasshopper", PL: "konik pospolity"},
)
G_GRYLLOTALPA = Species(
    name="Gryllotalpa gryllotalpa",
    local_names={EN: "European mole cricket", PL: "turkuć podjadek"},
)
G_CAMPESTRIS = Species(
    name="Gryllus campestris",
    local_names={EN: "European field cricket", PL: "świerszcz polny"},
)
A_DOMESTICUS = Species(
    name="Acheta domesticus", local_names={EN: "house cricket", PL: "świerszcz domowy"}
)
T_VIRIDISSIMA = Species(
    name="Tettigonia viridissima",
    local_names={EN: "great green bush-cricket", PL: "pasikonik zielony"},
)
P_GRISEOAPTERA = Species(
    name="Pholidoptera griseoaptera",
    local_names={EN: "dark bush-cricket", PL: "podkrzewin szary"},
)
D_HETERACANTHA = Species(
    name="Deinacrida heteracantha",
    local_names={EN: "Little Barrier giant wētā"},
    known_for=[{EN: "the heaviest known insect"}],
)

LOCUSTA = Genus(name="Locusta", children=[L_MIGRATORIA])
CHORTHIPPUS = Genus(name="Chorthippus", children=[C_BIGUTTULUS])
GRYLLOTALPA = Genus(name="Gryllotalpa", children=[G_GRYLLOTALPA])
GRYLLUS = Genus(name="Gryllus", children=[G_CAMPESTRIS])
ACHETA = Genus(name="Acheta", children=[A_DOMESTICUS])
TETTIGONIA = Genus(name="Tettigonia", children=[T_VIRIDISSIMA])
PHOLIDOPTERA = Genus(name="Pholidoptera", children=[P_GRISEOAPTERA])
DEINACRIDA = Genus(name="Deinacrida", children=[D_HETERACANTHA])

OEDIPODINAE = Subfamily(name="Oedipodinae", children=[LOCUSTA])
GOMPHOCERINAE = Subfamily(name="Gomphocerinae", children=[CHORTHIPPUS])
GRYLLINAE = Subfamily(name="Gryllinae", children=[GRYLLUS, ACHETA])

ACRIDIDAE = Family(name="Acrididae", children=[OEDIPODINAE, GOMPHOCERINAE])
GRYLLOTALPIDAE = Family(name="Gryllotalpidae", children=[GRYLLOTALPA])
GRYLLIDAE = Family(name="Gryllidae", children=[GRYLLINAE])
TETTIGONIIDAE = Family(name="Tettigoniidae", children=[TETTIGONIA, PHOLIDOPTERA])
ANOSTOSTOMATIDAE = Family(name="Anostostomatidae", children=[DEINACRIDA])

GRYLLIDEA = Infraorder(name="Gryllidea", children=[GRYLLOTALPIDAE, GRYLLIDAE])
TETTIGONIIDEA = Infraorder(
    name="Tettigoniidea", children=[TETTIGONIIDAE, ANOSTOSTOMATIDAE]
)

CAELIFERA = Suborder(name="Caelifera", children=[ACRIDIDAE])
ENSIFERA = Suborder(name="Ensifera", children=[GRYLLIDEA, TETTIGONIIDEA])

ORTHOPTERA = Order(name="Orthoptera", children=[CAELIFERA, ENSIFERA])
