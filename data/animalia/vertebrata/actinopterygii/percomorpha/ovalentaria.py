from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

O_NILOTICUS = Species(
    name="Oreochromis niloticus", local_names={EN: "Nile tilapia", PL: "tilapia nilowa"}
)
P_SCALARE = Species(
    name="Pterophyllum scalare",
    local_names={EN: "freshwater angelfish", PL: "ryba księżycowa, żaglowiec skalar"},
    known_for=[{EN: "A Fish Called Wanda"}],
)
E_VOLITANS = Species(
    name="Exocoetus volitans",
    local_names={
        EN: "tropical two-wing flyingfish, blue flyingfish",
        PL: "ptaszor jaskółczy",
    },
)
C_PINNATIBARBATUS = Species(
    name="Cheilopogon pinnatibarbatus",
    local_names={EN: "Bennett's flying fish", PL: "wylotek przezroczystopłetwy"},
    known_for=[{EN: "one of the four-winged flying fish"}],
)
A_OCELLARIS = Species(
    name="Amphiprion ocellaris",
    local_names={
        EN: "ocellaris clownfish",
        PL: "błazenek plamisty, amfiprion plamisty",
    },
    known_for=[{EN: "main characters in Finding Nemo"}],
)
P_RETICULATA = Species(
    name="Poecilia reticulata",
    local_names={EN: "guppy, millionfish, rainbowfish", PL: "pawie oczko, gupik"},
)

OREOCHROMIS = Genus(name="Oreochromis", children=[O_NILOTICUS])
PTEROPHYLLUM = Genus(name="Pterophyllum", children=[P_SCALARE])
EXOCOETUS = Genus(name="Exocoetus", children=[E_VOLITANS])
CHEILOPOGON = Genus(name="Cheilopogon", children=[C_PINNATIBARBATUS])
AMPHIPRION = Genus(name="Amphiprion", children=[A_OCELLARIS])
POECILIA = Genus(name="Poecilia", children=[P_RETICULATA])

CICHLIDAE = Family(name="Cichlidae", children=[OREOCHROMIS, PTEROPHYLLUM])
EXOCOETIDAE = Family(name="Exocoetidae", children=[EXOCOETUS, CHEILOPOGON])
POMACENTRIDAE = Family(name="Pomacentridae", children=[AMPHIPRION])
POECILIIDAE = Family(name="Poeciliidae", children=[POECILIA])

CICHLIFORMES = Order(name="Cichliformes", children=[CICHLIDAE])
BELONIFORMES = Order(name="Beloniformes", children=[EXOCOETIDAE])
CYPRINODONTIFORMES = Order(name="Cyprinodontiformes", children=[POECILIIDAE])

ATHERINOMORPHAE = Clade(
    name="Atherinomorphae", children=[BELONIFORMES, CYPRINODONTIFORMES]
)

OVALENTARIA_A = Clade(children=[CICHLIFORMES, ATHERINOMORPHAE])
OVALENTARIA = Clade(name="Ovalentaria", children=[OVALENTARIA_A, POMACENTRIDAE])
