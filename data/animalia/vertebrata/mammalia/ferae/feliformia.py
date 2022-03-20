from clade import Clade, Family, Genus, Species, Subfamily, Suborder, Superfamily
from constants import EN, PL

from .felidae import FELIDAE

H_HYAENA = Species(
    name="Hyaena hyaena", local_names={EN: "striped hyena", PL: "hiena pręgowana"}
)
C_CROCUTA = Species(
    name="Crocuta crocuta",
    local_names={
        EN: "spotted hyena, laughing hyena",
        PL: "hiena centkowana, krokuta cętkowana",
    },
    known_for=[{EN: "Shenzi, Banzai and Ed from The Lion King"}],
)
S_SURICATTA = Species(
    name="Suricata suricatta",
    local_names={EN: "meerkat, suricate", PL: "surykatka szara"},
    known_for=[{EN: "Timon from The Lion King"}],
)
U_EDWARDSII = Species(
    name="Urva edwardsii",
    local_names={EN: "Indian grey mongoose", PL: "mangusta indyjska"},
    known_for=[{EN: "Rikki-Tikki-Tavi"}],
)
C_FEROX = Species(
    name="Cryptoprocta ferox", local_names={EN: "fossa", PL: "fossa madagaskarska"}
)

HYAENA = Genus(name="Hyaena", children=[H_HYAENA])
CROCUTA = Genus(name="Crocuta", children=[C_CROCUTA])
SURICATA = Genus(name="Suricata", children=[S_SURICATTA])
URVA = Genus(name="Urva", children=[U_EDWARDSII])
CRYPTOPROCTA = Genus(name="Cryptoprocta", children=[C_FEROX])

HYAENINAE = Subfamily(name="Hyaeninae", children=[HYAENA, CROCUTA])

HYAENIDAE = Family(name="Hyaenidae", children=[HYAENINAE])
HERPESTIDAE = Family(name="Herpestidae", children=[SURICATA, URVA])
EUPLERIDAE = Family(name="Eupleridae", children=[CRYPTOPROCTA])

HERPESTOIDEA_A = Clade(children=[HERPESTIDAE, EUPLERIDAE])

HERPESTOIDEA = Superfamily(name="Herpestoidea", children=[HYAENIDAE, HERPESTOIDEA_A])

FELIFORMIA = Suborder(name="Feliformia", children=[HERPESTOIDEA, FELIDAE])
