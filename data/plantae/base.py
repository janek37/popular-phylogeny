from clade import Clade, Class, Family, Genus, Kingdom, Order, Phylum, Species
from constants import EN, PL
from image import Image, License

from .land_plants import EMBRYOPHYTA

P_PALMATA = Species(
    name="Palmaria palmata",
    local_names={EN: "dulse"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Palmaria_palmata_1_Crouan.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Palmaria_palmata_1_Crouan.jpg",
        author="Pierre-Louis Crouan (1798-1871) & Hippolyte-Marie Crouan (1802-1871)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_CRISPUS = Species(
    name="Chondrus crispus",
    local_names={EN: "carrageen moss"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chondrus_crispus_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-034_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/Chondrus_crispus_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-034_cropped.jpg",
        author="Koeh-034.jpg: Franz Eugen Köhler, Köhler's Medizinal-Pflanzen; derivative work: Totodu74 (talk)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_TENERA = Species(
    name="Pyropia tenera",
    local_names={EN: "nori", PL: "nori, szkarłatnica delikatna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nori.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/be/Nori.jpg",
        author="Alice Wiegand, (Lyzzy)",
        license=License.CC_BY_SA_3_0,
    ),
)
U_LACTUCA = Species(
    name="Ulva lactuca",
    local_names={EN: "sea lettuce", PL: "sałata morska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ulva_lactuca_Ibiza.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Ulva_lactuca_Ibiza.jpg",
        author="Tigerente",
        license=License.CC_BY_SA_3_0,
    ),
)
T_ARBORICOLA = Species(
    name="Trebouxia arboricola",
    known_for=[{EN: "very common lichen photobiont"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lichen_cross_section_%E2%80%93_heteromeric_thallus.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Lichen_cross_section_%E2%80%93_heteromeric_thallus.svg",
        author="Nefronus",
        license=License.CC_BY_SA_4_0,
    ),
)

PALMARIA = Genus(name="Palmaria", children=[P_PALMATA])
CHONDRUS = Genus(name="Chondrus", children=[C_CRISPUS])
PYROPIA = Genus(name="Pyropia", children=[P_TENERA])
ULVA = Genus(name="Ulva", children=[U_LACTUCA])
TREBOUXIA = Genus(name="Trebouxia", children=[T_ARBORICOLA])

PALMARIACEAE = Family(name="Palmariaceae", children=[PALMARIA])
GIGARTINACEAE = Family(name="Gigartinaceae", children=[CHONDRUS])
BANGIACEAE = Family(name="Bangiaceae", children=[PYROPIA])
ULVACEAE = Family(name="Ulvaceae", children=[ULVA])
TREBOUXIACEAE = Family(name="Trebouxiaceae", children=[TREBOUXIA])

PALMARIALES = Order(name="Palmariales", children=[PALMARIACEAE])
GIGARTINALES = Order(name="Gigartinales", children=[GIGARTINACEAE])
BANGIALES = Order(name="Bangiales", children=[BANGIACEAE])
ULVALES = Order(name="Ulvales", children=[ULVACEAE])
TREBOUXIALES = Order(name="Trebouxiales", children=[TREBOUXIACEAE])

FLORIDEOPHYCEAE = Class(name="Florideophyceae", children=[PALMARIALES, GIGARTINALES])
BANGIOPHYCEAE = Class(name="Bangiophyceae", children=[BANGIALES])
ULVOPHYCEAE = Class(name="Ulvophyceae", children=[ULVALES])
TREBOUXIAPHYCEAE = Class(name="Trebouxiaphyceae", children=[TREBOUXIALES])

RODOPHYTA = Phylum(name="Rodophyta", children=[FLORIDEOPHYCEAE, BANGIOPHYCEAE])
CHLOROPHYTA = Phylum(name="Chlorophyta", children=[ULVOPHYCEAE, TREBOUXIAPHYCEAE])

VIRIDIPLANTAE = Clade(name="Viridiplantae", children=[CHLOROPHYTA, EMBRYOPHYTA])

ARCHAEOPLASTIDA = Kingdom(name="Archaeoplastida", children=[RODOPHYTA, VIRIDIPLANTAE])
