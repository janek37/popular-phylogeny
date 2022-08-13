from clade import (
    Clade,
    Class,
    Domain,
    Family,
    Genus,
    Order,
    Phylum,
    Species,
    Superphylum,
)
from constants import EN, NAME, PL
from image import Image, License

E_COLI = Species(
    name="Escherichia coli",
    local_names={PL: "pałeczka okrężnicy"},
    image=Image(
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/32/EscherichiaColi_NIAID.jpg",
        url="https://commons.wikimedia.org/wiki/File:EscherichiaColi_NIAID.jpg",
        author="Rocky Mountain Laboratories, NIAID, NIH",
        license=License.NIH,
    ),
)
S_ENTERICA = Species(
    name="Salmonella enterica",
    known_for=[{PL: "dur brzuszny", EN: "typhoid fever"}],
    image=Image(
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/27/Salmonella_enterica_serovar_typhimurium_01.jpg",
        url="https://commons.wikimedia.org/wiki/File:Salmonella_enterica_serovar_typhimurium_01.jpg",
        author="CDC",
        license=License.CDC,
    ),
)
Y_PESTIS = Species(
    name="Yersinia pestis",
    local_names={PL: "pałeczka dżumy"},
    known_for=[{EN: "bubonic plague", PL: "dżuma"}],
    image=Image(
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d0/Yersinia_pestis.jpg",
        url="https://commons.wikimedia.org/wiki/File:Yersinia_pestis.jpg",
        author="Rocky Mountain Laboratories, NIAID, NIH",
        license=License.NIH,
    ),
)
V_CHOLERAE = Species(
    name="Vibrio cholerae",
    known_for=[{EN: "cholera", PL: "cholera"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Vibrio_cholerae.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f6/Vibrio_cholerae.jpg",
        author="Tom Kirn, Ron Taylor, Louisa Howard - Dartmouth Electron Microscope Facility",
        license=License.DARTHMOUTH,
    ),
)
B_ANTHRACIS = Species(
    name="Bacillus anthracis",
    local_names={PL: "laseczka wąglika"},
    known_for=[{EN: "anthrax", PL: "wąglik"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Bacillus_anthracis.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/12/Bacillus_anthracis.png",
        author="CDC",
        license=License.CDC,
    ),
)
M_TUBERCULOSIS = Species(
    name="Mycobacterium tuberculosis",
    local_names={PL: "prątek gruźlicy"},
    known_for=[{EN: "tuberculosis", PL: "gruźlica"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mycobacterium_tuberculosis.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Mycobacterium_tuberculosis.jpg",
        author="CDC/ Janice Carr",
        license=License.CDC,
    ),
)
C_TETANI = Species(
    name="Clostridium tetani",
    local_names={PL: "laseczka tężca"},
    known_for=[{EN: "tetanus", PL: "tężec"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Clostridium_tetani_01.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c7/Clostridium_tetani_01.png",
        author="CDC",
        license=License.CDC,
    ),
)
C_BOTULINUM = Species(
    name="Clostridium botulinum",
    local_names={PL: "laseczka jadu kiełbasianego"},
    known_for=[
        {
            EN: "botulinum toxin, Botox",
            PL: "jad kiełbasiany, toksyna botulinowa, botulina",
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Clostridium_botulinum_01.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/58/Clostridium_botulinum_01.png",
        author="CDC",
        license=License.CDC,
    ),
)
T_PALLIDUM = Species(
    name="Treponema pallidum",
    local_names={PL: "krętek blady"},
    known_for=[{PL: "kiła", NAME: "syphilis"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:TreponemaPallidum.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/TreponemaPallidum.jpg",
        author="CDC/ Dr. David Cox",
        license=License.CDC,
    ),
)
N_GONORRHOEAE = Species(
    name="Neisseria gonorrhoeae",
    local_names={PL: "dwoinka rzeżączki"},
    known_for=[{EN: "gonorrhoea", PL: "rzeżączka"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Gonococcal_urethritis_PHIL_4085_lores.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/2e/Gonococcal_urethritis_PHIL_4085_lores.jpg",
        author="CDC/ Joe Millar",
        license=License.CDC,
    ),
)
C_TRACHOMATIS = Species(
    name="Chlamydia trachomatis",
    known_for=[{EN: "chlamydia", PL: "chlamydioza"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Chlamydia_trachomatis.tif",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/36/Chlamydia_trachomatis.tif",
        author="Centers for Disease Control and Prevention / Dr. E. Arum; Dr. N. Jacobs",
        license=License.CDC,
    ),
)
B_BURGDORFERI = Species(
    name="Borrelia burgdorferi",
    known_for=[{EN: "Lyme disease", PL: "borelioza"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lyme_disease_parasite_Borrelia_burgdorferi.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Lyme_disease_parasite_Borrelia_burgdorferi.jpg",
        author="CDC/ Claudia Molins",
        license=License.CDC,
    ),
)
R_PROWAZEKII = Species(
    name="Rickettsia prowazekii",
    known_for=[
        {EN: "epidemic fever", PL: "tyfus plamisty"},
        {EN: "possibly one of the closest relatives of proto-mitochondria"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:19028_lores.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/19028_lores.jpg",
        author="CDC/ Cornelius B. Philip, National Institute of Allergy and Infectious Diseases, "
        "Rocky Mountain Lab., Hamilton, Montana",
        license=License.CDC,
    ),
)
G_LITHOPHORA = Species(
    name="Gloeomargarita lithophora",
    known_for=[{EN: "possibly the closest relative of chloroplasts"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Minerals-06-00010-g005b.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/b/b8/Minerals-06-00010-g005b.png",
        author="Jinhua Li, Isabel Margaret Oliver, Nithavong Cam, Thomas Boudier, Marine Blondeau, "
        "Eric Leroy, Julie Cosmidis, Feriel Skouri-Panet, Jean-Michel Guigner, Céline Férard, "
        "Melanie Poinsot, David Moreira, Purificacion Lopez-Garcia, Corinne Cassier-Chauvat, "
        "Franck Chauvat, Karim Benzerara",
        license=License.CC_BY_SA_4_0,
    ),
)
P_MARINUS = Species(
    name="Prochlorococcus marinus",
    known_for=[{EN: "probably the most common photosyntetic organism"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Prochlorococcus_marinus_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/67/Prochlorococcus_marinus_%28cropped%29.jpg",
        author="Luke Thompson from Chisholm Lab and Nikki Watson from Whitehead, MIT",
        license=License.CC0,
    ),
)
S_AUREUS = Species(
    name="Staphylococcus aureus",
    local_names={PL: "gronkowiec złocisty"},
    known_for=[{EN: "MRSA (methicillin-resistant Staphylococcus aureus)"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Staphylococcus_aureus_VISA_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d3/Staphylococcus_aureus_VISA_2.jpg",
        author="CDC/ Matthew J. Arduino, DRPH; Photo Credit: Janice Haney Carr",
        license=License.CDC,
    ),
)
T_NAMIBIENSIS = Species(
    name="Thiomargarita namibiensis",
    known_for=[{EN: "the largest known bacteria, visible to the naked eye"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Sulphide_bacteria_crop.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Sulphide_bacteria_crop.jpg",
        author="NASA",
        license=License.NASA,
    ),
)
L_ACIDOPHILUS = Species(
    name="Lactobacillus acidophilus",
    known_for=[
        {EN: "one of the most common probiotic bacteria in dairy products"},
        {EN: "part of vaginal microbiota"},
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Lactobacillus_acidophilus_SEM.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/61/Lactobacillus_acidophilus_SEM.jpg",
        author="Mogana Das Murtey and Patchamuthu Ramasamy",
        license=License.CC_BY_SA_3_0,
    ),
)
H_PYLORI = Species(
    name="Helicobacter pylori",
    known_for=[{EN: "peptic ulcer disease", PL: "choroba wrzodowa"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Helicobacter_pylori_diagram.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Helicobacter_pylori_diagram.png",
        author="Y tambe",
        license=License.CC_BY_SA_3_0,
    ),
)

ESCHERICHIA = Genus(name="Escherichia", children=[E_COLI])
SALMONELLA = Genus(name="Salmonella", children=[S_ENTERICA])
YERSINIA = Genus(name="Yersinia", children=[Y_PESTIS])
VIBRIO = Genus(name="Vibrio", children=[V_CHOLERAE])
BACILLUS = Genus(name="Bacillus", children=[B_ANTHRACIS])
MYCOBACTERIUM = Genus(name="Mycobacterium", children=[M_TUBERCULOSIS])
CLOSTRIDIUM = Genus(name="Clostridium", children=[C_TETANI, C_BOTULINUM])
TREPOMENA = Genus(name="Trepomena", children=[T_PALLIDUM])
BORRELIA = Genus(name="Borrelia", children=[B_BURGDORFERI])
NEISSERIA = Genus(name="Neisseria", children=[N_GONORRHOEAE])
CHLAMYDIA = Genus(name="Chlamydia", children=[C_TRACHOMATIS])
RICKETTSIA = Genus(name="Rickettsia", children=[R_PROWAZEKII])
GLOEOMARGARITA = Genus(name="Gloeomargarita", children=[G_LITHOPHORA])
PROCHLOROCOCCUS = Genus(name="Prochlorococcus", children=[P_MARINUS])
STAPHYLOCOCCUS = Genus(name="Staphylococcus", children=[S_AUREUS])
THIOMARGARITA = Genus(name="Thiomargarita", children=[T_NAMIBIENSIS])
LACTOBACILLUS = Genus(
    name="Lactobacillus",
    children=[L_ACIDOPHILUS],
    local_names={PL: "pałeczki kwasu mlekowego"},
)
HELICOBACTER = Genus(name="Helicobacter", children=[H_PYLORI])

ENTEROBACTERIACEAE = Family(
    name="Enterobacteriaceae", children=[ESCHERICHIA, SALMONELLA]
)
YERSINIACEAE = Family(name="Yersiniaceae", children=[YERSINIA])
VIBRIONACEAE = Family(name="Vibrionaceae", children=[VIBRIO])
BACILLACEAE = Family(name="Bacillaceae", children=[BACILLUS])
MYCOBACTERIACEAE = Family(name="Mycobacteriaceae", children=[MYCOBACTERIUM])
CLOSTRIDIACEAE = Family(name="Clostridiaceae", children=[CLOSTRIDIUM])
SPIROCHAETACEAE = Family(name="Spirochaetaceae", children=[TREPOMENA, BORRELIA])
NEISSERIACEAE = Family(name="Neisseriaceae", children=[NEISSERIA])
RICKETTSIACEAE = Family(name="Rickettsiaceae", children=[RICKETTSIA])
CHLAMYDIACEAE = Family(name="Chlamydiaceae", children=[CHLAMYDIA])
GLOEOMARGARITACEAE = Family(name="Gloeomargaritaceae", children=[GLOEOMARGARITA])
PROCHLORACEAE = Family(name="Prochloraceae", children=[PROCHLOROCOCCUS])
STAPHYLOCOCCACEAE = Family(name="Staphylococcaceae", children=[STAPHYLOCOCCUS])
THIOTRICHACEAE = Family(name="Thiotrichaceae", children=[THIOMARGARITA])
LACTOBACILLACEAE = Family(name="Lactobacillaceae", children=[LACTOBACILLUS])
HELICOBACTERACEAE = Family(name="Helicobacteraceae", children=[HELICOBACTER])

ENTEROBACTERALES = Order(
    name="Enterobacterales", children=[ENTEROBACTERIACEAE, YERSINIACEAE]
)
VIBRIONALES = Order(name="Vibrionales", children=[VIBRIONACEAE])
BACILLALES = Order(name="Bacillales", children=[BACILLACEAE, STAPHYLOCOCCACEAE])
MYCOBACTERIALES = Order(name="Mycobacteriales", children=[MYCOBACTERIACEAE])
CLOSTRIDIALES = Order(name="Clostridiales", children=[CLOSTRIDIACEAE])
SPIROCHAETALES = Order(name="Spirochaetales", children=[SPIROCHAETACEAE])
NEISSERIALES = Order(name="Neisseriales", children=[NEISSERIACEAE])
CHLAMYDIALES = Order(name="Chlamydiales", children=[CHLAMYDIACEAE])
RICKETTSIALES = Order(name="Rickettsiales", children=[RICKETTSIACEAE])
GLOEOMARGARITALES = Order(name="Gloeomargaritales", children=[GLOEOMARGARITACEAE])
SYNECHOCOCCALES = Order(name="Synechococcales", children=[PROCHLORACEAE])
THIOTRICHALES = Order(name="Thiotrichales", children=[THIOTRICHACEAE])
LACTOBACILLALES = Order(
    name="Lactobacillales",
    children=[LACTOBACILLACEAE],
    local_names={EN: "lactic acid bacteria", PL: "bakterie kwasu mlekowego"},
)
CAMPYLOBACTERALES = Order(name="Campylobacterales", children=[HELICOBACTERACEAE])

# https://www.researchgate.net/publication/23983123_Phylogenomics_and_protein_signatures_elucidating_the_evolutionary_relationships_among_the_Gammaproteobacteria
GAMMAPROTEOBACTERIA_A = Clade(children=[ENTEROBACTERALES, VIBRIONALES])

GAMMAPROTEOBACTERIA = Class(
    name="Gammaproteobacteria", children=[GAMMAPROTEOBACTERIA_A, THIOTRICHALES]
)
BETAPROTEOBACTERIA = Class(name="Betaproteobacteria", children=[NEISSERIALES])
BACILLI = Class(name="Bacilli", children=[BACILLALES, LACTOBACILLALES])
ACTINOMYCETIA = Class(name="Actinomycetia", children=[MYCOBACTERIALES])
CLOSTRIDIA = Class(name="Clostridia", children=[CLOSTRIDIALES])
ALPHAPROTEOBACTERIA = Class(name="Alphaproteobacteria", children=[RICKETTSIALES])
CYANOPHYCEAE = Class(name="Cyanophyceae", children=[SYNECHOCOCCALES])
CAMPYLOBACTERIA = Class(name="Campylobacteria", children=[CAMPYLOBACTERALES])

BETA_GAMMA_PROTEOBACTERIA = Clade(children=[GAMMAPROTEOBACTERIA, BETAPROTEOBACTERIA])

PROTEOBACTERIA = Phylum(
    name="Proteobacteria", children=[ALPHAPROTEOBACTERIA, BETA_GAMMA_PROTEOBACTERIA]
)
FIRMICUTES = Phylum(name="Firmicutes", children=[BACILLI, CLOSTRIDIA])
ACTINOBACTERIA = Phylum(name="Actinobacteria", children=[ACTINOMYCETIA])
SPIROCHAETES = Phylum(name="Spirochaetes", children=[SPIROCHAETALES])
CHLAMYDIOTA = Phylum(name="Chlamydiota", children=[CHLAMYDIALES])
CYANOBACTERIA = Phylum(name="Cyanobacteria", children=[GLOEOMARGARITALES, CYANOPHYCEAE])
CAMPYLOBACTEROTA = Phylum(name="Campylobacterota", children=[CAMPYLOBACTERIA])

PVC_SUPERPHYLUM = Superphylum(name="PVC superphylum", children=[CHLAMYDIOTA])

HYDROBACTERIA_B = Clade(children=[PROTEOBACTERIA, CAMPYLOBACTEROTA])
HYDROBACTERIA_A = Clade(children=[HYDROBACTERIA_B, PVC_SUPERPHYLUM])

FIRMICUTES_ACTINOBACTERIA = Clade(children=[FIRMICUTES, ACTINOBACTERIA])
TERRABACTERIA = Clade(
    name="Terrabacteria", children=[FIRMICUTES_ACTINOBACTERIA, CYANOBACTERIA]
)
HYDROBACTERIA = Clade(name="Hydrobacteria", children=[HYDROBACTERIA_A, SPIROCHAETES])

BACTERIA = Domain(name="Bacteria", children=[HYDROBACTERIA, TERRABACTERIA])
