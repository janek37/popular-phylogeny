from clade import (
    Clade,
    Cohort,
    Family,
    Genus,
    Order,
    Species,
    Subcohort,
    Subfamily,
    Superorder,
)
from constants import EN, PL
from image import Image, License

from .cypriniformes import CYPRINIFORMES

# region CLUPEIFORMES
C_HARENGUS = Species(
    name="Clupea harengus",
    local_names={
        EN: "Atlantic herring",
        PL: "śledź pospolity, śledź atlantycki, śledź oceaniczny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Clupea_harengus_Gervais.flipped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Clupea_harengus_Gervais.flipped.jpg",
        author="Gervais et Boulart, 1877",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_PILCHARDUS = Species(
    name="Sardina pilchardus",
    local_names={EN: "European pilchard", PL: "sardynka europejska"},
    known_for=[{EN: "sardines"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sardina_pilchardus_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Sardina_pilchardus_Gervais.jpg",
        author="Gervais et Boulart, 1877",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_SPRATTUS = Species(
    name="Sprattus sprattus",
    local_names={EN: "European sprat", PL: "szprot, sardynka norweska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sprattus_sprattus_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1a/Sprattus_sprattus_Gervais.jpg",
        author="Gervais et Boulart, 1877",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_ENCRASICOLUS = Species(
    name="Engraulis encrasicolus",
    local_names={EN: "European anchovy", PL: "sardela europejska"},
    known_for=[{EN: "traditional pizza topping"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Engraulis_encrasicolus_Gervais_flipped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f0/Engraulis_encrasicolus_Gervais_flipped.jpg",
        author="Gervais et Boulart, 1877",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

CLUPEA = Genus(name="Clupea", children=[C_HARENGUS])
SARDINA = Genus(name="Sardina", children=[S_PILCHARDUS])
SPRATTUS = Genus(name="Sprattus", children=[S_SPRATTUS])
ENGRAULIS = Genus(name="Engraulis", children=[E_ENCRASICOLUS])

CLUPEINAE = Subfamily(name="Clupeinae", children=[CLUPEA, SPRATTUS])
ALOSINAE = Subfamily(name="Alosinae", children=[SARDINA])

CLUPEIDAE = Family(name="Clupeidae", children=[CLUPEINAE, ALOSINAE])
ENGRAULIDAE = Family(name="Engraulidae", children=[ENGRAULIS])

CLUPEIFORMES = Order(name="Clupeiformes", children=[CLUPEIDAE, ENGRAULIDAE])
# endregion CLUPEIFORMES

# region CHARACIFORMES
P_INNESI = Species(
    name="Paracheirodon innesi",
    local_names={EN: "neon tetra", PL: "bystrzyk neonowy, neon Innesa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paracheirodon_innesi_(aka).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Paracheirodon_innesi_%28aka%29.jpg",
        author="André Karwath aka Aka",
        license=License.CC_BY_SA_2_5,
    ),
)
P_NATTERERI = Species(
    name="Pygocentrus nattereri",
    local_names={
        EN: "red-bellied piranha, red piranha",
        PL: "pirania czarnoogonowa, pirania czerwona, pirania Natterera",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pygocentrus_nattereri_-_Karlsruhe_Zoo_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Pygocentrus_nattereri_-_Karlsruhe_Zoo_01.jpg",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)

PARACHEIRODON = Genus(name="Paracheirodon", children=[P_INNESI])
PYGOCENTRUS = Genus(name="Pygocentrus", children=[P_NATTERERI])

CHARACIDAE = Family(name="Characidae", children=[PARACHEIRODON])
SERRASALMIDAE = Family(name="Serrasalmidae", children=[PYGOCENTRUS])

CHARACIFORMES = Order(name="Characiformes", children=[CHARACIDAE, SERRASALMIDAE])
# endregion CHARACIFORMES

# region SILURIPHYSAE
A_ALBIFRONS = Species(
    name="Apteronotus albifrons",
    local_names={EN: "black ghost knifefish", PL: "duch brazylijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apteronotus_albifrons_Aquarium_tropical_du_Palais_de_la_Porte_Dor%C3%A9e_10_04_2016_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Apteronotus_albifrons_Aquarium_tropical_du_Palais_de_la_Porte_Dor%C3%A9e_10_04_2016_2.jpg",
        author="Vassil",
        license=License.CC0,
    ),
)
E_ELECTRICUS = Species(
    name="Electrophorus electricus",
    local_names={EN: "electric eel", PL: "węgorz elektryczny, strętwa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_38638_Gymnotus_electricus.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/FMIB_38638_Gymnotus_electricus.jpeg",
        author="Robert Hermann Schomburgk",
        license=License.FMIB,
    ),
)
P_HYPOPHTHALMUS = Species(
    name="Pangasianodon hypophthalmus",
    local_names={
        EN: "iridescent shark, iridescent shark catfish",
        PL: "panga, sum rekini",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Iridescent_Shark_Catfish.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Iridescent_Shark_Catfish.jpg",
        author="User:Lerdsuwa",
        license=License.CC_BY_SA_3_0,
    ),
)
S_GLANIS = Species(
    name="Silurus glanis",
    local_names={EN: "wels catfish, sheatfish", PL: "sum pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Silurus_glanis1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Silurus_glanis1.jpg",
        author="Krüger",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_NEBULOSUS = Species(
    name="Ameiurus nebulosus",
    local_names={EN: "brown bullhead", PL: "byczek, amerykański sumik karłowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ameiurus_nebulosus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Ameiurus_nebulosus.jpg",
        author="Noel Burkhead",
        license=License.CC_BY_SA_2_5,
    ),
)

APTERONOTUS = Genus(name="Apteronotus", children=[A_ALBIFRONS])
ELECTROPHORUS = Genus(name="Electrophorus", children=[E_ELECTRICUS])
PANGASIANODON = Genus(name="Pangasianodon", children=[P_HYPOPHTHALMUS])
SILURUS = Genus(name="Silurus", children=[S_GLANIS])
AMEIURUS = Genus(name="Ameiurus", children=[A_NEBULOSUS])

APTERONOTIDAE = Family(name="Apteronotidae", children=[APTERONOTUS])
GYMNOTIDAE = Family(name="Gymnotidae", children=[ELECTROPHORUS])
PANGASIIDAE = Family(name="Pangasiidae", children=[PANGASIANODON])
SILURIDAE = Family(name="Siluridae", children=[SILURUS])
ICTALURIDAE = Family(name="Ictaluridae", children=[AMEIURUS])

SILURIFORMES_A = Clade(children=[PANGASIIDAE, ICTALURIDAE])

GYMNOTIFORMES = Order(name="Gymnotiformes", children=[APTERONOTIDAE, GYMNOTIDAE])
SILURIFORMES = Order(name="Siluriformes", children=[SILURIFORMES_A, SILURIDAE])

SILURIPHYSAE = Superorder(name="Siluriphysae", children=[GYMNOTIFORMES, SILURIFORMES])
# endregion SILURIPHYSAE

OSTARIOPHYSI_A = Clade(children=[CHARACIFORMES, SILURIPHYSAE])
OSTARIOPHYSI = Subcohort(name="Ostariophysi", children=[CYPRINIFORMES, OSTARIOPHYSI_A])

OTOCEPHALA = Cohort(name="Otocephala", children=[CLUPEIFORMES, OSTARIOPHYSI])
