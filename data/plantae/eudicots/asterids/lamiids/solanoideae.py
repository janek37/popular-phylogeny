from clade import Clade, Genus, Species, Subfamily, Subgenus, Tribe
from constants import EN, IMAGE, PL
from image import Image, License

M_OFFICINARUM = Species(
    name="Mandragora officinarum",
    local_names={EN: "mandrake", PL: "mandragora lekarska"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mandragora_officinalis_botanical_illustration.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fe/Mandragora_officinalis_botanical_illustration.jpg",
        author="Sibthrop, J., Smith, J.E.",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
D_STRAMONIUM = Species(
    name="Datura stramonium",
    local_names={EN: "thorn apple, jimsonweed", PL: "bieluń dziędzierzawa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Datura_stramonium_Bielu%C5%84_dzi%C4%99dzierzawa_Seed_01.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/46/Datura_stramonium_Bielu%C5%84_dzi%C4%99dzierzawa_Seed_01.jpg",
        author="Agnieszka Kwiecień (Nova)",
        license=License.CC_BY_3_0,
    ),
)
A_BELLADONNA = Species(
    name="Atropa belladonna",
    local_names={EN: "belladonna, deadly nightshade", PL: "pokrzyk wilcza jagoda"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Atropa_belladonna_(Tollkirsche).JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Atropa_belladonna_%28Tollkirsche%29.JPG",
        author="Tubifex",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
S_LYCOPERSICUM = Species(
    name="Solanum lycopersicum",
    local_names={EN: "tomato", PL: "pomidor zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Maduraci%C3%B3n_del_tomate_(Solanum_lycopersicum).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/83/Maduraci%C3%B3n_del_tomate_%28Solanum_lycopersicum%29.jpg",
        author="Juan Carlos Fonseca Mata",
        license=License.CC_BY_SA_4_0,
    ),
)
S_TUBEROSUM = Species(
    name="Solanum tuberosum",
    local_names={EN: "potato", PL: "kartofel, ziemniak"},
    known_for=[
        {
            EN: "edible tubers",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Solanales_-_Solanum_tuberosum_-_3.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/4/4a/Solanales_-_Solanum_tuberosum_-_3.jpg",
                author="DenesFeri",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Solanum_tuberosum_Barbara_(03).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c6/Solanum_tuberosum_Barbara_%2803%29.jpg",
        author="Thomas Springer",
        license=License.CC0,
    ),
)
S_MELONGENA = Species(
    name="Solanum melongena",
    local_names={EN: "eggplant, aubergine", PL: "bakłażan, oberżyna, psianka podłużna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Solanum_melongena_-_Parc_Floral.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/aa/Solanum_melongena_-_Parc_Floral.jpg",
        author="Dinkum",
        license=License.CC_BY_SA_3_0,
    ),
)
C_ANNUUM = Species(
    name="Capsicum annuum",
    local_names={PL: "papryka roczna"},
    known_for=[
        {
            EN: "bell pepper",
            PL: "papryka słodka",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Red_bell_pepper.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/5/5c/Red_bell_pepper.jpg",
                author="AntanO",
                license=License.CC_BY_SA_4_0,
            ),
        },
        {
            EN: "chili pepper",
            PL: "papryka chili",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Peppers_in_Vientiane.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/bb/Peppers_in_Vientiane.jpg",
                author="Mx. Granger",
                license=License.CC0,
            ),
        },
        {
            EN: "jalapeño",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Jalape%C3%B1o_pile.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/Jalape%C3%B1o_pile.jpg",
                author="Jeffery Martin",
                license=License.CC0,
            ),
        },
        {
            EN: "cayenne pepper",
            PL: "pieprz cayenne",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Cayenne_Pepper_(cropped).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/d/d1/Cayenne_Pepper_%28cropped%29.jpg",
                author="Alabama Extension",
                license=License.CC0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Capsicum_annuum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-027.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Capsicum_annuum_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-027.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
C_FRUTESCENS = Species(
    name="Capsicum frutescens",
    local_names={PL: "papryka owocowa"},
    known_for=[
        {
            EN: "piri piri",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Piri_piri.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e9/Piri_piri.jpg",
                author="Orrling",
                license=License.CC_BY_SA_3_0,
            ),
        },
        {
            EN: "Tabasco",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Tabasco_bottle_2013.jpeg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/f/fd/Tabasco_bottle_2013.jpeg",
                author="Skb8721",
                license=License.CC_BY_SA_3_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CapsicumFrutescens.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/CapsicumFrutescens.jpg",
        author="Taken by  Fanghong",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CHINENSE = Species(
    name="Capsicum chinense",
    local_names={
        EN: "habanero-type pepper",
        PL: "papryka habanero",
        IMAGE: Image(
            url="https://commons.wikimedia.org/wiki/File:Habanero_Chillies_at_Super_Pollo,_Xpujil,_Campeche,_Mexico.jpg",
            image_url="https://upload.wikimedia.org/wikipedia/commons/4/44/Habanero_Chillies_at_Super_Pollo%2C_Xpujil%2C_Campeche%2C_Mexico.jpg",
            author="Bernard DUPONT",
            license=License.CC_BY_SA_2_0,
        ),
    },
    known_for=[{EN: "the hottest peppers"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Solanaceae_Capsicum_chinense_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/ab/Solanaceae_Capsicum_chinense_2.jpg",
        author="NasserHalaweh",
        license=License.CC_BY_SA_4_0,
    ),
)

SOLANUM_SENSU_STRICTO = Subgenus(
    name="Solanum sensu stricto", children=[S_LYCOPERSICUM, S_TUBEROSUM]
)
SOLANUM_SUBGENUS_LEPTOSTEMONUM = Subgenus(
    name="Solanum subg. Leptostemonum", children=[S_MELONGENA]
)

CAPSICUM_A = Clade(children=[C_FRUTESCENS, C_CHINENSE])

MANDRAGORA = Genus(name="Mandragora", children=[M_OFFICINARUM])
DATURA = Genus(name="Datura", children=[D_STRAMONIUM])
ATROPA = Genus(name="Atropa", children=[A_BELLADONNA])
SOLANUM = Genus(
    name="Solanum", children=[SOLANUM_SENSU_STRICTO, SOLANUM_SUBGENUS_LEPTOSTEMONUM]
)
CAPSICUM = Genus(name="Capsicum", children=[C_ANNUUM, CAPSICUM_A])

MANDRAGOREAE = Tribe(name="Mandragoreae", children=[MANDRAGORA])
DATUREAE = Tribe(name="Datureae", children=[DATURA])
HYOSCYAMEAE = Tribe(name="Hyoscyameae", children=[ATROPA])
SOLANEAE = Tribe(name="Solaneae", children=[SOLANUM])
CAPSICEAE = Tribe(name="Capsiceae", children=[CAPSICUM])

# https://www.researchgate.net/publication/257251395_Discovery_of_novel_plastid_phenylalanine_trnF_pseudogenes_defines_a_distinctive_clade_in_Solanaceae
PSEUDOSOLANOIDS_A = Clade(children=[SOLANEAE, CAPSICEAE])
PSEUDOSOLANOIDS = Clade(children=[DATUREAE, PSEUDOSOLANOIDS_A])
SOLANOIDEAE_A = Clade(children=[MANDRAGOREAE, PSEUDOSOLANOIDS])

SOLANOIDEAE = Subfamily(name="Solanoideae", children=[SOLANOIDEAE_A, HYOSCYAMEAE])
