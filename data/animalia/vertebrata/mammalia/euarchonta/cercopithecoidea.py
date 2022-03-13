from clade import Clade, Family, Genus, Species, Subfamily, Superfamily, Tribe
from constants import EN, PL

M_FUSCATA = Species(
    name="Macaca fuscata",
    local_names={EN: "Japanese macaque", PL: "makak japoński"},
    known_for=[{EN: "three wise monkeys"}],
)
M_MULATTA = Species(
    name="Macaca mulatta",
    local_names={EN: "rhesus macaque", PL: "rezus, makak królewski"},
    known_for=[{EN: "Rh blood group system"}],
)
M_SPHINX = Species(
    name="Mandrillus sphinx", local_names={EN: "mandrill", PL: "mandryl barwnolicy"}
)
P_HAMADRYAS = Species(
    name="Papio hamadryas",
    local_names={EN: "sacred baboon, hamadryas baboon", PL: "pawian płaszczowy"},
)
C_DIANA = Species(
    name="Cercopithecus diana", local_names={EN: "Diana monkey", PL: "koczkodan Diany"}
)
N_LARVATUS = Species(
    name="Nasalis larvatus",
    local_names={EN: "proboscis monkey", PL: "nosacz sundajski"},
    known_for=[{EN: "internet meme"}],
)

MACACA = Genus(name="Macaca", children=[M_FUSCATA, M_MULATTA])
MANDRILLUS = Genus(name="Mandrillus", children=[M_SPHINX])
PAPIO = Genus(name="Papio", children=[P_HAMADRYAS])
CERCOPITHECUS = Genus(name="Cercopithecus", children=[C_DIANA])
NASALIS = Genus(name="Nasalis", children=[N_LARVATUS])

PAPIONINI_A = Clade(children=[MANDRILLUS, PAPIO])

PAPIONINI = Tribe(name="Papionini", children=[MACACA, PAPIONINI_A])
CERCOPITHECINI = Tribe(name="Cercopithecini", children=[CERCOPITHECUS])

CERCOPITHECINAE = Subfamily(
    name="Cercopithecinae", children=[PAPIONINI, CERCOPITHECINI]
)
COLOBINAE = Subfamily(name="Colobinae", children=[NASALIS])

CERCOPITHECIDAE = Family(name="Cercopithecidae", children=[CERCOPITHECINAE, COLOBINAE])

CERCOPITHECOIDEA = Superfamily(name="Cercopithecoidea", children=[CERCOPITHECIDAE])
