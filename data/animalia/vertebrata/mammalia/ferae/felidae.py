from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, PL

S_FATALIS = Species(
    name="Smilodon fatalis",
    local_names={EN: "saber-toothed tiger", PL: "tygrys szablozębny"},
)
P_TIGRIS = Species(
    name="Panthera tigris", local_names={EN: "tiger", PL: "tygrys azjatycki"}
)
P_UNCIA = Species(
    name="Panthera uncia",
    local_names={EN: "snow leopard", PL: "pantera śnieżna, irbis śnieżny"},
)
P_ONCA = Species(
    name="Panthera onca", local_names={EN: "jaguar", PL: "jaguar amerykański"}
)
P_LEO = Species(name="Panthera leo", local_names={EN: "lion", PL: "lew afrykański"})
P_PARDUS = Species(
    name="Panthera pardus",
    local_names={EN: "leopard", PL: "pantera, leopard, lampart plamisty"},
)
C_CARACAL = Species(
    name="Caracal caracal", local_names={EN: "caracal", PL: "karakal stepowy"}
)
L_SERVAL = Species(
    name="Leptailurus serval", local_names={EN: "serval", PL: "serwal sawannowy"}
)
L_PARDALIS = Species(
    name="Leopardus pardalis", local_names={EN: "ocelot", PL: "ocelot wielki"}
)
L_LYNX = Species(
    name="Lynx lynx", local_names={EN: "Eurasian lynx", PL: "ryś euroazjatycki"}
)
L_RUFUS = Species(
    name="Lynx rufus", local_names={EN: "bobcat, red lynx", PL: "ryś rudy"}
)
A_JUBATUS = Species(
    name="Acinonyx jubatus",
    local_names={EN: "cheetah", PL: "gepard grzywiasty"},
    known_for=[{EN: "the fastest land animal"}],
)
P_CONCOLOR = Species(
    name="Puma concolor",
    local_names={EN: "cougar, puma, mountain lion", PL: "kuguar, puma płowa"},
)
P_BENGALENSIS = Species(
    name="Prionailurus bengalensis",
    local_names={EN: "leopard cat", PL: "kot bengalski, kotek bengalski"},
)
F_SILVESTRIS = Species(
    name="Felis silvestris", local_names={EN: "European wildcat", PL: "żbik europejski"}
)
F_LYBICA = Species(
    name="Felis lybica",
    local_names={EN: "African wildcat", PL: "żbik afrykański, kot nubijski"},
)
F_CATUS = Species(
    name="Felis catus", local_names={EN: "domestic cat", PL: "kot domowy"}
)

PANTHERA_A = Clade(children=[P_TIGRIS, P_UNCIA])
PANTHERA_B = Clade(children=[P_LEO, P_PARDUS])
PANTHERA_C = Clade(children=[P_ONCA, PANTHERA_B])

FELIS_A = Clade(children=[F_LYBICA, F_CATUS])

SMILODON = Genus(name="Smilodon", children=[S_FATALIS])
PANTHERA = Genus(name="Panthera", children=[PANTHERA_A, PANTHERA_C])
CARACAL = Genus(name="Caracal", children=[C_CARACAL])
LEPTAILURUS = Genus(name="Leptailurus", children=[L_SERVAL])
LEOPARDUS = Genus(name="Leopardus", children=[L_PARDALIS])
LYNX = Genus(name="Lynx", children=[L_LYNX, L_RUFUS])
ACINONYX = Genus(name="Acinonyx", children=[A_JUBATUS])
PUMA = Genus(name="Puma", children=[P_CONCOLOR])
PRIONAILURUS = Genus(name="Prionailurus", children=[P_BENGALENSIS])
FELIS = Genus(name="Felis", children=[F_SILVESTRIS, FELIS_A])

FELINAE_A = Clade(children=[CARACAL, LEPTAILURUS])
FELINAE_B = Clade(children=[ACINONYX, PUMA])
FELINAE_C = Clade(children=[PRIONAILURUS, FELIS])
FELINAE_D = Clade(children=[FELINAE_B, FELINAE_C])
FELINAE_E = Clade(children=[LYNX, FELINAE_D])
FELINAE_F = Clade(children=[LEOPARDUS, FELINAE_E])

MACHAIRODONTINAE = Subfamily(name="Machairodontinae", children=[SMILODON])
PANTHERINAE = Subfamily(name="Pantherinae", children=[PANTHERA])
FELINAE = Subfamily(name="Felinae", children=[FELINAE_A, FELINAE_F])

FELIDAE_A = Clade(children=[PANTHERINAE, FELINAE])

FELIDAE = Family(name="Felidae", children=[MACHAIRODONTINAE, FELIDAE_A])
