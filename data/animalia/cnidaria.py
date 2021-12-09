from clade import Class, Family, Genus, Order, Phylum, Species, Subphylum
from constants import EN, PL

A_EQUINA = Species(
    name="Actinia equina", local_names={EN: "beadlet anemone", PL: "ukwiał koński"}
)
A_CERVICORNIS = Species(name="Acropora cervicornis", local_names={EN: "staghorn coral"})
H_VULGARIS = Species(
    name="Hydra vulgaris",
    local_names={EN: "fresh-water polyp", PL: "stułbia pospolita"},
)
C_FUSCESCENS = Species(
    name="Chrysaora fuscescens", local_names={EN: "Pacific sea nettle"}
)

ACTINIA = Genus(name="Actinia", children=[A_EQUINA])
ACROPORA = Genus(name="Acropora", children=[A_CERVICORNIS])
HYDRA = Genus(name="Hydra", children=[H_VULGARIS])
CHRYSAORA = Genus(
    name="Chrysaora",
    children=[C_FUSCESCENS],
    local_names={EN: "sea nettle", PL: "meduza kompasowa"},
)

ACTINIIDAE = Family(name="Actiniidae", children=[ACTINIA])
ACROPORIDAE = Family(name="Acroporidae", children=[ACROPORA])
HYDRIDAE = Family(name="Hydridae", children=[HYDRA])
PELAGIIDAE = Family(name="Pelagiidae", children=[CHRYSAORA])

ACTINIARIA = Order(name="Actiniaria", children=[ACTINIIDAE])
SCLERACTINIA = Order(name="Scleractinia", children=[ACROPORIDAE])
ANTHOATHECATA = Order(name="Anthoathecata", children=[HYDRIDAE])
SEMAEOSTOMEAE = Order(name="Semaeostomeae", children=[PELAGIIDAE])

ANTHOZOA = Class(name="Anthozoa", children=[ACTINIARIA, SCLERACTINIA])
HYDROZOA = Class(name="Hydrozoa", children=[ANTHOATHECATA])
SCYPHOZOA = Class(name="Scyphozoa", children=[SEMAEOSTOMEAE])

MEDUSOZOA = Subphylum(name="Medusozoa", children=[HYDROZOA, SCYPHOZOA])

CNIDARIA = Phylum(name="Cnidaria", children=[ANTHOZOA, MEDUSOZOA])
