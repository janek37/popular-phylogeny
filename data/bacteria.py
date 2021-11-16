from clade import Domain, Clade, Superphylum, Phylum, Class, Order, Family, Genus, Species
from constants import PL, EN, LA

E_COLI = Species(name='Escherichia coli', local_names={PL: 'Pałeczka okrężnicy'})
S_ENTERICA = Species(name='Salmonella enterica', known_for=[{PL: 'dur brzuszny', EN: 'typhoid fever'}])

Y_PESTIS = Species(name='Yersinia pestis', local_names={PL: 'Pałeczka dżumy'})
V_CHOLERAE = Species(name='Vibrio cholerae')
B_ANTHRACIS = Species(name='Bacillus anthracis', local_names={PL: 'Laseczka wąglika'})
M_TUBERCULOSIS = Species(name='Mycobacterium tuberculosis', local_names={PL: 'Prątek gruźlicy'})
C_TETANI = Species(name='Clostridium tetani', local_names={PL: 'Laseczka tężca'})
C_BOTULINUM = Species(name='Clostridium botulinum', local_names={PL: 'Laseczka jadu kiełbasianego'})
T_PALLIDUM = Species(
    name='Treponema pallidum',
    local_names={PL: 'Krętek blady'},
    known_for=[{PL: 'kiła', LA: 'syphilis'}],
)
N_GONORRHOEAE = Species(name='Neisseria gonorrhoeae', local_names={PL: 'Dwoinka rzeżączki'})
C_TRACHOMATIS = Species(name='Chlamydia trachomatis')
B_BURGDORFERI = Species(name='Borrelia burgdorferi', known_for=[{EN: 'Lyme disease', PL: 'borelioza'}])
R_PROWAZEKII = Species(
    name='Rickettsia prowazekii',
    known_for=[
        {EN: 'epidemic fever', PL: 'tyfus plamisty'},
        {EN: 'possibly one of the closest relatives of proto-mitochondria'},
    ],
)
G_LITHOPHORA = Species(
    name='Gloeomargarita lithophora',
    known_for=[{EN: 'possibly the closest relative of chloroplasts'}],
)
S_AUREUS = Species(
    name='Staphylococcus aureus',
    local_names={PL: 'gronkowiec złocisty'},
    known_for=[{EN: 'MRSA (methicillin-resistant Staphylococcus aureus)'}],
)

ESCHERICHIA = Genus(name='Escherichia', children=[E_COLI])
SALMONELLA = Genus(name='Salmonella', children=[S_ENTERICA])
YERSINIA = Genus(name='Yersinia', children=[Y_PESTIS])
VIBRIO = Genus(name='Vibrio', children=[V_CHOLERAE])
BACILLUS = Genus(name='Bacillus', children=[B_ANTHRACIS])
MYCOBACTERIUM = Genus(name='Mycobacterium', children=[M_TUBERCULOSIS])
CLOSTRIDIA = Genus(name='Clostridia', children=[C_TETANI, C_BOTULINUM])
TREPOMENA = Genus(name='Trepomena', children=[T_PALLIDUM])
BORRELIA = Genus(name='Borrelia', children=[B_BURGDORFERI])
NEISSERIA = Genus(name='Neisseria', children=[N_GONORRHOEAE])
CHLAMYDIA = Genus(name='Chlamydia', children=[C_TRACHOMATIS])
RICKETTSIA = Genus(name='Rickettsia', children=[R_PROWAZEKII])
GLOEOMARGARITA = Genus(name='Gloeomargarita', children=[G_LITHOPHORA])
STAPHYLOCOCCUS = Genus(name='Staphylococcus', children=[S_AUREUS])

ENTEROBACTERIACEAE = Family(name='Enterobacteriaceae', children=[ESCHERICHIA, SALMONELLA])
YERSINIACEAE = Family(name='Yersiniaceae', children=[YERSINIA])
VIBRIONACEAE = Family(name='Vibrionaceae', children=[VIBRIO])
BACILLACEAE = Family(name='Bacillaceae', children=[BACILLUS])
MYCOBACTERIACEAE = Family(name='Mycobacteriaceae', children=[MYCOBACTERIUM])
CLOSTRIDIACEAE = Family(name='Clostridiaceae', children=[CLOSTRIDIA])
SPIROCHAETACEAE = Family(name='Spirochaetaceae', children=[TREPOMENA, BORRELIA])
NEISSERIACEAE = Family(name='Neisseriaceae', children=[NEISSERIA])
RICKETTSIACEAE = Family(name='Rickettsiaceae', children=[RICKETTSIA])
CHLAMYDIACEAE = Family(name='Chlamydiaceae', children=[CHLAMYDIA])
GLOEOMARGARITACEAE = Family(name='Gloeomargaritaceae', children=[GLOEOMARGARITA])
STAPHYLOCOCCACEAE = Family(name='Staphylococcaceae', children=[STAPHYLOCOCCUS])

ENTEROBACTERALES = Order(name='Enterobacterales', children=[ENTEROBACTERIACEAE, YERSINIACEAE])
VIBRIONALES = Order(name='Vibrionales', children=[VIBRIONACEAE])
BACILLALES = Order(name='Bacillales', children=[BACILLACEAE, STAPHYLOCOCCACEAE])
MYCOBACTERIALES = Order(name='Mycobacteriales', children=[MYCOBACTERIACEAE])
CLOSTRIDIALES = Order(name='Clostridiales', children=[CLOSTRIDIACEAE])
SPIROCHAETALES = Order(name='Spirochaetales', children=[SPIROCHAETACEAE])
NEISSERIALES = Order(name='Neisseriales', children=[NEISSERIACEAE])
CHLAMYDIALES = Order(name='Chlamydiales', children=[CHLAMYDIACEAE])
RICKETTSIALES = Order(name='Rickettsiales', children=[RICKETTSIACEAE])
GLOEOMARGARITALES = Order(name='Gleomargaritales', children=[GLOEOMARGARITACEAE])

GAMMAPROTEOBACTERIA = Class(name='Gammaproteobacteria', children=[ENTEROBACTERALES, VIBRIONALES])
BETAPROTEOBACTERIA = Class(name='Betaproteobacteria', children=[NEISSERIALES])
BACILLI = Class(name='Bacilli', children=[BACILLALES])
ACTINOMYCETIA = Class(name='Actinomycetia', children=[MYCOBACTERIALES])
CLOSTRIDIA = Class(name='Clostridia', children=[CLOSTRIDIALES])
ALPHAPROTEOBACTERIA = Class(name='Alphaproteobacteria', children=[RICKETTSIALES])

BETA_GAMMA_PROTEOBACTERIA = Clade(children=[GAMMAPROTEOBACTERIA, BETAPROTEOBACTERIA])

PROTEOBACTERIA = Phylum(name='Proteobacteria', children=[ALPHAPROTEOBACTERIA, BETA_GAMMA_PROTEOBACTERIA])
FIRMICUTES = Phylum(name='Firmicutes', children=[BACILLI, CLOSTRIDIA])
ACTINOBACTERIA = Phylum(name='Actinobacteria', children=[ACTINOMYCETIA])
SPIROCHAETES = Phylum(name='Spirochaetes', children=[SPIROCHAETALES])
CHLAMYDIAE = Phylum(name='Chlamydiae', children=[CHLAMYDIALES])
CYANOBACTERIA = Phylum(name='Cyanobacteria', children=[GLOEOMARGARITALES])

PLANCTOBACTERIA = Superphylum(name='Planctobacteria', children=[CHLAMYDIAE])

PLANCTO_PROTEO_BACTERIA = Clade(children=[PROTEOBACTERIA, PLANCTOBACTERIA])

FIRMICUTES_ACTINOBACTERIA = Clade(children=[FIRMICUTES, ACTINOBACTERIA])
TERRABACTERIA = Clade(name='Terrabacteria', children=[FIRMICUTES_ACTINOBACTERIA, CYANOBACTERIA])
GRACILLICUTES = Clade(name='Gracillicutes', children=[PLANCTO_PROTEO_BACTERIA, SPIROCHAETES])

BACTERIA = Domain(name='Bacteria', children=[GRACILLICUTES, TERRABACTERIA])