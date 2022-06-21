from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

C_AURA = Species(
    name="Cathartes aura",
    local_names={EN: "turkey vulture", PL: "sęp-indyk, sępnik różowogłowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Turkey_vultures_(01731).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1a/Turkey_vultures_%2801731%29.jpg",
        author="Rhododendrites",
        license=License.CC_BY_SA_4_0,
    ),
)
V_GRYPHUS = Species(
    name="Vultur gryphus",
    local_names={EN: "Andean condor", PL: "kondor wielki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Andean_Condor_Vultur_Gryphus_(42232966).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/Andean_Condor_Vultur_Gryphus_%2842232966%29.jpeg",
        author="Scott Nelson",
        license=License.CC_BY_3_0,
    ),
)
G_CALIFORNIANUS = Species(
    name="Gymnogyps californianus",
    local_names={EN: "California condor", PL: "kondor kalifornijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gymnogyps_californianus_-San_Diego_Zoo-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Gymnogyps_californianus_-San_Diego_Zoo-8a.jpg",
        author="Stacy from San Diego",
        license=License.CC_BY_2_0,
    ),
)
S_SERPENTARIUS = Species(
    name="Sagittarius serpentarius",
    local_names={EN: "secretarybird", PL: "sekretarz"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sagittarius_serpentarius_-captivity-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Sagittarius_serpentarius_-captivity-8a.jpg",
        author="Mark Kent",
        license=License.CC_BY_SA_2_0,
    ),
)
G_FULVUS = Species(
    name="Gyps fulvus",
    local_names={EN: "griffon vulture", PL: "sęp płowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gyps_fulvus_01_by_Line1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/Gyps_fulvus_01_by_Line1.jpg",
        author="Liné1",
        license=License.CC_BY_SA_3_0,
    ),
)
H_LEUCOCEPHALUS = Species(
    name="Haliaeetus leucocephalus",
    local_names={EN: "bald eagle", PL: "bielik amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bald_Eagle_(Haliaeetus_leucocephalus)_in_Kachemak_Bay,_Alaska.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Bald_Eagle_%28Haliaeetus_leucocephalus%29_in_Kachemak_Bay%2C_Alaska.jpg",
        author="Andy Morffew from Itchen Abbas, Hampshire, UK",
        license=License.CC_BY_2_0,
    ),
)
H_ALBICILLA = Species(
    name="Haliaeetus albicilla",
    local_names={EN: "white-tailed eagle", PL: "bielik zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Haliaeetus_albicilla_-Wroc%C5%82aw_Zoo_-Poland-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Haliaeetus_albicilla_-Wroc%C5%82aw_Zoo_-Poland-8a.jpg",
        author="Maciej Kasprzyk",
        license=License.CC_BY_SA_2_0,
    ),
)
A_CHRYSAETOS = Species(
    name="Aquila chrysaetos",
    local_names={EN: "golden eagle", PL: "orzeł przedni"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%D0%91%D0%B5%D1%80%D0%BA%D1%83%D1%82_(Aquila_chrysaetos).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/%D0%91%D0%B5%D1%80%D0%BA%D1%83%D1%82_%28Aquila_chrysaetos%29.jpg",
        author="Jarkko Järvinen",
        license=License.CC_BY_SA_2_0,
    ),
)
A_GENTILIS = Species(
    name="Accipiter gentilis",
    local_names={EN: "northern goshawk", PL: "jastrząb zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Northern_Goshawk_ad_M2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Northern_Goshawk_ad_M2.jpg",
        author="Norbert Kenntner, Berlin",
        license=License.CC_BY_SA_3_0,
    ),
)
A_NISUS = Species(
    name="Accipiter nisus",
    local_names={EN: "Eurasian sparrowhawk", PL: "krogulec zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sparrowhawk_Accipiter_nisus_(38008003851).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Sparrowhawk_Accipiter_nisus_%2838008003851%29.jpg",
        author="gailhampshire from Cradley, Malvern, U.K",
        license=License.CC_BY_2_0,
    ),
)
M_MILVUS = Species(
    name="Milvus milvus",
    local_names={EN: "red kite", PL: "kania ruda"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Milvus_milvus_(portrait).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Milvus_milvus_%28portrait%29.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_3_0,
    ),
)
B_JAMAICENSIS = Species(
    name="Buteo jamaicensis",
    local_names={EN: "red-tailed hawk", PL: "myszołów rdzawosterny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Red-tailed_Hawk_(Buteo_jamaicensis)_(12059507526).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Red-tailed_Hawk_%28Buteo_jamaicensis%29_%2812059507526%29.jpg",
        author="Andrew C",
        license=License.CC_BY_2_0,
    ),
)
B_BUTEO = Species(
    name="Buteo buteo",
    local_names={EN: "common buzzard", PL: "myszołów zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Buteo_buteo_-_Common_Buzzard,_Adana_2021-03-27_04.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/Buteo_buteo_-_Common_Buzzard%2C_Adana_2021-03-27_04.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
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

CATHARTIFORMES = Order(name="Cathartiformes", children=[CATHARTIDAE])
ACCIPITRIFORMES = Order(name="Accipitriformes", children=[SAGITTARIIDAE, ACCIPITRIDAE])

ACCIPITRIMORPHAE = Clade(
    name="Accipitrimorphae", children=[CATHARTIFORMES, ACCIPITRIFORMES]
)
