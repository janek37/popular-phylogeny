from clade import Clade, Family, Genus, Parvorder, Species
from constants import EN, PL, URL
from image import Image, License

P_MAJOR = Species(
    name="Parus major",
    local_names={EN: "great tit", PL: "sikora bogatka, bogatka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Parus_major_poised.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Parus_major_poised.jpg",
        author="Francis Franklin",
        license=License.CC_BY_SA_4_0,
    ),
)
C_CAERULEUS = Species(
    name="Cyanistes caeruleus",
    local_names={EN: "Eurasian blue tit", PL: "sikora modra, modraszka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyanistes_Caeruleus_Oulu_20120303.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Cyanistes_Caeruleus_Oulu_20120303.JPG",
        author="Estormiz",
        license=License.CC0,
    ),
)
P_ATER = Species(
    name="Periparus ater",
    local_names={EN: "coal tit", PL: "sikora sosnówka, sosnówka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyprus_coal_tit_(Periparus_ater_cypriotes)_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Cyprus_coal_tit_%28Periparus_ater_cypriotes%29_2.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
P_PALUSTRIS = Species(
    name="Poecile palustris",
    local_names={EN: "marsh tit", PL: "sikora uboga"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Marsh_Tit_(Poecile_palustris)_(5).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4a/Marsh_Tit_%28Poecile_palustris%29_%285%29.jpg",
        author="Ken Billington",
        license=License.CC_BY_SA_3_0,
    ),
)
L_CRISTATUS = Species(
    name="Lophophanes cristatus",
    local_names={
        EN: "European crested tit",
        PL: "sikora czubatka, czubatka europejska",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crested_Tit_(Parus_cristatus)_(8521270202).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/57/Crested_Tit_%28Parus_cristatus%29_%288521270202%29.jpg",
        author="Ron Knight from Seaford, East Sussex, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)
B_BICOLOR = Species(
    name="Baeolophus bicolor",
    local_names={EN: "tufted titmouse", PL: "sikora dwubarwna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:TuftedTitmouse_Gam.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/TuftedTitmouse_Gam.jpg",
        author="MarshBunny",
        license=License.CC_BY_SA_4_0,
    ),
)
R_PENDULINUS = Species(
    name="Remiz pendulinus",
    local_names={EN: "Eurasian penduline tit", PL: "remiz zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eurasian_Penduline_Tit_(Remiz_pendulinus)_(14180503850).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Eurasian_Penduline_Tit_%28Remiz_pendulinus%29_%2814180503850%29.jpg",
        author="Ron Knight from Seaford, East Sussex, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)
A_ARVENSIS = Species(
    name="Alauda arvensis",
    local_names={EN: "Eurasian skylark", PL: "skowronek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Skylark_(Alauda_arvensis)_by_Neil_Smith.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Skylark_%28Alauda_arvensis%29_by_Neil_Smith.jpg",
        author="Neil Smith",
        license=License.CC_BY_SA_2_0,
    ),
)
E_ALPESTRIS = Species(
    name="Eremophila alpestris",
    local_names={EN: "horned lark, shore lark", PL: "górniczek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Horned_Lark_(Eremophila_alpestris)_(46821240104).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Horned_Lark_%28Eremophila_alpestris%29_%2846821240104%29.jpg",
        author="Imran Shah from Islamabad, Pakistan",
        license=License.CC_BY_SA_2_0,
    ),
)
G_CRISTATA = Species(
    name="Galerida cristata",
    local_names={EN: "crested lark", PL: "pośmieciuszka, dzierlatka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crested_lark_(Galerida_cristata_cristata)_Hungary.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Crested_lark_%28Galerida_cristata_cristata%29_Hungary.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
H_RUSTICA = Species(
    name="Hirundo rustica",
    local_names={EN: "barn swallow, European swallow", PL: "jaskółka dymówka, dymówka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hirundo_rustica_147461220.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Hirundo_rustica_147461220.jpg",
        author="Михаил Голомысов",
        license=License.CC_BY_4_0,
    ),
)
P_SPILODERA = Species(
    name="Petrochelidon spilodera",
    local_names={
        EN: "African swallow, South African cliff swallow",
        PL: "jaskółka towarzyska",
    },
    known_for=[
        {EN: "carrying coconuts", URL: "https://montypython.fandom.com/wiki/Swallow"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:South_African_cliff_swallow,_Petrochelidon_spilodera,_at_Suikerbosrand_Nature_Reserve,_Gauteng,_South_Africa_(22748291963).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/South_African_cliff_swallow%2C_Petrochelidon_spilodera%2C_at_Suikerbosrand_Nature_Reserve%2C_Gauteng%2C_South_Africa_%2822748291963%29.jpg",
        author="Derek Keats from Johannesburg, South Africa",
        license=License.CC_BY_2_0,
    ),
)
D_URBICUM = Species(
    name="Delichon urbicum",
    local_names={EN: "common house martin", PL: "jaskółka oknówka, oknówka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Northern_house_martin-_David_Raju.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Northern_house_martin-_David_Raju.jpg",
        author="Davidvraju",
        license=License.CC_BY_SA_4_0,
    ),
)
A_CAUDATUS = Species(
    name="Aegithalos caudatus",
    local_names={EN: "long-tailed tit, long-tailed bushtit", PL: "raniuszek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Long-tailed_tit_Gennevilliers_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/45/Long-tailed_tit_Gennevilliers_03.jpg",
        author="Alexis Lours",
        license=License.CC_BY_4_0,
    ),
)

PARUS = Genus(name="Parus", children=[P_MAJOR])
CYANISTES = Genus(name="Cyanistes", children=[C_CAERULEUS])
PERIPARUS = Genus(name="Periparus", children=[P_ATER])
POECILE = Genus(name="Poecile", children=[P_PALUSTRIS])
LOPHOPHANES = Genus(name="Lophophanes", children=[L_CRISTATUS])
BAEOLOPHUS = Genus(name="Baeolophus", children=[B_BICOLOR])
REMIZ = Genus(name="Remiz", children=[R_PENDULINUS])
ALAUDA = Genus(name="Alauda", children=[A_ARVENSIS])
EREMOPHILA = Genus(name="Eremophila", children=[E_ALPESTRIS])
GALERIDA = Genus(name="Galerida", children=[G_CRISTATA])
HIRUNDO = Genus(name="Hirundo", children=[H_RUSTICA])
PETROCHELIDON = Genus(name="Petrochelidon", children=[P_SPILODERA])
DELICHON = Genus(name="Delichon", children=[D_URBICUM])
AEGITHALOS = Genus(name="Aegithalos", children=[A_CAUDATUS])

PARIDAE_A = Clade(children=[PARUS, CYANISTES])
PARIDAE_B = Clade(children=[POECILE, LOPHOPHANES])
PARIDAE_C = Clade(children=[PARIDAE_B, BAEOLOPHUS])
PARIDAE_D = Clade(children=[PERIPARUS, PARIDAE_C])

# https://www.researchgate.net/publication/241692441_Multilocus_phylogeny_of_the_avian_family_Alaudidae_larks_reveals_complex_morphological_evolution_non-monophyletic_genera_and_hidden_species_diversity
ALAUDIDAE_A = Clade(children=[ALAUDA, GALERIDA])

# https://www.sciencedirect.com/science/article/abs/pii/S1055790304003501
# https://ars.els-cdn.com/content/image/1-s2.0-S1055790304003501-gr1.jpg
HIRUNDINIDAE_A = Clade(children=[PETROCHELIDON, DELICHON])

PARIDAE = Family(name="Paridae", children=[PARIDAE_A, PARIDAE_D])
REMIZIDAE = Family(name="Remizidae", children=[REMIZ])
ALAUDIDAE = Family(name="Alaudidae", children=[ALAUDIDAE_A, EREMOPHILA])
HIRUNDINIDAE = Family(name="Hirundinidae", children=[HIRUNDO, HIRUNDINIDAE_A])
AEGITHALIDAE = Family(name="Aegithalidae", children=[AEGITHALOS])

SYLVIIDA_A = Clade(children=[PARIDAE, REMIZIDAE])
SYLVIIDA_B = Clade(children=[HIRUNDINIDAE, AEGITHALIDAE])
SYLVIIDA_C = Clade(children=[ALAUDIDAE, SYLVIIDA_B])

SYLVIIDA = Parvorder(name="Sylviida", children=[SYLVIIDA_A, SYLVIIDA_C])
