from clade import Clade, Family, Genus, Species, Subfamily
from constants import EN, PL
from image import Image, License

F_COELEBS = Species(
    name="Fringilla coelebs",
    local_names={EN: "common chaffinch", PL: "zięba zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fringilla_coelebs_on_branch.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/45/Fringilla_coelebs_on_branch.jpg",
        author="Martin Kunz",
        license=License.CC_BY_3_0,
    ),
)
P_PYRRHULA = Species(
    name="Pyrrhula pyrrhula",
    local_names={EN: "Eurasian bullfinch", PL: "gil zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pyrrhula_Pyrrhula_Kittila_20120305.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/02/Pyrrhula_Pyrrhula_Kittila_20120305.JPG",
        author="Estormiz",
        license=License.CC0,
    ),
)
L_CANNABINA = Species(
    name="Linaria cannabina",
    local_names={EN: "common linnet", PL: "makolągwa zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carduelis_cannabina_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Carduelis_cannabina_2.jpg",
        author="Wilhelm von Wright",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_CARDUELIS = Species(
    name="Carduelis carduelis",
    local_names={EN: "European goldfinch", PL: "szczygieł"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Goldfinch_(Carduelis_carduelis)_adult.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2b/Goldfinch_%28Carduelis_carduelis%29_adult.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_3_0,
    ),
)
S_CANARIA = Species(
    name="Serinus canaria",
    local_names={EN: "wild cannary, common cannary, Atlantic cannary", PL: "kanarek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Serinus_canaria_-Parque_Rural_del_Nublo,_Gran_Canaria,_Spain_-male-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/Serinus_canaria_-Parque_Rural_del_Nublo%2C_Gran_Canaria%2C_Spain_-male-8a.jpg",
        author="Juan Emilio",
        license=License.CC_BY_SA_2_0,
    ),
)
S_SPINUS = Species(
    name="Spinus spinus",
    local_names={EN: "Eurasian siskin, common siskin", PL: "czyżyk, czyż zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carduelis_spinus_male.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Carduelis_spinus_male.jpg",
        author="Sławek Staszczuk (photoss [AT] hotmail.co.uk)",
        license=License.CC_BY_SA_3_0,
    ),
)
S_TRISTIS = Species(
    name="Spinus tristis",
    local_names={EN: "American goldfinch", PL: "czyż złotawy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carduelis-tristis-001.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Carduelis-tristis-001.jpg",
        author="Mdf",
        license=License.CC_BY_SA_3_0,
    ),
)

FRINGILLA = Genus(name="Fringilla", children=[F_COELEBS])
PYRRHULA = Genus(name="Pyrrhula", children=[P_PYRRHULA])
LINARIA = Genus(name="Linaria", children=[L_CANNABINA])
CARDUELIS = Genus(name="Carduelis", children=[C_CARDUELIS])
SERINUS = Genus(name="Serinus", children=[S_CANARIA])
SPINUS = Genus(name="Spinus", children=[S_SPINUS, S_TRISTIS])

CARDUELINAE_A = Clade(children=[SERINUS, SPINUS])
CARDUELINAE_B = Clade(children=[CARDUELIS, CARDUELINAE_A])
CARDUELINAE_C = Clade(children=[LINARIA, CARDUELINAE_B])

FRINGILLINAE = Subfamily(name="Fringillinae", children=[FRINGILLA])
CARDUELINAE = Subfamily(name="Carduelinae", children=[PYRRHULA, CARDUELINAE_C])

FRINGILLIDAE = Family(name="Fringillidae", children=[FRINGILLINAE, CARDUELINAE])
