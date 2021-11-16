from clade import Clade, Species, Genus, Family, Order, Subfamily, Tribe
from constants import EN, PL
from .asparagales import ASPARAGALES
from .poales import POALES

A_CALAMUS = Species(name='Acorus calamus', local_names={EN: 'sweet flag', PL: 'tatarak zwyczajny'})
Z_MARINA = Species(
    name='Zostera marina',
    local_names={EN: 'eelgrass', PL: 'trawa morska, zostera morska'},
    known_for=[{EN: 'one of the most common species of seagrass'}],
)
L_MINOR = Species(name='Lemna minor', local_names={EN: 'common duckweed', PL: 'rzęsa drobna'})
L_CANDIDUM = Species(name='Lilium candidum', local_names={EN: 'Madonna lily', PL: 'lilia biała'})
L_LANCIFOLIUM = Species(
    name='Lilium lancifolium',
    local_names={EN: 'tiger lily', PL: 'lilia tygrysia'},
    known_for=[{EN: "chief's daughter in Peter Pan"}],
)
T_GESNERIANA = Species(name='Tulipa gesneriana', local_names={EN: 'garden tulip', PL: 'tulipan ogrodowy'})
C_NUCIFERA = Species(name='Cocos nucifera', local_names={EN: 'coconut palm', PL: 'palma kokosowa, kokos właściwy'})
E_GUINEENSIS = Species(
    name='Elaeis guineensis',
    local_names={EN: 'oil palm', PL: 'palma olejowa, olejowiec gwinejski'},
    known_for=[{EN: 'palm oil', PL: 'olej palmowy'}],
)
E_OLERACEA = Species(
    name='Euterpe oleracea',
    local_names={EN: 'açaí palm', PL: 'euterpa warzywna'},
    known_for=[{EN: 'açaí berries', PL: 'jagody açaí'}],
)
P_DACTYLIFERA = Species(
    name='Phoenix dactylifera',
    local_names={EN: 'date palm', PL: 'palma daktylowa, daktylowiec właściwy'},
)
A_MERRILLII = Species(
    name='Adonidia merrillii',
    local_names={EN: 'Manila palm, Christmas palm', PL: 'palma bożonarodzeniowa'},
    known_for=[{EN: 'commonly placed in hotels, casinos and shopping malls'}],
)
M_PARADISIACA = Species(name='Musa × paradisiaca', local_names={EN: 'banana', PL: 'banan zwyczajny'})
Z_OFFICINALE = Species(name='Zingiber officinale', local_names={EN: 'ginger', PL: 'imbir lekarski'})
E_CARDAMOMUM = Species(name='Elettaria cardamomum', local_names={EN: 'green cardamom', PL: 'kardamon malabarski'})

ACORUS = Genus(name='Acorus', children=[A_CALAMUS])
ZOSTERA = Genus(name='Zostera', children=[Z_MARINA])
LEMNA = Genus(name='Lemna', children=[L_MINOR])
LILIUM = Genus(name='Lilium', children=[L_CANDIDUM, L_LANCIFOLIUM])
TULIPA = Genus(name='Tulipa', children=[T_GESNERIANA])
COCOS = Genus(name='Cocos', children=[C_NUCIFERA])
ELAEIS = Genus(name='Elaeis', children=[E_GUINEENSIS])
EUTERPE = Genus(name='Euterpe', children=[E_OLERACEA])
PHOENIX = Genus(name='Phoenix', children=[P_DACTYLIFERA])
ADONIDIA = Genus(name='Adonidia', children=[A_MERRILLII])
MUSA = Genus(name='Genus', children=[M_PARADISIACA])
ZINGIBER = Genus(name='Zingiber', children=[Z_OFFICINALE])
ELETTARIA = Genus(name='Elettaria', children=[E_CARDAMOMUM])

COCOSEAE = Tribe(name='Cocoseae', children=[COCOS, ELAEIS])
EUTERPEAE = Tribe(name='Euterpeae', children=[EUTERPE])
PHOENICEAE = Tribe(name='Phoeniceae', children=[PHOENIX])
ARECAE = Tribe(name='Arecae', children=[ADONIDIA])

# https://www.researchgate.net/publication/44651559_Complete_Generic-Level_Phylogenetic_Analyses_of_Palms_Arecaceae_with_Comparisons_of_Supertree_and_Supermatrix_Approaches/figures
ARECOIDEAE_A = Clade(children=[EUTERPEAE, ARECAE])

ARECOIDEAE = Subfamily(name='Arecoideae', children=[COCOSEAE, ARECOIDEAE_A])
CORYPHOIDEAE = Subfamily(name='Coryphoideae', children=[PHOENICEAE])

ACORACEAE = Family(name='Acoraceae', children=[ACORUS])
ZOSTERACEAE = Family(name='Zosteraceae', children=[ZOSTERA])
ARACEAE = Family(name='Araceae', children=[LEMNA])
LILIACEAE = Family(name='Liliaceae', children=[LILIUM, TULIPA])
ARECACEAE = Family(name='Arecaceae', children=[ARECOIDEAE, CORYPHOIDEAE])
MUSACEAE = Family(name='Musaceae', children=[MUSA])
ZINGIBERACEAE = Family(name='Zingiberaceae', children=[ZINGIBER, ELETTARIA])

ACORALES = Order(name='Acorales', children=[ACORACEAE])
ALISMATALES = Order(name='Alismatales', children=[ZOSTERACEAE, ARACEAE])
LILIALES = Order(name='Liliales', children=[LILIACEAE])
ARECALES = Order(name='Arecales', children=[ARECACEAE])
ZINGIBERALES = Order(name='Zingiberales', children=[MUSACEAE, ZINGIBERACEAE])

ZINGIBERALES_POALES = Clade(children=[ZINGIBERALES, POALES])
COMMELINIDAE = Clade(name='commelinidae', children=[ARECALES, ZINGIBERALES_POALES])

ASPARAGALES_COMMELINIDS = Clade(children=[ASPARAGALES, COMMELINIDAE])
MONOCOTYLEDONES_B = Clade(children=[LILIALES, ASPARAGALES_COMMELINIDS])
MONOCOTYLEDONES_A = Clade(children=[ALISMATALES, MONOCOTYLEDONES_B])

MONOCOTYLEDONES = Clade(
    name='monocotyledones',
    local_names={EN: 'monocots', PL: 'jednoliścienne'},
    children=[ACORALES, MONOCOTYLEDONES_A],
)
