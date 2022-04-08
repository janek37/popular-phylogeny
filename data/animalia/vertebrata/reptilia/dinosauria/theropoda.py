from clade import Clade, Family, Genus, Species, Superfamily
from constants import EN, PL

from .avialae import AVIALAE

C_BAURI = Species(name="Coelophysis bauri", extinct=True)
D_WETHERILLI = Species(name="Dilophosaurus wetherilli", extinct=True)
C_SASTREI = Species(
    name="Carnotaurus sastrei",
    known_for=[{EN: "villains from the film Dinosaur"}],
    extinct=True,
)
C_NASICORNIS = Species(name="Ceratosaurus nasicornis", extinct=True)
S_AEGYPTIACUS = Species(name="Spinosaurus aegyptiacus", extinct=True)
B_WALKERI = Species(name="Baryonyx walkeri", extinct=True)
M_BUCKLANDII = Species(name="Megalosaurus bucklandii", extinct=True)
A_FRAGILIS = Species(name="Allosaurus fragilis", extinct=True)
T_REX = Species(
    name="Tyrannosaurus rex",
    local_names={EN: "T-Rex", PL: "tyranozaur rex"},
    extinct=True,
)
C_LONGIPES = Species(
    name="Compsognathus longipes",
    known_for=[{EN: "one of the smallest known (non-avialan) dinosaurs"}],
    extinct=True,
)
D_BREVITERTIUS = Species(
    name="Dromiceiomimus brevitertius",
    known_for=[{EN: "Ryan North's Dinosaur Comics"}],
    extinct=True,
)
D_ANTIRRHOPUS = Species(name="Deinonychus antirrhopus", extinct=True)
V_MONGOLIENSIS = Species(name="Velociraptor mongoliensis", extinct=True)
U_OSTROMMAYSI = Species(
    name="Utahraptor ostrommaysi",
    known_for=[{EN: "Ryan North's Dinosaur Comics"}],
    extinct=True,
)

COELOPHYSIS = Genus(name="Coelophysis", children=[C_BAURI])
DILOPHOSAURUS = Genus(name="Dilophosaurus", children=[D_WETHERILLI])
CARNOTAURUS = Genus(name="Carnotaurus", children=[C_SASTREI])
CERATOSAURUS = Genus(name="Ceratosaurus", children=[C_NASICORNIS])
SPINOSAURUS = Genus(name="Spinosaurus", children=[S_AEGYPTIACUS])
BARYONYX = Genus(name="Baryonyx", children=[B_WALKERI])
MEGALOSAURUS = Genus(name="Megalosaurus", children=[M_BUCKLANDII])
ALLOSAURUS = Genus(name="Allosaurus", children=[A_FRAGILIS])
TYRANNOSAURUS = Genus(name="Tyrannosaurus", children=[T_REX])
COMPSOGNATHUS = Genus(name="Compsognathus", children=[C_LONGIPES])
DROMICEIOMIMUS = Genus(name="Dromiceiomimus", children=[D_BREVITERTIUS])
DEINONYCHUS = Genus(name="Deinonychus", children=[D_ANTIRRHOPUS])
VELOCIRAPTOR = Genus(name="Velociraptor", children=[V_MONGOLIENSIS])
UTAHRAPTOR = Genus(name="Utahraptor", children=[U_OSTROMMAYSI])

COELOPHYSIDAE = Family(name="Coelophysidae", children=[COELOPHYSIS])
DILOPHOSAURIDAE = Family(name="Dilophosauridae", children=[DILOPHOSAURUS])
ABELISAURIDAE = Family(name="Abelisauridae", children=[CARNOTAURUS])
CERATOSAURIDAE = Family(name="Ceratosauridae", children=[CERATOSAURUS])
SPINOSAURIDAE = Family(name="Spinosauridae", children=[SPINOSAURUS, BARYONYX])
MEGALOSAURIDAE = Family(name="Megalosauridae", children=[MEGALOSAURUS])
ALLOSAURIDAE = Family(name="Allosauridae", children=[ALLOSAURUS])
TYRANNOSAURIDAE = Family(name="Tyrannosauridae", children=[TYRANNOSAURUS])
COMPSOGNATHIDAE = Family(name="Compsognathidae", children=[COMPSOGNATHUS])
ORNITHOMIMIDAE = Family(name="Ornithomimidae", children=[DROMICEIOMIMUS])
# unresolved
DROMAEOSAURIDAE = Family(
    name="Dromaeosauridae", children=[DEINONYCHUS, VELOCIRAPTOR, UTAHRAPTOR]
)

COELOPHYSOIDEA = Superfamily(name="Coelophysoidea", children=[COELOPHYSIDAE])
MEGALOSAUROIDEA = Superfamily(
    name="Megalosauroidea", children=[SPINOSAURIDAE, MEGALOSAURIDAE]
)
ALLOSAUROIDEA = Superfamily(name="Allosauroidea", children=[ALLOSAURIDAE])
TYRANNOSAUROIDEA = Superfamily(name="Tyrannosauroidea", children=[TYRANNOSAURIDAE])

CERATOSAURIA = Clade(name="Ceratosauria", children=[ABELISAURIDAE, CERATOSAURIDAE])
ORNITHOMIMOSAURIA = Clade(name="Ornithomimosauria", children=[ORNITHOMIMIDAE])

MANIRAPTORA = Clade(name="Maniraptora", children=[DROMAEOSAURIDAE, AVIALAE])
MANIRAPTORIFORMES = Clade(
    name="Maniraptoriformes", children=[ORNITHOMIMOSAURIA, MANIRAPTORA]
)
NEOCOELUROSAURIA = Clade(
    name="Neocoelurosauria", children=[COMPSOGNATHIDAE, MANIRAPTORIFORMES]
)
COELUROSAURIA = Clade(
    name="Coelurosauria", children=[TYRANNOSAUROIDEA, NEOCOELUROSAURIA]
)
AVETHEROPODA = Clade(name="Avetheropoda", children=[ALLOSAUROIDEA, COELUROSAURIA])
TETANURAE = Clade(name="Tetanurae", children=[MEGALOSAUROIDEA, AVETHEROPODA])
AVEROSTRA = Clade(name="Averostra", children=[CERATOSAURIA, TETANURAE])

THEROPODA_A = Clade(children=[DILOPHOSAURIDAE, AVEROSTRA])

THEROPODA = Clade(name="Theropoda", children=[COELOPHYSOIDEA, THEROPODA_A])
