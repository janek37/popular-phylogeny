from clade import (
    Clade,
    Family,
    Genus,
    Infraclass,
    Megacohort,
    Order,
    Species,
    Supercohort,
    Superorder,
)
from constants import EN, PL
from image import Image, License

from .acanthomorpha import ACANTHOMORPHA
from .otocephala import OTOCEPHALA
from .protacanthopterygii import PROTACANTHOPTERYGII
from .stomiati import STOMIATI

A_ANGUILLA = Species(
    name="Anguilla anguilla",
    local_names={EN: "European eel", PL: "węgorz europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_35739_Anguilla_vulgaris_--_Anguilla.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/FMIB_35739_Anguilla_vulgaris_--_Anguilla.jpeg",
        author="Felice Supino",
        license=License.FMIB,
    ),
)
M_HELENA = Species(
    name="Muraena helena",
    local_names={EN: "Mediterranean moray, Roman eel", PL: "murena śródziemnomorska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Murenahelena.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Murenahelena.jpg",
        author="steven van tendeloo",
        license=License.CC_BY_SA_3_0,
    ),
)
H_TERGISUS = Species(
    name="Hiodon tergisus",
    local_names={EN: "mooneye"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hiodon_tergisus_NOAA.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Hiodon_tergisus_NOAA.jpg",
        author="United States Great Lakes Environmental Research Laboratory",
        license=License.NOAA,
    ),
)
A_GIGAS = Species(
    name="Arapaima gigas",
    local_names={EN: "arapaima, pirarucu", PL: "arapaima"},
    known_for=[{EN: "one of the largest freshwater fish"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arapaimidae_Arapaima_gigas_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Arapaimidae_Arapaima_gigas_2.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
G_PETERSII = Species(
    name="Gnathonemus petersii",
    local_names={EN: "Peters's elephantnose fish", PL: "trąbonos, mruk Petersa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:MormyrusJury.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/MormyrusJury.jpg",
        author="J. Jury",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
M_PUNCTATUM = Species(
    name="Myctophum punctatum",
    local_names={EN: "spotted lanternfish", PL: "świetlik tępogłowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myctophum_punctatum1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b7/Myctophum_punctatum1.jpg",
        author="Emma Kissling",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

ANGUILLA = Genus(name="Anguilla", children=[A_ANGUILLA])
MURAENA = Genus(name="Muraena", children=[M_HELENA])
HIODON = Genus(name="Hiodon", children=[H_TERGISUS])
ARAPAIMA = Genus(name="Arapaima", children=[A_GIGAS])
GNATHONEMUS = Genus(name="Gnathonemus", children=[G_PETERSII])
MYCTOPHUM = Genus(name="Myctophum", children=[M_PUNCTATUM])

ANGUILLIDAE = Family(name="Anguillidae", children=[ANGUILLA])
MURAENIDAE = Family(name="Muraenidae", children=[MURAENA])
HIODONTIDAE = Family(name="Hiodontidae", children=[HIODON])
OSTEOGLOSSIDAE = Family(name="Osteoglossidae", children=[ARAPAIMA])
MORMYRIDAE = Family(name="Mormyridae", children=[GNATHONEMUS])
MYCTOPHIDAE = Family(name="Myctophidae", children=[MYCTOPHUM])

ANGUILLIFORMES = Order(name="Anguilliformes", children=[ANGUILLIDAE, MURAENIDAE])
HIODONTIFORMES = Order(name="Hiodontiformes", children=[HIODONTIDAE])
OSTEOGLOSSIFORMES = Order(
    name="Osteoglossiformes", children=[OSTEOGLOSSIDAE, MORMYRIDAE]
)
MYCTOPHIFORMES = Order(name="Myctophiformes", children=[MYCTOPHIDAE])

ELOPOMORPHA = Superorder(name="Elopomorpha", children=[ANGUILLIFORMES])
OSTEOGLOSSOMORPHA = Superorder(
    name="Osteoglossomorpha", children=[HIODONTIFORMES, OSTEOGLOSSIFORMES]
)

NEOTELEOSTEI = Clade(name="Neoteleostei", children=[MYCTOPHIFORMES, ACANTHOMORPHA])

EUTELEOSTEI_A = Clade(children=[STOMIATI, NEOTELEOSTEI])
EUTELEOSTEI = Clade(name="Euteleostei", children=[PROTACANTHOPTERYGII, EUTELEOSTEI_A])

CLUPEOCEPHALA = Supercohort(name="Clupeocephala", children=[OTOCEPHALA, EUTELEOSTEI])

OSTEOGLOSSOCEPHALAI = Megacohort(
    name="Osteoglossocephalai", children=[OSTEOGLOSSOMORPHA, CLUPEOCEPHALA]
)

TELEOSTEI = Infraclass(name="Teleostei", children=[ELOPOMORPHA, OSTEOGLOSSOCEPHALAI])
