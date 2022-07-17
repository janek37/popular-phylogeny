from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

from .amygdaloideae import AMYGDALOIDEAE
from .rosoideae import ROSOIDEAE

C_SATIVA = Species(
    name="Cannabis sativa",
    local_names={PL: "konopie siewne"},
    known_for=[
        {
            EN: "THC",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:THC.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/THC.svg",
                author="Harbin",
                license=License.PUBLIC_DOMAIN_CHEM,
            ),
        },
        {EN: "marijuana"},
        {EN: "hashish", PL: "haszysz"},
        {EN: "hemp"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cannabis_Sativa_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Cannabis_Sativa_1.jpg",
        author="Gaurav Dhwaj Khadka",
        license=License.CC_BY_SA_4_0,
    ),
)
C_INDICA = Species(
    name="Cannabis indica",
    local_names={PL: "konopie indyjskie"},
    known_for=[
        {EN: "marijuana"},
        {EN: "hashish", PL: "haszysz"},
        {EN: "higher concentrations of THC"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Himachal_Pradesh_-_Manali_-_Cannabis_Sativa_var._Indica_(4135437745).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/72/Himachal_Pradesh_-_Manali_-_Cannabis_Sativa_var._Indica_%284135437745%29.jpg",
        author="Miran  Rijavec",
        license=License.CC_BY_2_0,
    ),
)
H_LUPULUS = Species(
    name="Humulus lupulus",
    local_names={PL: "chmiel zwyczajny", EN: "common hop, hops"},
    known_for=[{EN: "beer", PL: "piwo"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hop_(Humulus_lupulus)_(16678811553).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Hop_%28Humulus_lupulus%29_%2816678811553%29.jpg",
        author="Luc.T from Buggenhout, België",
        license=License.CC_BY_2_0,
    ),
)
F_CARICA = Species(
    name="Ficus carica",
    local_names={PL: "figowiec pospolity"},
    known_for=[
        {
            EN: "fig",
            PL: "figa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Breva_ficus_carica.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/41/Breva_ficus_carica.jpg",
                author="Emi Yañez from Barcelona, Spain",
                license=License.CC_BY_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ficus_carica_Panasc%C3%A8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Ficus_carica_Panasc%C3%A8.jpg",
        author="AxelRohdeElias; Caricated on commons by: Galloramenu",
        license=License.CC_BY_2_0,
    ),
)
F_BENJAMINA = Species(
    name="Ficus benjamina",
    local_names={EN: "weeping fig, ficus tree", PL: "fikus, figowiec benjamina"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_070123-3739_Ficus_benjamina.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f5/Starr_070123-3739_Ficus_benjamina.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
F_RELIGIOSA = Species(
    name="Ficus religiosa",
    local_names={EN: "sacred fig", PL: "figowiec pagodowy"},
    known_for=[{EN: "significant in Hinduism, Buddhism and Jaininsm"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ficus_religiosa_%C3%A0_Pushkar_(Rajasthan)_(5).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Ficus_religiosa_%C3%A0_Pushkar_%28Rajasthan%29_%285%29.jpg",
        author="Ji-Elle",
        license=License.CC_BY_SA_4_0,
    ),
)
A_ALTILIS = Species(
    name="Artocarpus altilis",
    local_names={EN: "breadfruit", PL: "chlebowiec właściwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Artocarpus_altilis_(fruit).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/57/Artocarpus_altilis_%28fruit%29.jpg",
        author="Hans Hillewaert",
        license=License.CC_BY_SA_3_0,
    ),
)
A_HETEROPHYLLUS = Species(
    name="Artocarpus heterophyllus",
    local_names={
        EN: "jackfruit",
        PL: "drzewo bochenkowe, dżakfrut, chlebowiec różnolistny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Artocarpus_heterophyllus_(Jackfruit)_(28260465513).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Artocarpus_heterophyllus_%28Jackfruit%29_%2828260465513%29.jpg",
        author="Treeworld Wholesale",
        license=License.CC_BY_2_0,
    ),
)
M_ALBA = Species(
    name="Morus alba",
    local_names={EN: "white mulberry", PL: "morwa biała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Morus_alba_8966.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Morus_alba_8966.jpg",
        author="Schurdl",
        license=License.CC_BY_SA_4_0,
    ),
)
U_DIOICA = Species(
    name="Urtica dioica",
    local_names={EN: "common nettle", PL: "pokrzywa zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Br%C3%A4nn%C3%A4ssla_(Urtica_Dioica).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/01/Br%C3%A4nn%C3%A4ssla_%28Urtica_Dioica%29.jpg",
        author="Skalle-Per Hedenhös",
        license=License.CC_BY_SA_4_0,
    ),
)
U_MINOR = Species(
    name="Ulmus minor",
    local_names={EN: "field elm", PL: "wiąz pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ulmus_minor_leaves.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Ulmus_minor_leaves.jpg",
        author="Moinats",
        license=License.CC_BY_SA_4_0,
    ),
)
U_AMERICANA = Species(
    name="Ulmus americana",
    local_names={EN: "American elm", PL: "wiąz amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ulmus_americana_(5101983801).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Ulmus_americana_%285101983801%29.jpg",
        author="Matt Lavin from Bozeman, Montana, USA",
        license=License.CC_BY_SA_2_0,
    ),
)

CANNABIS = Genus(name="Cannabis", children=[C_SATIVA, C_INDICA])
HUMULUS = Genus(name="Humulus", children=[H_LUPULUS])
FICUS = Genus(name="Ficus", children=[F_CARICA, F_BENJAMINA, F_RELIGIOSA])
ARTOCARPUS = Genus(name="Artocarpus", children=[A_ALTILIS, A_HETEROPHYLLUS])
MORUS = Genus(name="Morus", children=[M_ALBA])
URTICA = Genus(name="Urtica", children=[U_DIOICA])
ULMUS = Genus(name="Ulmus", children=[U_MINOR, U_AMERICANA])

FICEAE = Tribe(name="Ficeae", children=[FICUS])
ARTOCARPEAE = Tribe(name="Artocarpeae", children=[ARTOCARPUS])
MOREAE = Tribe(name="Moreae", children=[MORUS])

ARTOCARPEAE_MOREAE = Clade(children=[ARTOCARPEAE, MOREAE])

CANNABACEAE = Family(name="Cannabaceae", children=[CANNABIS, HUMULUS])
MORACEAE = Family(name="Moraceae", children=[FICEAE, ARTOCARPEAE_MOREAE])
URTICACEAE = Family(name="Urticaceae", children=[URTICA])
ROSACEAE = Family(name="Rosaceae", children=[AMYGDALOIDEAE, ROSOIDEAE])
ULMACEAE = Family(name="Ulmaceae", children=[ULMUS])

MORACEAE_URTICACEAE = Clade(children=[MORACEAE, URTICACEAE])

URTICALEAN_ROSIDS_A = Clade(children=[CANNABACEAE, MORACEAE_URTICACEAE])

URTICALEAN_ROSIDS = Clade(
    name="urticalean rosids", children=[ULMACEAE, URTICALEAN_ROSIDS_A]
)

ROSALES = Order(name="Rosales", children=[URTICALEAN_ROSIDS, ROSACEAE])
