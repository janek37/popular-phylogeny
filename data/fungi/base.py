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
)
from constants import EN, IMAGE, PL
from image import Image, License

from .mushrooms import BASIDIOMYCOTA

S_CHARTARUM = Species(
    name="Stachybotrys chartarum",
    local_names={EN: "toxic black mold"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stachybotrys_chartarum_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ad/Stachybotrys_chartarum_01.jpg",
        author="Antyo99",
        license=License.CC_BY_SA_4_0,
    ),
)
A_ORYZAE = Species(
    name="Aspergillus oryzae",
    known_for=[
        {
            EN: "sake",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Yasukuni_Shrine_Sacred-Sake;_August_2019.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Yasukuni_Shrine_Sacred-Sake%3B_August_2019.jpg",
                author="MIKI Yoshihito",
                license=License.CC_BY_2_0,
            ),
        },
        {
            EN: "soy sauce",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:SoySauceDSC00235.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/SoySauceDSC00235.jpg",
                author="kskbuddy",
                license=License.PUBLIC_DOMAIN_USER,
            ),
        },
        {
            EN: "miso",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Miso_003.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Miso_003.jpg",
                author="http://www.oofree.net/photo_food/p1/miso1.html",
                license=License.CC0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aspergillus_oryzae.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/35/Aspergillus_oryzae.jpg",
        author="Yulianna.x",
        license=License.CC_BY_SA_4_0,
    ),
)
P_CAMEMBERTI = Species(
    name="Penicillium camemberti",
    known_for=[
        {
            EN: "camembert",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Camembert_de_Normandie_(AOP)_10.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/63/Camembert_de_Normandie_%28AOP%29_10.jpg",
                author="Coyau",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "brie",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Brie_Le_Roitelet.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Brie_Le_Roitelet.jpg",
                author="Thomon",
                license=License.CC_BY_SA_4_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pcamemberti.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/92/Pcamemberti.jpg",
        author="John W. (John William) Harshberger, J.W.",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_RUBENS = Species(
    name="Penicillium rubens",
    known_for=[
        {
            EN: "penicilin",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Penicillin_core.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/99/Penicillin_core.svg",
                author="Yikrazuul",
                license=License.PUBLIC_DOMAIN_CHEM,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Penicillium_rubens_(type_specimen).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/Penicillium_rubens_%28type_specimen%29.png",
        author="Houbraken, J., Frisvad, J.C. & Samson, R.A",
        license=License.CC_BY_SA_4_0,
    ),
)
P_DIGITATUM = Species(
    name="Penicillium digitatum",
    known_for=[
        {EN: "blue mold of citrus", PL: "niebieska zgnilizna owoców cytrusowych"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Penicillium_digitatum_166137242.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Penicillium_digitatum_166137242.jpg",
        author="Nicola van Berkel",
        license=License.CC_BY_SA_4_0,
    ),
)
P_EXPANSUM = Species(
    name="Penicillium expansum",
    known_for=[{EN: "blue mold of apples", PL: "mokra zgnilizna jabłek"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Penicillium_expansum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/92/Penicillium_expansum.jpg",
        author="H.J. Larsen, Bugwood.org",
        license=License.CC_BY_3_0,
    ),
)
P_ROQUEFORTI = Species(
    name="Penicillium roqueforti",
    known_for=[
        {
            EN: "Roquefort",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Wikicheese_-_Roquefort_-_20150417_-_003.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/bf/Wikicheese_-_Roquefort_-_20150417_-_003.jpg",
                author="Thesupermat",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fig._2._-_Penicillium_roqueforti_-_Thom_-_1906.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9f/Fig._2._-_Penicillium_roqueforti_-_Thom_-_1906.png",
        author="Charles Thom (1872-1956)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_CEREVISIAE = Species(
    name="Saccharomyces cerevisiae",
    known_for=[
        {
            EN: "ale",
            PL: "piwo górnej fermentacji",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Australian_pale_ale.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Australian_pale_ale.jpg",
                author="Finbar.concaig",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "baker's yeast",
            PL: "drożdże piekarskie",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Compressed_fresh_yeast_-_1.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Compressed_fresh_yeast_-_1.jpg",
                author="Hellahulla",
                license=License.CC_BY_SA_3_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Saccharomyces_cerevisiae_SEM.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Saccharomyces_cerevisiae_SEM.jpg",
        author="Mogana Das Murtey and Patchamuthu Ramasamy",
        license=License.CC_BY_SA_3_0,
    ),
)
C_ALBICANS = Species(
    name="Candida albicans",
    known_for=[{EN: "candidiasis", PL: "drożdżyca, kandydoza"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Candida_albicans_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Candida_albicans_2.jpg",
        author="GrahamColm",
        license=License.CC_BY_SA_3_0,
    ),
)
H_LACTIFLUORUM = Species(
    name="Hypomyces lactifluorum",
    local_names={EN: "lobster mushroom"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hypomyces_lactifluorum_Oaxaca.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Hypomyces_lactifluorum_Oaxaca.jpg",
        author="Alan Rockefeller",
        license=License.CC_BY_SA_4_0,
    ),
)
M_ESCULENTA = Species(
    name="Morchella esculenta",
    local_names={EN: "morel mushroom", PL: "smardz jadalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Morchella_esculenta_9603.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Morchella_esculenta_9603.jpg",
        author="Amada44",
        license=License.CC_BY_SA_3_0,
    ),
)
T_MAGNATUM = Species(
    name="Tuber magnatum",
    local_names={EN: "white truffle", PL: "trufla biała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tuber_magnatum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/75/Tuber_magnatum.jpg",
        author="Marco Plassio",
        license=License.CC_BY_SA_3_0,
    ),
)
C_ARBUSCULA = Species(
    name="Cladonia arbuscula",
    local_names={EN: "shrubby cup lichen", PL: "chrobotek leśny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cladonia_arbuscula_61164722.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Cladonia_arbuscula_61164722.jpg",
        author="Nova Patch",
        license=License.CC_BY_SA_4_0,
    ),
)
F_CAPERATA = Species(
    name="Flavoparmelia caperata",
    local_names={EN: "common greenshield lichen"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flavoparmelia_caperata_177290187.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Flavoparmelia_caperata_177290187.jpg",
        author="stephvg",
        license=License.CC0,
    ),
)
C_PURPUREA = Species(
    name="Claviceps purpurea",
    local_names={PL: "buławinka czerwona"},
    known_for=[{EN: "ergot", PL: "sporysz"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Claviceps_purpurea_s.l._(38857911412).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Claviceps_purpurea_s.l._%2838857911412%29.jpg",
        author="Björn S...",
        license=License.CC_BY_SA_2_0,
    ),
)
O_UNILATERALIS = Species(
    name="Ophiocordyceps unilateralis",
    known_for=[{EN: "controlling the behavior of infected ants"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ophiocordyceps_unilateralis_B.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Ophiocordyceps_unilateralis_B.png",
        author="David P. Hughes, Maj-Britt Pontoppidan",
        license=License.CC_BY_2_5,
    ),
)

PENICILLIUM_SECTION = Clade(children=[P_DIGITATUM, P_EXPANSUM])

STACHYBOTRYS = Genus(name="Stachybotrys", children=[S_CHARTARUM])
ASPERGILLUS = Genus(name="Aspergillus", children=[A_ORYZAE])
# research revealed multiple contradicting subtrees, there seems to be no consensus
PENICILLIUM = Genus(
    name="Penicillium",
    children=[P_CAMEMBERTI, P_RUBENS, PENICILLIUM_SECTION, P_ROQUEFORTI],
)
SACCHAROMYCES = Genus(name="Saccharomyces", children=[S_CEREVISIAE])
CANDIDA = Genus(name="Candida", children=[C_ALBICANS])
HYPOMYCES = Genus(name="Hypomyces", children=[H_LACTIFLUORUM])
MORCHELLA = Genus(name="Morchella", children=[M_ESCULENTA])
TUBER = Genus(name="Tuber", children=[T_MAGNATUM])
CLADONIA = Genus(name="Cladonia", children=[C_ARBUSCULA])
FLAVOPARMELIA = Genus(name="Flavoparmelia", children=[F_CAPERATA])
CLAVICEPS = Genus(name="Claviceps", children=[C_PURPUREA])
OPHIOCORDYCEPS = Genus(name="Ophiocordyceps", children=[O_UNILATERALIS])

STACHYBOTRYACEAE = Family(name="Stachybotryaceae", children=[STACHYBOTRYS])
TRICHOCOMACEAE = Family(name="Trichocomaceae", children=[ASPERGILLUS, PENICILLIUM])
SACCHAROMYCETACEAE = Family(
    name="Saccharomycetaceae", children=[SACCHAROMYCES, CANDIDA]
)
HYPOCREACEAE = Family(name="Hypocreaceae", children=[HYPOMYCES])
MORCHELLACEAE = Family(name="Morchellaceae", children=[MORCHELLA])
TUBERACEAE = Family(name="Tuberaceae", children=[TUBER])
CLADONIACEAE = Family(name="Cladoniaceae", children=[CLADONIA])
PARMELIACEAE = Family(name="Parmeliaceae", children=[FLAVOPARMELIA])
CLAVICIPITACEAE = Family(name="Clavicipitaceae", children=[CLAVICEPS])
OPHIOCORDYCIPITACEAE = Family(name="Ophiocordycipitaceae", children=[OPHIOCORDYCEPS])

# https://www.researchgate.net/publication/325346148_Introgression_and_gene_family_contraction_drive_the_evolution_of_lifestyle_and_host_shifts_of_hypocrealean_fungi
HYPOCREALES_B = Clade(children=[CLAVICIPITACEAE, OPHIOCORDYCIPITACEAE])
HYPOCREALES_A = Clade(children=[HYPOCREACEAE, HYPOCREALES_B])

HYPOCREALES = Order(name="Hypocreales", children=[STACHYBOTRYACEAE, HYPOCREALES_A])
EUROTIALES = Order(name="Eurotiales", children=[TRICHOCOMACEAE])
SACCHAROMYCETALES = Order(name="Saccharomycetales", children=[SACCHAROMYCETACEAE])
PEZIZALES = Order(name="Pezizales", children=[MORCHELLACEAE, TUBERACEAE])
LECANORALES = Order(name="Lecanorales", children=[CLADONIACEAE, PARMELIACEAE])

SORDARIOMYCETES = Class(name="Sordariomycetes", children=[HYPOCREALES])
EUROTIOMYCETES = Class(name="Eurotiomycetes", children=[EUROTIALES])
SACCHAROMYCETES = Class(name="Saccharomycetes", children=[SACCHAROMYCETALES])
PEZIZOMYCETES = Class(name="Pezizomycetes", children=[PEZIZALES])
LECANOROMYCETES = Class(name="Lecanoromycetes", children=[LECANORALES])

DOTHIDEOMYCETA = Clade(
    name="Dothideomyceta", children=[EUROTIOMYCETES, LECANOROMYCETES]
)
LEOTIOMYCETA = Clade(name="Leotiomyceta", children=[SORDARIOMYCETES, DOTHIDEOMYCETA])
PEZIZOMYCOTINA = Subphylum(
    name="Pezizomycotina", children=[LEOTIOMYCETA, PEZIZOMYCETES]
)

ASCOMYCOTA = Phylum(name="Ascomycota", children=[PEZIZOMYCOTINA, SACCHAROMYCETES])

EUMYCOTA = Kingdom(name="Eumycota", children=[ASCOMYCOTA, BASIDIOMYCOTA])
