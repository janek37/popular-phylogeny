from clade import Clade, Family, Genus, Order, Species, Subfamily, Subgenus
from constants import EN, IMAGE, PL
from image import Image, License

S_ALBA = Species(
    name="Salix alba",
    local_names={EN: "white willow", PL: "wierzba biała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ruggell-Salix_Alba-Oskarietle-Obj_1103-04ASD.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/Ruggell-Salix_Alba-Oskarietle-Obj_1103-04ASD.jpg",
        author="Asurnipal",
        license=License.CC_BY_SA_4_0,
    ),
)
S_BABYLONICA = Species(
    name="Salix babylonica",
    local_names={EN: "weeping willow", PL: "wierzba płacząca, wierzba babilońska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Weeping_willow_in_Kingston_Hospital.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Weeping_willow_in_Kingston_Hospital.jpg",
        author="Secretlondon",
        license=License.CC_BY_SA_4_0,
    ),
)
P_TREMULA = Species(
    name="Populus tremula",
    local_names={PL: "osika", EN: "aspen"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Populus_tremula_Topola_osika_2020-07-02_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Populus_tremula_Topola_osika_2020-07-02_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)
P_ALBA = Species(
    name="Populus alba",
    local_names={PL: "topola biała", EN: "silver poplar"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Populus_alba,_Santa_Coloma_de_Farners.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Populus_alba%2C_Santa_Coloma_de_Farners.jpg",
        author="Josep Gesti",
        license=License.CC_BY_SA_4_0,
    ),
)
P_DELTOIDES = Species(
    name="Populus deltoides",
    local_names={EN: "eastern cottonwood, necklace poplar", PL: "topola deltoidalna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Populus_deltoides_monilifera_femalecatkins.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Populus_deltoides_monilifera_femalecatkins.jpg",
        author="Dave Powell, USDA Forest Service",
        license=License.CC_BY_3_0_US,
    ),
)
P_EDULIS = Species(
    name="Passiflora edulis",
    local_names={EN: "passion fruit", PL: "marakuja, męczennica jadalna"},
    known_for=[
        {
            EN: "edible fruit",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Passiflora_passion_fruit_cross_section_with_white_background.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Passiflora_passion_fruit_cross_section_with_white_background.jpg",
                author="Hans B. at Dutch Wikipedia",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flowers_of_Passiflora_edulis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flowers_of_Passiflora_edulis.jpg",
        author="Rehman Abubakr",
        license=License.CC_BY_SA_4_0,
    ),
)
P_INCARNATA = Species(
    name="Passiflora incarnata",
    local_names={EN: "maypop", PL: "kwiat Męki Pańskiej, męczennica cielista"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Passiflora_incarnata_002.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/73/Passiflora_incarnata_002.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
R_ARNOLDII = Species(
    name="Rafflesia arnoldii",
    local_names={EN: "giant padma", PL: "bukietnica Arnolda"},
    known_for=[{EN: "giant flowers imitating rotting flesh"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:RAFFLESIA_ARNOLDII.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/RAFFLESIA_ARNOLDII.jpg",
        author="Mhmd.fahrezzy",
        license=License.CC_BY_SA_4_0,
    ),
)
E_PULCHERRIMA = Species(
    name="Euphorbia pulcherrima",
    local_names={EN: "poinsettia", PL: "gwiazda betlejemska, wilczomlecz nadobny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Euphorbia_pulcherrima_07.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Euphorbia_pulcherrima_07.JPG",
        author="Vinayaraj",
        license=License.CC_BY_SA_3_0,
    ),
)
E_ESULA = Species(
    name="Euphorbia esula",
    local_names={PL: "wilczomlecz lancetowaty", EN: "leafy spurge"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20150722Euphorbia_esula4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/05/20150722Euphorbia_esula4.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
E_MILII = Species(
    name="Euphorbia milii",
    local_names={
        EN: "crown of thorns, Christ plant",
        PL: "korona cierniowa, wilczomlecz lśniący, wilczomlecz okazały",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Euphorbia_milii_2915.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Euphorbia_milii_2915.jpg",
        author="Vengolis",
        license=License.CC_BY_SA_4_0,
    ),
)
E_EPITHYMOIDES = Species(
    name="Euphorbia epithymoides",
    local_names={EN: "cushion spurge", PL: "wilczomlecz złocisty, wilczomlecz pstry"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Euphorbia_epithymoides_kz08.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/94/Euphorbia_epithymoides_kz08.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
E_TRIGONA = Species(
    name="Euphorbia trigona",
    local_names={
        EN: "African milk tree, cathedral cactus, Abyssinian euphorbia, high chaparall",
        PL: "wilczomlecz trójżebrowy",
    },
    known_for=[{EN: "one of the cactus-like euphorbias"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Euphorbia_trigona_-_leaves.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5d/Euphorbia_trigona_-_leaves.jpg",
        author="Juan Carlos Fonseca Mata",
        license=License.CC_BY_SA_4_0,
    ),
)
H_BRASILIENSIS = Species(
    name="Hevea brasiliensis",
    local_names={EN: "rubber tree", PL: "kauczukowiec brazylijski"},
    known_for=[{EN: "rubber", PL: "kauczuk"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hevea_brasiliensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-071.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Hevea_brasiliensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-071.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
V_ODORATA = Species(
    name="Viola odorata",
    local_names={PL: "fiołek wonny", EN: "wood violet"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Viola_odorata_Garden_060402Aw.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Viola_odorata_Garden_060402Aw.jpg",
        author="Strobilomyces",
        license=License.CC_BY_SA_3_0,
    ),
)
V_WITTROCKIANA = Species(
    name="Viola × wittrockiana",
    local_names={PL: "bratek ogrodowy, fiołek ogrodowy", EN: "garden pansy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Viola_%C3%97_wittrockiana_001.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ef/Viola_%C3%97_wittrockiana_001.jpg",
        author="Anelka",
        license=License.CC0,
    ),
)
H_PERFORATUM = Species(
    name="Hypericum perforatum",
    local_names={PL: "dziurawiec zwyczajny", EN: "perforate St John's-wort"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hypericum_perforatum,_flos_.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Hypericum_perforatum%2C_flos_.jpg",
        author="Taras-fedora-syn",
        license=License.CC_BY_SA_4_0,
    ),
)
E_COCA = Species(
    name="Erythroxylum coca",
    local_names={PL: "krasnodrzew pospolity", EN: "coca"},
    known_for=[
        {
            EN: "cocaine",
            PL: "kokaina",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Kokain_-_Cocaine.svg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Kokain_-_Cocaine.svg",
                author="NEUROtiker",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        },
        {
            EN: "Coca-Cola",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:CocaColaBottle_background_free.png",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/CocaColaBottle_background_free.png",
                author="CocaColaBottle_background_free.jpg: Jorgebarrios; derivative work: RanZag (talk)",
                license=License.CC_BY_SA_3_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coca_(Erythroxylum_coca)_en_Meta_(Colombia)_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e7/Coca_%28Erythroxylum_coca%29_en_Meta_%28Colombia%29_1.jpg",
        author="Danna Guevara",
        license=License.CC_BY_4_0,
    ),
)
M_ESCULENTA = Species(
    name="Manihot esculenta",
    local_names={PL: "maniok jadalny", EN: "cassava"},
    known_for=[
        {
            PL: "tapioka",
            EN: "tapioca",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:A_plate_of_Tapioca.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/c/c8/A_plate_of_Tapioca.jpg",
                author="Linason Blessing",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "edible tuberous root",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cassava_(2).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Cassava_%282%29.jpg",
                author="Renatosjoao",
                license=License.CC_BY_SA_4_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Manihot_esculenta_cassava_flower_vijayanrajapuram.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/Manihot_esculenta_cassava_flower_vijayanrajapuram.jpg",
        author="Vijayanrajapuram",
        license=License.CC_BY_SA_4_0,
    ),
)
R_COMMUNIS = Species(
    name="Ricinus communis",
    local_names={PL: "rącznik pospolity", EN: "castor bean"},
    known_for=[{PL: "rycyna", EN: "ricin"}, {PL: "olej rycynowy", EN: "castor oil"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ricinus_communis0.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/Ricinus_communis0.jpg",
        author="Kurt Stüber [1]",
        license=License.CC_BY_SA_3_0,
    ),
)
L_USITATISSIMUM = Species(
    name="Linum usitatissimum",
    local_names={PL: "len zwyczajny", EN: "flax, linseed"},
    known_for=[{EN: "linen"}, {EN: "linseed oil", PL: "olej lniany"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_Flax_or_Linseed_(Linum_usitatissimum)_flower._Chapeltoun_North_Ayrshire.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Common_Flax_or_Linseed_%28Linum_usitatissimum%29_flower._Chapeltoun_North_Ayrshire.jpg",
        author="Rosser1954",
        license=License.CC_BY_SA_4_0,
    ),
)

POPULUS_SECTION_POPULUS = Clade(
    name="Populus sect. Populus", children=[P_TREMULA, P_ALBA]
)  # Section
POPULUS_SECTION_AIGEIROS = Clade(
    name="Populus sect. Aigeiros", children=[P_DELTOIDES]
)  # Section

EUPHORBIA_SUBGENUS_CHAMAESYCE = Subgenus(
    name="Euphorbia subg. Chamaesyce", children=[E_PULCHERRIMA]
)
EUPHORBIA_SUBGENUS_ESULA = Subgenus(
    name="Euphorbia subg. Esula", children=[E_ESULA, E_EPITHYMOIDES]
)
EUPHORBIA_SUBGENUS_EUPHORBIA = Subgenus(
    name="Euphorbia subg. Euphorbia", children=[E_MILII, E_TRIGONA]
)

# https://www.semanticscholar.org/paper/Molecular-phylogeny-of-Euphorbia-subg.-Esula-sect.-Barres-Vilatersana/9b11a4173a044abfe1303714a82106d511e1dcd1
EUPHORBIA_A = Clade(
    children=[EUPHORBIA_SUBGENUS_CHAMAESYCE, EUPHORBIA_SUBGENUS_EUPHORBIA]
)

SALIX = Genus(name="Salix", children=[S_ALBA, S_BABYLONICA])
POPULUS = Genus(
    name="Populus", children=[POPULUS_SECTION_POPULUS, POPULUS_SECTION_AIGEIROS]
)
PASSIFLORA = Genus(name="Passiflora", children=[P_EDULIS, P_INCARNATA])
RAFFLESIA = Genus(name="Rafflesia", children=[R_ARNOLDII])
EUPHORBIA = Genus(name="Euphorbia", children=[EUPHORBIA_A, EUPHORBIA_SUBGENUS_ESULA])
HEVEA = Genus(name="Hevea", children=[H_BRASILIENSIS])
VIOLA = Genus(name="Viola", children=[V_ODORATA, V_WITTROCKIANA])
HYPERICUM = Genus(name="Hypericum", children=[H_PERFORATUM])
ERYTHROXYLUM = Genus(name="Erythroxylum", children=[E_COCA])
MANIHOT = Genus(name="Manihot", children=[M_ESCULENTA])
RICINUS = Genus(name="Ricinus", children=[R_COMMUNIS])
LINUM = Genus(name="Linum", children=[L_USITATISSIMUM])

EUPHORBIOIDEAE = Subfamily(name="Euphorbioideae", children=[EUPHORBIA])
CROTONOIDEAE = Subfamily(name="Crotonoideae", children=[HEVEA, MANIHOT])
ACALYPHOIDEAE = Subfamily(name="Acalyphoideae", children=[RICINUS])

# https://www.researchgate.net/publication/334479852_Euphorbiaceae_Phylogeny_Poster_-_Major_SubfamiliesSelected_Genera
EUPHORBIACEAE_A = Clade(children=[EUPHORBIOIDEAE, ACALYPHOIDEAE])

SALICACEAE = Family(name="Salicaceae", children=[SALIX, POPULUS])
PASSIFLORACEAE = Family(name="Passifloraceae", children=[PASSIFLORA])
RAFFLESIACEAE = Family(name="Rafflesiaceae", children=[RAFFLESIA])
EUPHORBIACEAE = Family(name="Euphorbiaceae", children=[EUPHORBIACEAE_A, CROTONOIDEAE])
VIOLACEAE = Family(name="Violaceae", children=[VIOLA])
HYPERICACEAE = Family(name="Hypericaceae", children=[HYPERICUM])
ERYTHROXYLACEAE = Family(name="Erythroxylaceae", children=[ERYTHROXYLUM])
LINACEAE = Family(name="Linaceae", children=[LINUM])

SALICOIDS = Clade(name="salicoids", children=[SALICACEAE, PASSIFLORACEAE])
RAFFLESIACEAE_EUPHORBIACEAE = Clade(children=[RAFFLESIACEAE, EUPHORBIACEAE])
EUPHORBIOIDS = Clade(
    name="euphorbioids", children=[RAFFLESIACEAE_EUPHORBIACEAE, LINACEAE]
)
PARIETAL_CLADE = Clade(name="parietal clade", children=[SALICOIDS, VIOLACEAE])

MALPIGHIALES_A = Clade(children=[PARIETAL_CLADE, EUPHORBIOIDS])
MALPIGHIALES_B = Clade(children=[HYPERICACEAE, ERYTHROXYLACEAE])

MALPIGHIALES = Order(name="Malpighiales", children=[MALPIGHIALES_A, MALPIGHIALES_B])
