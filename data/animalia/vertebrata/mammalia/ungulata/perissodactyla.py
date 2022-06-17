from clade import Clade, Family, Genus, Order, Species, Suborder, Superfamily
from constants import EN, IMAGE, LA, PL
from image import Image, License

E_FERUS = Species(
    name="Equus ferus",
    local_names={EN: "wild horse", PL: "tarpan dziki"},
    known_for=[{EN: "horses and ponies", PL: "konie i kuce"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Przewalski-Pferd_Equus_ferus_przewalskii_Tiergarten-Nuernberg-7.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Przewalski-Pferd_Equus_ferus_przewalskii_Tiergarten-Nuernberg-7.jpg",
        author="Rufus46",
        license=License.CC_BY_SA_3_0,
    ),
)
E_AFRICANUS = Species(
    name="Equus africanus",
    local_names={
        EN: "African wild ass",
        PL: "osioł afrykański, osioł dziki, osioł nubijski",
    },
    known_for=[
        {
            LA: "Equus africanus asinus",
            EN: "domestic donkey",
            PL: "osioł domowy",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Equus_africanus_asinus.004_-_Arteixo.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Equus_africanus_asinus.004_-_Arteixo.jpg",
                author="Fernando Losada Rodríguez",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Equus_africanus_somaliensis_2_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Equus_africanus_somaliensis_2_%28cropped%29.jpg",
        author="Ericj",
        license=License.CC_BY_SA_3_0,
    ),
)
E_QUAGGA = Species(
    name="Equus quagga",
    local_names={EN: "plains zebra, common zebra", PL: "zebra stepowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Equus_quagga_burchellii_-_Etosha,_2014.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/45/Equus_quagga_burchellii_-_Etosha%2C_2014.jpg",
        author="Yathin S Krishnappa",
        license=License.CC_BY_SA_3_0,
    ),
)
T_INDICUS = Species(
    name="Tapirus indicus",
    local_names={
        EN: "Malayan tapir, Asian tapir, Indian tapir",
        PL: "tapir malajski, tapir czaprakowy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schabrackentapir_Tapirus_indicus_Tiergarten-Nuernberg-3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2e/Schabrackentapir_Tapirus_indicus_Tiergarten-Nuernberg-3.jpg",
        author="Rufus46",
        license=License.CC_BY_SA_3_0,
    ),
)
T_TERRESTRIS = Species(
    name="Tapirus terrestris",
    local_names={EN: "South American tapir", PL: "tapir anta, tapir amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tapirus_terrestris_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Tapirus_terrestris_%28cropped%29.jpg",
        author="Jean-Marc Rosier (http://www.cjrosier.com + http://www.gordes-immobilier.com)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_SIMUM = Species(
    name="Ceratotherium simum",
    local_names={EN: "white rhinoceros", PL: "nosorożec biały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Adult_White_Rhinoceros_(Ceratotherium_simum_simum)_(CWPG).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bf/Adult_White_Rhinoceros_%28Ceratotherium_simum_simum%29_%28CWPG%29.jpg",
        author="Vauxford",
        license=License.CC_BY_SA_4_0,
    ),
)
C_ANTIQUITATIS = Species(
    name="Coelodonta antiquitatis",
    local_names={EN: "woolly rhinoceros", PL: "nosorożec włochaty"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Woolly_rhinoceros_(Coelodonta_antiquitatis)_-_Mauricio_Ant%C3%B3n.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/Woolly_rhinoceros_%28Coelodonta_antiquitatis%29_-_Mauricio_Ant%C3%B3n.jpg",
        author="Mauricio Antón",
        license=License.CC_BY_2_5,
    ),
)
P_TRANSOURALICUM = Species(
    name="Paraceratherium transouralicum",
    known_for=[{EN: "one of the largest land mammals"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Indricotherium.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Indricotherium.png",
        author="Tim Bertelink",
        license=License.CC_BY_SA_4_0,
    ),
)

EQUUS_A = Clade(children=[E_AFRICANUS, E_QUAGGA])

EQUUS = Genus(name="Equus", children=[E_FERUS, EQUUS_A])
TAPIRUS = Genus(name="Tapirus", children=[T_INDICUS, T_TERRESTRIS])
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
