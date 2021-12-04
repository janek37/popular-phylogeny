from clade import Clade, Family, Genus, Species, Subfamily, Subtribe, Tribe
from constants import EN, PL

from .asteroideae import ASTEROIDEAE

G_JAMESONII = Species(
    name="Gerbera jamesonii",
    local_names={EN: "Barberton daisy", PL: "gerbera Jamesona"},
)
C_INTYBUS = Species(
    name="Cichorium intybus",
    local_names={EN: "common chickory", PL: "cykoria podróżnik"},
    known_for=[
        {EN: "salad leaves", PL: "jadalne listki"},
        {EN: "coffee substitute", PL: "kawa zbożowa"},
    ],
)
L_SATIVA = Species(
    name="Lactuca sativa", local_names={EN: "lettuce", PL: "sałata siewna"}
)
C_CARDUNCULUS = Species(
    name="Cynara cardunculus",
    local_names={EN: "globe artichoke", PL: "karczoch zwyczajny"},
)
C_CYANUS = Species(
    name="Centaurea cyanus", local_names={EN: "cornflower", PL: "chaber bławatek"}
)
C_ARVENSE = Species(
    name="Cirsium arvense",
    local_names={EN: "creeping thistle", PL: "oset, ostrożeń polny"},
)
A_MINUS = Species(
    name="Arctium minus",
    local_names={EN: "lesser burdock", PL: "łopian mniejszy"},
    known_for=[{EN: "burrs", PL: "rzepy"}],
)
T_OFFICINALE = Species(
    name="Taraxacum officinale",
    local_names={
        EN: "common dandelion",
        PL: "mlecz, dmuchawiec, mniszek lekarski, mniszek pospolity",
    },
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
