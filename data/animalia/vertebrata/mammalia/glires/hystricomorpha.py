from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Parvorder,
    Species,
    Suborder,
    Superfamily,
)
from constants import EN, PL
from image import Image, License

H_CRISTATA = Species(
    name="Hystrix cristata",
    local_names={EN: "crested porcupine", PL: "jeżozwierz afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hystrix_cristata_qtl1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Hystrix_cristata_qtl1.jpg",
        author="Quartl",
        license=License.CC_BY_SA_3_0,
    ),
)
H_GLABER = Species(
    name="Heterocephalus glaber",
    local_names={EN: "naked mole-rat", PL: "golec piaskowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Farumfer.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/Farumfer.jpg",
        author="Josemarjauregui",
        license=License.CC_BY_SA_3_0,
    ),
)
E_DORSATUM = Species(
    name="Erethizon dorsatum",
    local_names={EN: "North American porcupine", PL: "urson amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Young_North_American_Porcupine.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Young_North_American_Porcupine.jpg",
        author="L.G.Cullens",
        license=License.CC_BY_SA_4_0,
    ),
)
C_PORCELLUS = Species(
    name="Cavia porcellus",
    local_names={
        EN: "domestic guinea pig, domestic cavy",
        PL: "świnka morska, kawia domowa",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cobaya_(Cavia_porcellus),_Tierpark_Hellabrunn,_M%C3%BAnich,_Alemania,_2012-06-17,_DD_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/Cobaya_%28Cavia_porcellus%29%2C_Tierpark_Hellabrunn%2C_M%C3%BAnich%2C_Alemania%2C_2012-06-17%2C_DD_01.JPG",
        author="Diego Delso",
        license=License.CC_BY_SA_3_0,
    ),
)
H_HYDROCHAERIS = Species(
    name="Hydrochoerus hydrochaeris",
    local_names={EN: "greater capybara", PL: "kapibara wielka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Capybara_(Hydrochoerus_hydrochaeris).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Capybara_%28Hydrochoerus_hydrochaeris%29.JPG",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
C_LANIGERA = Species(
    name="Chinchilla lanigera",
    local_names={
        EN: "long-tailed chinchilla, coastal/common/lesser chinchilla",
        PL: "szynszyla mała",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chinchilla_lanigera_(Wroclaw_zoo)-2.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Chinchilla_lanigera_%28Wroclaw_zoo%29-2.JPG",
        author="Guérin Nicolas (messages)",
        license=License.CC_BY_SA_3_0,
    ),
)
M_COYPUS = Species(
    name="Myocastor coypus",
    local_names={EN: "nutria, coypu", PL: "nutria amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ragondin_(Myocastor_coypus)_(09).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Ragondin_%28Myocastor_coypus%29_%2809%29.jpg",
        author="Gzen92",
        license=License.CC_BY_SA_4_0,
    ),
)
O_DEGUS = Species(
    name="Octodon degus",
    local_names={EN: "common degu", PL: "koszatniczka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Octodon_degus_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Octodon_degus_2.jpg",
        author="Algirdas",
        license=License.PUBLIC_DOMAIN,
    ),
)

HYSTRIX = Genus(name="Hystrix", children=[H_CRISTATA])
HETEROCEPHALUS = Genus(name="Heterocephalus", children=[H_GLABER])
ERETHIZON = Genus(name="Erethizon", children=[E_DORSATUM])
CAVIA = Genus(name="Cavia", children=[C_PORCELLUS])
HYDROCHOERUS = Genus(name="Hydrochoerus", children=[H_HYDROCHAERIS])
CHINCHILLA = Genus(name="Chinchilla", children=[C_LANIGERA])
MYOCASTOR = Genus(name="Myocastor", children=[M_COYPUS])
OCTODON = Genus(name="Octodon", children=[O_DEGUS])

HYSTRICIDAE = Family(name="Hystricidae", children=[HYSTRIX])
HETEROCEPHALIDAE = Family(name="Heterocephalidae", children=[HETEROCEPHALUS])
ERETHIZONTIDAE = Family(name="Erethizontidae", children=[ERETHIZON])
CAVIIDAE = Family(name="Caviidae", children=[CAVIA, HYDROCHOERUS])
CHINCHILLIDAE = Family(name="Chinchillidae", children=[CHINCHILLA])
ECHIMYIDAE = Family(name="Echimyidae", children=[MYOCASTOR])
OCTODONTIDAE = Family(name="Octodontidae", children=[OCTODON])

CAVIOIDEA = Superfamily(name="Cavioidea", children=[ERETHIZONTIDAE, CAVIIDAE])
OCTODONTOIDEA = Superfamily(name="Octodontoidea", children=[ECHIMYIDAE, OCTODONTIDAE])

CAVIOMORPHA_A = Clade(children=[CHINCHILLIDAE, OCTODONTOIDEA])

PHIOMORPHA = Parvorder(name="Phiomorpha", children=[HYSTRICIDAE, HETEROCEPHALIDAE])
CAVIOMORPHA = Parvorder(name="Caviomorpha", children=[CAVIOIDEA, CAVIOMORPHA_A])

HYSTRICOGNATHI = Infraorder(name="Hystricognathi", children=[PHIOMORPHA, CAVIOMORPHA])

HYSTRICOMORPHA = Suborder(name="Hystricomorpha", children=[HYSTRICOGNATHI])
