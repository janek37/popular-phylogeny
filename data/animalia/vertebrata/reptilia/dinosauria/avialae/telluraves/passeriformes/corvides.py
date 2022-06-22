from clade import Clade, Family, Genus, Infraorder, Species, Subfamily, Superfamily
from constants import EN, PL
from image import Image, License

from .paradisaeidae import PARADISAEIDAE

C_CORAX = Species(
    name="Corvus corax",
    local_names={
        EN: "common raven, western raven, northen raven",
        PL: "kruk zwyczajny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Corvus_corax_(Common_Raven),_Yosemite_NP,_CA,_US_-_Diliff.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Corvus_corax_%28Common_Raven%29%2C_Yosemite_NP%2C_CA%2C_US_-_Diliff.jpg",
        author="Diliff",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CORNIX = Species(
    name="Corvus cornix",
    local_names={EN: "hooded crow", PL: "wrona siwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hooded_Crow_(Corvus_cornix)_(11).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Hooded_Crow_%28Corvus_cornix%29_%2811%29.jpg",
        author="Ken Billington",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CORONE = Species(
    name="Corvus corone",
    local_names={EN: "carrion crow", PL: "wrona czarna, wroniec, czarnowron"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carrion_crow_(Corvus_corone)_Georges_Valbon_2022_03_18_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Carrion_crow_%28Corvus_corone%29_Georges_Valbon_2022_03_18_01.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)
C_BRACHYRHYNCHOS = Species(
    name="Corvus brachyrhynchos",
    local_names={EN: "American crow", PL: "wrona amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:2014-04-29_01_Northwestern_crow_(Corvus_brachyrhynchos_caurinus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/2014-04-29_01_Northwestern_crow_%28Corvus_brachyrhynchos_caurinus%29.jpg",
        author="Gordon Leggett",
        license=License.CC_BY_SA_4_0,
    ),
)
C_FRUGILEGUS = Species(
    name="Corvus frugilegus",
    local_names={EN: "rook", PL: "gawron"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rook-Corvus_frugilegus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b5/Rook-Corvus_frugilegus.jpg",
        author="Andreas Trepte",
        license=License.CC_BY_SA_2_5,
    ),
)
C_MONEDULA = Species(
    name="Coloeus monedula",
    local_names={EN: "western jackdaw", PL: "kawka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coloeus_monedula_01.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Coloeus_monedula_01.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
G_GLANDARIUS = Species(
    name="Garrulus glandarius",
    local_names={EN: "Eurasian jay", PL: "sójka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Garrulus_glandarius_B_Luc_Viatour.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/Garrulus_glandarius_B_Luc_Viatour.jpg",
        author="Luc Viatour",
        license=License.CC_BY_SA_3_0,
    ),
)
P_PICA = Species(
    name="Pica pica",
    local_names={EN: "Eurasian magpie, common magpie", PL: "sroka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_magpie_(Pica_pica).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Common_magpie_%28Pica_pica%29.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
C_CRISTATA = Species(
    name="Cyanocitta cristata",
    local_names={EN: "blue jay", PL: "modrosójka błękitna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyanocitta_cristata2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/14/Cyanocitta_cristata2.jpg",
        author="Marumari at English Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
O_ORIOLUS = Species(
    name="Oriolus oriolus",
    local_names={EN: "Eurasian golden oriole", PL: "wilga zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Golden_Oriole_(Oriolus_oriolus)_(35634174602).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Golden_Oriole_%28Oriolus_oriolus%29_%2835634174602%29.jpg",
        author="Imran Shah from Islamabad, Pakistan",
        license=License.CC_BY_SA_2_0,
    ),
)

# https://bmcecolevol.biomedcentral.com/articles/10.1186/1471-2148-12-72
CORVUS_A = Clade(children=[C_CORAX, C_FRUGILEGUS])
CORVUS_B = Clade(children=[C_CORNIX, C_CORONE])  # sometimes considered subspecies
CORVUS_C = Clade(children=[CORVUS_B, C_BRACHYRHYNCHOS])

CORVUS = Genus(name="Corvus", children=[CORVUS_A, CORVUS_C])
COLOEUS = Genus(name="Coloeus", children=[C_MONEDULA])
GARRULUS = Genus(name="Garrulus", children=[G_GLANDARIUS])
PICA = Genus(name="Pica", children=[P_PICA])
CYANOCITTA = Genus(name="Cyanocitta", children=[C_CRISTATA])
ORIOLUS = Genus(name="Oriolus", children=[O_ORIOLUS])

CORVINAE_A = Clade(children=[CORVUS, COLOEUS])
CORVINAE_B = Clade(children=[GARRULUS, PICA])

CORVINAE = Subfamily(name="Corvinae", children=[CORVINAE_A, CORVINAE_B])
CYANOCORACINAE = Subfamily(name="Cyanocoracinae", children=[CYANOCITTA])

CORVIDAE = Family(name="Corvidae", children=[CORVINAE, CYANOCORACINAE])
ORIOLIDAE = Family(name="Oriolidae", children=[ORIOLUS])

CORVOIDEA = Superfamily(name="Corvoidea", children=[CORVIDAE, PARADISAEIDAE])
ORIOLOIDEA = Subfamily(name="Orioloidea", children=[ORIOLIDAE])

CORVIDES = Infraorder(name="Corvides", children=[CORVOIDEA, ORIOLOIDEA])
