from clade import Clade, Family, Genus, Order, Species, Subfamily, Superorder
from constants import EN, IMAGE, NAME, PL
from image import Image, License

E_LUCIUS = Species(
    name="Esox lucius",
    local_names={EN: "northern pike", PL: "szczupak pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Esox_lucius1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Esox_lucius1.jpg",
        author="Timothy Knepp",
        license=License.FWS,
    ),
)
S_SALAR = Species(
    name="Salmo salar",
    local_names={
        EN: "Atlantic salmon",
        PL: "łosoś pospolity, łosoś atlantycki, łosoś szlachetny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salmo_salar.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/39/Salmo_salar.jpg",
        author="Timothy Knepp",
        license=License.FWS,
    ),
)
S_TRUTTA = Species(
    name="Salmo trutta",
    local_names={EN: "brown trout"},
    known_for=[
        {
            NAME: "Salmo trutta trutta",
            EN: "sea trout",
            PL: "troć wędrowna, troć atlantycka",
        },
        {NAME: "Salmo trutta fario", EN: "river trout", PL: "pstrąg potokowy"},
        {NAME: "Salmo trutta lacustris", EN: "lake trout", PL: "troć jeziorowa"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bachforelle_Zeichnung.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/35/Bachforelle_Zeichnung.jpg",
        author="Duane Raver",
        license=License.FWS,
    ),
)
S_FONTINALIS = Species(
    name="Salvelinus fontinalis",
    local_names={EN: "brook trout", PL: "pstrąg źródlany"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brook_Trout_Salvelinus_fontinalis_2900px.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Brook_Trout_Salvelinus_fontinalis_2900px.jpg",
        author="Derek Ramsey",
        license=License.CC_BY_SA_2_5,
    ),
)
O_MYKISS = Species(
    name="Oncorhynchus mykiss",
    local_names={EN: "rainbow trout", PL: "tęczak, pstrąg tęczowy"},
    known_for=[
        {
            EN: "steelhead",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Steelhead_Oncorhynchus_mykiss.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/2b/Steelhead_Oncorhynchus_mykiss.jpg",
                author="A. Hoen and Co.",
                license=License.USPOSTAL,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trout.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Trout.jpg",
        author="Jonathunder",
        license=License.CC_BY_SA_3_0,
    ),
)
C_ALBULA = Species(
    name="Coregonus albula",
    local_names={EN: "vendace, European cisco", PL: "sielawa europejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coregonus_albula_(Pieni).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Coregonus_albula_%28Pieni%29.jpg",
        author='encyclopedia, "Pieni Tietosanakirja"',
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_ARTEDI = Species(
    name="Coregonus artedi",
    local_names={EN: "cisco, tullibee", PL: "sielawa amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cisco.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Cisco.jpg",
        author="Ellen Edmonson",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

ESOX = Genus(name="Esox", children=[E_LUCIUS])
SALMO = Genus(name="Salmo", children=[S_SALAR, S_TRUTTA])
SALVELINUS = Genus(name="Salvelinus", children=[S_FONTINALIS])
ONCORHYNCHUS = Genus(name="Oncorhynchus", children=[O_MYKISS])
COREGONUS = Genus(name="Coregonus", children=[C_ALBULA, C_ARTEDI])

SALMONINAE_A = Clade(children=[SALMO, SALVELINUS])

SALMONINAE = Subfamily(name="Salmoninae", children=[SALMONINAE_A, ONCORHYNCHUS])
COREGONINAE = Subfamily(name="Coregoninae", children=[COREGONUS])

ESOCIDAE = Family(name="Esocidae", children=[ESOX])
SALMONIDAE = Family(name="Salmonidae", children=[SALMONINAE, COREGONINAE])

ESOCIFORMES = Order(name="Esociformes", children=[ESOCIDAE])
SALMONIFORMES = Order(name="Salmoniformes", children=[SALMONIDAE])

PROTACANTHOPTERYGII = Superorder(
    name="Protacanthopterygii", children=[ESOCIFORMES, SALMONIFORMES]
)
