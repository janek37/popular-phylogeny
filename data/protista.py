from clade import Clade, Class, Family, Genus, Order, Phylum, Species, Superphylum
from constants import EN, PL
from image import Image, License

P_MALARIAE = Species(
    name="Plasmodium malariae",
    known_for=[{EN: "malaria"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mature_Plasmodium_malariae_schizont_PHIL_2715_lores.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/02/Mature_Plasmodium_malariae_schizont_PHIL_2715_lores.jpg",
        author="CDC/ Dr. Mae Melvin",
        license=License.CDC,
    ),
)
P_CAUDATUM = Species(
    name="Paramecium caudatum",
    local_names={PL: "pantofelek"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Инфузория_туфелька_2.tif",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/07/Инфузория_туфелька_2.tif",
        author="Alexander Klepnev",
        license=License.CC_BY_SA_4_0,
    ),
)
T_VAGINALIS = Species(
    name="Trichomonas vaginalis",
    local_names={PL: "rzęsistek pochwowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trichomonas_vaginalis_(20).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Trichomonas_vaginalis_%2820%29.png",
        author="fickleandfreckled@Flickr",
        license=License.CC_BY_2_0,
    ),
)
A_PROTEUS = Species(
    name="Amoeba proteus",
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Amoeba_proteus.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Amoeba_proteus.jpg",
        author="Cymothoa exigua",
        license=License.CC_BY_SA_3_0,
    ),
)
F_SEPTICA = Species(
    name="Fuligo septica",
    local_names={EN: "dog vomit slime mold"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Fuligo_septica_bl1.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Fuligo_septica_bl1.JPG",
        author="Siga",
        license=License.PUBLIC_DOMAIN_SELF,
    ),
)
P_POLYCEPHALUM = Species(
    name="Physarum polycephalum",
    local_names={EN: "the blob"},
    known_for=[{EN: "can solve the shortest path problem"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Physarum_polycephalum_plasmodium.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6d/Physarum_polycephalum_plasmodium.jpg",
        author="frankenstoen@Flickr",
        license=License.CC_BY_2_5,
    ),
)
P_CHROMATOPHORA = Species(
    name="Paulinella chromatophora",
    known_for=[{EN: "photosyntetic plastids unrelated to chloroplasts"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paulinella_chromatophora.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/Paulinella_chromatophora.jpg",
        author="Luis Delaye, Cecilio Valadez-Cano, Bernardo Pérez-Zamorano",
        license=License.CC_BY_2_5,
    ),
)
F_VESICULOSUS = Species(
    name="Fucus vesiculosus",
    local_names={EN: "bladder wrack", PL: "morszczyn pęcherzykowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bladder_Wrack_(Fucus_vesiculosus)_-_geograph.org.uk_-_224125.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/80/Bladder_Wrack_%28Fucus_vesiculosus%29_-_geograph.org.uk_-_224125.jpg",
        author="Anne Burgess",
        license=License.CC_BY_SA_2_0,
    ),
)
U_PINNATIFIDA = Species(
    name="Undaria pinnatifida",
    local_names={EN: "wakame, Japanese kelp"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_868_Undaria_pinnatifida_Japanese_kelp.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ca/CSIRO_ScienceImage_868_Undaria_pinnatifida_Japanese_kelp.jpg",
        author="division, Commonwealth Scientific and Industrial Research Organisation",
        license=License.CC_BY_3_0,
    ),
)
M_PYRIFERA = Species(
    name="Macrocystis pyrifera",
    local_names={EN: "giant kelp, bladder kelp", PL: "wielkomorszcz gruszkonośny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sanc0063_-_Flickr_-_NOAA_Photo_Library.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f8/Sanc0063_-_Flickr_-_NOAA_Photo_Library.jpg",
        author="Claire Fackler, Channel Islands National Marine Sanctuary, National Oceanic and Atmospheric Administration",
        license=License.CC_BY_2_0,
    ),
)
B_PAXILLIFER = Species(
    name="Bacillaria paxillifer",
    known_for=[{EN: "one of the thousands of diatom species"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bacillaria_paxillifera.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/78/Bacillaria_paxillifera.jpg",
        author="Dr Alexandra Kraberg",
        license=License.CC_BY_3_0,
    ),
)
T_PSEUDONANA = Species(
    name="Thalassiosira pseudonana",
    known_for=[{EN: "the first marine phytoplankton to have its genome sequenced"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Oogonium_--_3_(34809275943).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/22/Oogonium_--_3_%2834809275943%29.jpg",
        author="Oregon State University",
        license=License.CC_BY_SA_2_0,
    ),
)
T_BRUCEI = Species(
    name="Trypanosoma brucei",
    local_names={PL: "świdrowiec nagany"},
    known_for=[{EN: "African sleeping sickness", PL: "śpiączka afrykańska"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Trypanosoma_brucei_gambiense_-_epimastigote.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/6c/Trypanosoma_brucei_gambiense_-_epimastigote.jpg",
        author="Stefan Walkowski",
        license=License.CC_BY_SA_4_0,
    ),
)
B_CANIS = Species(
    name="Babesia canis",
    known_for=[{EN: "babesiosis in dogs", PL: "babeszjoza psów"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Babesia-canis-dog.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Babesia-canis-dog.jpg",
        author="Alan R Walker",
        license=License.CC_BY_SA_3_0,
    ),
)

PLASMODIUM = Genus(name="Plasmodium", children=[P_MALARIAE])
PARAMECIUM = Genus(name="Paramecium", children=[P_CAUDATUM])
TRICHOMONAS = Genus(name="Trichomonas", children=[T_VAGINALIS])
AMOEBA = Genus(name="Amoeba", children=[A_PROTEUS])
FULIGO = Genus(name="Fuligo", children=[F_SEPTICA])
PHYSARUM = Genus(name="Physarum", children=[P_POLYCEPHALUM])
PAULINELLA = Genus(name="Paulinella", children=[P_CHROMATOPHORA])
FUCUS = Genus(name="Fucus", children=[F_VESICULOSUS])
UNDARIA = Genus(name="Undaria", children=[U_PINNATIFIDA])
MACROCYSTIS = Genus(name="Macrocystis", children=[M_PYRIFERA])
BACILLARIA = Genus(name="Bacillaria", children=[B_PAXILLIFER])
THALASSIOSIRA = Genus(name="Thalassiosira", children=[T_PSEUDONANA])
TRYPANOSOMA = Genus(name="Trypanosoma", children=[T_BRUCEI])
BABESIA = Genus(name="Babesia", children=[B_CANIS])

PLASMODIIDAE = Family(name="Plasmodiidae", children=[PLASMODIUM])
PARAMECIIDAE = Family(name="Parameciidae", children=[PARAMECIUM])
TRICHOMONADIDAE = Family(name="Trichomonadidae", children=[TRICHOMONAS])
AMOEBIDAE = Family(name="Amoebidae", children=[AMOEBA])
PHYSARACEAE = Family(name="Physaraceae", children=[FULIGO, PHYSARUM])
PAULINELLIDAE = Family(name="Paulinellidae", children=[PAULINELLA])
FUCACEAE = Family(name="Fucaceae", children=[FUCUS])
ALARIACEAE = Family(name="Alariaceae", children=[UNDARIA])
LAMINARIACEAE = Family(name="Laminariaceae", children=[MACROCYSTIS])
BACILLARIACEAE = Family(name="Bacillariaceae", children=[BACILLARIA])
THALASSIOSIRACEAE = Family(name="Thalassiosiraceae", children=[THALASSIOSIRA])
TRYPANOSOMATIDAE = Family(name="Trypanosomatidae", children=[TRYPANOSOMA])
BABESIIDAE = Family(name="Babesiidae", children=[BABESIA])

HAEMOSPORORIDA = Order(name="Haemospororida", children=[PLASMODIIDAE])
PENICULIDA = Order(name="Peniculida", children=[PARAMECIIDAE])
TRICHOMONADIDA = Order(name="Trichomonadida", children=[TRICHOMONADIDAE])
TUBULINIDA = Order(name="Tubulinida", children=[AMOEBIDAE])
PHYSARALES = Order(name="Physarales", children=[PHYSARACEAE])
EUGLYPHIDA = Order(name="Euglyphida", children=[PAULINELLIDAE])
FUCALES = Order(name="Fucales", children=[FUCACEAE])
LAMINARIALES = Order(name="Laminariales", children=[ALARIACEAE, LAMINARIACEAE])
BACILLARIALES = Order(name="Bacillariales", children=[BACILLARIACEAE])
THALASSIOSIRALES = Order(name="Thalassiosirales", children=[THALASSIOSIRACEAE])
TRYPANOSOMATIDA = Order(name="Trypanosomatida", children=[TRYPANOSOMATIDAE])
PIROPLASMIDA = Order(name="Piroplasmida", children=[BABESIIDAE])

ACONOIDASIDA = Class(name="Aconoidasida", children=[HAEMOSPORORIDA, PIROPLASMIDA])
OLIGOHYMENOPHOREA = Class(name="Oligohymenophorea", children=[PENICULIDA])
TUBULINEA = Class(name="Tubulinea", children=[TUBULINIDA])
MYXOGASTRIA = Class(name="Myxogastria", children=[PHYSARALES])
IMBRICATEA = Class(name="Imbricatea", children=[EUGLYPHIDA])
PHAEOPHYCEAE = Class(name="Phaeophyceae", children=[FUCALES, LAMINARIALES])
BACILLARIAPHYCEAE = Class(
    name="Bacillariaphyceae", children=[BACILLARIALES, THALASSIOSIRALES]
)
KINETOPLASTEA = Class(name="Kinetoplastea", children=[TRYPANOSOMATIDA])

CILIOPHORA = Phylum(name="Ciliophora", children=[OLIGOHYMENOPHOREA])
APICOMPLEXA = Phylum(name="Apicomplexa", children=[ACONOIDASIDA])
METAMONADA = Phylum(name="Metamonada", children=[TRICHOMONADIDA])
AMOEBOZOA = Phylum(name="Amoebozoa", children=[TUBULINEA, MYXOGASTRIA])
CERCOZOA = Phylum(name="Cercozoa", children=[IMBRICATEA])
OCHROPHYTA = Phylum(name="Ochrophyta", children=[PHAEOPHYCEAE, BACILLARIAPHYCEAE])
EUGLENOZOA = Phylum(name="Euglenozoa", children=[KINETOPLASTEA])

ALVEOLATA = Superphylum(name="Alveolata", children=[CILIOPHORA, APICOMPLEXA])
DISCICRISTATA = Superphylum(name="Discicristata", children=[EUGLENOZOA])

SAR_A = Clade(children=[ALVEOLATA, OCHROPHYTA])
SAR = Clade(name="SAR", children=[SAR_A, CERCOZOA])
