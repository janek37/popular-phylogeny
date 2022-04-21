from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL
from image import Image, License

P_MONODON = Species(
    name="Penaeus monodon",
    local_names={EN: "giant tiger prawn", PL: "krewetka tygrysia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_2844_A_Prawn.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/13/CSIRO_ScienceImage_2844_A_Prawn.jpg",
        author="Marine Research, Commonwealth Scientific and Industrial Research Organisation",
        license=License.CC_BY_3_0,
    ),
)
L_VANNAMEI = Species(
    name="Litopenaeus vannamei",
    local_names={
        EN: "whiteleg shrimp, Pacific white shrimp, King prawn",
        PL: "krewetka biała",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Penaeus_vannamei_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Penaeus_vannamei_01.jpg",
        author="Agricultural Research Service",
        license=License.USDA,
    ),
)
S_HISPIDUS = Species(
    name="Stenopus hispidus",
    local_names={
        EN: "coral banded shrimp, banded cleaner shrimp",
        PL: "krewetka boksująca",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stenopus_hispidus_(46585256025).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Stenopus_hispidus_%2846585256025%29.jpg",
        author="LASZLO ILYES from Cleveland, Ohio, USA",
        license=License.CC_BY_2_0,
    ),
)
P_BOREALIS = Species(
    name="Pandalus borealis",
    local_names={EN: "northern shrimp, pink shrimp", PL: "krewetka północna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pandalus_borealis_Hakkeijima.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Pandalus_borealis_Hakkeijima.jpg",
        author="Totti",
        license=License.CC_BY_SA_4_0,
    ),
)
H_GAMMARUS = Species(
    name="Homarus gammarus",
    local_names={EN: "European lobster", PL: "homar europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Homarus_gammarus.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/Homarus_gammarus.JPG",
        author="Arnstein Rønning",
        license=License.CC_BY_3_0,
    ),
)
N_NORVEGICUS = Species(
    name="Nephrops norvegicus",
    local_names={EN: "Norway lobster, Dublin Bay prawn", PL: "homarzec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nephrops_norvegicus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Nephrops_norvegicus.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
P_ELEPHAS = Species(
    name="Palinurus elephas",
    local_names={EN: "European spiny lobster", PL: "langusta"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Monaco.Mus%C3%A9e_oc%C3%A9anographique089.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1f/Monaco.Mus%C3%A9e_oc%C3%A9anographique089.jpg",
        author="Georges Jansoone (JoJan)",
        license=License.CC_BY_3_0,
    ),
)
A_ASTACUS = Species(
    name="Astacus astacus",
    local_names={EN: "European crayfish", PL: "rak rzeczny, rak szlachetny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Astacus_astacus_male.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Astacus_astacus_male.jpg",
        author="Dragon187",
        license=License.CC_BY_SA_3_0,
    ),
)
P_BERNHARDUS = Species(
    name="Pagurus bernhardus",
    local_names={EN: "common hermit crab", PL: "pustelnik bernardyn"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pagurus_bernhardus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Pagurus_bernhardus.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
C_PAGURUS = Species(
    name="Cancer pagurus",
    local_names={EN: "edible/brown crab", PL: "krab kieszeniec"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cancer_pagurus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Cancer_pagurus.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_4_0,
    ),
)
M_MERCENARIA = Species(
    name="Menippe mercenaria",
    local_names={EN: "Florida stone crab"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_51200_Stone_Crab_(Male).jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/FMIB_51200_Stone_Crab_%28Male%29.jpeg",
        author="H. L. Todd",
        license=License.PUBLIC_DOMAIN,
    ),
)
C_SAPIDUS = Species(
    name="Callinectes sapidus",
    local_names={EN: "Atlantic blue crab", PL: "krab błękitny, kalinek błękitny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Callinectes_sapidus_(blue_crab)_(Cayo_Costa_Island,_Florida,_USA)_5.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/de/Callinectes_sapidus_%28blue_crab%29_%28Cayo_Costa_Island%2C_Florida%2C_USA%29_5.jpg",
        author="James St. John",
        license=License.CC_BY_2_0,
    ),
)
B_LATRO = Species(
    name="Birgus latro",
    local_names={
        EN: "coconut crab, robber crab, palm thief",
        PL: "krab kokosowy, krab palmowy",
    },
    known_for=[{EN: "the largest terrestrial arthropod"}, {EN: "Tamatoa from Moana"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crabe_cocotiers_Birgus_latro_(Linnaeus_1777).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/33/Crabe_cocotiers_Birgus_latro_%28Linnaeus_1777%29.jpg",
        author="Jebulon",
        license=License.CC0,
    ),
)

PENAEUS = Genus(name="Penaeus", children=[P_MONODON])
LITOPENAEUS = Genus(name="Litopenaeus", children=[L_VANNAMEI])
STENOPUS = Genus(name="Stenopus", children=[S_HISPIDUS])
PANDALUS = Genus(name="Pandalus", children=[P_BOREALIS])
HOMARUS = Genus(name="Homarus", children=[H_GAMMARUS])
NEPHROPS = Genus(name="Nephrops", children=[N_NORVEGICUS])
PAULINURUS = Genus(name="Paulinurus", children=[P_ELEPHAS])
ASTACUS = Genus(name="Astacus", children=[A_ASTACUS])
PAGURUS = Genus(name="Pagurus", children=[P_BERNHARDUS])
CANCER = Genus(name="Cancer", children=[C_PAGURUS])
MENIPPE = Genus(name="Menippe", children=[M_MERCENARIA])
CALLINECTES = Genus(name="Callinectes", children=[C_SAPIDUS])
BIRGUS = Genus(name="Birgus", children=[B_LATRO])

PENAEIDAE = Family(name="Penaeidae", children=[PENAEUS, LITOPENAEUS])
STENOPODIDAE = Family(name="Stenopodidae", children=[STENOPUS])
PANDALIDAE = Family(name="Pandalidae", children=[PANDALUS])
NEPHROPIDAE = Family(name="Nephropidae", children=[HOMARUS, NEPHROPS])
PALINURIDAE = Family(name="Palinuridae", children=[PAULINURUS])
ASTACIDAE = Family(name="Astacidae", children=[ASTACUS])
PAGURIDAE = Family(name="Paguridae", children=[PAGURUS])
CANCRIDAE = Family(name="Cancridae", children=[CANCER])
PORTUNIDAE = Family(name="Portunidae", children=[CALLINECTES])
COENOBITIDAE = Family(name="Coenobitidae", children=[BIRGUS])

HETEROTREMATA_A = Clade(
    children=[MENIPPE, PORTUNIDAE]
)  # Menippidae is not monophyletic
HETEROTREMATA = Clade(
    name="Heterotremata", children=[CANCRIDAE, HETEROTREMATA_A]
)  # Subsection

EUBRACHYURA = Clade(name="Eubrachyura", children=[HETEROTREMATA])  # Section

STENOPODIDEA = Infraorder(name="Stenopodidea", children=[STENOPODIDAE])
CARIDEA = Infraorder(name="Caridea", children=[PANDALIDAE])
ASTACIDEA = Infraorder(name="Astacidea", children=[NEPHROPIDAE, ASTACIDAE])
ACHELATA = Infraorder(name="Achelata", children=[PALINURIDAE])
ANOMURA = Infraorder(name="Anomura", children=[PAGURIDAE, COENOBITIDAE])
BRACHYURA = Infraorder(name="Brachyura", children=[EUBRACHYURA])

PLEOCYEMATA_A = Clade(children=[STENOPODIDEA, CARIDEA])
REPTANTIA_A = Clade(children=[ASTACIDEA, ACHELATA])
REPTANTIA_B = Clade(children=[ANOMURA, BRACHYURA])
REPTANTIA = Clade(name="Reptantia", children=[REPTANTIA_A, REPTANTIA_B])

DENDROBRANCHIATA = Suborder(name="Dendrobranchiata", children=[PENAEIDAE])
PLEOCYEMATA = Suborder(name="Pleocyemata", children=[PLEOCYEMATA_A, REPTANTIA])

DECAPODA = Order(name="Decapoda", children=[DENDROBRANCHIATA, PLEOCYEMATA])
