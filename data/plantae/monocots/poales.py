from clade import (
    Clade,
    Family,
    Genus,
    Order,
    Species,
    Subfamily,
    Subtribe,
    Supertribe,
    Tribe,
)
from constants import EN, IMAGE, PL
from image import Image, License

T_LATIFOLIA = Species(
    name="Typha latifolia",
    local_names={EN: "broadleaf cattail", PL: "pałka wodna, pałka szerokolistna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Typha_latifolia_Finland.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Typha_latifolia_Finland.jpg",
        author="Petritap",
        license=License.CC_BY_SA_3_0,
    ),
)
A_COMOSUS = Species(
    name="Ananas comosus",
    local_names={EN: "pineapple", PL: "ananas jadalny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:%E0%B4%95%E0%B5%88%E0%B4%A4%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B4%95%E0%B5%8D%E0%B4%95.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/%E0%B4%95%E0%B5%88%E0%B4%A4%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B4%95%E0%B5%8D%E0%B4%95.jpg",
        author="Suniltg at Malayalam Wikipedia",
        license=License.CC_BY_3_0,
    ),
)
P_PRATENSIS = Species(
    name="Poa pratensis",
    local_names={EN: "Kentucky bluegrass, smooth meadow-grass", PL: "wiechlina łąkowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Poa_pratensis_-_Flickr_-_aspidoscelis_(1).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c2/Poa_pratensis_-_Flickr_-_aspidoscelis_%281%29.jpg",
        author="Patrick Alexander from Las Cruces, NM",
        license=License.CC0,
    ),
)
F_OVINA = Species(
    name="Festuca ovina",
    local_names={EN: "sheep fescue", PL: "kostrzewa owcza"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:443_Festuca_ovina,_Festuca_rubra.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3f/443_Festuca_ovina%2C_Festuca_rubra.jpg",
        author="Carl Axel Magnus Lindman",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
T_AESTIVUM = Species(
    name="Triticum aestivum",
    local_names={EN: "common wheat, bread wheat", PL: "pszenica zwyczajna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Triticum_aestivum_136645751.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a0/Triticum_aestivum_136645751.jpg",
        author="bgirardot",
        license=License.CC0,
    ),
)
T_DURUM = Species(
    name="Triticum durum",
    local_names={EN: "durum wheat, pasta wheat", PL: "pszenica durum, pszenica twarda"},
    known_for=[
        {
            EN: "pasta",
            PL: "makaron",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_11385_Pasta_made_from_durum_wheat.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/ea/CSIRO_ScienceImage_11385_Pasta_made_from_durum_wheat.jpg",
                author="division, CSIRO",
                license=License.CC_BY_3_0,
            ),
        },
        {
            EN: "couscous",
            PL: "kuskus",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Couscous-01.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Couscous-01.jpg",
                author="Josefine Stenudd",
                license=License.CC_BY_2_0,
            ),
        },
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trigo.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1a/Trigo.jpg",
        author="Ximénex",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
H_VULGARE = Species(
    name="Hordeum vulgare",
    local_names={EN: "barley", PL: "jęczmień zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Escourgeon-Hordeum_vulgare_subsp._vulgare.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Escourgeon-Hordeum_vulgare_subsp._vulgare.jpg",
        author="raul.dupagne",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
A_SATIVA = Species(
    name="Avena sativa",
    local_names={EN: "oat", PL: "owies zwyczajny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Avena-sativa-Ruedershausen.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/69/Avena-sativa-Ruedershausen.jpg",
        author="FranciscoWelterSchultes",
        license=License.CC0,
    ),
)
S_CEREALE = Species(
    name="Secale cereale",
    local_names={EN: "rye", PL: "żyto zwyczajne"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ear_of_rye.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/79/Ear_of_rye.jpg",
        author="LSDSL",
        license=License.CC_BY_SA_3_0,
    ),
)
O_SATIVA = Species(
    name="Oryza sativa",
    local_names={EN: "rice, Asian rice", PL: "ryż siewny"},
    known_for=[
        {
            EN: "white rice",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:White_rice_on_a_brown_table.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/White_rice_on_a_brown_table.jpg",
                author="ImageParty",
                license=License.CC_BY_SA_4_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Kanchanaburi,_Thailand,_Asian_rice_(Oryza_sativa)_grass.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/48/Kanchanaburi%2C_Thailand%2C_Asian_rice_%28Oryza_sativa%29_grass.jpg",
        author="Vyacheslav Argenberg",
        license=License.CC_BY_4_0,
    ),
)
B_OLDHAMII = Species(
    name="Bambusa oldhamii",
    local_names={EN: "giant timber bamboo"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Starr-110330-3981-Bambusa_oldhamii-habit-Garden_of_Eden_Keanae-Maui_(24987725271).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b7/Starr-110330-3981-Bambusa_oldhamii-habit-Garden_of_Eden_Keanae-Maui_%2824987725271%29.jpg",
        author="Forest and Kim Starr",
        license=License.CC_BY_3_0_US,
    ),
)
P_MILIACEUM = Species(
    name="Panicum miliaceum",
    local_names={EN: "proso millet", PL: "proso"},
    known_for=[
        {
            PL: "kasza jaglana",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Proso_pseno.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/94/Proso_pseno.jpg",
                author="Luděk Kovář – ludek@kovar.biz",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_Millet_Panicum_miliaceum_(6485810627).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8a/Common_Millet_Panicum_miliaceum_%286485810627%29.jpg",
        author="Len Worthington",
        license=License.CC_BY_SA_2_0,
    ),
)
Z_MAYS = Species(
    name="Zea mays",
    local_names={EN: "corn, maize", PL: "kukurydza"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zea_mays_004.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2b/Zea_mays_004.JPG",
        author="H. Zell",
        license=License.CC_BY_SA_3_0,
    ),
)
C_CITRATUS = Species(
    name="Cymbopogon citratus",
    local_names={PL: "trawa cytrynowa, palczatka cytrynowa", EN: "lemon grass"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cymbopogon_citratus_4zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Cymbopogon_citratus_4zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
S_BICOLOR = Species(
    name="Sorghum bicolor",
    local_names={PL: "sorgo dwubarwne", EN: "sorghum"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sorghum_bicolor,_Ma%C3%A7anet_de_la_Selva.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Sorghum_bicolor%2C_Ma%C3%A7anet_de_la_Selva.jpg",
        author="Josep Gesti",
        license=License.CC_BY_SA_4_0,
    ),
)
S_OFFICINARUM = Species(
    name="Saccharum officinarum",
    local_names={PL: "trzcina cukrowa, cukrowiec lekarski", EN: "sugarcane"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Saccharum_officinarum,_Mozambique.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/11/Saccharum_officinarum%2C_Mozambique.jpg",
        author="Ton Rulkens",
        license=License.CC_BY_SA_2_0,
    ),
)
P_AUSTRALIS = Species(
    name="Phragmites australis",
    local_names={PL: "trzcina pospolita", EN: "common reed"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Phragmites_australis_175613692.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/25/Phragmites_australis_175613692.jpg",
        author="Eppu",
        license=License.CC_BY_4_0,
    ),
)
C_PAPYRUS = Species(
    name="Cyperus papyrus",
    local_names={
        EN: "papyrus, papyrus sedge, paper reed, Indian matting plant, or Nile grass",
        PL: "trzcina papirusowa, cibora papirusowa",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Cyperus_papyrus_15zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/4f/Cyperus_papyrus_15zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)

TYPHA = Genus(name="Typha", children=[T_LATIFOLIA])
ANANAS = Genus(name="Ananas", children=[A_COMOSUS])
POA = Genus(name="Poa", children=[P_PRATENSIS])
FESTUCA = Genus(name="Festuca", children=[F_OVINA])
TRITICUM = Genus(name="Triticum", children=[T_AESTIVUM, T_DURUM])
HORDEUM = Genus(name="Hordeum", children=[H_VULGARE])
AVENA = Genus(name="Avena", children=[A_SATIVA])
SECALE = Genus(name="Secale", children=[S_CEREALE])
ORYZA = Genus(name="Oryza", children=[O_SATIVA])
BAMBUSA = Genus(name="Bambusa", local_names={PL: "bambus"}, children=[B_OLDHAMII])
PANICUM = Genus(name="Panicum", children=[P_MILIACEUM])
ZEA = Genus(name="Zea", children=[Z_MAYS])
CYMBOPOGON = Genus(name="Cymbopogon", children=[C_CITRATUS])
SORGHUM = Genus(name="Sorghum", children=[S_BICOLOR])
SACCHARUM = Genus(name="Saccharum", children=[S_OFFICINARUM])
PHRAGMITES = Genus(name="Phragmites", children=[P_AUSTRALIS])
CYPERUS = Genus(name="Cyperus", children=[C_PAPYRUS])

POINAE = Subtribe(name="Poinae", children=[POA])
LOLIINAE = Subtribe(name="Loliinae", children=[FESTUCA])
AVENINAE = Subtribe(name="Aveninae", children=[AVENA])
ORYZINAE = Subtribe(name="Oryzinae", children=[ORYZA])
BAMBUSINAE = Subtribe(name="Bambusinae", children=[BAMBUSA])
PANICINAE = Subtribe(name="Panicinae", children=[PANICUM])
TRIPSACINAE = Subtribe(name="Tripsacinae", children=[ZEA])
ANDROPOGONINAE = Subtribe(name="Andropogoninae", children=[CYMBOPOGON])
SACCHARINAE = Subtribe(name="Saccharinae", children=[SORGHUM, SACCHARUM])
MOLINIINAE = Subtribe(name="Moliniinae", children=[PHRAGMITES])

CHLOROPLAST_GROUP_1 = Clade(name="chloroplast group 1", children=[AVENINAE])
CHLOROPLAST_GROUP_2 = Clade(name="chloroplast group 2", children=[POINAE, LOLIINAE])

# many sources, e.g.
# https://www.researchgate.net/publication/6760501_Sequence_variation_of_chloroplast_gene_infA-rpl36_region_occurred_in_some_Triticeae_species
TRITICUM_SECALE = Clade(children=[TRITICUM, SECALE])

# https://www.researchgate.net/publication/262373100_An_evolutionary_perspective_of_C_4_photosynthesis_in_maize
ANDROPOGONINAE_SACCHARINAE = Clade(children=[ANDROPOGONINAE, SACCHARINAE])

POEAE = Tribe(name="Poeae", children=[CHLOROPLAST_GROUP_1, CHLOROPLAST_GROUP_2])
TRITICEAE = Tribe(name="Triticeae", children=[TRITICUM_SECALE, HORDEUM])
ORYZEAE = Tribe(name="Oryzeae", children=[ORYZINAE])
BAMBUSEAE = Tribe(name="Bambuseae", children=[BAMBUSINAE])
PANICEAE = Tribe(name="Paniceae", children=[PANICINAE])
ANDROPOGONEAE = Tribe(
    name="Andropogoneae", children=[TRIPSACINAE, ANDROPOGONINAE_SACCHARINAE]
)
MOLINIEAE = Tribe(name="Molinieae", children=[MOLINIINAE])

POODAE = Supertribe(name="Poodae", children=[POEAE])
TRITICODAE = Supertribe(name="Triticodae", children=[TRITICEAE])
PANICODAE = Supertribe(name="Panicodae", children=[PANICEAE])
ANDROPOGONODAE = Supertribe(name="Andropogonodae", children=[ANDROPOGONEAE])

POOIDEAE = Subfamily(name="Pooideae", children=[POODAE, TRITICODAE])
ORYZOIDEAE = Subfamily(name="Oryzoideae", children=[ORYZEAE])
BAMBUSOIDEAE = Subfamily(name="Bambusoideae", children=[BAMBUSEAE])
PANICOIDEAE = Subfamily(name="Panicoideae", children=[PANICODAE, ANDROPOGONODAE])
ARUNDINOIDEAE = Subfamily(name="Arundinoideae", children=[MOLINIEAE])

POOIDEAE_BAMBUSOIDEAE = Clade(children=[POOIDEAE, BAMBUSOIDEAE])
BOP_CLADE = Clade(name="BOP clade", children=[POOIDEAE_BAMBUSOIDEAE, ORYZOIDEAE])
PACMAD_CLADE = Clade(name="PACMAD clade", children=[PANICOIDEAE, ARUNDINOIDEAE])

TYPHACEAE = Family(name="Typhaceae", children=[TYPHA])
BROMELIACEAE = Family(name="Bromeliaceae", children=[ANANAS])
POACEAE = Family(name="Poaceae", children=[BOP_CLADE, PACMAD_CLADE])
CYPERACEAE = Family(name="Cyperaceae", children=[CYPERUS])

BROMELIAD_CLADE = Clade(name="Bromeliad clade", children=[TYPHACEAE, BROMELIACEAE])

POALES_A = Clade(children=[CYPERACEAE, POACEAE])

POALES = Order(name="Poales", children=[BROMELIAD_CLADE, POALES_A])
