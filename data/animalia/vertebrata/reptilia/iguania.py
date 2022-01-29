from clade import Clade, Family, Genus, Species, Subfamily, Suborder
from constants import EN, PL

C_CHAMAELEON = Species(
    name="Chamaeleo chamaeleon",
    local_names={EN: "common chameleon", PL: "kameleon pospolity"},
)
C_KINGII = Species(
    name="Chlamydosaurus kingii",
    local_names={EN: "frilled lizard", PL: "agama kołnierzasta"},
)
M_HORRIDUS = Species(
    name="Moloch horridus",
    local_names={EN: "thorny devil", PL: "moloch kolczasty, moloch straszliwy"},
)
D_VOLANS = Species(
    name="Draco volans", local_names={EN: "common flying dragon", PL: "smok latający"}
)
I_IGUANA = Species(
    name="Iguana iguana", local_names={EN: "green iguana", PL: "legwan zielony"}
)
A_CAROLINENSIS = Species(
    name="Anolis carolinensis",
    local_names={EN: "green anole", PL: "anolis zielony"},
    known_for=[
        {EN: "one of the most notable color-changing lizards besides chameleons"}
    ],
)

CHAMAELEO = Genus(name="Chamaeleo", children=[C_CHAMAELEON])
CHLAMYDOSAURUS = Genus(name="Chlamydosaurus", children=[C_KINGII])
MOLOCH = Genus(name="Moloch", children=[M_HORRIDUS])
DRACO = Genus(name="Draco", children=[D_VOLANS])
IGUANA = Genus(name="Iguana", children=[I_IGUANA])
ANOLIS = Genus(name="Anolis", children=[A_CAROLINENSIS])

AMPHIBOLURINAE = Subfamily(name="Amphibolurinae", children=[CHLAMYDOSAURUS, MOLOCH])
DRACONINAE = Subfamily(name="Draconinae", children=[DRACO])

CHAMAELEONIDAE = Family(name="Chamaeleonidae", children=[CHAMAELEO])
AGAMIDAE = Family(name="Agamidae", children=[AMPHIBOLURINAE, DRACONINAE])
IGUANIDAE = Family(name="Iguanidae", children=[IGUANA])
DACTYLOIDAE = Family(name="Dactyloidae", children=[ANOLIS])

ACRODONTA = Clade(name="Acrodonta", children=[CHAMAELEONIDAE, AGAMIDAE])
PLEURODONTA = Clade(name="Pleurodonta", children=[IGUANIDAE, DACTYLOIDAE])

IGUANIA = Suborder(name="Iguania", children=[ACRODONTA, PLEURODONTA])
