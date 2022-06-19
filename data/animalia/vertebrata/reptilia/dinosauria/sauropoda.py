from clade import Clade, Family, Genus, Species, Subfamily, Superfamily
from constants import EN
from image import Image, License

B_EXCELSUS = Species(
    name="Brontosaurus excelsus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brontosaurus_by_Tom_Parker.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Brontosaurus_by_Tom_Parker.png",
        author="Tom Parker",
        license=License.CC_BY_SA_4_0,
    ),
)
A_LOUISAE = Species(
    name="Apatosaurus louisae",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apatosaurus_louisae_by_durbed.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Apatosaurus_louisae_by_durbed.jpg",
        author="Durbed",
        license=License.CC_BY_SA_3_0,
    ),
)
D_LONGUS = Species(
    name="Diplodocus longus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Diplodocus_longus(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f8/Diplodocus_longus%282%29.jpg",
        author="Dmitry Bogdanov",
        license=License.CC_BY_3_0,
    ),
)
B_ALTITHORAX = Species(
    name="Brachiosaurus altithorax",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brachiosaurus_DB.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Brachiosaurus_DB.jpg",
        author="Dmitry Bogdanov",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
A_HUINCULENSIS = Species(
    name="Argentinosaurus huinculensis",
    known_for=[{EN: "possibly the largest known land animal"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Argentinosaurus_BW.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Argentinosaurus_BW.jpg",
        author="Nobu Tamura",
        license=License.CC_BY_3_0,
    ),
)

BRONTOSAURUS = Genus(name="Brontosaurus", children=[B_EXCELSUS])
APATOSAURUS = Genus(
    name="Apatosaurus",
    children=[A_LOUISAE],
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
