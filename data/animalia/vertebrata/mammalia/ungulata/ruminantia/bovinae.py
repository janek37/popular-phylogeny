from clade import Genus, Species, Subfamily, Subgenus, Subtribe, Tribe
from constants import EN, PL
from image import Image, License

S_CAFFER = Species(
    name="Syncerus caffer",
    local_names={EN: "African buffalo", PL: "bawół afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:African_Buffalo_(Syncerus_caffer)_cow_..._(50118835268).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4c/African_Buffalo_%28Syncerus_caffer%29_cow_..._%2850118835268%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
B_ARNEE = Species(
    name="Bubalus arnee",
    local_names={EN: "wild water buffalo", PL: "bawół indyjski, arni azjatycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Indian_Water_Buffalo_Bubalus_arnee_by_Dr_Raju_Kasambe_IMG_0347_(11)_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Indian_Water_Buffalo_Bubalus_arnee_by_Dr_Raju_Kasambe_IMG_0347_%2811%29_%28cropped%29.jpg",
        author="Dr. Raju Kasambe",
        license=License.CC_BY_SA_4_0,
    ),
)
B_BUBALIS = Species(
    name="Bubalus bubalis",
    local_names={EN: "domestic water buffalo", PL: "wół domowy"},
    known_for=[{EN: "mozzarella"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bubalus_bubalis_(water_buffalo)_looking_at_the_viewer,_the_feet_in_a_pond,_in_Laos.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/Bubalus_bubalis_%28water_buffalo%29_looking_at_the_viewer%2C_the_feet_in_a_pond%2C_in_Laos.jpg",
        author="Basile Morin",
        license=License.CC_BY_SA_4_0,
    ),
)
B_BONASUS = Species(
    name="Bison bonasus",
    local_names={EN: "European bison, wisent, zubr", PL: "żubr europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flachlandwisent_(Bison_bonasus_bonasus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Flachlandwisent_%28Bison_bonasus_bonasus%29.jpg",
        author="Michael Gäbler",
        license=License.CC_BY_SA_3_0,
    ),
)
B_BISON = Species(
    name="Bison bison",
    local_names={EN: "American bison", PL: "bizon amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:American_bison_DZS.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/26/American_bison_DZS.jpg",
        author="RedGazelle123",
        license=License.CC_BY_SA_4_0,
    ),
)
B_GRUNNIENS = Species(
    name="Bos grunniens",
    local_names={EN: "domestic yak", PL: "jak udomowiony"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sarlyk_Yak2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Sarlyk_Yak2.jpg",
        author="Alexandr frolov",
        license=License.CC_BY_SA_4_0,
    ),
)
B_PRIMIGENIUS = Species(
    name="Bos primigenius",
    local_names={EN: "aurochs", PL: "tur leśny"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aurochs_reconstruction.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0d/Aurochs_reconstruction.jpg",
        author="Jaap Rouwenhorst (photograph) DFoidl (GIMP modifications)",
        license=License.CC_BY_SA_3_0,
    ),
)
B_TAURUS = Species(
    name="Bos taurus",
    local_names={EN: "cattle", PL: "bydło domowe"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cow_female_black_white.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0c/Cow_female_black_white.jpg",
        author="Keith Weller/USDA",
        license=License.USDA_ARS,
    ),
)
B_INDICUS = Species(
    name="Bos indicus",
    local_names={
        EN: "zebu, indicine cattle, humped cattle",
        PL: "bydło domowe garbaty, zebu indyjskie",
    },
    known_for=[
        {EN: "venerated within the Hindu religion", PL: "święte krowy w hinduizmie"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bos_taurus_indicus_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Bos_taurus_indicus_%28cropped%29.jpg",
        author="Scott Bauer, USDA ARS",
        license=License.USDA_ARS,
    ),
)

BISON = Subgenus(name="Bison", children=[B_BONASUS, B_BISON])
BOS_SUBGENUS_POEPHAGUS = Subgenus(name="Bos subg. Poephagus", children=[B_GRUNNIENS])
# unresolved
BOS_SUBGENUS_BOS = Subgenus(
    name="Bos subg. Bos", children=[B_PRIMIGENIUS, B_TAURUS, B_INDICUS]
)

SYNCERUS = Genus(name="Syncerus", children=[S_CAFFER])
BUBALUS = Genus(name="Bubalus", children=[B_ARNEE, B_BUBALIS])
# unresolved
BOS = Genus(name="Bos", children=[BISON, BOS_SUBGENUS_POEPHAGUS, BOS_SUBGENUS_BOS])

BUBALINA = Subtribe(name="Bubalina", children=[SYNCERUS, BUBALUS])
BOVINA = Subtribe(name="Bovina", children=[BISON, BOS])

BOVINI = Tribe(name="Bovini", children=[BUBALINA, BOVINA])

BOVINAE = Subfamily(name="Bovinae", children=[BOVINI])
