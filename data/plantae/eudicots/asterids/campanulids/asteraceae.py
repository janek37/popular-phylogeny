from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .asteroideae import ASTEROIDEAE

G_JAMESONII = Species(
    name="Gerbera jamesonii",
    local_names={EN: "Barberton daisy", PL: "gerbera Jamesona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gerbera_jamesonii.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Gerbera_jamesonii.jpg",
        author="Adeep309",
        license=License.CC_BY_4_0,
    ),
)
C_INTYBUS = Species(
    name="Cichorium intybus",
    local_names={EN: "common chicory", PL: "cykoria podróżnik"},
    known_for=[
        {
            EN: "salad leaves",
            PL: "jadalne liście",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cichorium_intybus_convar_foliosum20120319_02.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Cichorium_intybus_convar_foliosum20120319_02.jpg",
                author="Bff",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {EN: "coffee substitute", PL: "kawa zbożowa"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cichorium_intybus-alvesgaspar1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Cichorium_intybus-alvesgaspar1.jpg",
        author="Alvesgaspar",
        license=License.CC_BY_SA_3_0,
    ),
)
L_SATIVA = Species(
    name="Lactuca sativa",
    local_names={EN: "lettuce", PL: "sałata siewna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cos_lettuce_2017_A2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/27/Cos_lettuce_2017_A2.jpg",
        author="Fructibus",
        license=License.CC0,
    ),
)
C_CARDUNCULUS = Species(
    name="Cynara cardunculus",
    local_names={EN: "globe artichoke", PL: "karczoch zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:De_Kruidhof_Buitenpost._Bloemknop_van_een_kardoen_(Cynara_cardunculus)._16-10-2021_(actm.).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7e/De_Kruidhof_Buitenpost._Bloemknop_van_een_kardoen_%28Cynara_cardunculus%29._16-10-2021_%28actm.%29.jpg",
        author="Agnes Monkelbaan",
        license=License.CC_BY_SA_4_0,
    ),
)
C_CYANUS = Species(
    name="Centaurea cyanus",
    local_names={EN: "cornflower", PL: "chaber bławatek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20140428Centaurea_cyanus1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/20140428Centaurea_cyanus1.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
C_ARVENSE = Species(
    name="Cirsium arvense",
    local_names={EN: "creeping thistle", PL: "oset, ostrożeń polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20200701Cirsium_arvense3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/20200701Cirsium_arvense3.jpg",
        author="David Rasp",
        license=License.CC_BY_4_0,
    ),
)
A_MINUS = Species(
    name="Arctium minus",
    local_names={EN: "lesser burdock", PL: "łopian mniejszy"},
    known_for=[{EN: "burrs", PL: "rzepy"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arctium_minus_corimbo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/33/Arctium_minus_corimbo.jpg",
        author="Alberto Salguero",
        license=License.CC_BY_SA_3_0,
    ),
)
T_OFFICINALE = Species(
    name="Taraxacum officinale",
    local_names={
        EN: "common dandelion",
        PL: "mlecz, dmuchawiec, mniszek lekarski, mniszek pospolity",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Taraxacum_officinale--.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/Taraxacum_officinale--.jpg",
        author="Elekes Andor",
        license=License.CC_BY_SA_4_0,
    ),
)

GERBERA = Genus(name="Gerbera", children=[G_JAMESONII])
CICHORIUM = Genus(name="Cichorium", children=[C_INTYBUS])
LACTUCA = Genus(name="Lactuca", children=[L_SATIVA])
CYNARA = Genus(name="Cynara", children=[C_CARDUNCULUS])
CENTAUREA = Genus(name="Centaurea", children=[C_CYANUS])
CIRSIUM = Genus(name="Cirsium", children=[C_ARVENSE])
ARCTIUM = Genus(name="Arctium", children=[A_MINUS])
TARAXACUM = Genus(name="Taraxacum", children=[T_OFFICINALE])

# http://tolweb.org/Carduinae/128563
CARDUINAE_A = Clade(children=[CYNARA, CIRSIUM])

CARDUINAE = Subtribe(name="Carduinae", children=[CARDUINAE_A, ARCTIUM])
CENTAUREINAE = Subtribe(name="Centaureinae", children=[CENTAUREA])
CREPIDINAE = Subtribe(name="Crepidinae", children=[TARAXACUM])

MUTISIEAE = Tribe(name="Mutisieae", children=[GERBERA])
CICHORIEAE = Tribe(
    name="Cichorieae", children=[CICHORIUM, LACTUCA, CREPIDINAE]
)  # unresolved
CYNAREAE = Tribe(name="Cynareae", children=[CARDUINAE, CENTAUREINAE])

MUTISIOIDEAE = Subfamily(name="Mutisioideae", children=[MUTISIEAE])
CICHORIOIDEAE = Subfamily(name="Cichorioideae", children=[CICHORIEAE])
CARDUOIDEAE = Subfamily(name="Carduoideae", children=[CYNAREAE])

ASTERACEAE_A = Clade(children=[ASTEROIDEAE, CICHORIOIDEAE])
ASTERACEAE_B = Clade(children=[ASTERACEAE_A, CARDUOIDEAE])

ASTERACEAE = Family(name="Asteraceae", children=[ASTERACEAE_B, MUTISIOIDEAE])
