from clade import Family, Genus, Species, Suborder
from constants import EN, PL, URL
from image import Image, License

S_DOMESTICUS = Species(
    name="Sus domesticus",
    local_names={EN: "domestic pig", PL: "świnia domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sus_scrofa_f._domestica.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/Sus_scrofa_f._domestica.jpg",
        author="Czeva",
        license=License.CC_BY_SA_3_0,
    ),
)
S_SCROFA = Species(
    name="Sus scrofa",
    local_names={EN: "wild boar", PL: "dzik euroazjatycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sus_scrofa,_Lodz,_Poland_(js)03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Sus_scrofa%2C_Lodz%2C_Poland_%28js%2903.jpg",
        author="Jerzystrzelecki",
        license=License.CC_BY_3_0,
    ),
)
P_AFRICANUS = Species(
    name="Phacochoerus africanus",
    local_names={EN: "common warthog", PL: "guziec zwyczajny"},
    known_for=[
        {EN: "Pumbaa from The Lion King", URL: "https://disney.fandom.com/wiki/Pumbaa"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Nolan_warthog_(Phacochoerus_africanus_africanus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Nolan_warthog_%28Phacochoerus_africanus_africanus%29.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)

SUS = Genus(name="Sus", children=[S_DOMESTICUS, S_SCROFA])
PHACOCHOERUS = Genus(name="Phacochoerus", children=[P_AFRICANUS])

SUIDAE = Family(name="Suidae", children=[SUS, PHACOCHOERUS])

SUINA = Suborder(name="Suina", children=[SUIDAE])
