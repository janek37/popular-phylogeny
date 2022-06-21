from clade import Clade, Family, Genus, Infraclass, Order, Species
from constants import EN, PL
from image import Image, License

S_CAMELUS = Species(
    name="Struthio camelus",
    local_names={EN: "common ostrich", PL: "struś czerwonoskóry"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Masai_Mara_National_Reserve_17_-_common_ostrich_(Struthio_camelus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/Masai_Mara_National_Reserve_17_-_common_ostrich_%28Struthio_camelus%29.jpg",
        author="Thomas Fuhrmann",
        license=License.CC_BY_SA_4_0,
    ),
)
D_NOVAEZEALANDIAE = Species(
    name="Dinornis novaezealandiae",
    local_names={EN: "North Island giant moa"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dinornis_novaezealandiae.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Dinornis_novaezealandiae.png",
        author="Frederick William Frohawk (16 July 1861 - 10 December 1946), an English zoological artist and lepidopterist.",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_AUSTRALIS = Species(
    name="Apteryx australis",
    local_names={EN: "southern brown kiwi, tokoeka, common kiwi", PL: "kiwi brunatny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:The_genera_of_birds_(white_background).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/The_genera_of_birds_%28white_background%29.jpg",
        author="Gray, George Robert; Hullmandel & Walton; Hullmandel, Charles Joseph; Mitchell, D. W.",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_MAXIMUS = Species(
    name="Aepyornis maximus",
    local_names={
        EN: "giant elephant-bird",
        PL: "struś madagaskarski, epiornis, mamutak",
    },
    known_for=[{EN: "possible origin of the roc (rukh) myth"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aepyornis_white_background.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Aepyornis_white_background.jpg",
        author="Unknown author",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_CASUARIUS = Species(
    name="Casuarius casuarius",
    local_names={EN: "southern cassowary", PL: "kazuar hełmiasty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Casuarius_casuarius_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Casuarius_casuarius_2.jpg",
        author="Користувач:DoroshenkoE",
        license=License.PUBLIC_DOMAIN_USER,
    ),
)
D_NOVAEHOLLANDIAE = Species(
    name="Dromaius novaehollandiae",
    local_names={EN: "emu", PL: "emu zwyczajne"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dromaius_novaehollandiae_qtl1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0d/Dromaius_novaehollandiae_qtl1.jpg",
        author="Quartl",
        license=License.CC_BY_SA_3_0,
    ),
)

STRUTHIO = Genus(name="Struthio", children=[S_CAMELUS])
DINORNIS = Genus(name="Dinornis", children=[D_NOVAEZEALANDIAE])
APTERYX = Genus(name="Apteryx", children=[A_AUSTRALIS])
AEPYORNIS = Genus(name="Aepyornis", children=[A_MAXIMUS])
CASUARIUS = Genus(name="Casuarius", children=[C_CASUARIUS])
DROMAIUS = Genus(name="Dromaius", children=[D_NOVAEHOLLANDIAE])

STRUTHIONIDAE = Family(name="Struthionidae", children=[STRUTHIO])
DINORNITHIDAE = Family(name="Dinornithidae", children=[DINORNIS])
APTERYGIDAE = Family(name="Apterygidae", children=[APTERYX])
AEPYORNITHIDAE = Family(name="Aepyornithidae", children=[AEPYORNIS])
CASUARIIDAE = Family(name="Casuariidae", children=[CASUARIUS, DROMAIUS])

STRUTHIONIFORMES = Order(name="Struthioniformes", children=[STRUTHIONIDAE])
DINORNITHIFORMES = Order(name="Dinornithiformes", children=[DINORNITHIDAE])
APTERYGIFORMES = Order(name="Apterygiformes", children=[APTERYGIDAE])
AEPYORNITHIFORMES = Order(name="Aepyornithiformes", children=[AEPYORNITHIDAE])
CASUARIIFORMES = Order(name="Casuariiformes", children=[CASUARIIDAE])

NOVAERATITAE_A = Clade(children=[APTERYGIFORMES, AEPYORNITHIFORMES])
NOVAERATITAE = Clade(name="Novaeratitae", children=[NOVAERATITAE_A, CASUARIIFORMES])

NOTOPALAEOGNATHAE = Clade(
    name="Notopalaeognathae", children=[DINORNITHIFORMES, NOVAERATITAE]
)

PALAEOGNATHAE = Infraclass(
    name="Palaeognathae", children=[STRUTHIONIFORMES, NOTOPALAEOGNATHAE]
)
