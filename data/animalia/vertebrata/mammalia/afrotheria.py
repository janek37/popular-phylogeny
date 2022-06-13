from clade import Clade, Family, Genus, Order, Species, Suborder, Superorder
from constants import EN, PL
from image import Image, License

from .proboscidea import PROBOSCIDEA

O_AFER = Species(
    name="Orycteropus afer",
    local_names={EN: "aardvark", PL: "mrównik afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aardvark_(Orycteropus_afer).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Aardvark_%28Orycteropus_afer%29.jpg",
        author="Theo Kruse Burgers' Zoo",
        license=License.CC_BY_SA_4_0,
    ),
)
R_PETERSI = Species(
    name="Rhynchocyon petersi",
    local_names={
        EN: "black and rufous elephant shrew, black and rufous sengi",
        PL: "sorkonos czarno-rdzawy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhynchocyon_petersi_from_side_cropped_mirror.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Rhynchocyon_petersi_from_side_cropped_mirror.png",
        author="Joey Makalintal from Pennsylvania, USA",
        license=License.CC_BY_SA_4_0,
    ),
)
C_ASIATICA = Species(
    name="Chrysochloris asiatica",
    local_names={EN: "Cape golden mole", PL: "złotokret zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chrysochloris_asiatica_-_1731-1795_-_Print_-_Iconographia_Zoologica_-_Special_Collections_University_of_Amsterdam.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Chrysochloris_asiatica_-_1731-1795_-_Print_-_Iconographia_Zoologica_-_Special_Collections_University_of_Amsterdam.jpg",
        author="Cornelis van Noorde",
        license=License.PUBLIC_DOMAIN,
    ),
)
T_ECAUDATUS = Species(
    name="Tenrec ecaudatus",
    local_names={EN: "tailless tenrec, common tenrec", PL: "tenrek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tenrec_ecaudatus_is_widespread_throughout_Seychelles.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Tenrec_ecaudatus_is_widespread_throughout_Seychelles.jpg",
        author="Yulia Kolosova",
        license=License.CC_BY_4_0,
    ),
)
S_SETOSUS = Species(
    name="Setifer setosus",
    local_names={
        EN: "greater hedgehog tenrec, large Madagaskar hedgehog",
        PL: "jeżokret kłujący",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ericulus_nigrescens_St.-Hilaire_1839.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/Ericulus_nigrescens_St.-Hilaire_1839.jpg",
        author="Unknown author",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_CAPENSIS = Species(
    name="Procavia capensis",
    local_names={EN: "rock hyrax, dassie, rock rabbit", PL: "góralek skalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rock_Hyrax_(Procavia_capensis)_(7042223567).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Rock_Hyrax_%28Procavia_capensis%29_%287042223567%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
T_MANATUS = Species(
    name="Trichechus manatus",
    local_names={
        EN: "North American manatee, West Indian manatee",
        PL: "manat karaibski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Manatee_photo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Manatee_photo.jpg",
        author="NASA",
        license=License.NASA,
    ),
)

ORYCTEROPUS = Genus(name="Orycteropus", children=[O_AFER])
RHYNCHOCYON = Genus(name="Rhynchocyon", children=[R_PETERSI])
CHRYSOCHLORIS = Genus(name="Chrysochloris", children=[C_ASIATICA])
TENREC = Genus(name="Tenrec", children=[T_ECAUDATUS])
SETIFER = Genus(name="Setifer", children=[S_SETOSUS])
PROCAVIA = Genus(name="Procavia", children=[P_CAPENSIS])
TRICHECHUS = Genus(name="Trichechus", children=[T_MANATUS])

ORYCTEROPODIDAE = Family(name="Orycteropodidae", children=[ORYCTEROPUS])
MACROSCELIDIDAE = Family(name="Macroscelididae", children=[RHYNCHOCYON])
CHRYSOCHLORIDAE = Family(name="Chrysochloridae", children=[CHRYSOCHLORIS])
TENRECIDAE = Family(name="Tenrecidae", children=[TENREC, SETIFER])
PROCAVIIDAE = Family(name="Procaviidae", children=[PROCAVIA])
TRICHECHIDAE = Family(name="Trichechidae", children=[TRICHECHUS])

TENRECOMORPHA = Suborder(name="Tenrecomorpha", children=[TENRECIDAE])

TUBULIDENTATA = Order(name="Tubulidentata", children=[ORYCTEROPODIDAE])
MACROSCELIDEA = Order(name="Macroscelidea", children=[MACROSCELIDIDAE])
AFROSORICIDA = Order(name="Afrosoricida", children=[CHRYSOCHLORIDAE, TENRECOMORPHA])
HYRACOIDEA = Order(name="Hyracoidea", children=[PROCAVIIDAE])
SIRENIA = Order(name="Sirenia", children=[TRICHECHIDAE])

AFROINSECTIVORA = Clade(name="Afroinsectivora", children=[MACROSCELIDEA, AFROSORICIDA])
TETHYTHERIA = Clade(name="Tethytheria", children=[SIRENIA, PROBOSCIDEA])

AFROINSECTIPHILIA = Clade(
    name="Afroinsectiphilia", children=[TUBULIDENTATA, AFROINSECTIVORA]
)
PAENUNGULATA = Clade(name="Paenungulata", children=[HYRACOIDEA, TETHYTHERIA])

AFROTHERIA = Superorder(name="Afrotheria", children=[AFROINSECTIPHILIA, PAENUNGULATA])
