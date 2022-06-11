from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

O_NILOTICUS = Species(
    name="Oreochromis niloticus",
    local_names={EN: "Nile tilapia", PL: "tilapia nilowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Til%C3%A1pia_ou_Sarotherodon_niloticus_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Til%C3%A1pia_ou_Sarotherodon_niloticus_2.jpg",
        author="Germano Roberto Schüür",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SCALARE = Species(
    name="Pterophyllum scalare",
    local_names={EN: "freshwater angelfish", PL: "ryba księżycowa, żaglowiec skalar"},
    known_for=[{EN: "A Fish Called Wanda"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pterophyllum_scalare_adult.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Pterophyllum_scalare_adult.jpg",
        author="Citron",
        license=License.CC_BY_SA_3_0,
    ),
)
E_VOLITANS = Species(
    name="Exocoetus volitans",
    local_names={
        EN: "tropical two-wing flyingfish, blue flyingfish",
        PL: "ptaszor jaskółczy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Exocoetus_volitans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Exocoetus_volitans.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN,
    ),
)
C_PINNATIBARBATUS = Species(
    name="Cheilopogon pinnatibarbatus",
    local_names={EN: "Bennett's flying fish", PL: "wylotek przezroczystopłetwy"},
    known_for=[{EN: "one of the four-winged flying fishes"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cheilopogon_pinnatibarbatus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cheilopogon_pinnatibarbatus.jpg",
        author="Jobin",
        license=License.PUBLIC_DOMAIN,
    ),
)
A_OCELLARIS = Species(
    name="Amphiprion ocellaris",
    local_names={
        EN: "ocellaris clownfish",
        PL: "błazenek plamisty, amfiprion plamisty",
    },
    known_for=[{EN: "main characters in Finding Nemo"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Amphiprion_ocellaris_(Clown_anemonefish)_Nemo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/85/Amphiprion_ocellaris_%28Clown_anemonefish%29_Nemo.jpg",
        author="Nhobgood Nick Hobgood",
        license=License.CC_BY_SA_3_0,
    ),
)
P_RETICULATA = Species(
    name="Poecilia reticulata",
    local_names={EN: "guppy, millionfish, rainbowfish", PL: "pawie oczko, gupik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Guppy_-_Poecilia_reticulata.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e7/Guppy_-_Poecilia_reticulata.jpg",
        author="Vincent Eisfeld",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SPHENOPS = Species(
    name="Poecilia sphenops",
    local_names={EN: "molly", PL: "molinezja ostropyska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Poecilia_sphenops.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/Poecilia_sphenops.jpg",
        author="Hugo Torres",
        license=License.CC_BY_2_5_ES,
    ),
)
X_HELLERII = Species(
    name="Xiphophorus hellerii",
    local_names={EN: "green swordtail", PL: "mieczyk Hellera"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Xiphophorus_hellerii_red_male_female_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/96/Xiphophorus_hellerii_red_male_female_01.jpg",
        author="Wojciech J. Płuciennik",
        license=License.CC_BY_SA_4_0,
    ),
)

OREOCHROMIS = Genus(name="Oreochromis", children=[O_NILOTICUS])
PTEROPHYLLUM = Genus(name="Pterophyllum", children=[P_SCALARE])
EXOCOETUS = Genus(name="Exocoetus", children=[E_VOLITANS])
CHEILOPOGON = Genus(name="Cheilopogon", children=[C_PINNATIBARBATUS])
AMPHIPRION = Genus(name="Amphiprion", children=[A_OCELLARIS])
POECILIA = Genus(name="Poecilia", children=[P_RETICULATA, P_SPHENOPS])
XIPHOPHORUS = Genus(name="Xiphophorus", children=[X_HELLERII])

CICHLIDAE = Family(name="Cichlidae", children=[OREOCHROMIS, PTEROPHYLLUM])
EXOCOETIDAE = Family(name="Exocoetidae", children=[EXOCOETUS, CHEILOPOGON])
POMACENTRIDAE = Family(name="Pomacentridae", children=[AMPHIPRION])
POECILIIDAE = Family(name="Poeciliidae", children=[POECILIA, XIPHOPHORUS])

CICHLIFORMES = Order(name="Cichliformes", children=[CICHLIDAE])
BELONIFORMES = Order(name="Beloniformes", children=[EXOCOETIDAE])
CYPRINODONTIFORMES = Order(name="Cyprinodontiformes", children=[POECILIIDAE])

ATHERINOMORPHAE = Clade(
    name="Atherinomorphae", children=[BELONIFORMES, CYPRINODONTIFORMES]
)

OVALENTARIA_A = Clade(children=[CICHLIFORMES, ATHERINOMORPHAE])
OVALENTARIA = Clade(name="Ovalentaria", children=[OVALENTARIA_A, POMACENTRIDAE])
