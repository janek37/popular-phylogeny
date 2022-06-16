from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, PL
from image import Image, License

S_FATALIS = Species(
    name="Smilodon fatalis",
    local_names={EN: "saber-toothed tiger", PL: "tygrys szablozębny"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/Smilodon_fatalis.jpg",
        author="Dantheman9758 at English Wikipedia",
        license=License.CC_BY_3_0,
    ),
)
P_TIGRIS = Species(
    name="Panthera tigris",
    local_names={EN: "tiger", PL: "tygrys azjatycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bengal_tiger_(Panthera_tigris_tigris)_female_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/97/Bengal_tiger_%28Panthera_tigris_tigris%29_female_3.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
P_UNCIA = Species(
    name="Panthera uncia",
    local_names={EN: "snow leopard", PL: "pantera śnieżna, irbis śnieżny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Uncia_uncia_-_A_tail_and_a_cat_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/71/Uncia_uncia_-_A_tail_and_a_cat_cropped.jpg",
        author="Marit & Toomas Hinnosaar",
        license=License.CC_BY_2_0,
    ),
)
P_ONCA = Species(
    name="Panthera onca",
    local_names={EN: "jaguar", PL: "jaguar amerykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Jaguar_(Panthera_onca_palustris)_male_Three_Brothers_River.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ac/Jaguar_%28Panthera_onca_palustris%29_male_Three_Brothers_River.JPG",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
P_LEO = Species(
    name="Panthera leo",
    local_names={EN: "lion", PL: "lew afrykański"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Panthera_leo_(male)_(181091659).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0d/Panthera_leo_%28male%29_%28181091659%29.jpg",
        author="Daniel Aufgang",
        license=License.CC_BY_3_0,
    ),
)
P_PARDUS = Species(
    name="Panthera pardus",
    local_names={EN: "leopard", PL: "pantera, leopard, lampart plamisty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leopard_(Panthera_pardus)_(51984659585).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Leopard_%28Panthera_pardus%29_%2851984659585%29.jpg",
        author="Bernard DUPONT from FRANCE",
        license=License.CC_BY_SA_2_0,
    ),
)
C_CARACAL = Species(
    name="Caracal caracal",
    local_names={EN: "caracal", PL: "karakal stepowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Caracal_caracal_175387938.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e7/Caracal_caracal_175387938.jpg",
        author="Kelly Abram",
        license=License.CC_BY_4_0,
    ),
)
L_SERVAL = Species(
    name="Leptailurus serval",
    local_names={EN: "serval", PL: "serwal sawannowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Serval_(3076183690).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1b/Serval_%283076183690%29.jpg",
        author="Vince Smith from London, United Kingdom",
        license=License.CC_BY_2_0,
    ),
)
L_PARDALIS = Species(
    name="Leopardus pardalis",
    local_names={EN: "ocelot", PL: "ocelot wielki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leopardus_pardalis_Jaime_Duque_Park.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Leopardus_pardalis_Jaime_Duque_Park.jpg",
        author="Petruss",
        license=License.CC_BY_SA_4_0,
    ),
)
L_LYNX = Species(
    name="Lynx lynx",
    local_names={EN: "Eurasian lynx", PL: "ryś euroazjatycki"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20130711_EurasianLynx_IMG_8059.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3a/20130711_EurasianLynx_IMG_8059.png",
        author="Jon Glittenberg",
        license=License.CC_BY_SA_4_0,
    ),
)
L_RUFUS = Species(
    name="Lynx rufus",
    local_names={EN: "bobcat, red lynx", PL: "ryś rudy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bobcat2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dc/Bobcat2.jpg",
        author="Calibas",
        license=License.PUBLIC_DOMAIN,
    ),
)
A_JUBATUS = Species(
    name="Acinonyx jubatus",
    local_names={EN: "cheetah", PL: "gepard grzywiasty"},
    known_for=[{EN: "the fastest land animal"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Acinonyx_jubatus_at_Parc_des_F%C3%A9lins_05.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/Acinonyx_jubatus_at_Parc_des_F%C3%A9lins_05.jpg",
        author="Abujoy",
        license=License.CC_BY_4_0,
    ),
)
P_CONCOLOR = Species(
    name="Puma concolor",
    local_names={EN: "cougar, puma, mountain lion", PL: "kuguar, puma płowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Puma_concolor_stanleyana_-_Texas_Park_-_Lanzarote_-PC10.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Puma_concolor_stanleyana_-_Texas_Park_-_Lanzarote_-PC10.jpg",
        author="Luis Miguel Bugallo Sánchez(Lmbuga)",
        license=License.CC_BY_SA_3_0,
    ),
)
P_BENGALENSIS = Species(
    name="Prionailurus bengalensis",
    local_names={EN: "leopard cat", PL: "kot bengalski, kotek bengalski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prionailurus_bengalensis_euptilurus_(9413725653).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Prionailurus_bengalensis_euptilurus_%289413725653%29.jpg",
        author="Biodiversity Heritage Library",
        license=License.CC_BY_2_0,
    ),
)
F_SILVESTRIS = Species(
    name="Felis silvestris",
    local_names={EN: "European wildcat", PL: "żbik europejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Felis_silvestris_silvestris_Luc_Viatour.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d0/Felis_silvestris_silvestris_Luc_Viatour.jpg",
        author="Lviatour",
        license=License.CC_BY_SA_3_0,
    ),
)
F_LYBICA = Species(
    name="Felis lybica",
    local_names={EN: "African wildcat", PL: "żbik afrykański, kot nubijski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Felis_silvestris_cafra.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/19/Felis_silvestris_cafra.jpg",
        author="Leonemanuel",
        license=License.CC_BY_SA_4_0,
    ),
)
F_CATUS = Species(
    name="Felis catus",
    local_names={EN: "domestic cat", PL: "kot domowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Felis_catus-cat_on_snow.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg",
        author="Von.grzanka",
        license=License.CC_BY_SA_3_0,
    ),
)

PANTHERA_A = Clade(children=[P_TIGRIS, P_UNCIA])
PANTHERA_B = Clade(children=[P_LEO, P_PARDUS])
PANTHERA_C = Clade(children=[P_ONCA, PANTHERA_B])

FELIS_A = Clade(children=[F_LYBICA, F_CATUS])

SMILODON = Genus(name="Smilodon", children=[S_FATALIS])
PANTHERA = Genus(name="Panthera", children=[PANTHERA_A, PANTHERA_C])
CARACAL = Genus(name="Caracal", children=[C_CARACAL])
LEPTAILURUS = Genus(name="Leptailurus", children=[L_SERVAL])
LEOPARDUS = Genus(name="Leopardus", children=[L_PARDALIS])
LYNX = Genus(name="Lynx", children=[L_LYNX, L_RUFUS])
ACINONYX = Genus(name="Acinonyx", children=[A_JUBATUS])
PUMA = Genus(name="Puma", children=[P_CONCOLOR])
PRIONAILURUS = Genus(name="Prionailurus", children=[P_BENGALENSIS])
FELIS = Genus(name="Felis", children=[F_SILVESTRIS, FELIS_A])

FELINAE_A = Clade(children=[CARACAL, LEPTAILURUS])
FELINAE_B = Clade(children=[ACINONYX, PUMA])
FELINAE_C = Clade(children=[PRIONAILURUS, FELIS])
FELINAE_D = Clade(children=[FELINAE_B, FELINAE_C])
FELINAE_E = Clade(children=[LYNX, FELINAE_D])
FELINAE_F = Clade(children=[LEOPARDUS, FELINAE_E])

MACHAIRODONTINAE = Subfamily(name="Machairodontinae", children=[SMILODON])
PANTHERINAE = Subfamily(name="Pantherinae", children=[PANTHERA])
FELINAE = Subfamily(name="Felinae", children=[FELINAE_A, FELINAE_F])

FELIDAE_A = Clade(children=[PANTHERINAE, FELINAE])

FELIDAE = Family(name="Felidae", children=[MACHAIRODONTINAE, FELIDAE_A])
