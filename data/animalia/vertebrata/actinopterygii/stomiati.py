from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL

S_BOA = Species(name="Stomias boa", local_names={EN: "boa dragonfish", PL: "wężor"})
P_ALTIVELIS = Species(
    name="Plecoglossus altivelis", local_names={EN: "ayu, sweetfish", PL: "aju"}
)
O_EPERLANUS = Species(
    name="Osmerus eperlanus", local_names={EN: "European smelt", PL: "stynka"}
)
T_PACIFICUS = Species(
    name="Thaleichthys pacificus",
    local_names={EN: "eulachon, candlefish", PL: "olakon"},
)

STOMIAS = Genus(name="Stomias", children=[S_BOA])
PLECOGLOSSUS = Genus(name="Plecoglossus", children=[P_ALTIVELIS])
OSMERUS = Genus(name="Osmerus", children=[O_EPERLANUS])
THALEICHTHYS = Genus(name="Thaleichthys", children=[T_PACIFICUS])

STOMIIDAE = Family(name="Stomiidae", children=[STOMIAS])
PLECOGLOSSIDAE = Family(name="Plecoglossidae", children=[PLECOGLOSSUS])
OSMERIDAE = Family(name="Osmeridae", children=[OSMERUS, THALEICHTHYS])

STOMIIFORMES = Order(name="Stomiiformes", children=[STOMIIDAE])
OSMERIFORMES = Order(name="Osmeriformes", children=[PLECOGLOSSIDAE, OSMERIDAE])

STOMIATI = Clade(name="Stomiati", children=[STOMIIFORMES, OSMERIFORMES])
