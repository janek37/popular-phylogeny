from clade import Clade, Genus, Species, Subfamily, Subtribe, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

P_SATIVUM = Species(
    name="Pisum sativum",
    local_names={EN: "pea", PL: "groch zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Doperwt_rijserwt_peulen_Pisum_sativum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bc/Doperwt_rijserwt_peulen_Pisum_sativum.jpg",
        author="Rasbak",
        license=License.CC_BY_SA_3_0,
    ),
)
L_ODORATUS = Species(
    name="Lathyrus odoratus",
    local_names={EN: "sweat pea", PL: "groszek pachnący"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:P1000296_Lathyrus_odoratus_(Painted_Lady)_(Leguminosae).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/P1000296_Lathyrus_odoratus_%28Painted_Lady%29_%28Leguminosae%29.JPG",
        author="Magnus Manske",
        license=License.CC_BY_SA_3_0,
    ),
)
R_PSEUDOACACIA = Species(
    name="Robinia pseudoacacia",
    local_names={EN: "black locust, false acacia", PL: "robinia akacjowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20150513Robinia_pseudoacacia6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ea/20150513Robinia_pseudoacacia6.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
A_LINEARIS = Species(
    name="Aspalathus linearis",
    local_names={EN: "rooibos", PL: "aspalat prosty"},
    known_for=[
        {
            EN: "rooibos herbal tea",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Rooibos_geschnitten.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Rooibos_geschnitten.jpg",
                author="soultea.de/André Helbig",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rooibos_(Aspalathus_linearis).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/Rooibos_%28Aspalathus_linearis%29.jpg",
        author="Winfried Bruenken (Amrum)",
        license=License.CC_BY_SA_2_5,
    ),
)
L_ALBUS = Species(
    name="Lupinus albus",
    local_names={EN: "white lupin", PL: "łubin biały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Portrait_fleur_lupin86.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Portrait_fleur_lupin86.JPG",
        author="Regissierra",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
A_HYPOGAEA = Species(
    name="Arachis hypogaea",
    local_names={
        EN: "peanut",
        PL: "orzech ziemny, orzech arachidowy, orzacha podziemna",
    },
    known_for=[
        {
            EN: "peanuts",
            PL: "orzeszki ziemne, fistaszki",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Peanuts_(Arachis_hypogaea)_-_in_shell,_shell_cracked_open,_shelled,_peeled.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/fb/Peanuts_%28Arachis_hypogaea%29_-_in_shell%2C_shell_cracked_open%2C_shelled%2C_peeled.jpg",
                author="Ivar Leidus",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arachis_hypogaea_L._(3870805747).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Arachis_hypogaea_L._%283870805747%29.jpg",
        author="Dinesh Valke from Thane, India",
        license=License.CC_BY_SA_2_0,
    ),
)
C_ARIETINUM = Species(
    name="Cicer arietinum",
    local_names={EN: "chickpea", PL: "cieciorka, ciecierzyca pospolita"},
    known_for=[
        {
            EN: "chickpeas",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Ordinary_chickpeas_in_a_ceramic_bowl.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Ordinary_chickpeas_in_a_ceramic_bowl.jpg",
                author="AlixSaz",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "falafel",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Bowl_of_falafel.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/2c/Bowl_of_falafel.jpg",
                author="EvanProdromou",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "hummus",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Hummus.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/df/Hummus.jpg",
                author="Donovan Govan.",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "chana masala",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Chana_masala_(7326920034).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/f2/Chana_masala_%287326920034%29.jpg",
                author="pelican from Tokyo, Japan",
                license=License.CC_BY_SA_2_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cicer_arietinum_003.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Cicer_arietinum_003.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
G_MAX = Species(
    name="Glycine max",
    local_names={EN: "soybean", PL: "soja"},
    known_for=[
        {
            EN: "soy beans",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Soy_Beans_Photographed_by_Trisorn_Triboon_02.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Soy_Beans_Photographed_by_Trisorn_Triboon_02.jpg",
                author="Tris T7",
                license=License.CC_BY_3_0,
            ),
        },
        {
            EN: "soy sauce",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:SoySauceDSC00235.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/0/03/SoySauceDSC00235.jpg",
                author="kskbuddy",
                license=License.PUBLIC_DOMAIN_USER,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Glycine_max_pod_ripe2_Carol_Rose_(10220373194).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b0/Glycine_max_pod_ripe2_Carol_Rose_%2810220373194%29.jpg",
        author="Harry Rose from South West Rocks, Australia",
        license=License.CC_BY_2_0,
    ),
)
P_VULGARIS = Species(
    name="Phaseolus vulgaris",
    local_names={EN: "common bean", PL: "fasola zwykła"},
    known_for=[
        {
            EN: "beans",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Kidney_beans.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Kidney_beans.jpg",
                author="Sanjay Acharya",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "green beans, string beans",
            PL: "fasolka szparagowa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Green_beans_in_a_pile.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Green_beans_in_a_pile.JPG",
                author="Jeffery Martin",
                license=License.CC0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Snijboon_peulen_Phaseolus_vulgaris.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Snijboon_peulen_Phaseolus_vulgaris.jpg",
        author="Rasbak",
        license=License.CC_BY_SA_3_0,
    ),
)
T_PRATENSE = Species(
    name="Trifolium pratense",
    local_names={EN: "red clover", PL: "koniczyna łąkowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trifolium_pratense_0522.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Trifolium_pratense_0522.jpg",
        author="池田正樹 (talk)masaki ikeda",
        license=License.CC_BY_SA_3_0,
    ),
)
T_REPENS = Species(
    name="Trifolium repens",
    local_names={EN: "white clover", PL: "koniczyna biała"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr_070313-5645_Trifolium_repens.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/99/Starr_070313-5645_Trifolium_repens.jpg",
        author="Forest & Kim Starr",
        license=License.CC_BY_3_0,
    ),
)
V_FABA = Species(
    name="Vicia faba",
    local_names={EN: "broad bean", PL: "wyka bób"},
    known_for=[
        {
            EN: "broad beans",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Broad_bean_pile.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e0/Broad_bean_pile.jpg",
                author="Bodhi Peace",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vicia_faba,_also_known_as_the_broad_bean,_fava_bean,_faba_bean,_field_bean,_bell_bean,_or_tic_bean.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/de/Vicia_faba%2C_also_known_as_the_broad_bean%2C_fava_bean%2C_faba_bean%2C_field_bean%2C_bell_bean%2C_or_tic_bean.jpg",
        author="free photos; Uploaded by Vinayaraj",
        license=License.CC_BY_2_0,
    ),
)
L_CULINARIS = Species(
    name="Lens culinaris",
    local_names={EN: "lentil", PL: "soczewica jadalna"},
    known_for=[
        {
            EN: "lentils",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Lens_culinaris_seeds.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Lens_culinaris_seeds.jpg",
                author="Rainer Zenz at German Wikipedia",
                license=License.PUBLIC_DOMAIN_USER,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prof._Dr._Thom%C3%A9%27s_Flora_von_Deutschland,_%C3%96sterreich_und_der_Schweiz,_in_Wort_und_Bild,_f%C3%BCr_Schule_und_Haus;_mit_..._Tafeln_..._von_Walter_M%C3%BCller_(Pl._450)_(7982430575)a.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Prof._Dr._Thom%C3%A9%27s_Flora_von_Deutschland%2C_%C3%96sterreich_und_der_Schweiz%2C_in_Wort_und_Bild%2C_f%C3%BCr_Schule_und_Haus%3B_mit_..._Tafeln_..._von_Walter_M%C3%BCller_%28Pl._450%29_%287982430575%29a.png",
        author="Migula, Walter; Thomé, Otto W.",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
G_GLABRA = Species(
    name="Glycyrrhiza glabra",
    local_names={EN: "liquorice, licorice", PL: "lukrecja gładka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Glycyrrhiza_glabra_Y02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Glycyrrhiza_glabra_Y02.jpg",
        author="Юрий Данилевский",
        license=License.CC_BY_SA_4_0,
    ),
)
T_FOENUM_GRAECUM = Species(
    name="Trigonella foenum-graecum",
    local_names={EN: "fenugreek", PL: "kozieradka pospolita"},
    known_for=[
        {
            EN: "edible seeds",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Fenugreek-methi-seeds.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6a/Fenugreek-methi-seeds.jpg",
                author="Humbads at en.wikipedia",
                license=License.PUBLIC_DOMAIN_USER,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Illustration_Trigonella_foenum-graecum0_clean.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Illustration_Trigonella_foenum-graecum0_clean.jpg",
        author="Prof. Dr. Otto Wilhelm Thomé; derivative work: Ninjatacoshell (talk)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
V_RADIATA = Species(
    name="Vigna radiata",
    local_names={EN: "mung bean", PL: "fasolka mung, fasola złota"},
    known_for=[
        {
            EN: "mung beans",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Bean_pod_of_Vigna_radiata_(mung_bean).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Bean_pod_of_Vigna_radiata_%28mung_bean%29.jpg",
                author="Sanjay Acharya",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vigna_radiata_(5000647141).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2c/Vigna_radiata_%285000647141%29.jpg",
        author="Dinesh Valke from Thane, India",
        license=License.CC_BY_SA_2_0,
    ),
)

PISUM = Genus(name="Pisum", children=[P_SATIVUM])
LATHYRUS = Genus(name="Lathyrus", children=[L_ODORATUS])
ROBINIA = Genus(name="Robinia", children=[R_PSEUDOACACIA])
ASPALATHUS = Genus(name="Aspalathus", children=[A_LINEARIS])
LUPINUS = Genus(name="Lupinus", children=[L_ALBUS])
ARACHIS = Genus(name="Arachis", children=[A_HYPOGAEA])
CICER = Genus(name="Cicer", children=[C_ARIETINUM])
GLYCINE = Genus(name="Glycine", children=[G_MAX])
PHASEOLUS = Genus(name="Phaseolus", children=[P_VULGARIS])
TRIFOLIUM = Genus(name="Trifolium", children=[T_PRATENSE, T_REPENS])
VICIA = Genus(name="Vicia", children=[V_FABA])
LENS = Genus(name="Lens", children=[L_CULINARIS])
GLYCYRRHIZA = Genus(name="Glycyrrhiza", children=[G_GLABRA])
TRIGONELLA = Genus(name="Trigonella", children=[T_FOENUM_GRAECUM])
VIGNA = Genus(name="Vigna", children=[V_RADIATA])

# https://www.researchgate.net/publication/233989057_Systematics_biogeography_and_character_evolution_of_the_legume_tribe_Fabeae_with_special_focus_on_the_middle-Atlantic_island_lineages
PISUM_LATHYRUS = Clade(children=[PISUM, LATHYRUS])
VICIA_LENS = Clade(children=[VICIA, LENS])

GLYCININAE = Subtribe(name="Glycininae", children=[GLYCINE])
PHASEOLINAE = Subtribe(name="Phaseolinae", children=[PHASEOLUS, VIGNA])

FABEAE = Tribe(name="Fabeae", children=[PISUM_LATHYRUS, VICIA_LENS])
ROBINIEAE = Tribe(name="Robinieae", children=[ROBINIA])
CROTALARIEAE = Tribe(name="Crotalarieae", children=[ASPALATHUS])
GENISTEAE = Tribe(name="Genisteae", children=[LUPINUS])
CICEREAE = Tribe(name="Cicereae", children=[CICER])
PHASEOLEAE = Tribe(name="Phaseoleae", children=[GLYCININAE, PHASEOLINAE])
TRIFOLIEAE = Tribe(name="Trifolieae", children=[TRIFOLIUM, TRIGONELLA])
GLYCYRRHIZEAE = Tribe(name="Glycyrrhizeae", children=[GLYCYRRHIZA])

GENISTOIDS = Clade(name="Genistoids", children=[CROTALARIEAE, GENISTEAE])

# http://tolweb.org/IRLC_(Inverted_Repeat-lacking_clade)/60358
FABEAE_TRIFOLIAE = Clade(children=[FABEAE, TRIFOLIEAE])
VICIOIDS = Clade(name="vicioids", children=[FABEAE_TRIFOLIAE, CICEREAE])
IRLC = Clade(name="inverted repeat-lacking clade", children=[VICIOIDS, GLYCYRRHIZEAE])

HOLOGALEGINA = Clade(name="Hologalegina", children=[IRLC, ROBINIEAE])

NPAAA_CLADE = Clade(
    name="non-protein amino acid-accumulating clade",
    children=[HOLOGALEGINA, PHASEOLEAE],
)

FABOIDEAE = Subfamily(name="Faboideae", children=[NPAAA_CLADE, GENISTOIDS, ARACHIS])
