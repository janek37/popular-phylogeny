from clade import Clade, Genus, Species, Subfamily, Supertribe, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

M_CHAMOMILLA = Species(
    name="Matricaria chamomilla",
    local_names={EN: "German chamomile", PL: "rumianek pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:12_Matricaria_chamomilla.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/12_Matricaria_chamomilla.jpg",
        author="Carl Axel Magnus Lindman",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_NOBILE = Species(
    name="Chamaemelum nobile",
    local_names={EN: "Roman chamomile", PL: "rumian rzymski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chamaemelum_nobile_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-012.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/59/Chamaemelum_nobile_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-012.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
A_ABSINTHIUM = Species(
    name="Artemisia absinthium",
    local_names={EN: "wormwood", PL: "bylica piołun"},
    known_for=[{EN: "absinthe", PL: "absynt"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20150821Artemisia_absinthium1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7f/20150821Artemisia_absinthium1.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
A_DRACUNCULUS = Species(
    name="Artemisia dracunculus",
    local_names={EN: "tarragon, estragon", PL: "estragon, bylica draganek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Artemisia_dracunculus_-_001x.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Artemisia_dracunculus_-_001x.jpg",
        author="Oceancetaceen - Alice Chodura",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_MORIFOLIUM = Species(
    name="Chrysanthemum × morifolium",
    local_names={
        EN: "'florist's daisy, hardy garden mum'",
        PL: "chryzantema, złocień chiński",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chrysanthemum_morifolium_(2).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/30/Chrysanthemum_morifolium_%282%29.JPG",
        author="Prenn",
        license=License.CC_BY_SA_3_0,
    ),
)
D_PINNATA = Species(
    name="Dahlia pinnata",
    local_names={EN: "garden dahlia", PL: "dalia ogrodowa, dalia zmienna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:,00_0904_Dahlia_%C3%97_pinnata.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/%2C00_0904_Dahlia_%C3%97_pinnata.jpg",
        author="W. Bulach",
        license=License.CC_BY_SA_4_0,
    ),
)
H_ANNUUS = Species(
    name="Helianthus annuus",
    local_names={EN: "common sunflower", PL: "słonecznik zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Helianthus_annuus_00001.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Helianthus_annuus_00001.jpg",
        author="Vengolis",
        license=License.CC_BY_SA_4_0,
    ),
)
H_TUBEROSUS = Species(
    name="Helianthus tuberosus",
    local_names={
        EN: "Jerusalem artichoke, sunroot",
        PL: "topinambur, słonecznik bulwiasty",
    },
    known_for=[
        {
            EN: "edible tubers",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Helianthus_tuberosus.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Helianthus_tuberosus.jpg",
                author="Hans B.~commonswiki",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Helianthus_tuberosus_Paludi_03.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Helianthus_tuberosus_Paludi_03.jpg",
        author="Syrio",
        license=License.CC_BY_SA_4_0,
    ),
)
C_OFFICINALIS = Species(
    name="Calendula officinalis",
    local_names={EN: "pot marigold", PL: "nagietek lekarski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Calendula_officinalis_macro_image.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/64/Calendula_officinalis_macro_image.jpg",
        author="FriendlyFoes",
        license=License.CC_BY_SA_4_0,
    ),
)
A_AMELLUS = Species(
    name="Aster amellus",
    local_names={EN: "European Michaelmas daisy, Italian aster", PL: "aster gawędka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Aster_amellus_flower_(04).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/60/Aster_amellus_flower_%2804%29.jpg",
        author="Andrea Moro",
        license=License.CC_BY_SA_4_0,
    ),
)
S_CANADENSIS = Species(
    name="Solidago canadensis",
    local_names={EN: "Canada goldenrod", PL: "nawłoć kanadyjska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20161013Solidago_canadensis4.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c9/20161013Solidago_canadensis4.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
L_NIVALE = Species(
    name="Leontopodium nivale",
    local_names={EN: "edelweiss", PL: "szarotka alpejska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Leontopodium_nivale_(alpinum)_(28558875687).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/24/Leontopodium_nivale_%28alpinum%29_%2828558875687%29.jpg",
        author="xulescu_g",
        license=License.CC_BY_SA_2_0,
    ),
)
T_FARFARA = Species(
    name="Tussilago farfara",
    local_names={EN: "coltsfoot", PL: "podbiał pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tussilago_farfara,_Coltsfoot_(33716499095).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Tussilago_farfara%2C_Coltsfoot_%2833716499095%29.jpg",
        author="gailhampshire from Cradley, Malvern, U.K",
        license=License.CC_BY_2_0,
    ),
)
S_REBAUDIANA = Species(
    name="Stevia rebaudiana",
    local_names={EN: "candyleaf", PL: "stewia"},
    known_for=[
        {
            EN: "sweetener",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Stevia_Tabs.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/0/0f/Stevia_Tabs.jpg",
                author="User:Thomas R. Schwarz",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%E7%94%9C%E8%8F%8A_Stevia_rebaudiana_-%E6%B3%B0%E5%9C%8B%E6%B8%85%E9%82%81%E8%8A%B1%E5%B1%95_Royal_Flora_Ratchaphruek,_Thailand-_(9240149538).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/10/%E7%94%9C%E8%8F%8A_Stevia_rebaudiana_-%E6%B3%B0%E5%9C%8B%E6%B8%85%E9%82%81%E8%8A%B1%E5%B1%95_Royal_Flora_Ratchaphruek%2C_Thailand-_%289240149538%29.jpg",
        author="阿橋 HQ",
        license=License.CC_BY_SA_2_0,
    ),
)
A_MILLEFOLIUM = Species(
    name="Achillea millefolium",
    local_names={EN: "common yarrow", PL: "krwarwnik pospolity"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Flowers._Achillea_millefolium.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/12/Flowers._Achillea_millefolium.jpg",
        author="llysmlv",
        license=License.CC_BY_4_0,
    ),
)
B_PERENNIS = Species(
    name="Bellis perennis",
    local_names={EN: "common daisy", PL: "stokrotka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%E3%83%92%E3%83%8A%E3%82%AE%E3%82%AF%E3%81%AE%E8%8A%B1(Bellis_perennis_L.).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a1/%E3%83%92%E3%83%8A%E3%82%AE%E3%82%AF%E3%81%AE%E8%8A%B1%28Bellis_perennis_L.%29.jpg",
        author="Latra Yokote",
        license=License.CC_BY_SA_4_0,
    ),
)
T_ERECTA = Species(
    name="Tagetes erecta",
    local_names={
        EN: "Aztec marigold, Mexican marigold, big marigold",
        PL: "aksamitka wzniesiona",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Tagetes_Erecta-Flower_02.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Tagetes_Erecta-Flower_02.jpg",
        author="Sabina Bajracharya",
        license=License.CC_BY_SA_4_0,
    ),
)
A_MONTANA = Species(
    name="Arnica montana",
    local_names={
        EN: "wolf's bane, leopard's bane, mountain tobacco, mountain arnica",
        PL: "arnika górska",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mountain_Arnica_-_Arnica_montana_(44236282062).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/01/Mountain_Arnica_-_Arnica_montana_%2844236282062%29.jpg",
        author="Björn S...",
        license=License.CC_BY_SA_2_0,
    ),
)

MATRICARIA = Genus(name="Matricaria", children=[M_CHAMOMILLA])
CHAMAEMELUM = Genus(name="Chamaemelum", children=[C_NOBILE])
ARTEMISIA = Genus(name="Artemisia", children=[A_ABSINTHIUM, A_DRACUNCULUS])
CHRYSANTHEMUM = Genus(name="Chrysanthemum", children=[C_MORIFOLIUM])
DAHLIA = Genus(name="Dahlia", children=[D_PINNATA])
HELIANTHUS = Genus(name="Helianthus", children=[H_ANNUUS, H_TUBEROSUS])
CALENDULA = Genus(name="Calendula", children=[C_OFFICINALIS])
ASTER = Genus(name="Aster", children=[A_AMELLUS])
SOLIDAGO = Genus(name="Solidago", children=[S_CANADENSIS])
LEONTOPODIUM = Genus(name="Leontopodium", children=[L_NIVALE])
TUSSILAGO = Genus(name="Tussilago", children=[T_FARFARA])
STEVIA = Genus(name="Stevia", children=[S_REBAUDIANA])
ACHILLEA = Genus(name="Achillea", children=[A_MILLEFOLIUM])
BELLIS = Genus(name="Bellis", children=[B_PERENNIS])
TAGETES = Genus(name="Tagetes", children=[T_ERECTA])
ARNICA = Genus(name="Arnica", children=[A_MONTANA])

# https://www.semanticscholar.org/paper/Molecular-phylogeny-of-Chrysanthemum,-Ajania-and-as-Zhao-Chen/1557e307fcb57f30f51615b3e3d9aceaa8d21a34
ANTHEMIDEAE_C = Clade(children=[MATRICARIA, ACHILLEA])
ANTHEMIDEAE_A = Clade(children=[ANTHEMIDEAE_C, CHAMAEMELUM])
ANTHEMIDEAE_B = Clade(children=[ARTEMISIA, CHRYSANTHEMUM])

# https://www.researchgate.net/publication/330620543_Convergent_origin_of_the_narrowly_lanceolate_leaf_in_the_genus_Aster-with_special_reference_to_an_unexpected_discovery_of_a_new_Aster_species_from_East_China
ASTEREAE_A = Clade(children=[ASTER, SOLIDAGO])

ANTHEMIDEAE = Tribe(name="Anthemideae", children=[ANTHEMIDEAE_A, ANTHEMIDEAE_B])
COREOPSIDEAE = Tribe(name="Coreopsideae", children=[DAHLIA])
HELIANTHEAE = Tribe(name="Heliantheae", children=[HELIANTHUS])
CALENDULEAE = Tribe(name="Calenduleae", children=[CALENDULA])
ASTEREAE = Tribe(name="Astereae", children=[ASTEREAE_A, BELLIS])
GNAPHALIEAE = Tribe(name="Gnaphalieae", children=[LEONTOPODIUM])
SENECIONEAE = Tribe(name="Senecioneae", children=[TUSSILAGO])
EUPATORIEAE = Tribe(name="Eupatorieae", children=[STEVIA])
TAGETEAE = Tribe(name="Tageteae", children=[TAGETES])
MADIEAE = Tribe(name="Madieae", children=[ARNICA])

# https://www.researchgate.net/publication/276250002_Cuticular_Patterns_on_Stylar_Hairs_in_Asteraceae_a_New_Micromorphological_Feature
ANTHEMIDEAE_ASTEREAE = Clade(children=[ANTHEMIDEAE, ASTEREAE])
ASTERODAE_A = Clade(children=[ANTHEMIDEAE_ASTEREAE, GNAPHALIEAE])
HELIANTHODAE_C = Clade(children=[EUPATORIEAE, MADIEAE])
HELIANTHODAE_A = Clade(children=[HELIANTHEAE, HELIANTHODAE_C])
HELIANTHODAE_B = Clade(children=[HELIANTHODAE_A, TAGETEAE])

ASTERODAE = Supertribe(name="Asterodae", children=[ASTERODAE_A, CALENDULEAE])
HELIANTHODAE = Supertribe(name="Helianthodae", children=[COREOPSIDEAE, HELIANTHODAE_B])
SENECIONODAE = Supertribe(name="Senecionodae", children=[SENECIONEAE])

# unresolved for now
ASTEROIDEAE = Subfamily(
    name="Asteroideae", children=[ASTERODAE, HELIANTHODAE, SENECIONODAE]
)
