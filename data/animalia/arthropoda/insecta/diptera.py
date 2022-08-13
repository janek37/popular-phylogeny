from clade import (
    Clade,
    Family,
    Genus,
    Infraorder,
    Order,
    Species,
    Subfamily,
    Suborder,
    Superfamily,
)
from constants import EN, PL
from image import Image, License

S_TRIFASCIATUM = Species(
    name="Simulium trifasciatum",
    known_for=[
        {EN: "one of many species of black flies", PL: "jeden z wielu gatunków meszek"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Simulium_trifasciatum_adult_(British_Entomology_by_John_Curtis-_765).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Simulium_trifasciatum_adult_%28British_Entomology_by_John_Curtis-_765%29.png",
        author="John Curtis’s British Entomology 1824–1840",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_VEXANS = Species(
    name="Aedes vexans",
    local_names={EN: "inland floodwater mosquito", PL: "doskwier pastwiskowy"},
    known_for=[{EN: "one of the most common mosquitos"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Inland_Floodwater_Mosquito_-_Aedes_vexans_%E2%99%82_(50046173648).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Inland_Floodwater_Mosquito_-_Aedes_vexans_%E2%99%82_%2850046173648%29.jpg",
        author="Christina Butler from Georgia, United States",
        license=License.CC_BY_2_0,
    ),
)
A_GAMBIAE = Species(
    name="Anopheles gambiae",
    known_for=[
        {
            EN: "one of the main malaria vectors in sub-Saharan Africa",
            PL: (
                "gatunek widliszka; "
                "jeden z głównych roznosicieli malarii w Afryce Subsaharyjskiej"
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Anopheles_gambiae_mosquito_feeding_1354.p_lores.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Anopheles_gambiae_mosquito_feeding_1354.p_lores.jpg",
        author="CDC/James Gathany",
        license=License.CDC,
    ),
)
T_RUTILUS = Species(
    name="Toxorhynchites rutilus",
    local_names={EN: "elephant mosquito, treehole predatory mosquito"},
    known_for=[{EN: "Jurassic Park"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Elephant_Mosquito_-_Toxorhynchites_rutilus_%E2%99%80_(31455665637).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/85/Elephant_Mosquito_-_Toxorhynchites_rutilus_%E2%99%80_%2831455665637%29.jpg",
        author="Christina Butler from Georgia, United States",
        license=License.CC_BY_2_0,
    ),
)
P_NEARCTICA = Species(
    name="Plecia nearctica",
    local_names={EN: "lovebug, honeymoon fly"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lovebugs_-_Plecia_nearctica,_Okaloacoochee_Slough_State_Forest,_Felda,_Florida.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Lovebugs_-_Plecia_nearctica%2C_Okaloacoochee_Slough_State_Forest%2C_Felda%2C_Florida.jpg",
        author="Judy Gallagher",
        license=License.CC_BY_2_0,
    ),
)
T_OLERACEA = Species(
    name="Tipula oleracea",
    local_names={EN: "marsh crane fly", PL: "komarnica warzywna, koziułka warzywna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tipula_oleracea_(3691508287).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Tipula_oleracea_%283691508287%29.jpg",
        author="Maximilian Paradiz from Merida, Mexico",
        license=License.CC_BY_2_0,
    ),
)
H_PLUVIALIS = Species(
    name="Haematopota pluvialis",
    local_names={EN: "common horse fly", PL: "mucha końska, jusznica deszczowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Haematopota_pluvialis_(Tabanidae)_(Common_Horse_Fly)_-_(imago),_Arnhem,_the_Netherlands_-_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/Haematopota_pluvialis_%28Tabanidae%29_%28Common_Horse_Fly%29_-_%28imago%29%2C_Arnhem%2C_the_Netherlands_-_2.jpg",
        author="B. Schoenmakers at waarneming.nl",
        license=License.CC_BY_3_0,
    ),
)
T_BOVINUS = Species(
    name="Tabanus bovinus",
    local_names={EN: "pale giant horse-fly", PL: "bąk bydlęcy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tabanus_bovinus_(44593523812).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Tabanus_bovinus_%2844593523812%29.jpg",
        author="Ben Sale from Stevenage, UK",
        license=License.CC_BY_2_0,
    ),
)
S_RIBESII = Species(
    name="Syrphus ribesii",
    local_names={EN: "common hoverfly", PL: "bzyg pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Syrphus_ribesii_04.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Syrphus_ribesii_04.JPG",
        author="AfroBrazilian",
        license=License.CC_BY_SA_4_0,
    ),
)
D_MELANOGASTER = Species(
    name="Drosophila melanogaster",
    local_names={EN: "fruit fly", PL: "muszka owocowa, wywilżna karłowata"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Drosophila_melanogaster_Proboscis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Drosophila_melanogaster_Proboscis.jpg",
        author="Sanjay Acharya",
        license=License.CC_BY_SA_4_0,
    ),
)
G_MORSITANS = Species(
    name="Glossina morsitans",
    local_names={EN: "tsetse fly", PL: "mucha tsetse"},
    known_for=[{EN: "African sleeping sickness", PL: "śpiączka afrykańska"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Glossina-morsitans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/be/Glossina-morsitans.jpg",
        author="Alan R Walker",
        license=License.CC_BY_SA_3_0,
    ),
)
M_DOMESTICA = Species(
    name="Musca domestica",
    local_names={EN: "house fly", PL: "mucha domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Musca_domestica_September_2007-1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Musca_domestica_September_2007-1.jpg",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)
L_SERICATA = Species(
    name="Lucilia sericata",
    local_names={EN: "common green bottle fly", PL: "mucha zielona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lucilia_sericata_8663.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Lucilia_sericata_8663.jpg",
        author="Amada44",
        license=License.CC_BY_SA_4_0,
    ),
)
C_VOMITORIA = Species(
    name="Calliphora vomitoria",
    local_names={EN: "blue bottle fly", PL: "mucha plujka, plujka burczało"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Calliphoridae_-_Calliphora_vomitoria.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Calliphoridae_-_Calliphora_vomitoria.JPG",
        author="Hectonichus",
        license=License.CC_BY_SA_4_0,
    ),
)
S_AFRICA = Species(
    name="Sarcophaga africa",
    known_for=[{EN: "the best known common flesh fly species"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fly_June_2009-4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/31/Fly_June_2009-4.jpg",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)
H_BOVIS = Species(
    name="Hypoderma bovis",
    local_names={EN: "ox warble fly, pale giant horse-fly", PL: "giez bydlęcy duży"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Giez_bydl%C4%99cy_du%C5%BCy,_giez_bydl%C4%99cy,_bydle%C5%84_(Tabanus_bovinus)_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7a/Giez_bydl%C4%99cy_du%C5%BCy%2C_giez_bydl%C4%99cy%2C_bydle%C5%84_%28Tabanus_bovinus%29_2.jpg",
        author="Iwona Kałuzińska",
        license=License.CC_BY_4_0,
    ),
)

SIMULIUM = Genus(name="Simulium", children=[S_TRIFASCIATUM])
AEDES = Genus(name="Aedes", children=[A_VEXANS])
ANOPHELES = Genus(name="Anopheles", children=[A_GAMBIAE])
TOXORHYNCHITES = Genus(name="Toxorhynchites", children=[T_RUTILUS])
PLECIA = Genus(name="Plecia", children=[P_NEARCTICA])
TIPULA = Genus(name="Tipula", children=[T_OLERACEA])
HAEMATOPOTA = Genus(name="Haematopota", children=[H_PLUVIALIS])
TABANUS = Genus(name="Tabanus", children=[T_BOVINUS])
SYRPHUS = Genus(name="Syrphus", children=[S_RIBESII])
DROSOPHILA = Genus(name="Drosophila", children=[D_MELANOGASTER])
GLOSSINA = Genus(name="Glossina", children=[G_MORSITANS])
MUSCA = Genus(name="Musca", children=[M_DOMESTICA])
LUCILLA = Genus(name="Lucilla", children=[L_SERICATA])
CALLIPHORA = Genus(name="Calliphora", children=[C_VOMITORIA])
SARCOPHAGA = Genus(name="Sarcophaga", children=[S_AFRICA])
HYPODERMA = Genus(name="Hypoderma", children=[H_BOVIS])

CULCINAE = Subfamily(name="Culcinae", children=[AEDES, TOXORHYNCHITES])
ANOPHELINAE = Subfamily(name="Anophelinae", children=[ANOPHELES])

SIMULIIDAE = Family(name="Simuliidae", children=[SIMULIUM])
CULICIDAE = Family(name="Culicidae", children=[CULCINAE, ANOPHELINAE])
BIBIONIDAE = Family(name="Bibionidae", children=[PLECIA])
TIPULIDAE = Family(name="Tipulidae", children=[TIPULA])
TABANIDAE = Family(name="Tabanidae", children=[HAEMATOPOTA, TABANUS])
SYRPHIDAE = Family(name="Syrphidae", children=[SYRPHUS])
DROSOPHILIDAE = Family(name="Drosophilidae", children=[DROSOPHILA])
GLOSSINIDAE = Family(name="Glossinidae", children=[GLOSSINA])
MUSCIDAE = Family(name="Muscidae", children=[MUSCA])
CALLIPHORIDAE = Family(name="Calliphoridae", children=[LUCILLA, CALLIPHORA])
SARCOPHAGIDAE = Family(name="Sarcophagidae", children=[SARCOPHAGA])
OESTRIDAE = Family(name="Oestridae", children=[HYPODERMA])

MUSCOIDEA = Superfamily(name="Muscoidea", children=[MUSCIDAE])
# unresolved
OESTROIDEA = Superfamily(
    name="Oestroidea", children=[CALLIPHORIDAE, SARCOPHAGIDAE, OESTRIDAE]
)

CALYPTRATAE_A = Clade(children=[MUSCOIDEA, OESTROIDEA])

ACALYPTRATAE = Clade(name="Acalyptratae", children=[DROSOPHILIDAE])  # Subsection
CALYPTRATAE = Clade(
    name="Calyptratae", children=[GLOSSINIDAE, CALYPTRATAE_A]
)  # Subsection

SCHIZOPHORA = Clade(name="Schizophora", children=[ACALYPTRATAE, CALYPTRATAE])  # Section

CULICOMORPHA = Infraorder(name="Culicomorpha", children=[SIMULIIDAE, CULICIDAE])
BIBIONOMORPHA = Infraorder(name="Bibionomorpha", children=[BIBIONIDAE])
MUSCOMORPHA = Infraorder(name="Muscomorpha", children=[SYRPHIDAE, SCHIZOPHORA])

BRACHYCERA = Suborder(name="Brachycera", children=[TABANIDAE, MUSCOMORPHA])

DIPTERA_B = Clade(children=[TIPULIDAE, BRACHYCERA])
DIPTERA_A = Clade(children=[BIBIONOMORPHA, DIPTERA_B])

DIPTERA = Order(name="Diptera", children=[CULICOMORPHA, DIPTERA_A])
