from clade import Clade, Family, Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL

L_ANGUSTIFOLIA = Species(
    name="Lavandula angustifolia",
    local_names={EN: "common lavender", PL: "lawenda wąskolistna"},
)
S_OFFICINALIS = Species(
    name="Salvia officinalis", local_names={EN: "common sage", PL: "szałwia lekarska"}
)
S_DIVINORUM = Species(
    name="Salvia divinorum",
    local_names={EN: "ska maría pastora, seer's sage", PL: "szałwia wieszcza"},
    known_for=[{EN: "psychoactive properties"}],
)
S_ROSMARINUS = Species(
    name="Salvia rosmarinus", local_names={EN: "rosemary", PL: "rozmaryn lekarski"}
)
S_HISPANICA = Species(
    name="Salvia hispanica", local_names={EN: "chia", PL: "chia, szałwia hiszpańska"}
)
M_SPICATA = Species(
    name="Mentha spicata", local_names={EN: "spearmint", PL: "mięta zielona"}
)
M_PIPERITA = Species(
    name="Mentha × piperita", local_names={EN: "peppermint", PL: "mięta pieprzowa"}
)
O_BASILICUM = Species(
    name="Ocimum basilicum", local_names={EN: "basil", PL: "bazylia pospolita"}
)
T_VULGARIS = Species(
    name="Thymus vulgaris", local_names={EN: "common thyme", PL: "macierzanka tymianek"}
)
N_CATARIA = Species(
    name="Nepeta cataria", local_names={EN: "catnip", PL: "kocimiętka właściwa"}
)
S_HORTENSIS = Species(
    name="Satureja hortensis", local_names={EN: "summer savory", PL: "cząber ogrodowy"}
)
O_VULGARE = Species(
    name="Origanum vulgare",
    local_names={EN: "oregano", PL: "oregano, lebiodka pospolita"},
)
O_MAJORANA = Species(
    name="Origanum majorana", local_names={EN: "marjoram", PL: "lemiodka majeranek"}
)
M_OFFICINALIS = Species(
    name="Melissa officinalis", local_names={EN: "lemon balm", PL: "melisa lekarska"}
)

SALVIA_SUBGENUS_SALVIA = Subgenus(name="Salvia subg. Salvia", children=[S_OFFICINALIS])
SALVIA_SUBGENUS_CALOSPHACE = Subgenus(
    name="Salvia subg. Calosphace", children=[S_DIVINORUM, S_HISPANICA]
)
SALVIA_SUBGENUS_ROSMARINUS = Subgenus(
    name="Salvia subg. Rosmarinus", children=[S_ROSMARINUS]
)

# https://www.researchgate.net/publication/343216227_Comparative_plastomic_analysis_and_insights_into_the_phylogeny_of_Salvia_Lamiaceae
SALVIA_A = Clade(children=[SALVIA_SUBGENUS_SALVIA, SALVIA_SUBGENUS_ROSMARINUS])

LAVANDULA = Genus(name="Lavandula", children=[L_ANGUSTIFOLIA])
SALVIA = Genus(name="Salvia", children=[SALVIA_A, SALVIA_SUBGENUS_CALOSPHACE])
MENTHA = Genus(name="Mentha", children=[M_SPICATA, M_PIPERITA])
OCIMUM = Genus(name="Ocimum", children=[O_BASILICUM])
THYMUS = Genus(name="Thymus", children=[T_VULGARIS])
NEPETA = Genus(name="Nepeta", children=[N_CATARIA])
SATUREJA = Genus(name="Satureja", children=[S_HORTENSIS])
ORIGANUM = Genus(name="Origanum", children=[O_VULGARE, O_MAJORANA])
MELISSA = Genus(name="Melissa", children=[M_OFFICINALIS])

# https://en.wikipedia.org/wiki/Lamiaceae
MENTHINAE_A = Clade(children=[MENTHA, SATUREJA])
MENTHINAE_B = Clade(children=[THYMUS, ORIGANUM])

SALVIINAE = Subtribe(name="Salviinae", children=[SALVIA, MELISSA])
MENTHINAE = Subtribe(name="Menthinae", children=[MENTHINAE_A, MENTHINAE_B])
NEPETINAE = Subtribe(name="Nepetinae", children=[NEPETA])

# https://www.nature.com/articles/s41598-017-02157-6
MENTHEAE_A = Clade(children=[MENTHINAE, NEPETINAE])

OCIMEAE = Tribe(name="Ocimeae", children=[LAVANDULA, OCIMUM])
MENTHEAE = Tribe(name="Mentheae", children=[SALVIINAE, MENTHEAE_A])

NEPETOIDEAE = Subfamily(name="Nepetoideae", children=[OCIMEAE, MENTHEAE])

LAMIACEAE = Family(name="Lamiaceae", children=[NEPETOIDEAE])
