from clade import Clade, Family, Genus, Species, Subfamily, Suborder
from constants import EN, IMAGE, PL
from image import Image, License

C_CHAMAELEON = Species(
    name="Chamaeleo chamaeleon",
    local_names={EN: "common chameleon", PL: "kameleon pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chamaeleo_chamaeleon_10249090.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f9/Chamaeleo_chamaeleon_10249090.jpg",
        author="Eliane Küpfer",
        license=License.CC_BY_SA_4_0,
    ),
)
C_KINGII = Species(
    name="Chlamydosaurus kingii",
    local_names={EN: "frilled lizard", PL: "agama kołnierzasta"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Haeckel_Lacertilia_(Chlamydosaurus_kingii).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Haeckel_Lacertilia_%28Chlamydosaurus_kingii%29.jpg",
        author="Ernst Haeckel",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
M_HORRIDUS = Species(
    name="Moloch horridus",
    local_names={EN: "thorny devil", PL: "moloch kolczasty, moloch straszliwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Thorny_devil_pale.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Thorny_devil_pale.jpg",
        author="KeresH",
        license=License.CC_BY_SA_3_0,
    ),
)
D_VOLANS = Species(
    name="Draco volans",
    local_names={EN: "common flying dragon", PL: "smok latający"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Draco_volans_44997932.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/75/Draco_volans_44997932.jpg",
        author="redrovertracy",
        license=License.CC_BY_4_0,
    ),
)
I_IGUANA = Species(
    name="Iguana iguana",
    local_names={EN: "green iguana", PL: "legwan zielony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Iguana_iguana_Portoviejo_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Iguana_iguana_Portoviejo_01.jpg",
        author="Cayambe",
        license=License.CC_BY_SA_3_0,
    ),
)
A_CAROLINENSIS = Species(
    name="Anolis carolinensis",
    local_names={EN: "green anole", PL: "anolis zielony"},
    known_for=[
        {
            EN: "one of the most notable color-changing lizards besides chameleons",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Anolis_carolinensis_color_change.png",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/85/Anolis_carolinensis_color_change.png",
                author="Huhnra",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Male_Anolis_carolinensis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/21/Male_Anolis_carolinensis.jpg",
        author="Euku",
        license=License.CC_BY_SA_3_0,
    ),
)

CHAMAELEO = Genus(name="Chamaeleo", children=[C_CHAMAELEON])
CHLAMYDOSAURUS = Genus(name="Chlamydosaurus", children=[C_KINGII])
MOLOCH = Genus(name="Moloch", children=[M_HORRIDUS])
DRACO = Genus(name="Draco", children=[D_VOLANS])
IGUANA = Genus(name="Iguana", children=[I_IGUANA])
ANOLIS = Genus(name="Anolis", children=[A_CAROLINENSIS])

AMPHIBOLURINAE = Subfamily(name="Amphibolurinae", children=[CHLAMYDOSAURUS, MOLOCH])
DRACONINAE = Subfamily(name="Draconinae", children=[DRACO])

CHAMAELEONIDAE = Family(name="Chamaeleonidae", children=[CHAMAELEO])
AGAMIDAE = Family(name="Agamidae", children=[AMPHIBOLURINAE, DRACONINAE])
IGUANIDAE = Family(name="Iguanidae", children=[IGUANA])
DACTYLOIDAE = Family(name="Dactyloidae", children=[ANOLIS])

ACRODONTA = Clade(name="Acrodonta", children=[CHAMAELEONIDAE, AGAMIDAE])
PLEURODONTA = Clade(name="Pleurodonta", children=[IGUANIDAE, DACTYLOIDAE])

IGUANIA = Suborder(name="Iguania", children=[ACRODONTA, PLEURODONTA])
