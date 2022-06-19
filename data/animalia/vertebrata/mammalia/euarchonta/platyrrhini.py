from clade import Clade, Family, Genus, Parvorder, Species
from constants import EN, PL
from image import Image, License

C_JACCHUS = Species(
    name="Callithrix jacchus",
    local_names={EN: "common marmoset", PL: "marmozeta zwyczajna, uistiti białoucha"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Callithrix_jacchus_-_MUSE.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Callithrix_jacchus_-_MUSE.JPG",
        author="Museo delle Scienze in Trento, Italy",
        license=License.CC_BY_SA_3_0,
    ),
)
S_IMPERATOR = Species(
    name="Saguinus imperator",
    local_names={EN: "emperor tamarin", PL: "tamaryna cesarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Emperor_Tamarin_(6916675012).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Emperor_Tamarin_%286916675012%29.jpg",
        author="Eric Kilby from Somerville, MA, USA",
        license=License.CC_BY_SA_2_0,
    ),
)
L_ROSALIA = Species(
    name="Leontopithecus rosalia",
    local_names={EN: "golden lion tamarin", PL: "marmozeta lwia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leontopithecus_rosalia_-_Copenhagen_Zoo_-_DSC09082.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Leontopithecus_rosalia_-_Copenhagen_Zoo_-_DSC09082.JPG",
        author="Daderot",
        license=License.CC0,
    ),
)
A_GUARIBA = Species(
    name="Alouatta guariba",
    local_names={EN: "brown howler", PL: "wyjec brązowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brown_howler_Monkey_8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Brown_howler_Monkey_8.jpg",
        author="Peter Schoen",
        license=License.CC_BY_SA_2_0,
    ),
)
A_GEOFFROYI = Species(
    name="Ateles geoffroyi",
    local_names={EN: "Geoffroy's spider monkey", PL: "czepiak czarnoręki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:AtelesVellerosusKeulemans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/AtelesVellerosusKeulemans.jpg",
        author="J G Keulemans",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_APELLA = Species(
    name="Sapajus apella",
    local_names={EN: "tufted capuchin", PL: "kapucynka czubata"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sapajus_apella_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e2/Sapajus_apella_%28cropped%29.jpg",
        author="Rufus46",
        license=License.CC_BY_SA_3_0,
    ),
)

CALLITHRIX = Genus(name="Callithrix", children=[C_JACCHUS])
SAGUINUS = Genus(name="Saguinus", children=[S_IMPERATOR])
LEONTOPITHECUS = Genus(name="Leontopithecus", children=[L_ROSALIA])
ALOUATTA = Genus(name="Alouatta", children=[A_GUARIBA])
ATELES = Genus(name="Ateles", children=[A_GEOFFROYI])
SAPAJUS = Genus(name="Sapajus", children=[S_APELLA])

# https://www.researchgate.net/publication/259499744_Evolutionary_genetics_and_implications_of_small_size_and_twinning_in_callitrichine_primates
CALLITRICHIDAE_A = Clade(children=[CALLITHRIX, LEONTOPITHECUS])

CALLITRICHIDAE = Family(name="Callitrichidae", children=[CALLITRICHIDAE_A, SAGUINUS])
ATELIDAE = Family(name="Atelidae", children=[ALOUATTA, ATELES])
CEBIDAE = Family(name="Cebidae", children=[SAPAJUS])

# https://www.researchgate.net/publication/259499744_Evolutionary_genetics_and_implications_of_small_size_and_twinning_in_callitrichine_primates
PLATYRRHINI_A = Clade(children=[CALLITRICHIDAE, CEBIDAE])

PLATYRRHINI = Parvorder(name="Platyrrhini", children=[PLATYRRHINI_A, ATELIDAE])
