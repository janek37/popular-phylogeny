from clade import Clade, Family, Genus, Species, Subtribe, Tribe
from constants import EN, PL

S_VULGARIS = Species(
    name="Syringa vulgaris", local_names={EN: "common lilac", PL: "lilak pospolity"}
)
O_EUROPAEA = Species(
    name="Olea europaea", local_names={EN: "olive", PL: "oliwka europejska"}
)
J_OFFICINALE = Species(
    name="Jasminum officinale",
    local_names={EN: "common jasmine", PL: "jaśmin lekarski"},
)
F_EXCELSIOR = Species(
    name="Fraxinus excelsior",
    local_names={EN: "European ash, common ash", PL: "jesion wyniosły"},
)
L_VULGARE = Species(
    name="Ligustrum vulgare",
    local_names={EN: "common privet", PL: "ligustr pospolity"},
    known_for=[{EN: "4 Privet Drive, home of Dursleys from Harry Potter"}],
)
F_INTERMEDIA = Species(
    name="Forsythia × intermedia",
    local_names={EN: "border forsythia", PL: "forsycja pośrednia"},
)

SYRINGA = Genus(name="Syringa", children=[S_VULGARIS])
LIGUSTRUM = Genus(name="Ligustrum", children=[L_VULGARE])
OLEA = Genus(name="Olea", children=[O_EUROPAEA])
JASMINUM = Genus(name="Jasminum", children=[J_OFFICINALE])
FRAXINUS = Genus(name="Fraxinus", children=[F_EXCELSIOR])
FORSYTHIA = Genus(name="Forsythia", children=[F_INTERMEDIA])

LIGUSTRINAE = Subtribe(name="Ligustrinae", children=[SYRINGA, LIGUSTRUM])
OLEINAE = Subtribe(name="Oleinae", children=[OLEA])
FRAXININAE = Subtribe(name="Fraxininae", children=[FRAXINUS])

# https://www.researchgate.net/publication/347381214_Resolving_the_Phylogeny_of_the_Olive_Family_Oleaceae_Confronting_Information_from_Organellar_and_Nuclear_Genomes
OLEEAE_A = Clade(children=[OLEINAE, FRAXININAE])

OLEEAE = Tribe(name="Oleeae", children=[LIGUSTRINAE, OLEEAE_A])
JASMINEAE = Tribe(name="Jasmineae", children=[JASMINUM])
FORSYTHIEAE = Tribe(name="Forsythieae", children=[FORSYTHIA])

# https://www.researchgate.net/publication/347381214_Resolving_the_Phylogeny_of_the_Olive_Family_Oleaceae_Confronting_Information_from_Organellar_and_Nuclear_Genomes
OLEACEAE_A = Clade(children=[OLEEAE, JASMINEAE])

OLEACEAE = Family(name="Oleaceae", children=[OLEACEAE_A, FORSYTHIEAE])
