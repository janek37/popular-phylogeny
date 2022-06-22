from clade import Clade, Family, Genus, Species
from constants import EN, PL
from image import Image, License

C_RESPUBLICA = Species(
    name="Cicinnurus respublica",
    local_names={EN: "Wilson's bird-of-paradise", PL: "latawiec krasnogrzbiety"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Wilson%27s_Bird_of_Paradise_Best.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Wilson%27s_Bird_of_Paradise_Best.jpg",
        author="Serhanoksay",
        license=License.CC_BY_SA_3_0,
    ),
)
C_REGIUS = Species(
    name="Cicinnurus regius",
    local_names={EN: "king bird-of-paradise", PL: "latawiec królewski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Birds_and_nature_(1906)_(14750483475).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/a/a4/Birds_and_nature_%281906%29_%2814750483475%29.jpg",
        author="Internet Archive Book Images",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
P_APODA = Species(
    name="Paradisaea apoda",
    local_names={EN: "greater bird-of-paradise", PL: "cudowronka wielka"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Paradisaea_apoda_(male)_-KL_Bird_Park-8a.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b2/Paradisaea_apoda_%28male%29_-KL_Bird_Park-8a.jpg",
        author="chee.hong",
        license=License.CC_BY_2_0,
    ),
)
P_MINOR = Species(
    name="Paradisaea minor",
    local_names={EN: "lesser bird-of-paradise", PL: "cudowronka mniejsza"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bird_of_Paradice_(8558963767).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/56/Bird_of_Paradice_%288558963767%29.jpg",
        author="Michael Gwyther-Jones from UK",
        license=License.CC_BY_2_0,
    ),
)
P_RAGGIANA = Species(
    name="Paradisaea raggiana",
    local_names={EN: "Raggiana bird-of-paradise", PL: "cudowronka krasnopióra"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Raggiana_Bird_of_Paradise_-_Raggiana_Bird_of_Paradise_-_Paradisaea_raggiana_(48610481443).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/fa/Raggiana_Bird_of_Paradise_-_Raggiana_Bird_of_Paradise_-_Paradisaea_raggiana_%2848610481443%29.jpg",
        author="gailhampshire from Cradley, Malvern, U.K",
        license=License.CC_BY_2_0,
    ),
)
P_RUBRA = Species(
    name="Paradisaea rubra",
    local_names={EN: "red bird-of-paradise", PL: "cudowronka czerwona"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bird_illustration_by_Histoire_Naturelle_des_Oiseaux_de_Paradis_et_Des_Rolliers_by_Jacques_Barraband,_digitally_enhanced_by_rawpixel-com_6.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Bird_illustration_by_Histoire_Naturelle_des_Oiseaux_de_Paradis_et_Des_Rolliers_by_Jacques_Barraband%2C_digitally_enhanced_by_rawpixel-com_6.jpg",
        author="Rawpixel",
        license=License.CC_BY_SA_4_0,
    ),
)
P_ALBERTI = Species(
    name="Pteridophora alberti",
    local_names={EN: "King of Saxony bird-of-paradise", PL: "wstęgogłów"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Pteridophora_alberti_-Papua_New_Guinea-8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Pteridophora_alberti_-Papua_New_Guinea-8.jpg",
        author="markaharper1",
        license=License.CC_BY_SA_2_0,
    ),
)
A_MAYERI = Species(
    name="Astrapia mayeri",
    local_names={EN: "ribbon-tailed astrapia", PL: "astrapia białosterna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ribbon-tailed_Astrapia_-_Papua_New_Guinea_(19981314929).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/25/Ribbon-tailed_Astrapia_-_Papua_New_Guinea_%2819981314929%29.jpg",
        author="Francesco Veronesi from Italy",
        license=License.CC_BY_SA_2_0,
    ),
)
L_SUPERBA = Species(
    name="Lophorina superba",
    local_names={
        EN: "greater lophorina, superb-bird-of-paradise",
        PL: "ozdobnik lirogłowy",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:CraspedophoraKeulemans_1.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b3/CraspedophoraKeulemans_1.jpg",
        author="J G Keulemans",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
L_VICTORIAE = Species(
    name="Lophorina victoriae",
    local_names={EN: "Victoria's riflebird", PL: "ozdobnik mały"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Victoria%27s_Riflebird_courtship_-_Lake_Eacham_-_Queensland_S4E8070_(22198704599).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/47/Victoria%27s_Riflebird_courtship_-_Lake_Eacham_-_Queensland_S4E8070_%2822198704599%29.jpg",
        author="Francesco Veronesi from Italy",
        license=License.CC_BY_SA_2_0,
    ),
)

# https://www.researchgate.net/publication/301538003_Can_the_Fisher-Lande_Process_Account_for_Birds_of_Paradise_and_Other_Sexual_Radiations
PARADISAEA_A = Clade(children=[P_APODA, P_RAGGIANA])
PARADISAEA_B = Clade(children=[PARADISAEA_A, P_MINOR])

CICINNURUS = Genus(name="Cicinnurus", children=[C_RESPUBLICA, C_REGIUS])
PARADISAEA = Genus(name="Paradisaea", children=[PARADISAEA_B, P_RUBRA])
PTERIDOPHORA = Genus(name="Pteridophora", children=[P_ALBERTI])
ASTRAPIA = Genus(name="Astrapia", children=[A_MAYERI])
LOPHORINA = Genus(name="Lophorina", children=[L_SUPERBA, L_VICTORIAE])

PARADISAEIDAE_B = Clade(children=[PARADISAEA, CICINNURUS])
PARADISAEIDAE_C = Clade(children=[PARADISAEIDAE_B, ASTRAPIA])
PARADISAEIDAE_D = Clade(children=[PARADISAEIDAE_C, LOPHORINA])

PARADISAEIDAE = Family(name="Paradisaeidae", children=[PARADISAEIDAE_D, PTERIDOPHORA])
