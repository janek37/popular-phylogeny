from clade import Clade, Family, Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL
from image import Image, License

L_ANGUSTIFOLIA = Species(
    name="Lavandula angustifolia",
    local_names={EN: "common lavender", PL: "lawenda wąskolistna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lamiales_-_Lavandula_angustifolia_-_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Lamiales_-_Lavandula_angustifolia_-_4.jpg",
        author="Emőke Dénes",
        license=License.CC_BY_SA_4_0,
    ),
)
S_OFFICINALIS = Species(
    name="Salvia officinalis",
    local_names={EN: "common sage", PL: "szałwia lekarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salvia_officinalis0.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5a/Salvia_officinalis0.jpg",
        author="Kurt Stüber",
        license=License.CC_BY_SA_3_0,
    ),
)
S_DIVINORUM = Species(
    name="Salvia divinorum",
    local_names={EN: "ska maría pastora, seer's sage", PL: "szałwia wieszcza"},
    known_for=[{EN: "psychoactive properties"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salvia-divinorum-flickr.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Salvia-divinorum-flickr.jpg",
        author="epistis",
        license=License.CC_BY_SA_2_0,
    ),
)
S_ROSMARINUS = Species(
    name="Salvia rosmarinus",
    local_names={EN: "rosemary", PL: "rozmaryn lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rosmarinus_officinalis_(Lamiaceae)_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6b/Rosmarinus_officinalis_%28Lamiaceae%29_01.jpg",
        author="Filo gèn'",
        license=License.CC_BY_SA_4_0,
    ),
)
S_HISPANICA = Species(
    name="Salvia hispanica",
    local_names={EN: "chia", PL: "chia, szałwia hiszpańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salvia_hispanica_kz2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a8/Salvia_hispanica_kz2.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
M_SPICATA = Species(
    name="Mentha spicata",
    local_names={EN: "spearmint", PL: "mięta zielona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mint_leaves_(Mentha_spicata).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Mint_leaves_%28Mentha_spicata%29.jpg",
        author="Commonists",
        license=License.CC_BY_SA_4_0,
    ),
)
M_PIPERITA = Species(
    name="Mentha × piperita",
    local_names={EN: "peppermint", PL: "mięta pieprzowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mentha_x_pip.crispa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Mentha_x_pip.crispa.jpg",
        author="Georgfotoart",
        license=License.CC_BY_SA_4_0,
    ),
)
O_BASILICUM = Species(
    name="Ocimum basilicum",
    local_names={EN: "basil", PL: "bazylia pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sweet_Basil_(Ocimum_basilicum).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Sweet_Basil_%28Ocimum_basilicum%29.jpg",
        author="Mokkie",
        license=License.CC_BY_SA_3_0,
    ),
)
T_VULGARIS = Species(
    name="Thymus vulgaris",
    local_names={EN: "common thyme", PL: "macierzanka tymianek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Thymus_vulgaris_4zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Thymus_vulgaris_4zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
N_CATARIA = Species(
    name="Nepeta cataria",
    local_names={EN: "catnip", PL: "kocimiętka właściwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nepeta_cataria,_2021-07-04,_Bethel_Park,_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/Nepeta_cataria%2C_2021-07-04%2C_Bethel_Park%2C_01.jpg",
        author="Cbaile19",
        license=License.CC0,
    ),
)
S_HORTENSIS = Species(
    name="Satureja hortensis",
    local_names={EN: "summer savory", PL: "cząber ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gartenbohnenkraut_April_2012.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Gartenbohnenkraut_April_2012.JPG",
        author="4028mdk09",
        license=License.CC_BY_SA_3_0,
    ),
)
O_VULGARE = Species(
    name="Origanum vulgare",
    local_names={EN: "oregano", PL: "oregano, lebiodka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Origanum_vulgare_inflorescence_-_Keila.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/17/Origanum_vulgare_inflorescence_-_Keila.jpg",
        author="Ivar Leidus",
        license=License.CC_BY_SA_4_0,
    ),
)
O_MAJORANA = Species(
    name="Origanum majorana",
    local_names={EN: "marjoram", PL: "lebiodka majeranek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_070906-8859_Origanum_majorana.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Starr_070906-8859_Origanum_majorana.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
M_OFFICINALIS = Species(
    name="Melissa officinalis",
    local_names={EN: "lemon balm", PL: "melisa lekarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lemon_balm_4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Lemon_balm_4.jpg",
        author="Killarnee",
        license=License.CC_BY_SA_4_0,
    ),
)

SALVIA_SUBGENUS_SALVIA = Subgenus(name="Salvia subg. Salvia", children=[S_OFFICINALIS])
SALVIA_SUBGENUS_CALOSPHACE = Subgenus(
    name="Salvia subg. Calosphace", children=[S_DIVINORUM, S_HISPANICA]
)
SALVIA_SUBGENUS_ROSMARINUS = Subgenus(
    name="Salvia subg. Rosmarinus", children=[S_ROSMARINUS]
)

# https://www.researchgate.net/publication/343216227_Comparative_plastomic_analysis_and_insights_into_the_phylogeny_of_Salvia_Lamiaceae
SALVIA_A = Clade(children=[SALVIA_SUBGENUS_SALVIA, SALVIA_SUBGENUS_ROSMARINUS])

LAVANDULA = Genus(name="Lavandula", children=[L_ANGUSTIFOLIA])
SALVIA = Genus(name="Salvia", children=[SALVIA_A, SALVIA_SUBGENUS_CALOSPHACE])
MENTHA = Genus(name="Mentha", children=[M_SPICATA, M_PIPERITA])
OCIMUM = Genus(name="Ocimum", children=[O_BASILICUM])
THYMUS = Genus(name="Thymus", children=[T_VULGARIS])
NEPETA = Genus(name="Nepeta", children=[N_CATARIA])
SATUREJA = Genus(name="Satureja", children=[S_HORTENSIS])
ORIGANUM = Genus(name="Origanum", children=[O_VULGARE, O_MAJORANA])
MELISSA = Genus(name="Melissa", children=[M_OFFICINALIS])

# https://en.wikipedia.org/wiki/Lamiaceae
MENTHINAE_A = Clade(children=[MENTHA, SATUREJA])
MENTHINAE_B = Clade(children=[THYMUS, ORIGANUM])

SALVIINAE = Subtribe(name="Salviinae", children=[SALVIA, MELISSA])
MENTHINAE = Subtribe(name="Menthinae", children=[MENTHINAE_A, MENTHINAE_B])
NEPETINAE = Subtribe(name="Nepetinae", children=[NEPETA])

# https://www.nature.com/articles/s41598-017-02157-6
MENTHEAE_A = Clade(children=[MENTHINAE, NEPETINAE])

OCIMEAE = Tribe(name="Ocimeae", children=[LAVANDULA, OCIMUM])
MENTHEAE = Tribe(name="Mentheae", children=[SALVIINAE, MENTHEAE_A])

NEPETOIDEAE = Subfamily(name="Nepetoideae", children=[OCIMEAE, MENTHEAE])

LAMIACEAE = Family(name="Lamiaceae", children=[NEPETOIDEAE])
