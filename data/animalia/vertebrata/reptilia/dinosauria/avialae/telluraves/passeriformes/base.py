from clade import Clade, Family, Genus, Infraorder, Order, Species, Suborder
from constants import EN, PL
from image import Image, License

from .corvides import CORVIDES
from .muscicapida import MUSCICAPIDA
from .passerida import PASSERIDA
from .sylviida import SYLVIIDA

M_NOVAEHOLLANDIAE = Species(
    name="Menura novaehollandiae",
    local_names={EN: "superb lyrebird", PL: "lirogon wspaniały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Menura_superba_-_Thomas_Davies.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/04/Menura_superba_-_Thomas_Davies.jpg",
        author="Thomas Davies",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

MENURA = Genus(name="Menura", children=[M_NOVAEHOLLANDIAE])

MENURIDAE = Family(name="Menuridae", children=[MENURA])

PASSERIDES_A = Clade(children=[MUSCICAPIDA, PASSERIDA])

PASSERIDES = Infraorder(name="Passerides", children=[SYLVIIDA, PASSERIDES_A])

PASSERI_A = Clade(children=[CORVIDES, PASSERIDES])

PASSERI = Suborder(name="Passeri", children=[PASSERI_A, MENURIDAE])

PASSERIFORMES = Order(name="Passeriformes", children=[PASSERI])
