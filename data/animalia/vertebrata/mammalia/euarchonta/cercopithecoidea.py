from clade import Clade, Family, Genus, Species, Subfamily, Superfamily, Tribe
from constants import EN, PL, URL
from image import Image, License

M_FUSCATA = Species(
    name="Macaca fuscata",
    local_names={EN: "Japanese macaque", PL: "makak japoński"},
    known_for=[{EN: "three wise monkeys"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Macaca_fuscata_in_Ueno_Zoo_2019_07.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/Macaca_fuscata_in_Ueno_Zoo_2019_07.jpg",
        author="Jopparn",
        license=License.CC_BY_SA_4_0,
    ),
)
M_MULATTA = Species(
    name="Macaca mulatta",
    local_names={EN: "rhesus macaque", PL: "rezus, makak królewski"},
    known_for=[{EN: "Rh blood group system"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rhesus_macaque_(Macaca_mulatta_mulatta)_female.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5e/Rhesus_macaque_%28Macaca_mulatta_mulatta%29_female.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
M_SPHINX = Species(
    name="Mandrillus sphinx",
    local_names={EN: "mandrill", PL: "mandryl barwnolicy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mandrill_at_SF_Zoo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9a/Mandrill_at_SF_Zoo.jpg",
        author="Sanjay Acharya",
        license=License.CC_BY_SA_4_0,
    ),
)
P_HAMADRYAS = Species(
    name="Papio hamadryas",
    local_names={EN: "sacred baboon, hamadryas baboon", PL: "pawian płaszczowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hamadryas_baboon.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/dd/Hamadryas_baboon.jpg",
        author="المُصوّر: مُعتز توفيق إغباريّة",
        license=License.CC_BY_SA_4_0,
    ),
)
C_DIANA = Species(
    name="Cercopithecus diana",
    local_names={EN: "Diana monkey", PL: "koczkodan Diany"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:2020-07-04_-_Dianameerkatze_(Cercopithecus_diana)_-_Tierpark_Gettorf_(10).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/2020-07-04_-_Dianameerkatze_%28Cercopithecus_diana%29_-_Tierpark_Gettorf_%2810%29.jpg",
        author="Fabian Horst",
        license=License.CC_BY_SA_4_0,
    ),
)
N_LARVATUS = Species(
    name="Nasalis larvatus",
    local_names={EN: "proboscis monkey", PL: "nosacz sundajski"},
    known_for=[
        {
            EN: "internet meme",
            URL: "https://knowyourmeme.com/photos/740852-reaction-images",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Proboscis_Monkey_in_Borneo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e5/Proboscis_Monkey_in_Borneo.jpg",
        author="David Dennis",
        license=License.CC_BY_SA_2_0,
    ),
)

MACACA = Genus(name="Macaca", children=[M_FUSCATA, M_MULATTA])
MANDRILLUS = Genus(name="Mandrillus", children=[M_SPHINX])
PAPIO = Genus(name="Papio", children=[P_HAMADRYAS])
CERCOPITHECUS = Genus(name="Cercopithecus", children=[C_DIANA])
NASALIS = Genus(name="Nasalis", children=[N_LARVATUS])

PAPIONINI_A = Clade(children=[MANDRILLUS, PAPIO])

PAPIONINI = Tribe(name="Papionini", children=[MACACA, PAPIONINI_A])
CERCOPITHECINI = Tribe(name="Cercopithecini", children=[CERCOPITHECUS])

CERCOPITHECINAE = Subfamily(
    name="Cercopithecinae", children=[PAPIONINI, CERCOPITHECINI]
)
COLOBINAE = Subfamily(name="Colobinae", children=[NASALIS])

CERCOPITHECIDAE = Family(name="Cercopithecidae", children=[CERCOPITHECINAE, COLOBINAE])

CERCOPITHECOIDEA = Superfamily(name="Cercopithecoidea", children=[CERCOPITHECIDAE])
