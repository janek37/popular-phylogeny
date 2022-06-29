from clade import Clade, Family, Genus, Order, Species, Subfamily, Subtribe, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

D_CARYOPHYLLUS = Species(
    name="Dianthus caryophyllus",
    local_names={EN: "carnation, clove pink", PL: "goździk ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dianthus_caryophyllus_apollo-2-xavier_cottage-yercaud-salem-India.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Dianthus_caryophyllus_apollo-2-xavier_cottage-yercaud-salem-India.jpg",
        author="Yercaud-elango",
        license=License.CC_BY_SA_4_0,
    ),
)
A_GITHAGO = Species(
    name="Agrostemma githago",
    local_names={EN: "common corn-cockle", PL: "kąkol polny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Agrostemma_githago_sl12.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Agrostemma_githago_sl12.jpg",
        author="Stefan.lefnaer",
        license=License.CC_BY_SA_4_0,
    ),
)
B_VULGARIS = Species(
    name="Beta vulgaris",
    local_names={EN: "beet", PL: "burak zwyczajny"},
    known_for=[
        {EN: "sugar beet", PL: "burak cukrowy"},
        {EN: "mangelwurzel", PL: "burak pastewny"},
        {EN: "chard", PL: "boćwina, burak liściowy"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Beta_vulgaris_L.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/68/Beta_vulgaris_L.jpg",
        author="Kagor",
        license=License.CC_BY_SA_3_0,
    ),
)
D_ROTUNDIFOLIA = Species(
    name="Drosera rotundifolia",
    local_names={EN: "round-leaved sundew", PL: "rosiczka okrągłolistna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Drosera_rotundifolia_Common_Sundew,_Round-leaved_Sundew)_primary_1_NH_20100718_Beth_Zimmer_Round_Leafed_Sundew_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/61/Drosera_rotundifolia_Common_Sundew%2C_Round-leaved_Sundew%29_primary_1_NH_20100718_Beth_Zimmer_Round_Leafed_Sundew_02.jpg",
        author="Sarkan47",
        license=License.CC_BY_SA_4_0,
    ),
)
D_MUSCIPULA = Species(
    name="Dionaea muscipula",
    local_names={EN: "Venus flytrap", PL: "muchołówka amerykańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Venus_Fly_Trap_(Dionaea_muscipula)_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Venus_Fly_Trap_%28Dionaea_muscipula%29_2.jpg",
        author="Mokkie",
        license=License.CC_BY_SA_4_0,
    ),
)
N_MIRABILIS = Species(
    name="Nepenthes mirabilis",
    local_names={EN: "common swamp pitcher-plant", PL: "dzbanecznik przedziwny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:N%E1%BA%AFp_%E1%BA%A5m.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/N%E1%BA%AFp_%E1%BA%A5m.jpg",
        author="Bùi Thụy Đào Nguyên",
        license=License.CC_BY_SA_3_0,
    ),
)
S_OLERACEA = Species(
    name="Spinacia oleracea",
    local_names={EN: "spinach", PL: "szpinak warzywny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:NdP_Spinacia_oleracea.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5e/NdP_Spinacia_oleracea.png",
        author="Gotthilf Heinrich von Schubert; File:Naturgeschichte des Pflanzenreichs Tafel XLIX.jpg: Аимаина хикари",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
R_HYBRIDUM = Species(
    name="Rheum × hybridum",
    local_names={EN: "rhubarb", PL: "rabarbar"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rheum.rhabarbarum.2515.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Rheum.rhabarbarum.2515.JPG",
        author="Chris.urs-o",
        license=License.CC_BY_SA_3_0,
    ),
)
C_QUINOA = Species(
    name="Chenopodium quinoa",
    local_names={EN: "quinoa", PL: "komosa ryżowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Quinoa_Chenopodium_quinoa.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Quinoa_Chenopodium_quinoa.jpg",
        author="Mohammed Shahid, International Center for Biosaline Agriculture",
        license=License.CC_BY_SA_4_0,
    ),
)
K_TRAGUS = Species(
    name="Kali tragus",
    local_names={EN: "tumbleweed, prickly Russian thistle"},
    known_for=[
        {
            EN: "most common tumbleweed plant",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Tumbleweed_038.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Tumbleweed_038.jpg",
                author="ImperfectTommy  / Edmond Meinfelder",
                license=License.CC_BY_2_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Salsola_kali_Habitus_CampodeCalatrava.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Salsola_kali_Habitus_CampodeCalatrava.jpg",
        author="Javier martin",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
F_ESCULENTUM = Species(
    name="Fagopyrum esculentum",
    local_names={EN: "buckwheat", PL: "gryka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fagopyrum_esculentum_kz07.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Fagopyrum_esculentum_kz07.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
R_ACETOSA = Species(
    name="Rumex acetosa",
    local_names={EN: "sorrel", PL: "szczaw zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rumex_acetosa_(Reichenbach_1909,_vol.24_0339)_clean,_no-description,_squared.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/Rumex_acetosa_%28Reichenbach_1909%2C_vol.24_0339%29_clean%2C_no-description%2C_squared.jpg",
        author="Reichenbach, Heinrich Gottlieb Ludwig; Reichenbach, Heinrich Gustav;",
        license=License.CC_BY_SA_4_0,
    ),
)
S_BUCKLEYI = Species(
    name="Schlumbergera × buckleyi",
    local_names={EN: "Christmas cactus", PL: "szlumbergera, kaktus bożonarodzeniowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schlumbergera_buckleyi_WPC3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ee/Schlumbergera_buckleyi_WPC3.jpg",
        author="Wayne Ray User:WayneRay",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
S_UNDATUS = Species(
    name="Selenicereus undatus",
    local_names={EN: "white-fleshed pitahaya", PL: "pitaja"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hylocereus_undatus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b7/Hylocereus_undatus.jpg",
        author="Prenn",
        license=License.CC_BY_SA_3_0,
    ),
)
M_HAHNIANA = Species(
    name="Mammillaria hahniana",
    local_names={EN: "old lady cactus", PL: "wymion, mamilaria"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mammillaria_hahniana_3zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Mammillaria_hahniana_3zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
O_MICRODASYS = Species(
    name="Opuntia microdasys",
    local_names={EN: "bunny ear cactus", PL: "opuncja drobnokolczasta"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Opuntia_microdasys_3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/36/Opuntia_microdasys_3.jpg",
        author="Stan Shebs",
        license=License.CC_BY_SA_3_0,
    ),
)
L_WILLIAMSII = Species(
    name="Lophophora williamsii",
    local_names={EN: "peyote", PL: "pejotl, jazgrza Williamsa"},
    known_for=[{EN: "psychoactive mescaline"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lophophora_williamsii_Bl%C3%BCte.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Lophophora_williamsii_Bl%C3%BCte.JPG",
        author="Dav Hir",
        license=License.CC_BY_SA_3_0,
    ),
)
A_ASTERIAS = Species(
    name="Astrophytum asterias",
    local_names={EN: "sand dollar cactus"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Astrophytum_asterias_nudum_3.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Astrophytum_asterias_nudum_3.JPG",
        author="Petar43",
        license=License.CC_BY_SA_4_0,
    ),
)
E_GRUSONII = Species(
    name="Echinocactus grusonii",
    local_names={
        EN: "golden barrel cactus, mother in law's cushion",
        PL: "złota beczka, poduszka/fotel teściowej",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Echinocactus_grusonii.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b9/Echinocactus_grusonii.JPG",
        author="Ripepette",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
C_GIGANTEA = Species(
    name="Carnegiea gigantea",
    local_names={EN: "saguaro", PL: "karnegia olbrzymia"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson,_Arizona_during_November_(63).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e7/Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson%2C_Arizona_during_November_%2863%29.jpg",
        author="WClarke",
        license=License.CC_BY_SA_3_0,
    ),
)
P_AVICULARE = Species(
    name="Polygonum aviculare",
    local_names={EN: "common knotgrass", PL: "rdest zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Polygonum_aviculare_Sturm63.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/33/Polygonum_aviculare_Sturm63.jpg",
        author="Johann Georg Sturm (Painter: Jacob Sturm)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)

DIANTHUS = Genus(name="Dianthus", children=[D_CARYOPHYLLUS])
AGROSTEMMA = Genus(name="Agrostemma", children=[A_GITHAGO])
BETA = Genus(name="Beta", children=[B_VULGARIS])
DROSERA = Genus(name="Drosera", children=[D_ROTUNDIFOLIA])
DIONAEA = Genus(name="Dionaea", children=[D_MUSCIPULA])
NEPENTHES = Genus(name="Nepenthes", children=[N_MIRABILIS])
SPINACIA = Genus(name="Spinacia", children=[S_OLERACEA])
RHEUM = Genus(name="Rheum", children=[R_HYBRIDUM])
CHENOPODIUM = Genus(name="Chenopodium", children=[C_QUINOA])
KALI = Genus(name="Kali", children=[K_TRAGUS])
FAGOPYRUM = Genus(name="Fagopyrum", children=[F_ESCULENTUM])
RUMEX = Genus(name="Rumex", children=[R_ACETOSA])
SCHLUMBERGERA = Genus(name="Schlumbergera", children=[S_BUCKLEYI])
SELENICEREUS = Genus(name="Selenicereus", children=[S_UNDATUS])
MAMMILARIA = Genus(name="Mammilaria", children=[M_HAHNIANA])
OPUNTIA = Genus(name="Opuntia", children=[O_MICRODASYS])
LOPHOMORA = Genus(name="Lophomora", children=[L_WILLIAMSII])
ASTROPHYTUM = Genus(name="Astrophytum", children=[A_ASTERIAS])
ECHINOCACTUS = Genus(name="Echinocactus", children=[E_GRUSONII])
CARNEGIEA = Genus(name="Carnegiea", children=[C_GIGANTEA])
POLYGONUM = Genus(name="Polygonum", children=[P_AVICULARE])

CACTINAE = Subtribe(name="Cactinae", children=[MAMMILARIA])

# https://www.semanticscholar.org/paper/Phylogenetic-relationships-and-evolution-of-growth-Hernández-Hernández-Hernández
CACTEAE_A = Clade(children=[CACTINAE, LOPHOMORA])
CACTEAE_B = Clade(children=[ASTROPHYTUM, ECHINOCACTUS])

BETEAE = Tribe(name="Beteae", children=[BETA])
FAGOPYREAE = Tribe(name="Fagopyreae", children=[FAGOPYRUM])
RUMICEAE = Tribe(name="Rumiceae", children=[RHEUM, RUMEX])
SALSOLEAE = Tribe(name="Salsoleae", children=[KALI])
CACTEAE = Tribe(name="Cacteae", children=[CACTEAE_A, CACTEAE_B])
RHIPSALIDEAE = Tribe(name="Rhipsalideae", children=[SCHLUMBERGERA])
HYLOCEREEAE = Tribe(name="Hylocereeae", children=[SELENICEREUS])
ECHINOCEREEAE = Tribe(name="Echinocereeae", children=[CARNEGIEA])
POLYGONEAE = Tribe(name="Polygoneae", children=[POLYGONUM])

# https://www.semanticscholar.org/paper/Phylogeny-and-evolution-of-the-epiphytic-(-)-Korotkova/4b7d67f2043a8fcd0f2797fa5b76c5a35e92273a
PHYLLOCACTEAE = Clade(name="Phyllocacteae", children=[HYLOCEREEAE, ECHINOCEREEAE])
CACTOIDEAE_A = Clade(children=[RHIPSALIDEAE, PHYLLOCACTEAE])

# https://www.researchgate.net/publication/351448060_The_complete_chloroplast_genome_of_the_medicinal_plant_Polygonum_cuspidatum_Polygonaceae_and_its_phylogenetic_implications_within_the_subfamily_Polygonoideae
POLYGONOIDEAE_A = Clade(children=[RUMICEAE, POLYGONEAE])

CHENOPODIOIDEAE = Subfamily(name="Chenopodioideae", children=[SPINACIA, CHENOPODIUM])
CACTOIDEAE = Subfamily(name="Cactoideae", children=[CACTEAE, CACTOIDEAE_A])
OPUNTIOIDEAE = Subfamily(name="Opuntioideae", children=[OPUNTIA])
BETOIDEAE = Subfamily(name="Betoideae", children=[BETEAE])
SALSOLOIDEAE = Subfamily(name="Salsoloideae", children=[SALSOLEAE])
POLYGONOIDEAE = Subfamily(name="Polygonoideae", children=[POLYGONOIDEAE_A, FAGOPYREAE])

AMARANTHACEAE_A = Clade(children=[BETOIDEAE, CHENOPODIOIDEAE])

CARYOPHYLLACEAE = Family(name="Caryophyllaceae", children=[DIANTHUS, AGROSTEMMA])
AMARANTHACEAE = Family(name="Amaranthaceae", children=[AMARANTHACEAE_A, SALSOLOIDEAE])
DROSERACEAE = Family(name="Droseraceae", children=[DROSERA, DIONAEA])
NEPENTHACEAE = Family(name="Nepenthaceae", children=[NEPENTHES])
POLYGONACEAE = Family(name="Polygonaceae", children=[POLYGONOIDEAE])
CACTACEAE = Family(name="Cactaceae", children=[CACTOIDEAE, OPUNTIOIDEAE])

# https://www.researchgate.net/publication/225486253_The_distribution_of_ester-linked_ferulic_acid_in_the_cell_walls_of_angiosperms
CARYOPHYLLACEAE_AMARANTHACEAE = Clade(children=[CARYOPHYLLACEAE, AMARANTHACEAE])
DROSERACEAE_NEPENTHACEAE = Clade(children=[DROSERACEAE, NEPENTHACEAE])
CARYOPHYLLALES_A = Clade(children=[CARYOPHYLLACEAE_AMARANTHACEAE, CACTACEAE])
CARYOPHYLLALES_B = Clade(children=[DROSERACEAE_NEPENTHACEAE, POLYGONACEAE])

CARYOPHYLLALES = Order(
    name="Caryophyllales", children=[CARYOPHYLLALES_A, CARYOPHYLLALES_B]
)
