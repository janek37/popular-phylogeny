from clade import Family, Genus, Species, Suborder
from constants import EN, PL
from image import Image, License

C_BACTRIANUS = Species(
    name="Camelus bactrianus",
    local_names={EN: "Bactrian camel", PL: "baktrian, wielbłąd dwugarbny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Camelus-bactrianus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Camelus-bactrianus.jpg",
        author="Chrumps",
        license=License.CC_BY_SA_4_0,
    ),
)
C_DROMEDARIUS = Species(
    name="Camelus dromedarius",
    local_names={EN: "dromedary, Arabian camel", PL: "dromader, wielbłąd jednogarbny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Em_-_Camelus_dromedarius_-_11.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Em_-_Camelus_dromedarius_-_11.jpg",
        author="Emőke Dénes",
        license=License.CC_BY_SA_4_0,
    ),
)
L_GLAMA = Species(
    name="Lama glama",
    local_names={EN: "llama", PL: "lama andyjska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Llama_(Lama_glama)_(19692833269).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Llama_%28Lama_glama%29_%2819692833269%29.jpg",
        author="Peter O'Connor aka anemoneprojectors",
        license=License.CC_BY_SA_2_0,
    ),
)
L_PACOS = Species(
    name="Lama pacos",
    local_names={EN: "alpaca", PL: "alpaka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Alpaca_in_Higashiyama_Zoo_-_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Alpaca_in_Higashiyama_Zoo_-_1.jpg",
        author="KKPCW",
        license=License.CC_BY_SA_4_0,
    ),
)

CAMELUS = Genus(name="Camelus", children=[C_BACTRIANUS, C_DROMEDARIUS])
LAMA = Genus(name="Lama", children=[L_GLAMA, L_PACOS])

CAMELIDAE = Family(name="Camelidae", children=[CAMELUS, LAMA])

TYLOPODA = Suborder(name="Tylopoda", children=[CAMELIDAE])
