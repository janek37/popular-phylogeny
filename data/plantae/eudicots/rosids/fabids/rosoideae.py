from clade import Clade, Genus, Species, Subfamily, Tribe
from constants import EN, PL
from image import Image, License

F_VESCA = Species(
    name="Fragaria vesca",
    local_names={EN: "wild strawberry", PL: "poziomka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%D0%97%D0%B5%D0%BC%D0%BB%D1%8F%D0%BD%D0%B8%D0%BA%D0%B0_%D0%BB%D0%B5%D1%81%D0%BD%D0%B0%D1%8F_(Fragaria_vesca)_f006.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/%D0%97%D0%B5%D0%BC%D0%BB%D1%8F%D0%BD%D0%B8%D0%BA%D0%B0_%D0%BB%D0%B5%D1%81%D0%BD%D0%B0%D1%8F_%28Fragaria_vesca%29_f006.jpg",
        author="Ural-66",
        license=License.CC_BY_SA_4_0,
    ),
)
F_ANANASSA = Species(
    name="Fragaria × ananassa",
    local_names={EN: "garden strawberry", PL: "poziomka truskawka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fruits_of_Fragaria_%C3%97_ananassa.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0c/Fruits_of_Fragaria_%C3%97_ananassa.JPG",
        author="Alpsdake",
        license=License.CC_BY_SA_3_0,
    ),
)
R_CANINA = Species(
    name="Rosa canina",
    local_names={EN: "dog rose", PL: "róża dzika"},
    known_for=[{EN: "jams", PL: "dżemy"}, {EN: "tea", PL: "herbata"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lago_Pudro_-_Rosa_canina_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Lago_Pudro_-_Rosa_canina_02.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
R_MISTER_LINCOLN = Species(
    name="Rosa 'Mister Lincoln'",
    known_for=[{EN: "one of the most popular red roses"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rosa_%27Mister_Lincoln%27_kz01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9a/Rosa_%27Mister_Lincoln%27_kz01.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
R_IDAEUS = Species(
    name="Rubus idaeus",
    local_names={EN: "red raspberry", PL: "malina właściwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20190803_Rubus_idaeus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/20190803_Rubus_idaeus.jpg",
        author="Kahvilokki",
        license=License.CC_BY_SA_4_0,
    ),
)
R_PLICATUS = Species(
    name="Rubus plicatus",
    local_names={EN: "European blackberry", PL: "jeżyna fałdowana"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rubus_plicatus_fruit_kz1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9b/Rubus_plicatus_fruit_kz1.jpg",
        author="Kenraiz",
        license=License.CC_BY_SA_3_0,
    ),
)
R_CAESIUS = Species(
    name="Rubus caesius",
    local_names={EN: "European dewberry", PL: "jeżyna popielica"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rubus_caesius_(43961725271).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/Rubus_caesius_%2843961725271%29.jpg",
        author="Björn S...",
        license=License.CC_BY_SA_2_0,
    ),
)

FRAGARIA = Genus(name="Fragaria", children=[F_VESCA, F_ANANASSA])
ROSA = Genus(name="Rosa", children=[R_CANINA, R_MISTER_LINCOLN])
RUBUS = Genus(name="Rubus", children=[R_IDAEUS, R_PLICATUS, R_CAESIUS])

POTENTILLEAE = Tribe(name="Potentilleae", children=[FRAGARIA])
ROSEAE = Tribe(name="Roseae", children=[ROSA])
RUBEAE = Tribe(name="Rubeae", children=[RUBUS])

ROSOIDEAE_A = Clade(children=[POTENTILLEAE, ROSEAE])
ROSOIDEAE = Subfamily(name="Rosoideae", children=[ROSOIDEAE_A, RUBEAE])
