from clade import Clade, Family, Genus, Order, Species, Subfamily, Suborder, Superfamily
from constants import EN, LA, PL

T_SCRIPTA = Species(
    name="Trachemys scripta",
    local_names={EN: "pond turtle", PL: "żółw ozdobny"},
    known_for=[
        {
            LA: "Trachemys scripta elegans",
            EN: "red-eared slider",
            PL: "żółw czerwonolicy",
        }
    ],
)
C_PICTA = Species(
    name="Chrysemys picta",
    local_names={EN: "painted turtle", PL: "żółw malowany, żółwik malowany"},
)
T_CAROLINA = Species(
    name="Terrapene carolina",
    local_names={EN: "common box turtle", PL: "terapena karolińska"},
)
C_VANDENBURGHI = Species(
    name="Chelonoidis vandenburghi",
    local_names={EN: "Alcedo giant tortoise"},
    known_for=[
        {
            EN: "one of the most numerous species of Galápagos tortoise",
            PL: "jeden z najliczniejszych gatunków żółwi słoniowych",
        }
    ],
)
L_OLIVACEA = Species(
    name="Lepidochelys olivacea",
    local_names={EN: "olive ridley sea turtle", PL: "żółw oliwkowy"},
    known_for=[{EN: "the most common sea turtle"}],
)
C_SERPENTINA = Species(
    name="Chelydra serpentina",
    local_names={
        EN: "common snapping turtle",
        PL: "żółw jaszczurowaty, żółw kajmanowy, skorpucha jaszczurowata",
    },
)
M_TEMMINCKII = Species(
    name="Macrochelys temminckii",
    local_names={EN: "alligator snapping turtle", PL: "żółw sępi, skorpucha sępia"},
)
D_CORIACEA = Species(
    name="Dermochelys coriacea",
    local_names={
        EN: "leatherback sea turtle, luth, lute turtle. leathery turtle",
        PL: "żółw skórzasty",
    },
    known_for=[{EN: "the largest living turtle"}],
)

C_NIGER = Clade(
    name="Chelonoidis niger complex",
    local_names={EN: "Galápagos tortoise", PL: "żółw z Galapagos, żółw słoniowy"},
    children=[C_VANDENBURGHI],
)  # Species complex

TRACHEMYS = Genus(name="Trachemys", children=[T_SCRIPTA])
CHRYSEMYS = Genus(name="Chrysemys", children=[C_PICTA])
TERRAPENE = Genus(name="Terrapene", children=[T_CAROLINA])
CHELONOIDIS = Genus(name="Chelonoidis", children=[C_NIGER])
LEPIDOCHELYS = Genus(name="Lepidochelys", children=[L_OLIVACEA])
CHELYDRA = Genus(name="Chelydra", children=[C_SERPENTINA])
MACROCHELYS = Genus(name="Macrochelys", children=[M_TEMMINCKII])
DERMOCHELYS = Genus(name="Dermochelys", children=[D_CORIACEA])

DEIROCHELYINAE = Subfamily(name="Deirochelyinae", children=[TRACHEMYS, CHRYSEMYS])
EMYDINAE = Subfamily(name="Emydinae", children=[TERRAPENE])

EMYDIDAE = Family(name="Emydidae", children=[DEIROCHELYINAE, EMYDINAE])
TESTUDINIDAE = Family(name="Testudinidae", children=[CHELONOIDIS])
CHELONIIDAE = Family(name="Cheloniidae", children=[LEPIDOCHELYS])
CHELYDRIDAE = Family(name="Chelydridae", children=[CHELYDRA, MACROCHELYS])
DERMOCHELYIDAE = Family(name="Dermochelyidae", children=[DERMOCHELYS])

TESTUDINOIDEA = Superfamily(name="Testudinoidea", children=[EMYDIDAE, TESTUDINIDAE])
CHELONIOIDEA = Superfamily(name="Chelonioidea", children=[CHELONIIDAE, DERMOCHELYIDAE])

AMERICHELYDIA = Clade(name="Americhelydia", children=[CHELONIOIDEA, CHELYDRIDAE])

CRYPTODIRA = Suborder(name="Cryptodira", children=[TESTUDINOIDEA, AMERICHELYDIA])

TESTUDINES = Order(name="Testudines", children=[CRYPTODIRA])
