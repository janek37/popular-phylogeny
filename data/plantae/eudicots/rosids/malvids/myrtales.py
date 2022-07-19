from clade import Clade, Family, Genus, Order, Species, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

P_DIOICA = Species(
    name="Pimenta dioica",
    local_names={EN: "allspice", PL: "ziele angielskie, korzennik lekarski"},
    known_for=[
        {
            EN: "dried fruit used for seasoning",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:AllspiceSeeds.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/AllspiceSeeds.jpg",
                author="Brian Arthur",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pimenta_dioica,_flowers.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/94/Pimenta_dioica%2C_flowers.jpg",
        author="Tauʻolunga",
        license=License.CC_BY_SA_3_0,
    ),
)
F_MAGELLANICA = Species(
    name="Fuchsia magellanica",
    local_names={EN: "hummingbird fuchsia", PL: "fuksja magellańska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fucsia,_Aretillos,_Pendientes,_Zarcillo_de_la_Reina_(Fuchsia_magellanica)_(14542219880).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Fucsia%2C_Aretillos%2C_Pendientes%2C_Zarcillo_de_la_Reina_%28Fuchsia_magellanica%29_%2814542219880%29.jpg",
        author="Alejandro  Bayer Tamayo from Armenia, Colombia",
        license=License.CC_BY_SA_2_0,
    ),
)
S_AROMATICUM = Species(
    name="Syzygium aromaticum",
    local_names={EN: "clove", PL: "goździkowiec korzenny, czapetka pachnąca"},
    known_for=[
        {
            PL: "goździki (przyprawa)",
            EN: "cloves",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cloves.JPG",
                image_url="https://upload.wikimedia.org/wikipedia/commons/3/33/Cloves.JPG",
                author="Jorge Barrios",
                license=License.PUBLIC_DOMAIN_SELF,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Syzygium_aromaticum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-030.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4b/Syzygium_aromaticum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-030.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
E_CAMALDULENSIS = Species(
    name="Eucalyptus camaldulensis",
    local_names={EN: "river red gum", PL: "eukaliptus kamaldulski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eucalyptus_camaldulensis_26.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Eucalyptus_camaldulensis_26.JPG",
        author="Vinayaraj",
        license=License.CC_BY_SA_3_0,
    ),
)
P_GRANATUM = Species(
    name="Punica granatum",
    local_names={EN: "pomegranate", PL: "granat właściwy"},
    known_for=[
        {
            EN: "edible fruit",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Pomegranate_fruit_-_whole_and_piece_with_arils.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/Pomegranate_fruit_-_whole_and_piece_with_arils.jpg",
                author="Ivar Leidus",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Punica_granatum_004.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e6/Punica_granatum_004.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
P_GUAJAVA = Species(
    name="Psidium guajava",
    local_names={EN: "common guava", PL: "gujawa pospolita"},
    known_for=[
        {
            EN: "edible fruit",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:%E1%BB%94i_%C4%91%C3%A0o_-pink_guava.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/%E1%BB%94i_%C4%91%C3%A0o_-pink_guava.jpg",
                author="Hungda",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Psidium_guajava_leaves_LR.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/45/Psidium_guajava_leaves_LR.jpg",
        author="PumpkinSky",
        license=License.CC_BY_SA_4_0,
    ),
)
M_COMMUNIS = Species(
    name="Myrtus communis",
    local_names={EN: "common myrtle", PL: "mirt zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Myrtus_communis_Common_Myrtle_%E1%83%9B%E1%83%95%E1%83%9D%E1%83%A0%E1%83%A1%E1%83%98%E1%83%9C%E1%83%98.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Myrtus_communis_Common_Myrtle_%E1%83%9B%E1%83%95%E1%83%9D%E1%83%A0%E1%83%A1%E1%83%98%E1%83%9C%E1%83%98.JPG",
        author="Lazaregagnidze",
        license=License.CC_BY_SA_4_0,
    ),
)

PIMENTA = Genus(name="Pimenta", children=[P_DIOICA])
FUCHSIA = Genus(name="Fuchsia", children=[F_MAGELLANICA])
SYZYGIUM = Genus(name="Syzygium", children=[S_AROMATICUM])
EUCALYPTUS = Genus(name="Eucalyptus", children=[E_CAMALDULENSIS])
PUNICA = Genus(name="Punica", children=[P_GRANATUM])
PSIDIUM = Genus(name="Psidium", children=[P_GUAJAVA])
MYRTUS = Genus(name="Myrtus", children=[M_COMMUNIS])

# https://www.researchgate.net/publication/312317456_Myrteae_phylogeny_calibration_biogeography_and_diversification_patterns_Increased_understanding_in_the_most_species_rich_tribe_of_Myrtaceae
MYRTEAE_A = Clade(children=[PIMENTA, PSIDIUM])

MYRTEAE = Tribe(name="Myrteae", children=[MYRTEAE_A, MYRTUS])
SYZYGIEAE = Tribe(name="Syzygieae", children=[SYZYGIUM])

# https://www.researchgate.net/publication/258164894_The_evolution_of_foliar_terpene_diversity_in_Myrtaceae
MYRTACEAE_A = Clade(children=[MYRTEAE, SYZYGIEAE])

MYRTACEAE = Family(name="Myrtaceae", children=[MYRTACEAE_A, EUCALYPTUS])
ONAGRACEAE = Family(name="Onagraceae", children=[FUCHSIA])
LYTHRACEAE = Family(name="Lythraceae", children=[PUNICA])

# https://www.researchgate.net/publication/321640262_A_continuous_morphological_approach_to_study_the_evolution_of_pollen_in_a_phylogenetic_context_An_example_with_the_order_Myrtales
LYTHRACEAE_ONAGRACEAE = Clade(children=[LYTHRACEAE, ONAGRACEAE])

MYRTALES = Order(name="Myrtales", children=[MYRTACEAE, LYTHRACEAE_ONAGRACEAE])
