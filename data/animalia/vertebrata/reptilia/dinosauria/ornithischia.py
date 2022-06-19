from clade import Clade, Family, Genus, Order, Species, Subfamily, Suborder
from image import Image, License

S_STENOPS = Species(
    name="Stegosaurus stenops",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202009_Stegosaurus_stenops.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/202009_Stegosaurus_stenops.png",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
A_MAGNIVENTRIS = Species(
    name="Ankylosaurus magniventris",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202007_Ankylosaurus_magniventris.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/202007_Ankylosaurus_magniventris.svg",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
P_ANDREWSI = Species(
    name="Protoceratops andrewsi",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Protoceratops_hellenikorhinus_Restoration.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Protoceratops_hellenikorhinus_Restoration.png",
        author="PaleoNeolitic",
        license=License.CC_BY_4_0,
    ),
)
T_HORRIDUS = Species(
    name="Triceratops horridus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Triceratops-000242.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/21/Triceratops-000242.jpg",
        author="Nobu Tamura, Derivative: MathKnight",
        license=License.CC_BY_SA_4_0,
    ),
)
S_ALBERTENSIS = Species(
    name="Styracosaurus albertensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Styracosaurus_BW_transparent.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Styracosaurus_BW_transparent.png",
        author="Nobu Tamura",
        license=License.CC_BY_SA_3_0,
    ),
)
I_BERNISSARTENSIS = Species(
    name="Iguanodon bernissartensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Iguanodon_new_NT.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Iguanodon_new_NT.jpg",
        author="Nobu Tamura",
        license=License.CC_BY_SA_4_0,
    ),
)
S_OSBORNI = Species(
    name="Saurolophus osborni",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Saurolophus_scalation.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Saurolophus_scalation.png",
        author="L. Xing and Y. Liu.",
        license=License.CC_BY_2_5,
    ),
)
P_WALKERI = Species(
    name="Parasaurolophus walkeri",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Parasaurolophus_walkeri.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Parasaurolophus_walkeri.png",
        author="Leandra Walters, Phil Senter, James H. Robins",
        license=License.CC_BY_2_5,
    ),
)
C_CASUARIUS = Species(
    name="Corythosaurus casuarius",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Corythosaurus_restoration_flipped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Corythosaurus_restoration_flipped.jpg",
        author="John Conway",
        license=License.CC_BY_SA_3_0,
    ),
)
P_WYOMINGENSIS = Species(
    name="Pachycephalosaurus wyomingensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202004_Pachycephalosaurus_wyomingensis.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/202004_Pachycephalosaurus_wyomingensis.png",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)

STEGOSAURUS = Genus(name="Stegosaurus", children=[S_STENOPS])
ANKYLOSAURUS = Genus(name="Ankylosaurus", children=[A_MAGNIVENTRIS])
PROTOCERATOPS = Genus(name="Protoceratops", children=[P_ANDREWSI])
TRICERATOPS = Genus(name="Triceratops", children=[T_HORRIDUS])
STYRACOSAURUS = Genus(name="Styracosaurus", children=[S_ALBERTENSIS])
IGUANODON = Genus(name="Iguanodon", children=[I_BERNISSARTENSIS])
SAUROLOPHUS = Genus(name="Saurolophus", children=[S_OSBORNI])
PARASAUROLOPHUS = Genus(name="Parasaurolophus", children=[P_WALKERI])
CORYTHOSAURUS = Genus(name="Corythosaurus", children=[C_CASUARIUS])
PACHYCEPHALOSAURUS = Genus(name="Pachycephalosaurus", children=[P_WYOMINGENSIS])

SAUROLOPHINAE = Subfamily(name="Saurolophinae", children=[SAUROLOPHUS])
LAMBEOSAURINAE = Subfamily(
    name="Lambeosaurinae", children=[PARASAUROLOPHUS, CORYTHOSAURUS]
)

STEGOSAURIDAE = Family(name="Stegosauridae", children=[STEGOSAURUS])
ANKYLOSAURIDAE = Family(name="Ankylosauridae", children=[ANKYLOSAURUS])
PROTOCERATOPSIDAE = Family(name="Protoceratopsidae", children=[PROTOCERATOPS])
CERATOPSIDAE = Family(name="Ceratopsidae", children=[TRICERATOPS, STYRACOSAURUS])
IGUANODONTIDAE = Family(name="Iguanodontidae", children=[IGUANODON])
HADROSAURIDAE = Family(name="Hadrosauridae", children=[SAUROLOPHINAE, LAMBEOSAURINAE])
PACHYCEPHALOSAURIDAE = Family(
    name="Pachycephalosauridae", children=[PACHYCEPHALOSAURUS]
)

STEGOSAURIA = Suborder(name="Stegosauria", children=[STEGOSAURIDAE])
ANKYLOSAURIA = Suborder(name="Ankylosauria", children=[ANKYLOSAURIDAE])
CERATOPSIA = Suborder(name="Ceratopsia", children=[PROTOCERATOPSIDAE, CERATOPSIDAE])
PACHYCEPHALOSAURIA = Suborder(
    name="Pachycephalosauria", children=[PACHYCEPHALOSAURIDAE]
)

ORNITHOPODA = Clade(name="Ornithopoda", children=[IGUANODONTIDAE, HADROSAURIDAE])
MARGINOCEPHALIA = Clade(
    name="Marginocephalia", children=[CERATOPSIA, PACHYCEPHALOSAURIA]
)

THYREOPHORA = Clade(name="Thyreophora", children=[STEGOSAURIA, ANKYLOSAURIA])
CERAPODA = Clade(name="Cerapoda", children=[MARGINOCEPHALIA, ORNITHOPODA])

ORNITHISCHIA = Order(name="Ornithischia", children=[THYREOPHORA, CERAPODA])
