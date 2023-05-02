from clade import Clade, Family, Genus, Order, Species, Subfamily, Tribe
from constants import EN, PL
from image import Image, License

P_ANISUM = Species(
    name="Pimpinella anisum",
    local_names={EN: "anise, aniseed", PL: "anyżek, biedrzeniec anyż"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Koehler1887-PimpinellaAnisum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Koehler1887-PimpinellaAnisum.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_AMMI = Species(
    name="Trachyspermum ammi",
    local_names={EN: "ajwain, ajowan, carom", PL: "indyjski kminek, chropawiec wonny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carom_Flowers.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Carom_Flowers.jpg",
        author="Bames24",
        license=License.CC_BY_SA_3_0,
    ),
)
C_MACULATUM = Species(
    name="Conium maculatum",
    local_names={EN: "poison hemlock", PL: "szczwół plamisty"},
    known_for=[{EN: "the death of Socrates"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Conium_maculatum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-191.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c2/Conium_maculatum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-191.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen (text on p. 154, illustrations in back)",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_SATIVUM = Species(
    name="Coriandrum sativum",
    local_names={EN: "coriander, cilantro", PL: "kolendra siewna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kolendra_siewna._(Coriandrum_sativum_L.)_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Kolendra_siewna._%28Coriandrum_sativum_L.%29_02.jpg",
        author="Niepokój Zbigniew",
        license=License.CC_BY_SA_4_0,
    ),
)
P_SATIVA = Species(
    name="Pastinaca sativa",
    local_names={EN: "parsnip", PL: "pasternak zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20170718Pastinaca_sativa1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/20170718Pastinaca_sativa1.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
C_CARVI = Species(
    name="Carum carvi",
    local_names={EN: "caraway, meridian fennel, Persian cumin", PL: "kminek zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:261_Carum_carvi.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/261_Carum_carvi.jpg",
        author="Carl Axel Magnus Lindman",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_PODAGRARIA = Species(
    name="Aegopodium podagraria",
    local_names={EN: "ground elder", PL: "podagrycznik pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aegopodium_podagraria_RF.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Aegopodium_podagraria_RF.jpg",
        author="Robert Flogaus-Faust",
        license=License.CC_BY_4_0,
    ),
)
A_CYNAPIUM = Species(
    name="Aethusa cynapium",
    local_names={EN: "fool's parsley", PL: "blekot pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Illustration_Aethusa_cynapium0_clean.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ec/Illustration_Aethusa_cynapium0_clean.jpg",
        author="User:Kilom691",
        license=License.CC_BY_SA_3_0,
    ),
)
O_CROCATA = Species(
    name="Oenanthe crocata",
    local_names={
        EN: "hemlock water-dropwort, dead man's fingers",
        PL: "kropidło szafranowe",
    },
    known_for=[{EN: "sardonic smile", PL: "uśmiech sardoniczny"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oenanthe_crocata_sward_at_Marden.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/df/Oenanthe_crocata_sward_at_Marden.jpg",
        author="Alex Lockton",
        license=License.CC_BY_SA_4_0,
    ),
)
L_OFFICINALE = Species(
    name="Levisticum officinale",
    local_names={EN: "lovage", PL: "lubczyk ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Liebstoeckel_roscheiderhof_H1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/18/Liebstoeckel_roscheiderhof_H1.jpg",
        author="Helge Klaus Rieder",
        license=License.CC0,
    ),
)
ANETHUM_GRAVEOLENS = Species(
    name="Anethum graveolens",
    local_names={EN: "dill", PL: "koper ogrodowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dill_(Anethum_graveolens).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9f/Dill_%28Anethum_graveolens%29.jpg",
        author="Burkhard Mücke",
        license=License.CC_BY_SA_4_0,
    ),
)
F_VULGARE = Species(
    name="Foeniculum vulgare",
    local_names={EN: "fennel", PL: "koper włoski, fenkuł włoski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Schiermonnikoog_-_Venkel_(Foeniculum_vulgare).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/Schiermonnikoog_-_Venkel_%28Foeniculum_vulgare%29.jpg",
        author="Rudolphous",
        license=License.CC_BY_SA_4_0,
    ),
)
APIUM_GRAVEOLENS = Species(
    name="Apium graveolens",
    local_names={EN: "celery, celeriac", PL: "seler zwyczajny, selery zwyczajne"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Apium_graveolens_002.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Apium_graveolens_002.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
E_MARITIMUM = Species(
    name="Eryngium maritimum",
    local_names={EN: "sea holly, seaside eryngo", PL: "mikołajek nadmorski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eryngium_maritimum_139000661.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Eryngium_maritimum_139000661.jpg",
        author="Michel Langeveld",
        license=License.CC_BY_SA_4_0,
    ),
)
D_CAROTA = Species(
    name="Daucus carota",
    local_names={EN: "carrot, wild carrot", PL: "marchew uprawna, marchew zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carotts_(Daucus_Carotta).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1c/Carotts_%28Daucus_Carotta%29.jpg",
        author="Randal.b",
        license=License.CC_BY_SA_3_0,
    ),
)
H_SOSNOWSKYI = Species(
    name="Heracleum sosnowskyi",
    local_names={EN: "Sosnowsky's hogweed", PL: "barszcz Sosnowskiego"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Barszcz_Sosnowskiego_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b7/Barszcz_Sosnowskiego_03.jpg",
        author="Jacek Proszyk",
        license=License.CC0,
    ),
)
P_CRISPUM = Species(
    name="Petroselinum crispum",
    local_names={EN: "common parsley", PL: "pietruszka zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Petroselinum_crispum_var._tuberosum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/ba/Petroselinum_crispum_var._tuberosum.jpg",
        author="Yelkrokoyade",
        license=License.CC_BY_SA_3_0,
    ),
)
C_VIROSA = Species(
    name="Cicuta virosa",
    local_names={EN: "cowbane, northern water hemlock", PL: "szalej jadowity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cicuta_virosa_creutzwald_57_02072005_1.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Cicuta_virosa_creutzwald_57_02072005_1.JPG",
        author="Olivier Pichard",
        license=License.CC_BY_SA_3_0,
    ),
)
H_HELIX = Species(
    name="Hedera helix",
    local_names={EN: "common ivy", PL: "bluszcz pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Hedera_helix_116923327.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/Hedera_helix_116923327.jpg",
        author="Daniel Das",
        license=License.CC0,
    ),
)
P_GINSENG = Species(
    name="Panax ginseng",
    local_names={EN: "ginseng", PL: "wszechlek żeń-szeń"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Korean_ginseng_on_snow.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/84/Korean_ginseng_on_snow.jpg",
        author="Scudsvlad",
        license=License.CC_BY_SA_4_0,
    ),
)
C_CYMINUM = Species(
    name="Cuminum cyminum",
    local_names={EN: "cumin", PL: "kmin rzymski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cuminum_cyminum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-198.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Cuminum_cyminum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-198.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_ARCHANGELICA = Species(
    name="Angelica archangelica",
    local_names={EN: "garden angelica", PL: "arcydzięgiel lekarski, dzięgiel litwor"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Angelica_archangelica_subsp._archangelica_Dzi%C4%99giel_litwor_2013-06-23_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/df/Angelica_archangelica_subsp._archangelica_Dzi%C4%99giel_litwor_2013-06-23_02.jpg",
        author="Agnieszka Kwiecień, Nova",
        license=License.CC_BY_SA_4_0,
    ),
)

PIMPINELLA = Genus(name="Pimpinella", children=[P_ANISUM])
TRACHYSPERMUM = Genus(name="Trachyspermum", children=[T_AMMI])
CONIUM = Genus(name="Conium", children=[C_MACULATUM])
CORIANDRUM = Genus(name="Coriandrum", children=[C_SATIVUM])
PASTINACA = Genus(name="Pastinaca", children=[P_SATIVA])
CARUM = Genus(name="Carum", children=[C_CARVI])
AEGOPODIUM = Genus(name="Aegopodium", children=[A_PODAGRARIA])
AETHUSA = Genus(name="Aethusa", children=[A_CYNAPIUM])
OENANTHE = Genus(name="Oenanthe", children=[O_CROCATA])
ANETHUM = Genus(name="Anethum", children=[ANETHUM_GRAVEOLENS])
FOENICULUM = Genus(name="Foeniculum", children=[F_VULGARE])
APIUM = Genus(name="Apium", children=[APIUM_GRAVEOLENS])
ERYNGIUM = Genus(name="Eryngium", children=[E_MARITIMUM])
DAUCUS = Genus(name="Daucus", children=[D_CAROTA])
HERACLEUM = Genus(name="Heracleum", children=[H_SOSNOWSKYI])
PETROSELINUM = Genus(name="Petroselinum", children=[P_CRISPUM])
CICUTA = Genus(name="Cicuta", children=[C_VIROSA])
HEDERA = Genus(name="Hedera", children=[H_HELIX])
PANAX = Genus(name="Panax", children=[P_GINSENG])
CUMINUM = Genus(name="Cuminum", children=[C_CYMINUM])
# https://www.researchgate.net/publication/263393806_Identification_of_species_and_materia_medica_within_Angelica_L_Umbelliferae_based_on_phylogeny_inferred_from_DNA_barcodes
ANGELICA = Genus(name="Angelica", children=[A_ARCHANGELICA, L_OFFICINALE])

# https://www.researchgate.net/publication/275771656_Taxonomy_of_the_tribe_Apieae_Apiaceae_revisited_as_revealed_by_molecular_phylogenies_and_morphological_characters
APIEAE_A = Clade(children=[ANETHUM, FOENICULUM])
APIEAE_B = Clade(children=[APIUM, PETROSELINUM])

PIMPINELLEAE = Tribe(name="Pimpinelleae", children=[PIMPINELLA])
PYRAMIDOPTEREAE = Tribe(name="Pyramidoptereae", children=[TRACHYSPERMUM])
CORIANDREAE = Tribe(name="Coriandreae", children=[CORIANDRUM])
TORDYLIEAE = Tribe(name="Tordylieae", children=[PASTINACA, HERACLEUM])
CAREAE = Tribe(name="Careae", children=[CARUM, AEGOPODIUM])
SELINEAE = Tribe(name="Selineae", children=[AETHUSA, ANGELICA])
OENANTHEAE = Tribe(name="Oenantheae", children=[OENANTHE, CICUTA])
SANICULEAE = Tribe(name="Saniculeae", children=[ERYNGIUM])
APIEAE = Tribe(name="Apieae", children=[APIEAE_A, APIEAE_B])
SCANDICEAE = Tribe(name="Scandiceae", children=[DAUCUS, CUMINUM])

# https://www.semanticscholar.org/paper/Major-clades-within-Apiaceae-subfamily-Apioideae-as-Downie-Spalik/135ee9257c5e624b9ba06523c228a77b2d2c32f5
# couldn't resolve better using available sources (many conflicts)
# probably there is at least [TORDYLIEAE, SELINEAE, CORIANDREAE, CONIUM]
# and maybe [PYRAMIDOPTEREAE, CAREAE]
APIOIDEAE_A = Clade(
    children=[
        TORDYLIEAE,
        SELINEAE,
        CORIANDREAE,
        CONIUM,
        APIEAE,
        PIMPINELLEAE,
        PYRAMIDOPTEREAE,
        CAREAE,
    ]
)
APIOIDEAE_B = Clade(children=[APIOIDEAE_A, SCANDICEAE])

APIOIDEAE = Subfamily(name="Apioideae", children=[APIOIDEAE_B, OENANTHEAE])
SANICULOIDEAE = Subfamily(name="Saniculoideae", children=[SANICULEAE])

APIACEAE = Family(name="Apiaceae", children=[APIOIDEAE, SANICULOIDEAE])
ARALIACEAE = Family(name="Araliaceae", children=[HEDERA, PANAX])

APIALES = Order(name="Apiales", children=[APIACEAE, ARALIACEAE])
