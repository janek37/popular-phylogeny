from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

C_AURA = Species(
    name="Cathartes aura",
    local_names={EN: "turkey vulture", PL: "sęp-indyk, sępnik różowogłowy"},
)
V_GRYPHUS = Species(
    name="Vultur gryphus", local_names={EN: "Andean condor", PL: "kondor wielki"}
)
G_CALIFORNIANUS = Species(
    name="Gymnogyps californianus",
    local_names={EN: "California condor", PL: "kondor kalifornijski"},
)
S_SERPENTARIUS = Species(
    name="Sagittarius serpentarius", local_names={EN: "secretarybird", PL: "sekretarz"}
)
G_FULVUS = Species(
    name="Gyps fulvus", local_names={EN: "griffon vulture", PL: "sęp płowy"}
)
H_LEUCOCEPHALUS = Species(
    name="Haliaeetus leucocephalus",
    local_names={EN: "bald eagle", PL: "bielik amerykański"},
)
H_ALBICILLA = Species(
    name="Haliaeetus albicilla",
    local_names={EN: "white-tailed eagle", PL: "bielik zwyczajny"},
)
A_CHRYSAETOS = Species(
    name="Aquila chrysaetos", local_names={EN: "golden eagle", PL: "orzeł przedni"}
)
A_GENTILIS = Species(
    name="Accipiter gentilis",
    local_names={EN: "northern goshawk", PL: "jastrząb zwyczajny"},
)
A_NISUS = Species(
    name="Accipiter nisus",
    local_names={EN: "Eurasian sparrowhawk", PL: "krogulec zwyczajny"},
)
M_MILVUS = Species(name="Milvus milvus", local_names={EN: "red kite", PL: "kania ruda"})
B_JAMAICENSIS = Species(
    name="Buteo jamaicensis",
    local_names={EN: "red-tailed hawk", PL: "myszołów rdzawosterny"},
)
B_BUTEO = Species(
    name="Buteo buteo", local_names={EN: "common buzzard", PL: "myszołów zwyczajny"}
)

CATHARTES = Genus(name="Cathartes", children=[C_AURA])
VULTUR = Genus(name="Vultur", children=[V_GRYPHUS])
GYMNOGYPS = Genus(name="Gymnogyps", children=[G_CALIFORNIANUS])
SAGITTARIUS = Genus(name="Sagittarius", children=[S_SERPENTARIUS])
GYPS = Genus(name="Gyps", children=[G_FULVUS])
HALIAEETUS = Genus(name="Haliaeetus", children=[H_LEUCOCEPHALUS, H_ALBICILLA])
AQUILA = Genus(name="Aquila", children=[A_CHRYSAETOS])
ACCIPITER = Genus(name="Accipiter", children=[A_GENTILIS, A_NISUS])
MILVUS = Genus(name="Milvus", children=[M_MILVUS])
BUTEO = Genus(name="Buteo", children=[B_JAMAICENSIS, B_BUTEO])

# https://www.sciencedirect.com/science/article/abs/pii/S105579031630224X
# https://ars.els-cdn.com/content/image/1-s2.0-S105579031630224X-gr1.jpg
CATHARTIDAE_A = Clade(children=[VULTUR, GYMNOGYPS])

# https://www.researchgate.net/publication/7815523_Phylogeny_of_eagles_Old_World_vultures_and_other_Accipitridae_based_on_nuclear_and_mitochondrial_DNA
ACCIPITRIDAE_A = Clade(children=[HALIAEETUS, BUTEO])
ACCIPITRIDAE_B = Clade(children=[ACCIPITRIDAE_A, MILVUS])
ACCIPITRIDAE_C = Clade(children=[ACCIPITRIDAE_B, ACCIPITER])
ACCIPITRIDAE_D = Clade(children=[ACCIPITRIDAE_C, AQUILA])

CATHARTIDAE = Family(name="Cathartidae", children=[CATHARTES, CATHARTIDAE_A])
SAGITTARIIDAE = Family(name="Sagittariidae", children=[SAGITTARIUS])
ACCIPITRIDAE = Family(name="Accipitridae", children=[GYPS, ACCIPITRIDAE_D])

CATHARTIFORMES = Order(name="Accipitriformes", children=[CATHARTIDAE])
ACCIPITRIFORMES = Order(name="Accipitriformes", children=[SAGITTARIIDAE, ACCIPITRIDAE])

ACCIPITRIMORPHAE = Clade(
    name="Accipitrimorphae", children=[CATHARTIFORMES, ACCIPITRIFORMES]
)
