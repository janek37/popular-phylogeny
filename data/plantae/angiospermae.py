from clade import Clade, Family, Genus, Order, Phylum, Species
from constants import EN, IMAGE, PL
from image import Image, License

from .eudicots import EUDICOTYLEDONES
from .monocots import MONOCOTYLEDONES

# based on APG IV

N_ALBA = Species(
    name="Nymphaea alba",
    local_names={
        EN: "European white water lily, white nenuphar",
        PL: "lilia wodna, nenufar, grzybiebie białe",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nymphaea_alba_in_Duisburg.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Nymphaea_alba_in_Duisburg.jpg",
        author="DerHexer",
        license=License.CC_BY_SA_3_0,
    ),
)
I_VERUM = Species(
    name="Illicium verum",
    local_names={EN: "star anise", PL: "anyż gwiaździsty, badian właściwy"},
    known_for=[
        {
            EN: "spice",
            PL: "roślina przyprawowa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Illicium_verum20170511_7552.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Illicium_verum20170511_7552.jpg",
                author="Bff",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {EN: "drug precursor (Tamiflu)", PL: "roślina lecznicza (Tamiflu)"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Illicium_verum_4zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Illicium_verum_4zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
M_VIRGINIANA = Species(
    name="Magnolia virginiana",
    local_names={EN: "sweetbay magnolia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Magnolia_virginiana.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Magnolia_virginiana.jpg",
        author="J E Theriot from houston, usa",
        license=License.CC_BY_2_0,
    ),
)
L_TULIPIFERA = Species(
    name="Liriodendron tulipifera",
    local_names={EN: "American tulip tree", PL: "tulipanowiec amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Liriodendron_tulipifera_(9443532577).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c8/Liriodendron_tulipifera_%289443532577%29.jpg",
        author="Virginia State Parks staff",
        license=License.CC_BY_2_0,
    ),
)
M_FRAGRANS = Species(
    name="Myristica fragrans",
    known_for=[
        {
            PL: "gałka muszkatołowa",
            EN: "nutmeg",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Myristica_Fragrans.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Myristica_Fragrans.jpg",
                author="Herusutimbul",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {PL: "kwiat muszkatołowy, macis", EN: "mace"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myristica_fragrans_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-097.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Myristica_fragrans_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-097.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
L_NOBILIS = Species(
    name="Laurus nobilis",
    local_names={EN: "laurel", PL: "wawrzyn szlachetny"},
    known_for=[
        {EN: "bay leaf", PL: "liść laurowy"},
        {EN: "laurel wreath", PL: "wieniec laurowy"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Laurus_nobilis_(K%C3%B6hler).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Laurus_nobilis_%28K%C3%B6hler%29.jpg",
        author="Franz Eugen Köhler & Walther Müller",
        license=License.CC_BY_2_5,
    ),
)
C_VERUM = Species(
    name="Cinnamomum verum",
    known_for=[
        {
            EN: "cinnamon",
            PL: "cynamon",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cinnamomum_verum_spices.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/de/Cinnamomum_verum_spices.jpg",
                author="Simon A. Eugster",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cinnamomum_verum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-182.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Cinnamomum_verum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-182.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_CAMPHORA = Species(
    name="Cinnamomum camphora",
    known_for=[
        {
            EN: "camphor",
            PL: "kamfora",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Alcanfor-2D.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/4e/Alcanfor-2D.svg",
                author="Manuel Almagro Rivas",
                license=License.CC_BY_SA_4_0,  # should be PD CHEM?
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cinnamomum_camphora_(K%C3%B6hler).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Cinnamomum_camphora_%28K%C3%B6hler%29.jpg",
        author="Hermann Adolf Köhler (1834 - 1879)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_AMERICANA = Species(
    name="Persea americana",
    local_names={
        EN: "avocado",
        PL: "awokado",
    },
    known_for=[
        {
            EN: "edible fruit",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Persea_americana_from_Canadian_supermarket.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Persea_americana_from_Canadian_supermarket.jpg",
                author="Wilfredor",
                license=License.CC0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Persea_americana_(Avocado)_tree_in_RDA,_Bogra_05.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Persea_americana_%28Avocado%29_tree_in_RDA%2C_Bogra_05.jpg",
        author="Afifa Afrin",
        license=License.CC_BY_SA_3_0,
    ),
)
P_NIGRUM = Species(
    name="Piper nigrum",
    local_names={EN: "black pepper", PL: "pieprz czarny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Piper_nigrum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-107.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fd/Piper_nigrum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-107.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_METHYSTICUM = Species(
    name="Piper methysticum",
    local_names={EN: "kava", PL: "kava, pieprz metystynowy"},
    known_for=[{EN: "psychoactive properties"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr-091104-8927-Piper_methysticum-leaves_and_flower_spikes-Kahanu_Gardens_NTBG_Kaeleku_Hana-Maui_(24620712229).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Starr-091104-8927-Piper_methysticum-leaves_and_flower_spikes-Kahanu_Gardens_NTBG_Kaeleku_Hana-Maui_%2824620712229%29.jpg",
        author="Forest and Kim Starr",
        license=License.CC_BY_3_0_US,
    ),
)
# Schinus molle (rosids)

NYMPHAEA = Genus(name="Nymphaea", children=[N_ALBA])
ILLICIUM = Genus(name="Illicium", children=[I_VERUM])
MAGNOLIA = Genus(name="Magnolia", children=[M_VIRGINIANA])
LIRIODENDRON = Genus(name="Liriodendron", children=[L_TULIPIFERA])
MYRISTICA = Genus(name="Myristica", children=[M_FRAGRANS])
LAURUS = Genus(name="Laurus", children=[L_NOBILIS])
CINNAMOMUM = Genus(name="Cinnamomum", children=[C_VERUM, C_CAMPHORA])
PERSEA = Genus(name="Persea", children=[P_AMERICANA])
PIPER = Genus(name="Piper", children=[P_NIGRUM, P_METHYSTICUM])

# multiple sources, e.g.
# https://www.researchgate.net/publication/340412028_The_Litsea_genome_and_the_evolution_of_the_laurel_family
LAURUS_CINNAMOMUM = Clade(children=[LAURUS, CINNAMOMUM])

NYMPHAEACEAE = Family(name="Nymphaeaceae", children=[NYMPHAEA])
SCHISANDRACEAE = Family(name="Schisandraceae", children=[ILLICIUM])
MAGNOLIACEAE = Family(name="Magnoliaceae", children=[MAGNOLIA, LIRIODENDRON])
MYRISTICACEAE = Family(name="Myristicaceae", children=[MYRISTICA])
LAURACEAE = Family(name="Lauraceae", children=[LAURUS_CINNAMOMUM, PERSEA])
PIPERACEAE = Family(name="Piperaceae", children=[PIPER])

NYMPHAEALES = Order(name="Nymphaeales", children=[NYMPHAEACEAE])
AUSTROBAILEYALES = Order(name="Austrobaileyales", children=[SCHISANDRACEAE])
MAGNOLIALES = Order(name="Magnoliales", children=[MAGNOLIACEAE, MYRISTICACEAE])
LAURALES = Order(name="Laurales", children=[LAURACEAE])
PIPERALES = Order(name="Piperales", children=[PIPERACEAE])

MAGNOLIALES_LAURALES = Clade(children=[MAGNOLIALES, LAURALES])

MAGNOLIIDAE = Clade(name="Magnoliidae", children=[MAGNOLIALES_LAURALES, PIPERALES])

MONOCOTYLEDONES_EUDICOTYLEDONES = Clade(children=[MONOCOTYLEDONES, EUDICOTYLEDONES])

ANGIOSPERMAE_B = Clade(children=[MAGNOLIIDAE, MONOCOTYLEDONES_EUDICOTYLEDONES])

ANGIOSPERMAE_A = Clade(children=[AUSTROBAILEYALES, ANGIOSPERMAE_B])

ANGIOSPERMAE = Phylum(name="Angiospermae", children=[NYMPHAEALES, ANGIOSPERMAE_A])
