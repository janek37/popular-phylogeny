from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily, Tribe
from constants import EN, PL

M_AURATUS = Species(
    name="Mesocricetus auratus",
    local_names={
        EN: "golden hamster, Syrian hamster",
        PL: "chomik syryjski, chomiczek syryjski",
    },
)
C_GLAREOLUS = Species(
    name="Clethrionomys glareolus", local_names={EN: "bank vole", PL: "nornica ruda"}
)
M_ARVALIS = Species(
    name="Microtus arvalis", local_names={EN: "common vole", PL: "nornik zwyczajny"}
)
L_LEMMUS = Species(
    name="Lemmus lemmus", local_names={EN: "Norway lemming", PL: "leming norweski"}
)
O_ZIBETHICUS = Species(
    name="Ondatra zibethicus", local_names={EN: "muskrat", PL: "piżmak amerykański"}
)
A_AMPHIBIUS = Species(
    name="Arvicola amphibius",
    local_names={EN: "water rat, European water vole", PL: "karczownik ziemnowodny"},
    known_for=[
        {EN: "Rat from The Wind in the Willows", PL: 'Szczur z "O czym szumią wierzby"'}
    ],
)
M_UNGUICULATUS = Species(
    name="Meriones unguiculatus",
    local_names={EN: "Mongolian gerbil", PL: "myszoskoczek mongolski, suwak mongolski"},
)
R_RATTUS = Species(
    name="Rattus rattus",
    local_names={EN: "black rat, roof rat, ship rat, house rat", PL: "szczur śniady"},
    known_for=[{EN: "Black Death"}],
)
R_NORVEGICUS = Species(
    name="Rattus norvegicus",
    local_names={
        EN: "common rat, street rat, sewer rat, brown rat",
        PL: "szczur wędrowny",
    },
    known_for=[{EN: "lab rat"}, {EN: "pet rat"}],
)
A_SYLVATICUS = Species(
    name="Apodemus sylvaticus", local_names={EN: "wood mouse", PL: "mysz zaroślowa"}
)
M_MUSCULUS = Species(
    name="Mus musculus",
    local_names={EN: "house mouse", PL: "mysz domowa"},
    known_for=[{EN: "lab mouse"}, {EN: "pet mouse"}],
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
