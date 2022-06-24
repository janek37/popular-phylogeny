from clade import Clade, Family, Genus, Order, Species
from constants import EN, JP, PL
from image import Image, License

A_BISPORUS = Species(
    name="Agaricus bisporus",
    local_names={
        EN: "button/cremini/portobello mushroom",
        PL: "pieczarka dwuzarodnikowa",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Agaricus_bisporus_G4.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Agaricus_bisporus_G4.JPG",
        author="Jerzy Opioła",
        license=License.CC_BY_SA_3_0,
    ),
)
L_EDODES = Species(
    name="Lentinula edodes",
    local_names={JP: "shiitake"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Shiitakegrowing.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/64/Shiitakegrowing.jpg",
        author="frankenstoen from Portland, Oregon",
        license=License.CC_BY_2_0,
    ),
)
F_VELUTIPES = Species(
    name="Flammulina velutipes",
    local_names={EN: "enoki", JP: "enokitake"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flammulina_velutipes_04.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Flammulina_velutipes_04.jpg",
        author="Eric Steinert",
        license=License.CC_BY_SA_3_0,
    ),
)
H_TESSELLATUS = Species(
    name="Hypsizygus tessellatus",
    local_names={EN: "beech/clamshell mushroom"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hypsizygus_marmoreus_20101123_a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Hypsizygus_marmoreus_20101123_a.jpg",
        author="Batholith",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
P_OSTREATUS = Species(
    name="Pleurotus ostreatus",
    local_names={EN: "oyster mushroom", PL: "boczniak ostrygowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pleurotus_ostreatus_109117645.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5f/Pleurotus_ostreatus_109117645.jpg",
        author="Ken Kneidel",
        license=License.CC0,
    ),
)
P_ERYNGII = Species(
    name="Pleurotus eryngii",
    local_names={EN: "king oyster mushroom", PL: "boczniak mikołajkowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kr%C3%A4uter-Seitling_Pleurotus_eryngii.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Kr%C3%A4uter-Seitling_Pleurotus_eryngii.jpg",
        author="Holger Krisp",
        license=License.CC_BY_3_0,
    ),
)
P_SEMILANCEATA = Species(
    name="Psilocybe semilanceata",
    local_names={EN: "liberty cap", PL: "czapka wolności, łysiczka lancetowata"},
    known_for=[{EN: "psychoactive psylocybin"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Psilocybe_semilanceata_(49153346451).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Psilocybe_semilanceata_%2849153346451%29.jpg",
        author="Lukas from London, England",
        license=License.CC_BY_SA_2_0,
    ),
)
A_MUSCARIA = Species(
    name="Amanita muscaria",
    local_names={PL: "muchomor czerwony", EN: "fly agaric"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fliegenpilz_fly_agaric_Amanita_muscaria.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Fliegenpilz_fly_agaric_Amanita_muscaria.JPG",
        author="Holger Krisp",
        license=License.CC_BY_3_0,
    ),
)
A_PHALLOIDES = Species(
    name="Amanita phalloides",
    local_names={PL: "muchomor sromotnikowy", EN: "death cap"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Amanita_phalloides_88334590.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Amanita_phalloides_88334590.jpg",
        author="Maxim Shashkov",
        license=License.CC_BY_4_0,
    ),
)
M_PROCERA = Species(
    name="Macrolepiota procera",
    local_names={PL: "czubajka kania", EN: "parasol mushroom"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Macrolepiota-procera.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Macrolepiota-procera.jpg",
        author="Chrumps",
        license=License.CC_BY_SA_4_0,
    ),
)
A_OSTOYAE = Species(
    name="Armillaria ostoyae",
    local_names={EN: "honey agaric", PL: "opieńka ciemna"},
    known_for=[
        {EN: "possibly the largest living organism on Earth (humungous fungus)"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Armillaria_ostoyae_159649917.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/41/Armillaria_ostoyae_159649917.jpg",
        author="Agnieszka Łubian",
        license=License.CC_BY_4_0,
    ),
)
C_GIGANTEA = Species(
    name="Calvatia gigantea",
    local_names={PL: "purchawka olbrzymia", EN: "giant pufflball"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Giant_Puffball_(Calvatia_gigantea)_(4951914366).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Giant_Puffball_%28Calvatia_gigantea%29_%284951914366%29.jpg",
        author="AnemoneProjectors (talk)",
        license=License.CC_BY_SA_2_0,
    ),
)

AGARICUS = Genus(name="Agaricus", children=[A_BISPORUS])
LENTINULA = Genus(name="Lentinula", children=[L_EDODES])
FLAMMULINA = Genus(name="Flammulina", children=[F_VELUTIPES])
HYPSIZYGUS = Genus(name="Hypsizygus", children=[H_TESSELLATUS])
PLEUROTUS = Genus(name="Pleurotus", children=[P_OSTREATUS, P_ERYNGII])
PSILOCYBE = Genus(name="Psilocybe", children=[P_SEMILANCEATA])
AMANITA = Genus(name="Amanita", children=[A_MUSCARIA, A_PHALLOIDES])
MACROLEPIOTA = Genus(name="Macrolepiota", children=[M_PROCERA])
ARMILLARIA = Genus(name="Armillaria", children=[A_OSTOYAE])
CALVATIA = Genus(name="Calvatia", children=[C_GIGANTEA])

# https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00019285/Gube/Dissertation.pdf
# unsure
AGARICACEAE_A = Clade(children=[AGARICUS, MACROLEPIOTA])

AGARICACEAE = Family(name="Agaricaceae", children=[AGARICACEAE_A, CALVATIA])
OMPHALOTACEAE = Family(name="Omphalotaceae", children=[LENTINULA])
PHYSALACRIACEAE = Family(name="Physalacriaceae", children=[FLAMMULINA, ARMILLARIA])
LYOPHYLLACEAE = Family(name="Lyophyllaceae", children=[HYPSIZYGUS])
PLEUROTACEAE = Family(name="Pleurotaceae", children=[PLEUROTUS])
HYMENOGASTRACEAE = Family(name="Hymenogastraceae", children=[PSILOCYBE])
AMANITACEAE = Family(name="Amanitaceae", children=[AMANITA])

MIRASMOID_CLADE = Clade(
    name="Mirasmoid clade", children=[OMPHALOTACEAE, PHYSALACRIACEAE]
)
AGARICOID_CLADE = Clade(
    name="Agaricoid clade", children=[AGARICACEAE, HYMENOGASTRACEAE]
)
PLUTEOID_CLADE = Clade(name="Pluteoid clade", children=[PLEUROTACEAE, AMANITACEAE])
# source: http://tolweb.org/Agaricales/20551
AGARICOID_TRICHOLOMATOID = Clade(children=[AGARICOID_CLADE, LYOPHYLLACEAE])

AGARICALES = Order(
    name="Agaricales",
    children=[AGARICOID_TRICHOLOMATOID, MIRASMOID_CLADE, PLUTEOID_CLADE],
)
