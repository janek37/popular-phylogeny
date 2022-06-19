from clade import Family, Genus, Species, Subfamily, Tribe
from constants import EN, PL, URL
from image import Image, License

C_CANADENSIS = Species(
    name="Cervus canadensis",
    local_names={EN: "elk, wapiti", PL: "wapiti, jeleń kanadyjski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rocky_Mountain_Bull_Elk.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Rocky_Mountain_Bull_Elk.jpg",
        author="MONGO",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
C_ELAPHUS = Species(
    name="Cervus elaphus",
    local_names={EN: "red deer", PL: "jeleń szlachetny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cervus_elaphus_Luc_Viatour_6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Cervus_elaphus_Luc_Viatour_6.jpg",
        author="Lviatour",
        license=License.CC_BY_SA_3_0,
    ),
)
D_DAMA = Species(
    name="Dama dama",
    local_names={
        EN: "European fallow deer, common fallow deer",
        PL: "daniel zwyczajny",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dama_dama8.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cc/Dama_dama8.JPG",
        author="B.Navez",
        license=License.CC_BY_SA_3_0,
    ),
)
O_VIRGINIANUS = Species(
    name="Odocoileus virginianus",
    local_names={
        EN: "whitetail, white-tailed deer",
        PL: "jeleń wirginijski, mulak białoogonowy",
    },
    known_for=[
        {EN: "Disney's Bambi", URL: "https://disney.fandom.com/wiki/Bambi_(character)"}
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%22Crown_Head%22_(51382475495).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/%22Crown_Head%22_%2851382475495%29.jpg",
        author="yrjö jyske from Finland",
        license=License.CC_BY_2_0,
    ),
)
R_TARANDUS = Species(
    name="Rangifer tarandus",
    local_names={EN: "reindeer, caribou", PL: "ren, karibu, renifer tundrowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20070818-0001-strolling_reindeer.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/af/20070818-0001-strolling_reindeer.jpg",
        author="Alexandre Buisse (Nattfodd)",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CAPREOLUS = Species(
    name="Capreolus capreolus",
    local_names={EN: "roe deer", PL: "sarna europejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Capreolus_(js)11.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Capreolus_%28js%2911.jpg",
        author="Jerzystrzelecki",
        license=License.CC_BY_3_0,
    ),
)
A_ALCES = Species(
    name="Alces alces",
    local_names={EN: "moose, elk", PL: "łoś euroazjatycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Moose_superior.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Moose_superior.jpg",
        author="USDA Forest Service",
        license=License.EPA,
    ),
)

CERVUS = Genus(name="Cervus", children=[C_CANADENSIS, C_ELAPHUS])
DAMA = Genus(name="Dama", children=[D_DAMA])
ODOCOILEUS = Genus(name="Odocoileus", children=[O_VIRGINIANUS])
RANGIFER = Genus(name="Rangifer", children=[R_TARANDUS])
CAPREOLUS = Genus(name="Capreolus", children=[C_CAPREOLUS])
ALCES = Genus(name="Alces", children=[A_ALCES])

RANGIFERINI = Tribe(name="Rangiferini", children=[ODOCOILEUS, RANGIFER])
CAPREOLINI = Tribe(name="Capreolini", children=[CAPREOLUS])
ALCEINI = Tribe(name="Alceini", children=[ALCES])

CERVINAE = Subfamily(name="Cervinae", children=[CERVUS, DAMA])
# unresolved
CAPREOLINAE = Subfamily(name="Capreolinae", children=[RANGIFERINI, CAPREOLINI, ALCEINI])

CERVIDAE = Family(name="Cervidae", children=[CERVINAE, CAPREOLINAE])
