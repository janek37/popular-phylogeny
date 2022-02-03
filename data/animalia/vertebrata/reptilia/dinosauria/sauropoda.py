from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN

B_EXCELSUS = Species(name="Brontosaurus excelsus")
A_AJAX = Species(name="Apatosaurus ajax")
D_LONGUS = Species(name="Diplodocus longus")
B_ALTITHORAX = Species(name="Brachiosaurus altithorax")
A_HUINCULENSIS = Species(
    name="Argentinosaurus huinculensis",
    known_for=[{EN: "probably the largest known land animal"}],
)

BRONTOSAURUS = Genus(name="Brontosaurus", children=[B_EXCELSUS])
APATOSAURUS = Genus(
    name="Apatosaurus",
    children=[A_AJAX],
    known_for=[{EN: "the Brontosaurus controversy"}],
)
DIPLODOCUS = Genus(name="Diplodocus", children=[D_LONGUS])
BRACHIOSAURUS = Genus(name="Brachiosaurus", children=[B_ALTITHORAX])
ARGENTINOSAURUS = Genus(name="Argentinosaurus", children=[A_HUINCULENSIS])

APATOSAURINAE = Subfamily(name="Apatosaurinae", children=[BRONTOSAURUS, APATOSAURUS])
DIPLODOCINAE = Superfamily(name="Diplodocinae", children=[DIPLODOCUS])

DIPLODOCIDAE = Family(name="Diplodocidae", children=[APATOSAURINAE, DIPLODOCINAE])
BRACHIOSAURIDAE = Family(name="Brachiosauridae", children=[BRACHIOSAURUS])

DIPLODOCOIDEA = Superfamily(name="Diplodocoidea", children=[DIPLODOCIDAE])

TITANOSAURIA = Clade(name="Titanosauria", children=[ARGENTINOSAURUS])

MACRONARIA = Clade(name="Macronaria", children=[BRACHIOSAURIDAE, TITANOSAURIA])

SAUROPODA = Clade(name="Sauropoda", children=[DIPLODOCOIDEA, MACRONARIA])
