from clade import Clade, Family, Genus, Order, Species
from constants import EN, PL
from image import Image, License

C_CANIS = Species(
    name="Ctenocephalides canis",
    local_names={EN: "dog flea", PL: "pchła psia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CtenecephalusCanis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/CtenecephalusCanis.jpg",
        author="Herms, William Brodbeck (1876-1949)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_FELIS = Species(
    name="Ctenocephalides felis",
    local_names={EN: "cat flea", PL: "pchła kocia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:SIPH_Pulicidae_Ctenocephalides_felis_felis.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/SIPH_Pulicidae_Ctenocephalides_felis_felis.png",
        author="Desmond W. Helmore",
        license=License.CC_BY_4_0,
    ),
)
P_IRRITANS = Species(
    name="Pulex irritans",
    local_names={EN: "human flea", PL: "pchła ludzka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:PulexIrritans.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/PulexIrritans.jpg",
        author="Herms, William Brodbeck (1876-1949)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
X_CHEOPIS = Species(
    name="Xenopsylla cheopis",
    local_names={EN: "oriental rat flea", PL: "pchła szczurza"},
    known_for=[{EN: "a primary vector of bubonic plague"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:XenopsyllaCheopisHerms.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/XenopsyllaCheopisHerms.jpg",
        author="Herms, William Brodbeck (1876-1949)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

CTENOCEPHALIDES = Genus(name="Ctenocephalides", children=[C_CANIS, C_FELIS])
PULEX = Genus(name="Pulex", children=[P_IRRITANS])
XENOPSYLLA = Genus(name="Xenopsylla", children=[X_CHEOPIS])

# https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1096-0031.2008.00211.x
PULICIDAE_A = Clade(children=[CTENOCEPHALIDES, PULEX])

PULICIDAE = Family(name="Pulicidae", children=[PULICIDAE_A, XENOPSYLLA])

SIPHONAPTERA = Order(name="Siphonaptera", children=[PULICIDAE])
