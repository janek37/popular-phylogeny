from clade import Clade, Family, Genus, Order, Species, Subgenus, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .asterids import ASTERIDS
from .caryophyllales import CARYOPHYLLALES
from .rosids import ROSIDS

R_ACRIS = Species(
    name="Ranunculus acris",
    local_names={EN: "meadow buttercup", PL: "jaskier ostry"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%E3%83%9F%E3%83%A4%E3%83%9E%E3%82%AD%E3%83%B3%E3%83%9D%E3%82%A6%E3%82%B2_Ranunculus_acris.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/00/%E3%83%9F%E3%83%A4%E3%83%9E%E3%82%AD%E3%83%B3%E3%83%9D%E3%82%A6%E3%82%B2_Ranunculus_acris.JPG",
        author="Alpsdake",
        license=License.CC_BY_SA_4_0,
    ),
)
P_RHOEAS = Species(
    name="Papaver rhoeas",
    local_names={EN: "common poppy", PL: "mak polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Papaver_rhoeas_in_Poland,_2020_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3c/Papaver_rhoeas_in_Poland%2C_2020_01.jpg",
        author="MichalPL",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SOMNIFERUM = Species(
    name="Papaver somniferum",
    local_names={EN: "opium poppy", PL: "mak lekarski"},
    known_for=[{EN: "opiates: morphine, codeine, heroin"}, {EN: "edible poppy seeds"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Papaver_somniferum_(2).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f7/Papaver_somniferum_%282%29.jpg",
        author="Linda Kenney from United Kingdom",
        license=License.CC_BY_SA_2_0,
    ),
)
A_NAPELLUS = Species(
    name="Aconitum napellus",
    local_names={EN: "wolfsbane", PL: "tojad mocny"},
    known_for=[{EN: "extremely poisonous"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aconitum_napellus_Palmstruch.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/19/Aconitum_napellus_Palmstruch.jpg",
        author="Johan Wilhelm Palmstruch (1770–1811)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
N_NUCIFERA = Species(
    name="Nelumbo nucifera",
    local_names={PL: "lotos orzechodajny", EN: "Indian lotus, sacred lotus"},
    known_for=[{EN: "trypohobia-triggering fruit"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sacred_lotus_Nelumbo_nucifera.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/Sacred_lotus_Nelumbo_nucifera.jpg",
        author="T.Voekler",
        license=License.CC_BY_SA_3_0,
    ),
)
M_INTEGRIFOLIA = Species(
    name="Macadamia integrifolia",
    local_names={
        PL: "makadamia",
        EN: "macadamia",
    },
    known_for=[
        {
            EN: "macadamia nuts",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Nuts_of_Macadamia_1152861.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Nuts_of_Macadamia_1152861.jpg",
                author="Wow Phochiangrak",
                license=License.CC0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_070112-3411_Macadamia_integrifolia.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Starr_070112-3411_Macadamia_integrifolia.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
P_ACERIFOLIA = Species(
    name="Platanus × acerifolia",
    local_names={PL: "platan klonolistny", EN: "London plane"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Platanus_%C3%97_acerifolia_-_Platan_kora_(7).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ae/Platanus_%C3%97_acerifolia_-_Platan_kora_%287%29.jpg",
        author="Synezis",
        license=License.CC_BY_SA_4_0,
    ),
)
P_OFFICINALIS = Species(
    name="Paeonia officinalis",
    local_names={EN: "common peony", PL: "peonia/piwonia lekarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paeonia_officinalis_Monte_Baldo_Orchi_152-1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cf/Paeonia_officinalis_Monte_Baldo_Orchi_152-1.jpg",
        author="Orchi",
        license=License.CC_BY_SA_3_0,
    ),
)
R_UVA_CRISPA = Species(
    name="Ribes uva-crispa",
    local_names={EN: "European gooseberry", PL: "agrest, porzeczka agrest"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ribes_uva-crispa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Ribes_uva-crispa.jpg",
        author="Tiia Monto",
        license=License.CC_BY_SA_4_0,
    ),
)
R_NIGRUM = Species(
    name="Ribes nigrum",
    local_names={EN: "blackcurrant", PL: "czarna porzeczka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ribes_nigrum_a1.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/05/Ribes_nigrum_a1.JPG",
        author="Jerzy Opioła",
        license=License.CC_BY_SA_3_0,
    ),
)
R_RUBRUM = Species(
    name="Ribes rubrum",
    local_names={EN: "redcurrant", PL: "czerwona porzeczka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ribes_rubrum_176116880.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/87/Ribes_rubrum_176116880.jpg",
        author="Zeke Marshall",
        license=License.CC0,
    ),
)
C_OVATA = Species(
    name="Crassula ovata",
    local_names={
        EN: "jade tree, money tree",
        PL: "drzewko szczęścia, grubosz jajowaty",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crassula_ovata_I.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/06/Crassula_ovata_I.jpg",
        author="Karl Thomas Moore",
        license=License.CC_BY_SA_4_0,
    ),
)
V_ALBUM = Species(
    name="Viscum album",
    local_names={EN: "European mistletoe", PL: "jemioła pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Viscum_album_mistel.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Viscum_album_mistel.jpg",
        author="Carl Axel Magnus Lindman",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_ALBUM = Species(
    name="Santalum album",
    local_names={EN: "Indian sandalwood", PL: "sandałowiec biały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Santalum_album_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-128.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e4/Santalum_album_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-128.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_VULGARIS = Species(
    name="Pulsatilla vulgaris",
    local_names={EN: "European pasqueflower", PL: "sasanka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gew%C3%B6hnliche_Kuhschelle_Pulsatilla_vulgaris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Gew%C3%B6hnliche_Kuhschelle_Pulsatilla_vulgaris.jpg",
        author="Holger Krisp",
        license=License.CC_BY_4_0,
    ),
)
A_CORONARIA = Species(
    name="Anemone coronaria",
    local_names={EN: "poppy anemone", PL: "zawilec wieńcowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anemone_coronaria_%27Hollandia%27_Zawilec_wie%C5%84cowaty_2019-08-25_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/98/Anemone_coronaria_%27Hollandia%27_Zawilec_wie%C5%84cowaty_2019-08-25_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
N_SATIVA = Species(
    name="Nigella sativa",
    local_names={
        EN: "black caraway, black cumin, kalonji, fennel flower",
        PL: "czarnuszka siewna",
    },
    known_for=[
        {
            EN: "black onion seeds",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Nigella_Sativa_Seed.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Nigella_Sativa_Seed.jpg",
                author="TheGoblin",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nigella_sativa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Nigella_sativa.jpg",
        author="k yamada from Yokohama, Japan",
        license=License.CC_BY_SA_2_0,
    ),
)
B_SEMPERVIRENS = Species(
    name="Buxus sempervirens",
    local_names={EN: "common box", PL: "bukszpan zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Buxus_sempervirens_%27Suffruticosa%27_2019-06-01_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/00/Buxus_sempervirens_%27Suffruticosa%27_2019-06-01_03.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)

RIBES_SUBGENUS_RIBES = Subgenus(name="Ribes subg. Ribes", children=[R_NIGRUM, R_RUBRUM])

RANUNCULUS = Genus(name="Ranunculus", children=[R_ACRIS])
PAPAVER = Genus(name="Papaver", children=[P_RHOEAS, P_SOMNIFERUM])
ACONITUM = Genus(name="Aconitum", children=[A_NAPELLUS])
NELUMBO = Genus(name="Nelumbo", children=[N_NUCIFERA])
MACADAMIA = Genus(name="Macadamia", children=[M_INTEGRIFOLIA])
PLATANUS = Genus(name="Platanus", children=[P_ACERIFOLIA])
PAEONIA = Genus(name="Paeonia", children=[P_OFFICINALIS])
RIBES = Genus(name="Ribes", children=[R_UVA_CRISPA, RIBES_SUBGENUS_RIBES])
CRASSULA = Genus(name="Crassula", children=[C_OVATA])
VISCUM = Genus(name="Viscum", children=[V_ALBUM])
SANTALUM = Genus(name="Santalum", children=[S_ALBUM])
PULSATILLA = Genus(name="Pulsatilla", children=[P_VULGARIS])
ANEMONE = Genus(name="Anemone", children=[A_CORONARIA])
NIGELLA = Genus(name="Nigella", children=[N_SATIVA])
BUXUS = Genus(name="Buxus", children=[B_SEMPERVIRENS])

RANUNCULEAE = Tribe(name="Ranunculeae", children=[RANUNCULUS])
DELPHINIEAE = Tribe(name="Delphinieae", children=[ACONITUM])
ANEMONEAE = Tribe(name="Anemoneae", children=[PULSATILLA, ANEMONE])
NIGELLEAE = Tribe(name="Nigelleae", children=[NIGELLA])

# https://www.researchgate.net/publication/339299453_Ranunculaceae_Phylogeny_Poster_RanPP_2020V3a
RANUNCULACEAE_A = Clade(children=[RANUNCULEAE, ANEMONEAE])
RANUNCULACEAE_B = Clade(children=[DELPHINIEAE, NIGELLEAE])

RANUNCULACEAE = Family(
    name="Ranunculaceae", children=[RANUNCULACEAE_A, RANUNCULACEAE_B]
)
PAPAVERACEAE = Family(name="Papaveraceae", children=[PAPAVER])
PAEONIACEAE = Family(name="Paeoniaceae", children=[PAEONIA])
GROSSULARIACEAE = Family(name="Grossulariaceae", children=[RIBES])
CRASSULACEAE = Family(name="Crassulaceae", children=[CRASSULA])
NELUMBONACEAE = Family(name="Nelumbonaceae", children=[NELUMBO])
PROTEACEAE = Family(name="Proteaceae", children=[MACADAMIA])
PLATANACEAE = Family(name="Platanaceae", children=[PLATANUS])
SANTALACEAE = Family(name="Santalaceae", children=[VISCUM, SANTALUM])
BUXACEAE = Family(name="Buxaceae", children=[BUXUS])

GROSSULARIACEAE_CRASSULACEAE = Clade(children=[GROSSULARIACEAE, CRASSULACEAE])
PLATANACEAE_PROTEACEAE = Clade(children=[PLATANACEAE, PROTEACEAE])

RANUNCULALES = Order(name="Ranunculales", children=[RANUNCULACEAE, PAPAVERACEAE])
PROTEALES = Order(name="Proteales", children=[NELUMBONACEAE, PLATANACEAE_PROTEACEAE])
SAXIFRAGALES = Order(
    name="Saxifragales", children=[PAEONIACEAE, GROSSULARIACEAE_CRASSULACEAE]
)
SANTALALES = Order(name="Santalales", children=[SANTALACEAE])
BUXALES = Order(name="Buxales", children=[BUXACEAE])

SUPERASTERIDS_A = Clade(children=[CARYOPHYLLALES, ASTERIDS])

SUPERROSIDS = Clade(name="superrosids", children=[SAXIFRAGALES, ROSIDS])
SUPERASTERIDS = Clade(name="superasterids", children=[SANTALALES, SUPERASTERIDS_A])

PENTAPETALAE = Clade(name="Pentapetalae", children=[SUPERROSIDS, SUPERASTERIDS])

EUDICOTYLEDONES_B = Clade(children=[BUXALES, PENTAPETALAE])
EUDICOTYLEDONES_A = Clade(children=[PROTEALES, EUDICOTYLEDONES_B])
EUDICOTYLEDONES = Clade(
    name="Eudicotyledones",
    local_names={EN: "eudicots", PL: "dwuliścienne"},
    children=[RANUNCULALES, EUDICOTYLEDONES_A],
)
