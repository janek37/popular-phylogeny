from clade import Family, Genus, Order, Species
from constants import EN, PL, URL
from image import Image, License

from .asteraceae import ASTERACEAE

C_MEDIUM = Species(
    name="Campanula medium",
    local_names={EN: "Canterbury bells", PL: "dzwonek ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Campanulaceae_-_Campanula_medium-7.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Campanulaceae_-_Campanula_medium-7.JPG",
        author="Hectonichus",
        license=License.CC_BY_SA_3_0,
    ),
)
C_RAPUNCULUS = Species(
    name="Campanula rapunculus",
    local_names={EN: "rampion bellflower", PL: "dzwonek rapunkuł"},
    known_for=[{EN: "Rapunzel", URL: "https://en.wikipedia.org/wiki/Rapunzel"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Campanulaceae_-_Campanula_rapunculus-5.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Campanulaceae_-_Campanula_rapunculus-5.JPG",
        author="Hectonichus",
        license=License.CC_BY_SA_3_0,
    ),
)

CAMPANULA = Genus(name="Campanula", children=[C_MEDIUM, C_RAPUNCULUS])

CAMPANULACEAE = Family(name="Campanulaceae", children=[CAMPANULA])

ASTERALES = Order(name="Asterales", children=[CAMPANULACEAE, ASTERACEAE])
