from clade import Family, Genus, Species, Suborder
from constants import EN, PL

H_AMPHIBIUS = Species(
    name="Hippopotamus amphibius",
    local_names={EN: "hippo, common hippopotamus", PL: "hipopotam nilowy"},
)

HIPPOPOTAMUS = Genus(name="Hippopotamus", children=[H_AMPHIBIUS])

HIPPOPOTAMIDAE = Family(name="Hippopotamidae", children=[HIPPOPOTAMUS])

WHIPPOMORPHA = Suborder(name="Whippomorpha", children=[HIPPOPOTAMIDAE])
