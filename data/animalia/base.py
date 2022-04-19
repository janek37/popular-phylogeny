from clade import (
    Clade,
    Class,
    Family,
    Genus,
    Kingdom,
    Order,
    Phylum,
    Species,
    Subphylum,
    Superphylum,
)
from constants import EN, PL
from image import Image, License

from .cnidaria import CNIDARIA
from .echinodermata import ECHINODERMATA
from .protostomia import PROTOSTOMIA
from .vertebrata import VERTEBRATA

# region PORIFERA
A_FISTULARIS = Species(
    name="Aplysina fistularis",
    local_names={EN: "yellow sponge"},
    known_for=[{EN: "SpongeBob SquarePants"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Reef3859_-_Flickr_-_NOAA_Photo_Library.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Reef3859_-_Flickr_-_NOAA_Photo_Library.jpg",
        author="Twilight Zone Expedition Team 2007, National Oceanic and Atmospheric Administration - Ocean Exploration.",
        license=License.CC_BY_2_0,
    ),
)
APLYSINA = Genus(name="Aplysina", children=[A_FISTULARIS])
APLYSINIDAE = Family(name="Aplysinidae", children=[APLYSINA])
VERONGIDA = Order(name="Verongida", children=[APLYSINIDAE])
DEMOSPONGIAE = Class(name="Demospongiae", children=[VERONGIDA])
PORIFERA = Phylum(name="Porifera", children=[DEMOSPONGIAE])
# endregion PORIFERA

# region TUNICATA
C_INTESTINALIS = Species(
    name="Ciona intestinalis",
    local_names={EN: "vase tunicate", PL: "przejrzystka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cionaintestinalis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Cionaintestinalis.jpg",
        author="perezoso",
        license=License.CC_BY_SA_3_0,
    ),
)
P_AURATA = Species(
    name="Polycarpa aurata",
    local_names={EN: "ox heart ascidian, gold-mouth sea squirt, ink-spot sea squirt"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tunicate_komodo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Tunicate_komodo.jpg",
        author="Nhobgood Nick Hobgood",
        license=License.CC_BY_SA_3_0,
    ),
)

CIONA = Genus(name="Ciona", children=[C_INTESTINALIS])
POLYCARPA = Genus(name="Polycarpa", children=[P_AURATA])

CIONIDAE = Family(name="Cionidae", children=[CIONA])
STYELIDAE = Family(name="Styelidae", children=[POLYCARPA])

ENTEROGONA = Order(name="Enterogona", children=[CIONIDAE])
STOLIDOBRANCHIA = Order(name="Stolidobranchia", children=[STYELIDAE])

ASCIDIACEA = Class(name="Ascidiacea", children=[ENTEROGONA, STOLIDOBRANCHIA])

TUNICATA = Subphylum(name="Tunicata", children=[ASCIDIACEA])
# endregion TUNICATA

CHORDATA = Phylum(name="Chordata", children=[TUNICATA, VERTEBRATA])

DEUTEROSTOMIA = Superphylum(name="Deuterostomia", children=[ECHINODERMATA, CHORDATA])

NEPHROZOA = Clade(name="Nephrozoa", children=[PROTOSTOMIA, DEUTEROSTOMIA])
PARAHOXOZOA = Clade(name="ParaHoxozoa", children=[CNIDARIA, NEPHROZOA])

ANIMALIA = Kingdom(name="Animalia", children=[PORIFERA, PARAHOXOZOA])
