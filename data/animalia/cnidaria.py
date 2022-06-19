from clade import Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL
from image import Image, License

A_EQUINA = Species(
    name="Actinia equina",
    local_names={EN: "beadlet anemone", PL: "ukwiał koński"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Actinia_equina2.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/da/Actinia_equina2.JPG",
        author="Attrattorestrano at Italian Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
A_CERVICORNIS = Species(
    name="Acropora cervicornis",
    local_names={EN: "staghorn coral"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hertshoon.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Hertshoon.jpg",
        author="Albert Kok at Dutch Wikipedia",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
H_VULGARIS = Species(
    name="Hydra vulgaris",
    local_names={EN: "fresh-water polyp", PL: "stułbia pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hydravulgaris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Hydravulgaris.jpg",
        author="Corvana",
        license=License.CC_BY_SA_3_0,
    ),
)
C_FUSCESCENS = Species(
    name="Chrysaora fuscescens",
    local_names={EN: "Pacific sea nettle"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sea_nettle_(Chrysaora_fuscescens)_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Sea_nettle_%28Chrysaora_fuscescens%29_2.jpg",
        author="Ed Bierman from Redwood City, USA",
        license=License.CC_BY_2_0,
    ),
)
A_AURITA = Species(
    name="Aurelia aurita",
    local_names={EN: "common jellyfish", PL: "chełbia modra"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aurelia-aurita2_hg.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Aurelia-aurita2_hg.jpg",
        author="Hannes Grobe",
        license=License.CC_BY_3_0,
    ),
)

ACTINIA = Genus(name="Actinia", children=[A_EQUINA])
ACROPORA = Genus(name="Acropora", children=[A_CERVICORNIS])
HYDRA = Genus(name="Hydra", children=[H_VULGARIS])
CHRYSAORA = Genus(
    name="Chrysaora",
    children=[C_FUSCESCENS],
    local_names={EN: "sea nettle", PL: "meduza kompasowa"},
)
AURELIA = Genus(name="Aurelia", children=[A_AURITA])

ACTINIIDAE = Family(name="Actiniidae", children=[ACTINIA])
ACROPORIDAE = Family(name="Acroporidae", children=[ACROPORA])
HYDRIDAE = Family(name="Hydridae", children=[HYDRA])
PELAGIIDAE = Family(name="Pelagiidae", children=[CHRYSAORA])
ULMARIDAE = Family(name="Ulmaridae", children=[AURELIA])

ACTINIARIA = Order(name="Actiniaria", children=[ACTINIIDAE])
SCLERACTINIA = Order(name="Scleractinia", children=[ACROPORIDAE])
ANTHOATHECATA = Order(name="Anthoathecata", children=[HYDRIDAE])
SEMAEOSTOMEAE = Order(name="Semaeostomeae", children=[PELAGIIDAE, ULMARIDAE])

ANTHOZOA = Class(name="Anthozoa", children=[ACTINIARIA, SCLERACTINIA])
HYDROZOA = Class(name="Hydrozoa", children=[ANTHOATHECATA])
SCYPHOZOA = Class(name="Scyphozoa", children=[SEMAEOSTOMEAE])

MEDUSOZOA = Subphylum(name="Medusozoa", children=[HYDROZOA, SCYPHOZOA])

CNIDARIA = Phylum(name="Cnidaria", children=[ANTHOZOA, MEDUSOZOA])
