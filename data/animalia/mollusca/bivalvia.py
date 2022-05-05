from clade import Clade, Class, Family, Genus, Order, Species, Subclass
from constants import EN, PL
from image import Image, License

M_MERCENARIA = Species(
    name="Mercenaria mercenaria",
    local_names={EN: "hard clam, quahog"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_51182_Quahaug_or_Little-necked_Clam,_Venus_mercenaria.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/FMIB_51182_Quahaug_or_Little-necked_Clam%2C_Venus_mercenaria.jpeg",
        author="Goode, George Brown (1884)",
        license=License.FMIB,
    ),
)
S_SOLIDISSIMA = Species(
    name="Spisula solidissima",
    local_names={EN: "Atlantic surf clam"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_38546_Surf_Clam_From_Life_Young_and_old_Annisquam,_Mass.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/FMIB_38546_Surf_Clam_From_Life_Young_and_old_Annisquam%2C_Mass.jpeg",
        author="Mayer, Alfred Goldsborough (1906)",
        license=License.FMIB,
    ),
)
T_GIGAS = Species(
    name="Tridacna gigas",
    local_names={EN: "giant clam", PL: "przydacznia olbrzymia"},
    known_for=[{EN: "the largest living bivalve", PL: "największe żyjące małże"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Giant_clam_or_Tridacna_gigas.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Giant_clam_or_Tridacna_gigas.jpg",
        author="Janderk",
        license=License.PUBLIC_DOMAIN,
    ),
)
C_EDULE = Species(
    name="Cerastoderma edule",
    local_names={EN: "common cockle", PL: "sercówka jadalna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:FMIB_48577_Cardium_edule_L.jpeg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/FMIB_48577_Cardium_edule_L.jpeg",
        author="Cooke, A. H .; Shipley, A. E .; Reed, F. R. C. (1895)",
        license=License.FMIB,
    ),
)
O_EDULIS = Species(
    name="Ostrea edulis",
    local_names={EN: "European flat oyster", PL: "ostryga jadalna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ostrea_edulis_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Ostrea_edulis_01.jpg",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
M_GIGAS = Species(
    name="Magallana gigas",
    local_names={EN: "Pacific oyster", PL: "ostryżyca japońska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Crassostrea_gigas_p1040847.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8c/Crassostrea_gigas_p1040847.jpg",
        author="David.Monniaux",
        license=License.CC_BY_SA_3_0,
    ),
)
C_VIRGINICA = Species(
    name="Crassostrea virginica",
    local_names={EN: "eastern oyster", PL: "ostryżyca amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eastern_oyster_outside.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Eastern_oyster_outside.jpg",
        author="Jud McCranie",
        license=License.CC_BY_SA_4_0,
    ),
)
P_MAXIMUS = Species(
    name="Pecten maximus",
    local_names={EN: "great scallop, king scallop", PL: "przegrzebek zwyczajny"},
    known_for=[{EN: "Shell logo"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Natural_History_-_Mollusca_-_The_Great_Scallop.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d0/Natural_History_-_Mollusca_-_The_Great_Scallop.jpg",
        author="Philip Henry Gosse  (1810–1888)",
        license=License.PUBLIC_DOMAIN,
    ),
)
P_MARGARITIFERA = Species(
    name="Pinctada margaritifera",
    local_names={EN: "black-lip pearl oyster", PL: "perłopław indyjski"},
    known_for=[{EN: "pearl production"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pinctada_margaritifera,_Aquarium_Finisterrae,_Galicia,_Spain.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c5/Pinctada_margaritifera%2C_Aquarium_Finisterrae%2C_Galicia%2C_Spain.jpg",
        author="Museos Científicos Coruñeses",
        license=License.CC_BY_SA_2_0,
    ),
)
M_EDULIS = Species(
    name="Mytilus edulis",
    local_names={EN: "blue mussel, common mussel", PL: "mul, omułek jadalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mytilus_edulis-y.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Mytilus_edulis-y.jpg",
        author="Magnefl",
        license=License.CC_BY_SA_3_0,
    ),
)
A_ANATINA = Species(
    name="Anodonta anatina",
    local_names={EN: "duck mussel", PL: "szczeżuja pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%D0%91%D0%B5%D0%B7%D0%B7%D1%83%D0%B1%D0%BA%D0%B0_(Anodonta_anatina).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/%D0%91%D0%B5%D0%B7%D0%B7%D1%83%D0%B1%D0%BA%D0%B0_%28Anodonta_anatina%29.jpg",
        author="Пономарьова Алевтина",
        license=License.CC_BY_SA_4_0,
    ),
)

MERCENARIA = Genus(name="Mercenaria", children=[M_MERCENARIA])
SPISULA = Genus(name="Spisula", children=[S_SOLIDISSIMA])
TRIDACNA = Genus(name="Tridacna", children=[T_GIGAS])
CERASTODERMA = Genus(name="Cerastoderma", children=[C_EDULE])
OSTREA = Genus(name="Ostrea", children=[O_EDULIS])
MAGALLANA = Genus(name="Magallana", children=[M_GIGAS])
CRASSOSTREA = Genus(name="Crassostrea", children=[C_VIRGINICA])
PECTEN = Genus(name="Pecten", children=[P_MAXIMUS])
PINCTADA = Genus(name="Pinctada", children=[P_MARGARITIFERA])
MYTILUS = Genus(name="Mytilus", children=[M_EDULIS])
ANODONTA = Genus(name="Anodonta", children=[A_ANATINA])

# https://link.springer.com/article/10.1007/s12526-021-01203-x
OSTREIDAE_A = Clade(children=[MAGALLANA, CRASSOSTREA])

VENERIDAE = Family(name="Veneridae", children=[MERCENARIA])
MACTRIDAE = Family(name="Mactridae", children=[SPISULA])
CARDIIDAE = Family(name="Cardiidae", children=[TRIDACNA, CERASTODERMA])
OSTREIDAE = Family(name="Ostreidae", children=[OSTREA, OSTREIDAE_A])
PECTINIDAE = Family(name="Pectinidae", children=[PECTEN])
PTERIIDAE = Family(name="Pteriidae", children=[PINCTADA])
MYTILIDAE = Family(name="Mytilidae", children=[MYTILUS])
UNIONIDAE = Family(name="Unionidae", children=[ANODONTA])

VENERIDA = Order(name="Venerida", children=[VENERIDAE, MACTRIDAE])
CARDIIDA = Order(name="Cardiida", children=[CARDIIDAE])
OSTREIDA = Order(name="Ostreida", children=[OSTREIDAE])
PECTINIDA = Order(name="Pectinida", children=[PECTINIDAE])
PTERIIDA = Order(name="Pteriida", children=[PTERIIDAE])
MYTILIDA = Order(name="Mytilida", children=[MYTILIDAE])
UNIONIDA = Order(name="Unionida", children=[UNIONIDAE])

HETERODONTA = Subclass(name="Heterodonta", children=[VENERIDA, CARDIIDA])
# unresolved
PTERIOMORPHIA = Subclass(
    name="Pteriomorphia", children=[OSTREIDA, PECTINIDA, PTERIIDA, MYTILIDA]
)
PALAEOHETERODONTA = Subclass(name="Palaeoheterodonta", children=[UNIONIDA])

# https://www.researchgate.net/publication/51785279_A_Molecular_Phylogeny_of_Bivalve_Mollusks_Ancient_Radiations_and_Divergences_as_Revealed_by_Mitochondrial_Genes
BIVALVIA_A = Clade(children=[HETERODONTA, PTERIOMORPHIA])

BIVALVIA = Class(name="Bivalvia", children=[BIVALVIA_A, PALAEOHETERODONTA])
