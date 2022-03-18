from clade import Clade, Family, Genus, Order, Species, Suborder, Superfamily
from constants import EN, LA, PL

E_FERUS = Species(
    name="Equus ferus",
    local_names={EN: "wild horse", PL: "tarpan dziki"},
    known_for=[{EN: "horses and ponies", PL: "konie i kuce"}],
)
E_AFRICANUS = Species(
    name="Equus africanus",
    local_names={
        EN: "African wild ass",
        PL: "osioł afrykański, osioł dziki, osioł nubijski",
    },
    known_for=[
        {LA: "Equus africanus asinus", EN: "domestic donkey", PL: "osioł domowy"}
    ],
)
E_QUAGGA = Species(
    name="Equus quagga",
    local_names={EN: "plains zebra, common zebra", PL: "zebra stepowa"},
)
T_INDICUS = Species(
    name="Tapirus indicus",
    local_names={
        EN: "Malayan tapir, Asian tapir, Indian tapir",
        PL: "tapir malajski, tapir czaprakowy",
    },
)
C_SIMUM = Species(
    name="Ceratotherium simum",
    local_names={EN: "white rhinoceros", PL: "nosorożec biały"},
)
C_ANTIQUITATIS = Species(
    name="Coelodonta antiquitatis",
    local_names={EN: "woolly rhinoceros", PL: "nosorożec włochaty"},
    extinct=True,
)
P_TRANSOURALICUM = Species(
    name="Paraceratherium transouralicum",
    known_for=[{EN: "one of the largest land mammals"}],
    extinct=True,
)

EQUUS_A = Clade(children=[E_AFRICANUS, E_QUAGGA])

EQUUS = Genus(name="Equus", children=[E_FERUS, EQUUS_A])
TAPIRUS = Genus(name="Tapirus", children=[T_INDICUS])
CERATOTHERIUM = Genus(name="Ceratotherium", children=[C_SIMUM])
COELODONTA = Genus(name="Coelodonta", children=[C_ANTIQUITATIS])
PARACERATHERIUM = Genus(name="Paraceratherium", children=[P_TRANSOURALICUM])

EQUIDAE = Family(name="Equidae", children=[EQUUS])
TAPIRIDAE = Family(name="Tapiridae", children=[TAPIRUS])
RHINOCEROTIDAE = Family(name="Rhinocerotidae", children=[CERATOTHERIUM, COELODONTA])
PARACERATHERIIDAE = Family(name="Paraceratheriidae", children=[PARACERATHERIUM])

TAPIROIDEA = Superfamily(name="Tapiroidea", children=[TAPIRIDAE])
RHINOCEROTOIDEA = Superfamily(
    name="Rhinocerotoidea", children=[RHINOCEROTIDAE, PARACERATHERIIDAE]
)

HIPPOMORPHA = Suborder(name="Hippomorpha", children=[EQUIDAE])
CERATOMORPHA = Suborder(name="Ceratomorpha", children=[TAPIROIDEA, RHINOCEROTOIDEA])

PERISSODACTYLA = Order(name="Perissodactyla", children=[HIPPOMORPHA, CERATOMORPHA])
