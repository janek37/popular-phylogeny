from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily, Tribe
from constants import EN, PL, URL
from image import Image, License

M_AURATUS = Species(
    name="Mesocricetus auratus",
    local_names={
        EN: "golden hamster, Syrian hamster",
        PL: "chomik syryjski, chomiczek syryjski",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Peach_the_pet_hamster.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Peach_the_pet_hamster.jpg",
        author="TetraHydroCannabinol",
        license=License.CC_BY_SA_3_0,
    ),
)
C_GLAREOLUS = Species(
    name="Clethrionomys glareolus",
    local_names={EN: "bank vole", PL: "nornica ruda"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bank_Vole_Myodes_glareolus_Grand_Union_Canal_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Bank_Vole_Myodes_glareolus_Grand_Union_Canal_1.jpg",
        author="AnemoneProjectors",
        license=License.CC_BY_SA_2_0,
    ),
)
M_ARVALIS = Species(
    name="Microtus arvalis",
    local_names={EN: "common vole", PL: "nornik zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Topillo1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Topillo1.jpg",
        author="José-Manuel Benito",
        license=License.CC_BY_SA_2_5,
    ),
)
L_LEMMUS = Species(
    name="Lemmus lemmus",
    local_names={EN: "Norway lemming", PL: "leming norweski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tunturisopuli_Lemmus_Lemmus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Tunturisopuli_Lemmus_Lemmus.jpg",
        author="Argus fin",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
O_ZIBETHICUS = Species(
    name="Ondatra zibethicus",
    local_names={EN: "muskrat", PL: "piżmak amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ondatra_zibethicus_FWS.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/27/Ondatra_zibethicus_FWS.jpg",
        author="David Menke",
        license=License.FWS,
    ),
)
A_AMPHIBIUS = Species(
    name="Arvicola amphibius",
    local_names={EN: "water rat, European water vole", PL: "karczownik ziemnowodny"},
    known_for=[
        {
            EN: "Rat from The Wind in the Willows",
            PL: 'Szczur z "O czym szumią wierzby"',
            URL: "https://en.wikipedia.org/wiki/The_Wind_in_the_Willows",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arvicola_amphibius.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/Arvicola_amphibius.jpg",
        author="Peter Trimming from Croydon, England",
        license=License.CC_BY_2_0,
    ),
)
M_UNGUICULATUS = Species(
    name="Meriones unguiculatus",
    local_names={EN: "Mongolian gerbil", PL: "myszoskoczek mongolski, suwak mongolski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Light_Red_Fox_Female_10-22-05.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5b/Light_Red_Fox_Female_10-22-05.jpg",
        author="Benmckune at en.wikipedia",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
R_RATTUS = Species(
    name="Rattus rattus",
    local_names={EN: "black rat, roof rat, ship rat, house rat", PL: "szczur śniady"},
    known_for=[{EN: "Black Death"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_10564_The_black_rat_Rattus_rattus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/CSIRO_ScienceImage_10564_The_black_rat_Rattus_rattus.jpg",
        author="division, CSIRO",
        license=License.CC_BY_3_0,
    ),
)
R_NORVEGICUS = Species(
    name="Rattus norvegicus",
    local_names={
        EN: "common rat, street rat, sewer rat, brown rat",
        PL: "szczur wędrowny",
    },
    known_for=[{EN: "lab rat"}, {EN: "pet rat"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rattus_norvegicus_(white_background).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/Rattus_norvegicus_%28white_background%29.png",
        author="Петроченко Віктор Іванович",
        license=License.CC_BY_SA_4_0,
    ),
)
A_SYLVATICUS = Species(
    name="Apodemus sylvaticus",
    local_names={EN: "wood mouse", PL: "mysz zaroślowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apodemus.sylvaticus.-.lindsey.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e3/Apodemus.sylvaticus.-.lindsey.jpg",
        author="James K. Lindsey",
        license=License.CC_BY_SA_2_5,
    ),
)
M_MUSCULUS = Species(
    name="Mus musculus",
    local_names={EN: "house mouse", PL: "mysz domowa"},
    known_for=[{EN: "lab mouse"}, {EN: "pet mouse"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mus_musculus_2254.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/49/Mus_musculus_2254.jpg",
        author="Amirekul",
        license=License.CC_BY_SA_4_0,
    ),
)

MESOCRICETUS = Genus(name="Mesocricetus", children=[M_AURATUS])
CLETHRIONOMYS = Genus(name="Clethrionomys", children=[C_GLAREOLUS])
MICROTUS = Genus(name="Microtus", children=[M_ARVALIS])
LEMMUS = Genus(name="Lemmus", children=[L_LEMMUS])
ONDATRA = Genus(name="Ondatra", children=[O_ZIBETHICUS])
ARVICOLA = Genus(name="Arvicola", children=[A_AMPHIBIUS])
MERIONES = Genus(name="Meriones", children=[M_UNGUICULATUS])
RATTUS = Genus(name="Rattus", children=[R_RATTUS, R_NORVEGICUS])
APODEMUS = Genus(name="Apodemus", children=[A_SYLVATICUS])
MUS = Genus(name="Mus", children=[M_MUSCULUS])

MYODINI = Tribe(name="Myodini", children=[CLETHRIONOMYS])
ARVICOLINI = Tribe(name="Arvicolini", children=[MICROTUS, ARVICOLA])
LEMMINI = Tribe(name="Lemmini", children=[LEMMUS])
ONDATRINI = Tribe(name="Ondatrini", children=[ONDATRA])

# https://www.researchgate.net/publication/225857808_Supraspecies_relationships_in_the_subfamily_Arvicolinae_Rodentia_Cricetidae_An_unexpected_result_of_nuclear_gene_analysis
ARVICOLINAE_A = Clade(children=[MYODINI, ARVICOLINI])
ARVICOLINAE_B = Clade(children=[ARVICOLINAE_A, LEMMINI])

# https://www.researchgate.net/publication/317386879_Masticatory_muscle_architecture_in_a_water-rat_from_Australasia_Murinae_Hydromys_and_its_implication_for_the_evolution_of_carnivory_in_rodents
MURINAE_A = Clade(children=[APODEMUS, MUS])

CRICETINAE = Subfamily(name="Cricetinae", children=[MESOCRICETUS])
ARVICOLINAE = Subfamily(name="Arvicolinae", children=[ARVICOLINAE_B, ONDATRINI])
GERBILLINAE = Subfamily(name="Gerbillinae", children=[MERIONES])
MURINAE = Subfamily(name="Murinae", children=[RATTUS, MURINAE_A])

CRICETIDAE = Family(name="Cricetidae", children=[CRICETINAE, ARVICOLINAE])
MURIDAE = Family(name="Muridae", children=[GERBILLINAE, MURINAE])

MUROIDEA = Superfamily(name="Muroidea", children=[CRICETIDAE, MURIDAE])

MYOMORPHA = Suborder(name="Myomorpha", children=[MUROIDEA])
