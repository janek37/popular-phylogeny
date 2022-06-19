from clade import Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL
from image import Image, License

P_LONGICEPS = Species(
    name="Pteranodon longiceps",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202009_Pteranodon_longiceps.svg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/202009_Pteranodon_longiceps.svg",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)
P_ANTIQUUS = Species(
    name="Pterodactylus antiquus",
    local_names={PL: "pterodaktyl"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pterodactylus_holotype_fly_mmartyniuk_white_background.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Pterodactylus_holotype_fly_mmartyniuk_white_background.png",
        author="Matthew P. Martyniuk",
        license=License.CC_BY_SA_4_0,
    ),
)
Q_NORTHROPI = Species(
    name="Quetzalcoatlus northropi",
    known_for=[{EN: "the largest known flying animal"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Quetzalcoatlus_by_johnson_mortimer-d9n2bd2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/Quetzalcoatlus_by_johnson_mortimer-d9n2bd2.jpg",
        author="Johnson Mortimer",
        license=License.CC_BY_3_0,
    ),
)

PTERANODON = Genus(name="Pteranodon", children=[P_LONGICEPS])
PTERODACTYLUS = Genus(name="Pterodactylus", children=[P_ANTIQUUS])
QUETZALCOATLUS = Genus(name="Quetzalcoatlus", children=[Q_NORTHROPI])

PTERANODONTIDAE = Family(name="Pteranodontidae", children=[PTERANODON])
AZHDARCHIDAE = Family(name="Azhdarchidae", children=[QUETZALCOATLUS])

EUPTERODACTYLOIDEA = Infraorder(
    name="Eupterodactyloidea", children=[PTERANODONTIDAE, AZHDARCHIDAE]
)

PTERODACTYLOIDEA = Suborder(
    name="Pterodactyloidea", children=[EUPTERODACTYLOIDEA, PTERODACTYLUS]
)

PTEROSAURIA = Order(name="Pterosauria", children=[PTERODACTYLOIDEA])
