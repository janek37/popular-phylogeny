from clade import Clade, Family, Genus, Order, Species, Suborder
from constants import EN, PL, URL
from image import Image, License

from .hystricomorpha import HYSTRICOMORPHA
from .myomorpha import MYOMORPHA
from .sciuromorpha import SCIUROMORPHA

O_PRINCEPS = Species(
    name="Ochotona princeps",
    local_names={EN: "American pika", PL: "szczekuszka amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ochotona_princeps_(6067926559).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0c/Ochotona_princeps_%286067926559%29.jpg",
        author="Jim Kravitz",
        license=License.CC_BY_2_0,
    ),
)
L_EUROPAEUS = Species(
    name="Lepus europaeus",
    local_names={EN: "European hare", PL: "zając szarak"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lepus_Europaeus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Lepus_Europaeus.jpg",
        author="Furu Maru",
        license=License.CC_BY_SA_3_0,
    ),
)
O_CUNICULUS = Species(
    name="Oryctolagus cuniculus",
    local_names={EN: "European rabbit", PL: "królik europejski"},
    known_for=[
        {EN: "domestic rabbit, bunny rabbit", PL: "królik domowy"},
        {EN: "dwarf rabbit", PL: "królik miniaturowy"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oryctolagus_cuniculus_Tasmania_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Oryctolagus_cuniculus_Tasmania_2.jpg",
        author="JJ Harrison (https://www.jjharrison.com.au/)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_FIBER = Species(
    name="Castor fiber",
    local_names={EN: "European beaver", PL: "bóbr europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Castoridae_Castor_fiber_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Castoridae_Castor_fiber_1.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)
G_BURSARIUS = Species(
    name="Geomys bursarius",
    local_names={EN: "plains pocket gopher", PL: "goffer równinny"},
    known_for=[
        {
            EN: "Disney's Winnie-the-Pooh",
            URL: "https://disney.fandom.com/wiki/Gopher_(Winnie_the_Pooh)",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Geomys_bursarius.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/19/Geomys_bursarius.jpg",
        author="Unknown author",
        license=License.NPS,
    ),
)

OCHOTONA = Genus(name="Ochotona", children=[O_PRINCEPS])
LEPUS = Genus(name="Lepus", children=[L_EUROPAEUS])
ORYCTOLAGUS = Genus(name="Oryctolagus", children=[O_CUNICULUS])
CASTOR = Genus(name="Castor", children=[C_FIBER])
GEOMYS = Genus(name="Geomys", children=[G_BURSARIUS])

OCHOTONIDAE = Family(name="Ochotonidae", children=[OCHOTONA])
LEPORIDAE = Family(name="Leporidae", children=[LEPUS, ORYCTOLAGUS])
CASTORIDAE = Family(name="Castoridae", children=[CASTOR])
GEOMYIDAE = Family(name="Geomyidae", children=[GEOMYS])

CASTORIMORPHA = Suborder(name="Castorimorpha", children=[CASTORIDAE, GEOMYIDAE])

RODENTIA_A = Clade(children=[CASTORIMORPHA, MYOMORPHA])
RODENTIA_B = Clade(children=[HYSTRICOMORPHA, RODENTIA_A])

LAGOMORPHA = Order(name="Lagomorpha", children=[LEPORIDAE, OCHOTONIDAE])
RODENTIA = Order(name="Rodentia", children=[SCIUROMORPHA, RODENTIA_B])

GLIRES = Clade(name="Glires", children=[LAGOMORPHA, RODENTIA])
