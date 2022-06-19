from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

S_BOA = Species(
    name="Stomias boa",
    local_names={EN: "boa dragonfish", PL: "wężor"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Stomias_boa_boa_Gervais.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c8/Stomias_boa_boa_Gervais.jpg",
        author="Gervais et Boulart",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_ALTIVELIS = Species(
    name="Plecoglossus altivelis",
    local_names={EN: "ayu, sweetfish", PL: "aju"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sweetfish,_Plecoglossus_altivelis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/Sweetfish%2C_Plecoglossus_altivelis.jpg",
        author="OAS at Japanese Wikipedia",
        license=License.CC_BY_SA_3_0,
    ),
)
O_EPERLANUS = Species(
    name="Osmerus eperlanus",
    local_names={EN: "European smelt", PL: "stynka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_46340_Smelt.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a3/FMIB_46340_Smelt.jpeg",
        author="Jonathan Couch",
        license=License.FMIB,
    ),
)
T_PACIFICUS = Species(
    name="Thaleichthys pacificus",
    local_names={EN: "eulachon, candlefish", PL: "olakon"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_51092_Eulachon.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/FMIB_51092_Eulachon.jpeg",
        author="H. L. Todd",
        license=License.FMIB,
    ),
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
