from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

S_BARRACUDA = Species(
    name="Sphyraena barracuda",
    local_names={EN: "great barracuda", PL: "barrakuda wielka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sphyraenidae_-_Sphyraena_barracuda_(Great_barracuda).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Sphyraenidae_-_Sphyraena_barracuda_%28Great_barracuda%29.JPG",
        author="Hectonichus",
        license=License.CC_BY_SA_4_0,
    ),
)
X_GLADIUS = Species(
    name="Xiphias gladius",
    local_names={EN: "swordfish", PL: "miecznik, włócznik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Swordfish-Xiphias_gladius.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Swordfish-Xiphias_gladius.png",
        author="NOAA Photo Library",
        license=License.NOAA,
    ),
)
I_PLATYPTERUS = Species(
    name="Istiophorus platypterus",
    local_names={EN: "Indo-Pacific sailfish", PL: "żaglica"},
    known_for=[{EN: "one of the fastest fish in the ocean"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Naturalis_Biodiversity_Center_-_RMNH.ART.194_-_Istiophorus_platypterus_(Shaw_and_Nodder)_-_Kawahara_Keiga_-_1823_-_1829_-_Siebold_Collection_-_new_version.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Naturalis_Biodiversity_Center_-_RMNH.ART.194_-_Istiophorus_platypterus_%28Shaw_and_Nodder%29_-_Kawahara_Keiga_-_1823_-_1829_-_Siebold_Collection_-_new_version.jpeg",
        author="Kawahara Keiga",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
M_NIGRICANS = Species(
    name="Makaira nigricans",
    local_names={EN: "Atlantic blue marlin", PL: "marlin błękitny, makaria błękitna"},
    known_for=[{EN: "The Old Man and the Sea", PL: "Stary człowiek i morze"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Atlantic_blue_marlin.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Atlantic_blue_marlin.jpg",
        author="NOAA",
        license=License.NOAA,
    ),
)
P_FLESUS = Species(
    name="Platichthys flesus",
    local_names={EN: "European flounder", PL: "flądra, stornia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Platichthys_flesus2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Platichthys_flesus2.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
H_HIPPOGLOSSUS = Species(
    name="Hippoglossus hippoglossus",
    local_names={EN: "Atlantic halibut", PL: "halibut atlantycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hippoglossus_hippoglossus1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a0/Hippoglossus_hippoglossus1.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_SOLEA = Species(
    name="Solea solea",
    local_names={EN: "common sole", PL: "sola zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_51246_Common_Sole_(Solea_vulgaris).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/FMIB_51246_Common_Sole_%28Solea_vulgaris%29.jpeg",
        author="Reinhold Thiele",
        license=License.FMIB,
    ),
)
C_HIPPURUS = Species(
    name="Coryphaena hippurus",
    local_names={
        EN: "mahi-mahi, common dolphinfish",
        PL: "złota makrela, smagla, koryfena",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coryphaena_hippurus.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Coryphaena_hippurus.png",
        author="Unknown author",
        license=License.NOAA,
    ),
)

SPHYRAENA = Genus(name="Sphyraena", children=[S_BARRACUDA])
XIPHIAS = Genus(name="Xiphias", children=[X_GLADIUS])
ISTIOPHORUS = Genus(name="Istiophorus", children=[I_PLATYPTERUS])
MAKAIRA = Genus(name="Makaira", children=[M_NIGRICANS])
PLATICHTHYS = Genus(name="Platichthys", children=[P_FLESUS])
HIPPOGLOSSUS = Genus(name="Hippoglossus", children=[H_HIPPOGLOSSUS])
SOLEA = Genus(name="Solea", children=[S_SOLEA])
CORYPHAENA = Genus(name="Coryphaena", children=[C_HIPPURUS])

SPHYRAENIDAE = Family(name="Sphyraenidae", children=[SPHYRAENA])
XIPHIIDAE = Family(name="Xiphiidae", children=[XIPHIAS])
ISTIOPHORIDAE = Family(name="Istiophoridae", children=[ISTIOPHORUS, MAKAIRA])
PLEURONECTIDAE = Family(name="Pleuronectidae", children=[PLATICHTHYS, HIPPOGLOSSUS])
SOLEIDAE = Family(name="Soleidae", children=[SOLEA])
CORYPHAENIDAE = Family(name="Coryphaenidae", children=[CORYPHAENA])

# no source, but rather obvious
ISTIOPHORIFORMES_A = Clade(children=[XIPHIIDAE, ISTIOPHORIDAE])

# not sure about Sphyraenidae, conflicting information
ISTIOPHORIFORMES = Order(
    name="Istiophoriformes", children=[SPHYRAENIDAE, ISTIOPHORIFORMES_A]
)
PLEURONECTIFORMES = Order(name="Pleuronectiformes", children=[PLEURONECTIDAE, SOLEIDAE])
# Carangiformes is not a clade

CARANGARIA_A = Clade(children=[ISTIOPHORIFORMES, PLEURONECTIFORMES])
CARANGARIA = Clade(name="Carangaria", children=[CARANGARIA_A, CORYPHAENIDAE])
