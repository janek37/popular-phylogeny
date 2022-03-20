from clade import Family, Genus, Species, Subfamily, Tribe
from constants import EN, PL

C_CANADENSIS = Species(
    name="Cervus canadensis",
    local_names={EN: "elk, wapiti", PL: "wapiti, jeleń kanadyjski"},
)
C_ELAPHUS = Species(
    name="Cervus elaphus", local_names={EN: "red deer", PL: "jeleń szlachetny"}
)
D_DAMA = Species(
    name="Dama dama",
    local_names={
        EN: "European fallow deer, common fallow deer",
        PL: "daniel zwyczajny",
    },
)
O_VIRGINIANUS = Species(
    name="Odocoileus virginianus",
    local_names={
        EN: "whitetail, white-tailed deer",
        PL: "jeleń wirginijski, mulak białoogonowy",
    },
    known_for=[{EN: "Disney's Bambi"}],
)
R_TARANDUS = Species(
    name="Rangifer tarandus",
    local_names={EN: "reindeer, caribou", PL: "ren, karibu, renifer tundrowy"},
)
C_CAPREOLUS = Species(
    name="Capreolus capreolus", local_names={EN: "roe deer", PL: "sarna europejska"}
)
A_ALCES = Species(
    name="Alces alces", local_names={EN: "moose, elk", PL: "łoś euroazjatycki"}
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
