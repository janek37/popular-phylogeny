from clade import Clade, Genus, Species, Subfamily, Tribe
from constants import EN, PL
from image import Image, License

O_MOSCHATUS = Species(
    name="Ovibos moschatus",
    local_names={EN: "muskox", PL: "wół piżmowy, piżmowół arktyczny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ovibos_moschatus_qtl3.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ed/Ovibos_moschatus_qtl3.jpg",
        author="Quartl",
        license=License.CC_BY_SA_3_0,
    ),
)
O_ARIES = Species(
    name="Ovis aries",
    local_names={EN: "domestic sheep", PL: "owca domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ovella._Galiza.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/cd/Ovella._Galiza.jpg",
        author="Luis Miguel Bugallo Sánchez (Lmbuga)",
        license=License.CC_BY_SA_3_0,
    ),
)
R_RUPICAPRA = Species(
    name="Rupicapra rupicapra",
    local_names={EN: "chamois", PL: "kozica północna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rupicapra_rupicapra_tatrica.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/f/f4/Rupicapra_rupicapra_tatrica.jpg",
        author="Jacek rybak",
        license=License.CC_BY_SA_4_0,
    ),
)
O_AMERICANUS = Species(
    name="Oreamnos americanus",
    local_names={EN: "mountain goat", PL: "koza śnieżna, kozioł śnieżny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mountain_Goat_Mount_Massive.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/16/Mountain_Goat_Mount_Massive.JPG",
        author="Darklich14",
        license=License.CC_BY_3_0,
    ),
)
C_HIRCUS = Species(
    name="Capra hircus",
    local_names={EN: "goat", PL: "koza domowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Capra_aegagrus_hircus_qtl2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/29/Capra_aegagrus_hircus_qtl2.jpg",
        author="Quartl",
        license=License.CC_BY_SA_3_0,
    ),
)
C_IBEX = Species(
    name="Capra ibex",
    local_names={EN: "alpine ibex", PL: "koziorożec alpejski"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Alpensteinbock_(Capra_ibex)_Zoo_Salzburg_2014_h.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/e/ea/Alpensteinbock_%28Capra_ibex%29_Zoo_Salzburg_2014_h.jpg",
        author="Manfred Werner - Tsui",
        license=License.CC_BY_SA_3_0,
    ),
)
E_THOMSONII = Species(
    name="Eudorcas thomsonii",
    local_names={
        EN: "Thomson's gazelle",
        PL: "tomi, gazela Thomsona, gazelopka sawannowa",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Eudorcas_thomsonii_-Serengeti_National_Park,_Tanzania-8.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Eudorcas_thomsonii_-Serengeti_National_Park%2C_Tanzania-8.jpg",
        author="Bob",
        license=License.CC_BY_3_0,
    ),
)
K_KOB = Species(
    name="Kobus kob",
    local_names={EN: "kob", PL: "kob żółty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ugandan_kob_(Kobus_kob_thomasi)_male.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3b/Ugandan_kob_%28Kobus_kob_thomasi%29_male.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
C_TAURINUS = Species(
    name="Connochaetes taurinus",
    local_names={
        EN: "blue wildebeest, common wildebeest, white-bearded gnu, brindled gnu",
        PL: "gnu pręgowane",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Connochaetes_taurinus_27zz.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/7e/Connochaetes_taurinus_27zz.jpg",
        author="Photo by David J. Stang",
        license=License.CC_BY_SA_4_0,
    ),
)
O_GAZELLA = Species(
    name="Oryx gazella",
    local_names={EN: "gemsbok, gemsbuck, South African oryx", PL: "oryks południowy"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:2832oryxIMGP3559.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/19/2832oryxIMGP3559.jpg",
        author="Pdeley",
        license=License.CC_BY_SA_4_0,
    ),
)

OVIBOS = Genus(name="Ovibos", children=[O_MOSCHATUS])
OVIS = Genus(name="Ovis", children=[O_ARIES])
RUPICAPRA = Genus(name="Rupicapra", children=[R_RUPICAPRA])
OREAMNOS = Genus(name="Oreamnos", children=[O_AMERICANUS])
CAPRA = Genus(name="Capra", children=[C_HIRCUS, C_IBEX])
EUDORCAS = Genus(name="Eudorcas", children=[E_THOMSONII])
KOBUS = Genus(name="Kobus", children=[K_KOB])
CONNOCHAETES = Genus(name="Connochaetes", children=[C_TAURINUS])
ORYX = Genus(name="Oryx", children=[O_GAZELLA])

CAPRINI_B = Clade(children=[RUPICAPRA, OREAMNOS])
CAPRINI_A = Clade(children=[CAPRINI_B, CAPRA])

OVIBOVINI = Tribe(name="Ovibovini", children=[OVIBOS])
CAPRINI = Tribe(name="Caprini", children=[OVIS, CAPRINI_A])

CAPRINAE = Subfamily(name="Caprinae", children=[OVIBOVINI, CAPRINI])
ANTILOPINAE = Subfamily(name="Antilopinae", children=[EUDORCAS])
REDUNCINAE = Subfamily(name="Reduncinae", children=[KOBUS])
ALCELAPHINAE = Subfamily(name="Alcelaphinae", children=[CONNOCHAETES])
HIPPOTRAGINAE = Subfamily(name="Hippotraginae", children=[ORYX])

AEGODONTIA_C = Clade(children=[ALCELAPHINAE, HIPPOTRAGINAE])
AEGODONTIA_B = Clade(children=[CAPRINAE, AEGODONTIA_C])
AEGODONTIA_A = Clade(children=[REDUNCINAE, AEGODONTIA_B])
AEGODONTIA = Clade(name="Aegodontia", children=[ANTILOPINAE, AEGODONTIA_A])
