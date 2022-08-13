from clade import Clade, Family, Genus, Order, Species, Subfamily, Suborder, Superfamily
from constants import EN, IMAGE, NAME, PL
from image import Image, License

T_SCRIPTA = Species(
    name="Trachemys scripta",
    local_names={EN: "pond turtle", PL: "żółw ozdobny"},
    known_for=[
        {
            NAME: "Trachemys scripta elegans",
            EN: "red-eared slider",
            PL: "żółw czerwonolicy",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:RedEaredSlider05.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/96/RedEaredSlider05.jpg",
                author="Greg Hume",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pseudemys_scripta_scripta_-_Yellow-bellied_slider_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Pseudemys_scripta_scripta_-_Yellow-bellied_slider_02.jpg",
        author="Captain-tucker",
        license=License.CC_BY_SA_3_0,
    ),
)
C_PICTA = Species(
    name="Chrysemys picta",
    local_names={EN: "painted turtle", PL: "żółw malowany, żółwik malowany"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eastern_Painted_Turtle_(Chrysemys_picta_picta)_(49866261538)_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/38/Eastern_Painted_Turtle_%28Chrysemys_picta_picta%29_%2849866261538%29_%28cropped%29.jpg",
        author="Danielle  Brigida",
        license=License.CC_BY_2_0,
    ),
)
T_CAROLINA = Species(
    name="Terrapene carolina",
    local_names={EN: "common box turtle", PL: "terapena karolińska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Florida_Box_Turtle_Digon3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/34/Florida_Box_Turtle_Digon3.jpg",
        author="Jonathan Zander (Digon3)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_VANDENBURGHI = Species(
    name="Chelonoidis vandenburghi",
    local_names={EN: "Alcedo giant tortoise"},
    known_for=[
        {
            EN: "one of the most numerous species of Galápagos tortoise",
            PL: "jeden z najliczniejszych gatunków żółwi słoniowych",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chelonoidis_vandenburghi_41213756.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Chelonoidis_vandenburghi_41213756.jpg",
        author="John Brew",
        license=License.CC_BY_SA_4_0,
    ),
)
L_OLIVACEA = Species(
    name="Lepidochelys olivacea",
    local_names={EN: "olive ridley sea turtle", PL: "żółw oliwkowy"},
    known_for=[{EN: "the most common sea turtle"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Olive_ridley_sea_turtle_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f2/Olive_ridley_sea_turtle_cropped.jpg",
        author="Brad Flickinger",
        license=License.CC_BY_SA_4_0,
    ),
)
C_SERPENTINA = Species(
    name="Chelydra serpentina",
    local_names={
        EN: "common snapping turtle",
        PL: "żółw jaszczurowaty, żółw kajmanowy, skorpucha jaszczurowata",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chelydra_serpentina_USGS.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Chelydra_serpentina_USGS.jpg",
        author="Jeff Lovich",
        license=License.USGS,
    ),
)
M_TEMMINCKII = Species(
    name="Macrochelys temminckii",
    local_names={EN: "alligator snapping turtle", PL: "żółw sępi, skorpucha sępia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Macrochelys_temminckiiHolbrookV1P24A_flipped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Macrochelys_temminckiiHolbrookV1P24A_flipped.jpg",
        author="Holbrook, John Edwards, 1794-1871 (English Wikipedia)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
D_CORIACEA = Species(
    name="Dermochelys coriacea",
    local_names={
        EN: "leatherback sea turtle, luth, lute turtle. leathery turtle",
        PL: "żółw skórzasty",
    },
    known_for=[{EN: "the largest living turtle"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leatherback_sea_turtle_Tinglar,_USVI_(5839996547).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Leatherback_sea_turtle_Tinglar%2C_USVI_%285839996547%29.jpg",
        author="U.S. Fish and Wildlife Service Southeast Region",
        license=License.CC_BY_2_0,
    ),
)

C_NIGER = Clade(
    name="Chelonoidis niger complex",
    local_names={EN: "Galápagos tortoise", PL: "żółw z Galapagos, żółw słoniowy"},
    children=[C_VANDENBURGHI],
)  # Species complex

TRACHEMYS = Genus(name="Trachemys", children=[T_SCRIPTA])
CHRYSEMYS = Genus(name="Chrysemys", children=[C_PICTA])
TERRAPENE = Genus(name="Terrapene", children=[T_CAROLINA])
CHELONOIDIS = Genus(name="Chelonoidis", children=[C_NIGER])
LEPIDOCHELYS = Genus(name="Lepidochelys", children=[L_OLIVACEA])
CHELYDRA = Genus(name="Chelydra", children=[C_SERPENTINA])
MACROCHELYS = Genus(name="Macrochelys", children=[M_TEMMINCKII])
DERMOCHELYS = Genus(name="Dermochelys", children=[D_CORIACEA])

DEIROCHELYINAE = Subfamily(name="Deirochelyinae", children=[TRACHEMYS, CHRYSEMYS])
EMYDINAE = Subfamily(name="Emydinae", children=[TERRAPENE])

EMYDIDAE = Family(name="Emydidae", children=[DEIROCHELYINAE, EMYDINAE])
TESTUDINIDAE = Family(name="Testudinidae", children=[CHELONOIDIS])
CHELONIIDAE = Family(name="Cheloniidae", children=[LEPIDOCHELYS])
CHELYDRIDAE = Family(name="Chelydridae", children=[CHELYDRA, MACROCHELYS])
DERMOCHELYIDAE = Family(name="Dermochelyidae", children=[DERMOCHELYS])

TESTUDINOIDEA = Superfamily(name="Testudinoidea", children=[EMYDIDAE, TESTUDINIDAE])
CHELONIOIDEA = Superfamily(name="Chelonioidea", children=[CHELONIIDAE, DERMOCHELYIDAE])

AMERICHELYDIA = Clade(name="Americhelydia", children=[CHELONIOIDEA, CHELYDRIDAE])

CRYPTODIRA = Suborder(name="Cryptodira", children=[TESTUDINOIDEA, AMERICHELYDIA])

TESTUDINES = Order(name="Testudines", children=[CRYPTODIRA])
