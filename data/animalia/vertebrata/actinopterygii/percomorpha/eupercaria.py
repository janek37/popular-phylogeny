from clade import Clade, Family, Genus, Order, Species, Superfamily
from constants import EN, PL
from image import Image, License

L_DIMIDIATUS = Species(
    name="Labroides dimidiatus",
    local_names={
        EN: "bluestreak cleaner wrasse",
        PL: "wargatek czyściciel, wargatek sanitarnik",
    },
    known_for=[{EN: "Oscar from Shark Tale"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bluestreak_cleaner_wrasse_(Labroides_dimidiatus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/36/Bluestreak_cleaner_wrasse_%28Labroides_dimidiatus%29.jpg",
        author="Rickard Zerpe",
        license=License.CC_BY_2_0,
    ),
)
S_VITREUS = Species(
    name="Sander vitreus",
    local_names={EN: "walleye", PL: "sandacz amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Denton_Walleye_1896.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Denton_Walleye_1896.png",
        author="Sherman Foote Denton",
        license=License.PUBLIC_DOMAIN,
    ),
)
S_LUCIOPERCA = Species(
    name="Sander lucioperca",
    local_names={EN: "zander, sander, pikeperch", PL: "sandacz pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sander_lucioperca_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Sander_lucioperca_2.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_FLUVIATILIS = Species(
    name="Perca fluviatilis",
    local_names={EN: "common perch, European perch", PL: "okoń pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aborre_(Perca_fluviatilis).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Aborre_%28Perca_fluviatilis%29.jpg",
        author="Munsterhjelm Art Center",
        license=License.CC_BY_SA_4_0,
    ),
)
P_VOLITANS = Species(
    name="Pterois volitans",
    local_names={EN: "red lionfish", PL: "skrzydlica pstra, ognica pstra"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_lion_fish_Pterois_volitans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Common_lion_fish_Pterois_volitans.jpg",
        author="Michael Gäbler",
        license=License.CC_BY_3_0,
    ),
)
P_MARCIDUS = Species(
    name="Psychrolutes marcidus",
    local_names={EN: "smooth-head blobfish"},
    known_for=[{EN: "internet meme"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Psychrolutes_marcidus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Psychrolutes_marcidus.jpg",
        author="Alan Riverstone McCulloch (1885-1925)",
        license=License.PUBLIC_DOMAIN,
    ),
)
S_AURATA = Species(
    name="Sparus aurata",
    local_names={EN: "gilt-head bream", PL: "dorada"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sparus_aurata.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Sparus_aurata.jpg",
        author="Werner",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_HEPATUS = Species(
    name="Paracanthurus hepatus",
    local_names={
        EN: "regal tang, palette surgeonfish, royal blue tang",
        PL: "chirurg, cyrulik, pokolec królewski",
    },
    known_for=[{EN: "Dory from Finding Nemo"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paletten-Doktorfisch_(Paracanthurus_hepatus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d6/Paletten-Doktorfisch_%28Paracanthurus_hepatus%29.jpg",
        author="Olbertz",
        license=License.CC_BY_SA_3_0,
    ),
)
S_OCELLATUS = Species(
    name="Sciaenops ocellatus",
    local_names={
        EN: "red drum, redfish, channel/spottail bass, puppy drum",
        PL: "korwin czerwony, kulbak czerwony",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_41953_Channel_Bass_(Sciaenops_ocellatus_(Linnaeus)).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/FMIB_41953_Channel_Bass_%28Sciaenops_ocellatus_%28Linnaeus%29%29.jpeg",
        author="Unknown author",
        license=License.FMIB,
    ),
)
P_DIACANTHUS = Species(
    name="Pygoplites diacanthus",
    local_names={EN: "royal angelfish", PL: "ustnik słoneczny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:XRF-Pygoplites_diacanthus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/XRF-Pygoplites_diacanthus.png",
        author="Xavier Romero-Frias",
        license=License.CC_BY_SA_3_0,
    ),
)
L_PISCATORIUS = Species(
    name="Lophius piscatorius",
    local_names={
        EN: "European angler or common monkfish",
        PL: "diabeł morski, żabnica nawęd",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lophius_piscatorius_Fr.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Lophius_piscatorius_Fr.png",
        author="H. Gervais et R. Boulart",
        license=License.CC_BY_SA_4_0,  # should be PUBLIC_DOMAIN
    ),
)
C_HOLBOELLI = Species(
    name="Ceratias holboelli",
    local_names={EN: "Krøyer's deep sea angler fish", PL: "matronica Holboella"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ceratias_holboelli.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Ceratias_holboelli.jpg",
        author="G. Brown Goode and Tarleton H. Bean",
        license=License.PUBLIC_DOMAIN,
    ),
)
M_MOLA = Species(
    name="Mola mola",
    local_names={EN: "ocean sunfish, common mola", PL: "mola, samogłów"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mola_mola_1898.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Mola_mola_1898.jpg",
        author="Unknown author",
        license=License.PUBLIC_DOMAIN,
    ),
)
T_RUBRIPES = Species(
    name="Takifugu rubripes",
    local_names={EN: "Japanese puffer, tiger puffer, torafugu"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Japanese_pufferfish_(Takifugu_rubripes).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Japanese_pufferfish_%28Takifugu_rubripes%29.png",
        author="Database Center for Life Science (DBCLS)",
        license=License.CC_BY_3_0,
    ),
)
D_HYSTRIX = Species(
    name="Diodon hystrix",
    local_names={
        EN: "spotted porcupinefish, black-spotted porcupinefish",
        PL: "rybojeż, jeżoryb, najeżka, jeżówka, diodon jeżyk",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_52102_Porcupine-fish,_Diodon_hystrix_(Linnaeus)_Tortugas_Islands.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/FMIB_52102_Porcupine-fish%2C_Diodon_hystrix_%28Linnaeus%29_Tortugas_Islands.jpeg",
        author="David Starr Jordan",
        license=License.FMIB,
    ),
)
M_SALMOIDES = Species(
    name="Micropterus salmoides",
    local_names={EN: "largemouth bass", PL: "bass wielkogębowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Micropterus_salmoides_with_white_background.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Micropterus_salmoides_with_white_background.jpg",
        author="Duane Raver",
        license=License.CC0,
    ),
)

LABROIDES = Genus(name="Labroides", children=[L_DIMIDIATUS])
SANDER = Genus(name="Sander", children=[S_VITREUS, S_LUCIOPERCA])
PERCA = Genus(name="Perca", children=[P_FLUVIATILIS])
PTEROIS = Genus(name="Pterois", children=[P_VOLITANS])
PSYCHROLUTES = Genus(name="Psychrolutes", children=[P_MARCIDUS])
SPARUS = Genus(name="Sparus", children=[S_AURATA])
PARACANTHURUS = Genus(name="Paracanthurus", children=[P_HEPATUS])
SCIAENOPS = Genus(name="Sciaenops", children=[S_OCELLATUS])
PYGOPLITES = Genus(name="Pygoplites", children=[P_DIACANTHUS])
LOPHIUS = Genus(name="Lophius", children=[L_PISCATORIUS])
CERATIAS = Genus(name="Ceratias", children=[C_HOLBOELLI])
MOLA = Genus(name="Mola", children=[M_MOLA])
TAKIFUGU = Genus(name="Takifugu", children=[T_RUBRIPES])
DIODON = Genus(name="Diodon", children=[D_HYSTRIX])
MICROPTERUS = Genus(name="Micropterus", children=[M_SALMOIDES])

LABRIDAE = Family(name="Labridae", children=[LABROIDES])
PERCIDAE = Family(name="Percidae", children=[SANDER, PERCA])
SCORPAENIDAE = Family(name="Scorpaenidae", children=[PTEROIS])
PSYCHROLUTIDAE = Family(name="Psychrolutidae", children=[PSYCHROLUTES])
SPARIDAE = Family(name="Sparidae", children=[SPARUS])
ACANTHURIDAE = Family(name="Acanthuridae", children=[PARACANTHURUS])
SCIAENIDAE = Family(name="Sciaenidae", children=[SCIAENOPS])
POMACANTHIDAE = Family(name="Pomacanthidae", children=[PYGOPLITES])
LOPHIIDAE = Family(name="Lophiidae", children=[LOPHIUS])
CERATIIDAE = Family(name="Ceratiidae", children=[CERATIAS])
MOLIDAE = Family(name="Molidae", children=[MOLA])
TETRAODONTIDAE = Family(name="Tetraodontidae", children=[TAKIFUGU])
DIODONTIDAE = Family(name="Diodontidae", children=[DIODON])
CENTRARCHIDAE = Family(name="Centrarchidae", children=[MICROPTERUS])

PERCOIDEA = Superfamily(name="Percoidea", children=[PERCIDAE, CENTRARCHIDAE])

# https://bmcecolevol.biomedcentral.com/articles/10.1186/s12862-017-0958-3
PERCIFORMES_A = Clade(children=[SCORPAENIDAE, PSYCHROLUTIDAE])

TETRAODONTIFORMES_A = Clade(children=[TETRAODONTIDAE, DIODONTIDAE])

LABRIFORMES = Order(name="Labriformes", children=[LABRIDAE])
PERCIFORMES = Order(name="Perciformes", children=[PERCOIDEA, PERCIFORMES_A])
SPARIFORMES = Order(name="Spariformes", children=[SPARIDAE])
ACANTHURIFORMES = Order(name="Acanthuriformes", children=[ACANTHURIDAE, SCIAENIDAE])
LOPHIIFORMES = Order(name="Lophiiformes", children=[LOPHIIDAE, CERATIIDAE])
TETRAODONTIFORMES = Order(
    name="Tetraodontiformes", children=[MOLIDAE, TETRAODONTIFORMES_A]
)

EUPERCARIA_A = Clade(children=[ACANTHURIFORMES, POMACANTHIDAE])
EUPERCARIA_B = Clade(children=[LOPHIIFORMES, TETRAODONTIFORMES])
EUPERCARIA_C = Clade(children=[SPARIFORMES, EUPERCARIA_B])
EUPERCARIA_D = Clade(children=[EUPERCARIA_C, EUPERCARIA_A])
EUPERCARIA_E = Clade(children=[PERCIFORMES, EUPERCARIA_D])
EUPERCARIA = Clade(name="Eupercaria", children=[LABRIFORMES, EUPERCARIA_E])
