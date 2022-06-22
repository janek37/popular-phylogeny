from clade import Clade, Family, Genus, Parvorder, Species, Superfamily
from constants import EN, PL, URL
from image import Image, License

B_GARRULUS = Species(
    name="Bombycilla garrulus",
    local_names={EN: "Bohemian waxwing", PL: "jemiołuszka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bombycilla_garrulus,_Saint_Petersburg_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Bombycilla_garrulus%2C_Saint_Petersburg_2.jpg",
        author="Ekaterina Chernetsova (Papchinskaya) from Saint-Petersburg, Russia",
        license=License.CC_BY_2_0,
    ),
)
E_RUBECULA = Species(
    name="Erithacus rubecula",
    local_names={EN: "European robin", PL: "rudzik"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Erithacus_rubecula_with_cocked_head.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Erithacus_rubecula_with_cocked_head.jpg",
        author="Francis C. Franklin",
        license=License.CC_BY_SA_3_0,
    ),
)
L_MEGARHYNCHOS = Species(
    name="Luscinia megarhynchos",
    local_names={EN: "common nightingale", PL: "słowik rdzawy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Luscinia_megarhynchos_-_01_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Luscinia_megarhynchos_-_01_%28cropped%29.jpg",
        author="Carlos Delgado",
        license=License.CC_BY_SA_4_0,
    ),
)
S_SIALIS = Species(
    name="Sialia sialis",
    local_names={EN: "eastern bluebird", PL: "błękitnik rudogardły"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sialia_sialisPCCA20070128-0764B.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Sialia_sialisPCCA20070128-0764B.jpg",
        author="Patrick Coin (Patrick Coin)",
        license=License.CC_BY_SA_2_5,
    ),
)
T_PHILOMELOS = Species(
    name="Turdus philomelos",
    local_names={EN: "song thrush", PL: "drozd śpiewak"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Song_Thrush_-_Turdus_philomelos,_Adana_2017-02-15-5.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Song_Thrush_-_Turdus_philomelos%2C_Adana_2017-02-15-5.jpg",
        author="Zeynel Cebeci",
        license=License.CC_BY_SA_4_0,
    ),
)
T_MIGRATORIUS = Species(
    name="Turdus migratorius",
    local_names={EN: "American robin", PL: "drozd wędrowny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Turdus_migratorius_4494.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c9/Turdus_migratorius_4494.jpg",
        author="Dori",
        license=License.CC_BY_SA_3_0_US,
    ),
)
T_MERULA = Species(
    name="Turdus merula",
    local_names={EN: "common blackbird", PL: "kos"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Turdus_merula_114061772.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Turdus_merula_114061772.jpg",
        author="Stephen James McWilliam",
        license=License.CC_BY_4_0,
    ),
)
S_VULGARIS = Species(
    name="Sturnus vulgaris",
    local_names={EN: "common starling", PL: "szpak zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Toulouse_-_Sturnus_vulgaris_-_2012-02-26_-_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Toulouse_-_Sturnus_vulgaris_-_2012-02-26_-_2.jpg",
        author="PierreSelim",
        license=License.CC_BY_SA_3_0,
    ),
)
M_POLYGLOTTOS = Species(
    name="Mimus polyglottos",
    local_names={EN: "northern mockingbird", PL: "przedrzeźniacz północny"},
    known_for=[
        {
            EN: "To Kill a Mockingbird",
            URL: "https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mimus_polyglottos_adult_02_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Mimus_polyglottos_adult_02_cropped.jpg",
        author="Captain-tucker",
        license=License.CC_BY_SA_3_0,
    ),
)
R_REGULUS = Species(
    name="Regulus regulus",
    local_names={EN: "goldcrest", PL: "mysikrólik zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Regulus_regulus_60North_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Regulus_regulus_60North_cropped.jpg",
        author="Regulus_regulus_60North.jpg: Cj Hughson from Shetland; derivative work: Bogbumper (talk)",
        license=License.CC_BY_2_0,
    ),
)
S_EUROPAEA = Species(
    name="Sitta europaea",
    local_names={EN: "Eurasian nuthatch, wood nuthatch", PL: "kowalik zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kleiber_Sitta_europaea-0447.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Kleiber_Sitta_europaea-0447.jpg",
        author="Isiwal",
        license=License.CC_BY_SA_4_0,
    ),
)
T_TROGLODYTES = Species(
    name="Troglodytes troglodytes",
    local_names={EN: "Eurasian wren", PL: "strzyżyk zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Winter_Wren_(Troglodytes_troglodytes)_(48953636563).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/23/Winter_Wren_%28Troglodytes_troglodytes%29_%2848953636563%29.jpg",
        author="Imran Shah from Islamabad, Pakistan",
        license=License.CC_BY_SA_2_0,
    ),
)

# https://royalsocietypublishing.org/doi/10.1098/rspb.2019.2400
TURDUS_A = Clade(children=[T_MIGRATORIUS, T_MERULA])

BOMBYCILLA = Genus(name="Bombycilla", children=[B_GARRULUS])
ERITHACUS = Genus(name="Erithacus", children=[E_RUBECULA])
LUSCINIA = Genus(name="Luscinia", children=[L_MEGARHYNCHOS])
SIALIA = Genus(name="Sialia", children=[S_SIALIS])
TURDUS = Genus(name="Turdus", children=[T_PHILOMELOS, TURDUS_A])
STURNUS = Genus(name="Sturnus", children=[S_VULGARIS])
MIMUS = Genus(name="Mimus", children=[M_POLYGLOTTOS])
REGULUS = Genus(name="Regulus", children=[R_REGULUS])
SITTA = Genus(name="Sitta", children=[S_EUROPAEA])
TROGLODYTES = Genus(name="Troglodytes", children=[T_TROGLODYTES])

BOMBYCILLIDAE = Family(name="Bombycillidae", children=[BOMBYCILLA])
MUSCICAPIDAE = Family(name="Muscicapidae", children=[ERITHACUS, LUSCINIA])
TURDIDAE = Family(name="Turdidae", children=[SIALIA, TURDUS])
STURNIDAE = Family(name="Sturnidae", children=[STURNUS])
MIMIDAE = Family(name="Mimidae", children=[MIMUS])
REGULIDAE = Family(name="Regulidae", children=[REGULUS])
SITTIDAE = Family(name="Sittidae", children=[SITTA])
TROGLODYTIDAE = Family(name="Troglodytidae", children=[TROGLODYTES])

MUSCICAPOIDEA_A = Clade(children=[MUSCICAPIDAE, TURDIDAE])
MUSCICAPOIDEA_B = Clade(children=[STURNIDAE, MIMIDAE])

BOMBYCILLOIDEA = Superfamily(name="Bombycilloidea", children=[BOMBYCILLIDAE])
MUSCICAPOIDEA = Superfamily(
    name="Muscicapoidea", children=[MUSCICAPOIDEA_A, MUSCICAPOIDEA_B]
)
CERTHIOIDEA = Superfamily(name="Certhioidea", children=[SITTIDAE, TROGLODYTIDAE])

MUSCICAPIDA_A = Clade(children=[REGULIDAE, CERTHIOIDEA])
MUSCICAPIDA_B = Clade(children=[MUSCICAPOIDEA, MUSCICAPIDA_A])

MUSCICAPIDA = Parvorder(name="Muscicapida", children=[BOMBYCILLOIDEA, MUSCICAPIDA_B])
