from clade import Family, Genus, Order, Species, Subfamily, Superfamily, Tribe
from constants import EN, PL
from image import Image, License

A_MACAO = Species(
    name="Ara macao",
    local_names={EN: "scarlet macaw", PL: "ara czerwona, ara żółtoskrzydła"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Scarlet_macaw_(Ara_macao).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/59/Scarlet_macaw_%28Ara_macao%29.jpg",
        author="T. Sagorski",
        license=License.CC_BY_SA_4_0,
    ),
)
A_ARARAUNA = Species(
    name="Ara ararauna",
    local_names={EN: "blue-and-yellow macaw", PL: "ara ararauna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Blue-and-gold_Macaw_(Ara_ararauna)_at_zoo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Blue-and-gold_Macaw_%28Ara_ararauna%29_at_zoo.jpg",
        author="John Benson",
        license=License.CC_BY_2_0,
    ),
)
C_SPIXII = Species(
    name="Cyanopsitta spixii",
    local_names={EN: "Spix's macaw, little blue macaw", PL: "ara modra"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:AraSpixiSmit.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/98/AraSpixiSmit.jpg",
        author="Joseph Smit",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_ERITHACUS = Species(
    name="Psittacus erithacus",
    local_names={EN: "Congo grey parrot", PL: "żako"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Psittacus_erithacus_qtl1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Psittacus_erithacus_qtl1.jpg",
        author="Quartl",
        license=License.CC_BY_SA_3_0,
    ),
)
M_UNDULATUS = Species(
    name="Melopsittacus undulatus",
    local_names={EN: "budgerigar, common parakeet", PL: "papużka falista"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Melopsittacus_undulatus_-Henry_Doorly_Zoo_-two-8a.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Melopsittacus_undulatus_-Henry_Doorly_Zoo_-two-8a.png",
        author="Jeff Coffman",
        license=License.CC_BY_2_0,
    ),
)
A_ROSEICOLLIS = Species(
    name="Agapornis roseicollis",
    local_names={EN: "rosy-faced lovebird", PL: "nierozłączka czerwonoczelna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Agapornis_roseicollis_-_Rosenk%C3%B6pfchen_-_Wildfarbig_-_Deutscher_Kanarien-_und_Vogelz%C3%BCchterbund_(DKB)_-_Vogelbund_-_Johann_Alexi.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Agapornis_roseicollis_-_Rosenk%C3%B6pfchen_-_Wildfarbig_-_Deutscher_Kanarien-_und_Vogelz%C3%BCchterbund_%28DKB%29_-_Vogelbund_-_Johann_Alexi.jpg",
        author="Johann Alexi",
        license=License.CC_BY_SA_4_0,
    ),
)
C_GALERITA = Species(
    name="Cacatua galerita",
    local_names={EN: "sulphur-crested cockatoo", PL: "kakadu żółtoczuba"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sulphur-crested_Cockatoo_(Cacatua_galerita)_(8079604543).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Sulphur-crested_Cockatoo_%28Cacatua_galerita%29_%288079604543%29.jpg",
        author="Ron Knight from Seaford, East Sussex, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)

ARA = Genus(name="Ara", children=[A_MACAO, A_ARARAUNA])
CYANOPSITTA = Genus(name="Cyanopsitta", children=[C_SPIXII])
PSITTACUS = Genus(name="Psittacus", children=[P_ERITHACUS])
MELOPSITTACUS = Genus(name="Melopsittacus", children=[M_UNDULATUS])
AGAPORNIS = Genus(name="Agapornis", children=[A_ROSEICOLLIS])
CACATUA = Genus(name="Cacatua", children=[C_GALERITA])

ARINI = Tribe(name="Arini", children=[ARA, CYANOPSITTA])
PSITTACINI = Tribe(name="Psittacini", children=[PSITTACUS])

ARINAE = Subfamily(name="Arinae", children=[ARINI])
PSITTACINAE = Subfamily(name="Psittacinae", children=[PSITTACINI])

PSITTACIDAE = Family(name="Psittacidae", children=[ARINAE, PSITTACINAE])
PSITTACULIDAE = Family(name="Psittaculidae", children=[MELOPSITTACUS, AGAPORNIS])
CACATUIDAE = Family(name="Cacatuidae", children=[CACATUA])

PSITTACOIDEA = Superfamily(name="Psittacoidea", children=[PSITTACIDAE, PSITTACULIDAE])
CACATUOIDEA = Superfamily(name="Cacatuoidea", children=[CACATUIDAE])

PSITTACIFORMES = Order(name="Psittaciformes", children=[PSITTACOIDEA, CACATUOIDEA])
