from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

S_ALBA = Species(
    name="Sinapis alba",
    local_names={EN: "white mustard", PL: "gorczyca biała"},
    known_for=[
        {
            EN: "yellow table mustard",
            PL: "musztarda stołowa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Field_Day%C2%A9_Mustard.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Field_Day%C2%A9_Mustard.jpg",
                author="Texas Lane",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sinapis_alba_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-265.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Sinapis_alba_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-265.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_VESICARIA = Species(
    name="Eruca vesicaria",
    local_names={EN: "rocket, arugola", PL: "rukola"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eruca_vesicaria_kz01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Eruca_vesicaria_kz01.jpg",
        author="Krzysztof Ziarnek, Kenraiz",
        license=License.CC_BY_SA_4_0,
    ),
)
L_SATIVUM = Species(
    name="Lepidium sativum",
    local_names={EN: "garden cress", PL: "rzeżucha, pieprzyca siewna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gartenkresse.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/Gartenkresse.jpg",
        author="de:Benutzer:Rainer Zenz",
        license=License.CC_BY_SA_3_0,
    ),
)
B_JUNCEA = Species(
    name="Brassica juncea",
    local_names={EN: "brown mustard", PL: "gorczyca sarepska, kapusta sitowata"},
    known_for=[
        {
            EN: "brown mustard",
            PL: "musztarda sarepska",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Musztarda_sarepska.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d7/Musztarda_sarepska.jpg",
                author="Artur Andrzej",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brassica_juncea-2-yercaud-salem-India.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Brassica_juncea-2-yercaud-salem-India.JPG",
        author="Yercaud-elango",
        license=License.CC_BY_SA_4_0,
    ),
)
B_OLERACEA = Species(
    name="Brassica oleracea",
    local_names={PL: "kapusta warzywna"},
    known_for=[
        {
            EN: "cabbage",
            PL: "kapusta",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Brassicales_-_Brassica_oleracea_convar._capitata_var._alba_2.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Brassicales_-_Brassica_oleracea_convar._capitata_var._alba_2.jpg",
                author="DenesFeri",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "broccoli",
            PL: "brokuł",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Broccoli_close_up_(49200262862).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Broccoli_close_up_%2849200262862%29.jpg",
                author="Alabama Extension",
                license=License.CC0,
            ),
        },
        {
            EN: "cauliflower",
            PL: "kalafior",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Brassica_oleracea_var_in_pabna.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/0/09/Brassica_oleracea_var_in_pabna.jpg",
                author="DelwarHossain",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "kale",
            PL: "jarmuż",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Boerenkool.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Boerenkool.jpg",
                author="Rasbak",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "Brussels sprouts",
            PL: "brukselka",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Rosenkohl-2.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Rosenkohl-2.jpg",
                author="Rainer Zenz",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "kohlrabi, German turnip",
            PL: "kalarepa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Brassicales_-_Brassica_oleraceae_var._gongylodes_1.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/86/Brassicales_-_Brassica_oleraceae_var._gongylodes_1.jpg",
                author="DenesFeri",
                license=License.CC_BY_SA_4_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brassica_oleracea_var._oleracea,_wilde_kool.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/13/Brassica_oleracea_var._oleracea%2C_wilde_kool.jpg",
        author="Georg Christian Oeder",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
B_RAPA = Species(
    name="Brassica rapa",
    local_names={PL: "kapusta właściwa"},
    known_for=[
        {
            EN: "turnip",
            PL: "rzepa",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Turnip_2622027.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Turnip_2622027.jpg",
                author="thebittenword.com",
                license=License.CC_BY_2_0,
            ),
        },
        {
            EN: "Napa cabbage, Chinese cabbage",
            PL: "kapusta pekińska",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:ChineseCabbage.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/ChineseCabbage.jpg",
                author="Jamie Nettles",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "bok choy",
            PL: "kapusta chińska",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Brassica_rapa_var._chinensis_(leaf).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/8c/Brassica_rapa_var._chinensis_%28leaf%29.jpg",
                author="おむこさん志望",
                license=License.CC_BY_2_5,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Brassica_rapa_(Raapzaad)_-_Overbosch,_Voorhout,_NL.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Brassica_rapa_%28Raapzaad%29_-_Overbosch%2C_Voorhout%2C_NL.jpg",
        author="Rudolphous",
        license=License.CC_BY_SA_4_0,
    ),
)
B_NAPUS = Species(
    name="Brassica napus",
    local_names={EN: "rapeseed, oilseed rape", PL: "kapusta rzepak"},
    known_for=[
        {
            PL: "brukiew",
            EN: "rutabaga, swede",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Rutabaga,_variety_nadmorska.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Rutabaga%2C_variety_nadmorska.JPG",
                author="Picasa user Seedambassadors",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oilsseed_rape_(Brassica_napus)_-_geograph.org.uk_-_2911885.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Oilsseed_rape_%28Brassica_napus%29_-_geograph.org.uk_-_2911885.jpg",
        author="Sandy B",
        license=License.CC_BY_SA_2_0,
    ),
)
R_RAPHANISTRUM = Species(
    name="Raphanus raphanistrum",
    local_names={EN: "radish", PL: "rzodkiew zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Radijs_planten_(Raphanus_sativus_subsp._sativus).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/77/Radijs_planten_%28Raphanus_sativus_subsp._sativus%29.jpg",
        author="Rasbak",
        license=License.CC_BY_SA_3_0,
    ),
)
A_RUSTICANA = Species(
    name="Armoracia rusticana",
    local_names={EN: "horseradish", PL: "chrzan pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20160723Armoracia_rusticana2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/89/20160723Armoracia_rusticana2.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
E_JAPONICUM = Species(
    name="Eutrema japonicum",
    local_names={EN: "wasabi", PL: "wasabi, chrzan japoński"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wasabi_japonica.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/91/Wasabi_japonica.jpg",
        author="Kassy2",
        license=License.CC_BY_SA_4_0,
    ),
)
C_PAPAYA = Species(
    name="Carica papaya",
    local_names={EN: "papaya", PL: "papaja, melonowiec właściwy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carica_papaya_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-029.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Carica_papaya_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-029.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
R_ODORATA = Species(
    name="Reseda odorata",
    local_names={EN: "garden mignonette", PL: "rezeda wonna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Reseda_odorata_1787.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Reseda_odorata_1787.jpg",
        author="James Sowerby",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_MAJUS = Species(
    name="Tropaeolum majus",
    local_names={EN: "garden nasturtium", PL: "nasturcja większa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tropaeolum_majus_A.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Tropaeolum_majus_A.jpg",
        author="Wouter Hagens",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
C_SPINOSA = Species(
    name="Capparis spinosa",
    local_names={EN: "caper", PL: "kapary cierniste"},
    known_for=[
        {
            EN: "capers",
            PL: "kapary",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Capers_jar.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/f0/Capers_jar.jpg",
                author="Whitebox at en.wikipedia",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Capparis_spinosa-IMG_3417.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Capparis_spinosa-IMG_3417.jpg",
        author="C T Johansson",
        license=License.CC_BY_SA_3_0,
    ),
)
M_LONGIPETALA = Species(
    name="Matthiola longipetala",
    local_names={EN: "evening stock", PL: "maciejka, lewkonia długopłatkowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Matthiola_longipetala.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Matthiola_longipetala.jpg",
        author="en:User:Al-Bargit",
        license=License.CC_BY_SA_3_0,
    ),
)

SINAPIS = Genus(name="Sinapis", children=[S_ALBA])
ERUCA = Genus(name="Eruca", children=[E_VESICARIA])
LEPIDIUM = Genus(name="Lepidium", children=[L_SATIVUM])
# research returned conflicting phylogenies of Brassica species
BRASSICA = Genus(name="Brassica", children=[B_JUNCEA, B_OLERACEA, B_RAPA, B_NAPUS])
RAPHANUS = Genus(name="Raphanus", children=[R_RAPHANISTRUM])
ARMORACIA = Genus(name="Armoracia", children=[A_RUSTICANA])
EUTREMA = Genus(name="Eutrema", children=[E_JAPONICUM])
CARICA = Genus(name="Carica", children=[C_PAPAYA])
RESEDA = Genus(name="Reseda", children=[R_ODORATA])
TROPAEOLUM = Genus(name="Tropaeolum", children=[T_MAJUS])
CAPPARIS = Genus(name="Capparis", children=[C_SPINOSA])
MATTHIOLA = Genus(name="Matthiola", children=[M_LONGIPETALA])

# https://www.researchgate.net/publication/283890506_Genetic_Differentiation_Molecular_Phylogenetic_Analysis_and_Ethnobotanical_Study_of_Eutrema_japonicum_and_E_tenue_in_Japan_and_E_yunnanense_in_China
BRASSICEAE_A = Clade(children=[BRASSICA, RAPHANUS])
BRASSICEAE_B = Clade(children=[BRASSICEAE_A, ERUCA])

BRASSICEAE = Tribe(name="Brassiceae", children=[SINAPIS, BRASSICEAE_B])
LEPIDIEAE = Tribe(name="Lepidieae", children=[LEPIDIUM])
CARDAMINEAE = Tribe(name="Cardamineae", children=[ARMORACIA])
EUTREMEAE = Tribe(name="Eutremeae", children=[EUTREMA])
ANCHONIEAE = Tribe(name="Anchonieae", children=[MATTHIOLA])

BRASSICACEAE_A = Clade(children=[BRASSICEAE, EUTREMEAE])
BRASSICACEAE_B = Clade(children=[LEPIDIEAE, CARDAMINEAE])
BRASSICACEAE_C = Clade(children=[BRASSICACEAE_A, ANCHONIEAE])

BRASSICACEAE = Family(name="Brassicaceae", children=[BRASSICACEAE_C, BRASSICACEAE_B])
CARICACEAE = Family(name="Caricaceae", children=[CARICA])
RESEDACEAE = Family(name="Resedaceae", children=[RESEDA])
TROPAEOLACEAE = Family(name="Tropaeolaceae", children=[TROPAEOLUM])
CAPPARACEAE = Family(name="Capparaceae", children=[CAPPARIS])

# https://www.researchgate.net/publication/51179989_Embryology_of_Koeberlinia_Koeberliniaceae_Evidence_for_core-Brassicalean_affinities
BRASSICALES_A = Clade(children=[BRASSICACEAE, CAPPARACEAE])
BRASSICALES_B = Clade(children=[BRASSICALES_A, RESEDACEAE])
BRASSICALES_C = Clade(children=[BRASSICALES_B, CARICACEAE])

BRASSICALES = Order(name="Brassicales", children=[BRASSICALES_C, TROPAEOLACEAE])
