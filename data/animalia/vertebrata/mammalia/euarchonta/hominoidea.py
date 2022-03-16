from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Superfamily, Tribe
from constants import EN, PL

H_LAR = Species(
    name="Hylobates lar",
    local_names={EN: "lar gibbon", PL: "gibon białoręki, gibbon białoręki"},
)
P_PYGMAEUS = Species(
    name="Pongo pygmaeus",
    local_names={EN: "Bornean orangutan", PL: "orangutan borneański"},
)
G_BLACKI = Species(
    name="Gigantopithecus blacki",
    known_for=[{EN: "speculated species of yeti, bigfoot etc."}],
    extinct=True,
)
G_GORILLA = Species(
    name="Gorilla gorilla", local_names={EN: "western gorilla", PL: "goryl nizinny"}
)
P_TROGLODYTES = Species(
    name="Pan troglodytes", local_names={EN: "chimpanzee", PL: "szympans zwyczajny"}
)
P_PANISCUS = Species(
    name="Pan paniscus", local_names={EN: "bonobo", PL: "bonobo, szympans karłowaty"}
)
A_AFRICANUS = Species(name="Australopithecus africanus", extinct=True)
H_HABILIS = Species(name="Homo habilis", extinct=True)
H_ERECTUS = Species(name="Homo erectus", extinct=True)
H_NEANDERTHALENSIS = Species(
    name="Homo neanderthalensis",
    local_names={EN: "Neanderthal", PL: "neandertalczyk, człowiek neandertalski"},
    extinct=True,
)
H_SAPIENS = Species(name="Homo sapiens")

HOMO_A = Clade(children=[H_NEANDERTHALENSIS, H_SAPIENS])
HOMO_B = Clade(children=[H_ERECTUS, HOMO_A])

HYLOBATES = Genus(name="Hylobates", children=[H_LAR])
PONGO = Genus(name="Pongo", children=[P_PYGMAEUS])
GIGANTOPITHECUS = Genus(name="Gigantopithecus", children=[G_BLACKI])
GORILLA = Genus(name="Gorilla", children=[G_GORILLA])
PAN = Genus(name="Pan", children=[P_TROGLODYTES, P_PANISCUS])
HOMO = Genus(name="Homo", children=[H_HABILIS, HOMO_B])
AUSTRALOPITHECUS = Genus(
    name="Australopithecus", children=[A_AFRICANUS, HOMO]
)  # anomaly

PANINA = Subtribe(name="Panina", children=[PAN])
HOMININA = Subtribe(name="Hominina", children=[AUSTRALOPITHECUS])

GORILLINI = Tribe(name="Gorillini", children=[GORILLA])
HOMININI = Tribe(name="Hominini", children=[PANINA, HOMININA])

PONGINAE = Subfamily(name="Ponginae", children=[PONGO, GIGANTOPITHECUS])
HOMININAE = Subfamily(name="Homininae", children=[GORILLINI, HOMININI])

HYLOBATIDAE = Family(name="Hylobatidae", children=[HYLOBATES])
HOMINIDAE = Family(name="Hominidae", children=[PONGINAE, HOMININAE])

HOMINOIDEA = Superfamily(name="Hominoidea", children=[HYLOBATIDAE, HOMINIDAE])
