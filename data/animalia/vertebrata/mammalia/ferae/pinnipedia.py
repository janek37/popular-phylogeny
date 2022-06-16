from clade import Clade, Family, Genus, Species
from constants import EN, PL
from image import Image, License

P_VITULINA = Species(
    name="Phoca vitulina",
    local_names={EN: "harbour seal, common seal", PL: "foka pospolita"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Common_seal_(Phoca_vitulina).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/76/Common_seal_%28Phoca_vitulina%29.jpg",
        author="Charles J. Sharp",
        license=License.CC_BY_SA_4_0,
    ),
)
M_ANGUSTIROSTRIS = Species(
    name="Mirounga angustirostris",
    local_names={
        EN: "northern elephant seal",
        PL: "słoń morski północny, mirunga północna",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Mirounga_angustirostris,_Point_Reyes_(cropped).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/52/Mirounga_angustirostris%2C_Point_Reyes_%28cropped%29.jpg",
        author="Frank Schulenburg",
        license=License.CC_BY_SA_3_0,
    ),
)
Z_CALIFORNIANUS = Species(
    name="Zalophus californianus",
    local_names={
        EN: "California sea lion",
        PL: "uchatka kalifornijska, uszanka kalifornijska",
    },
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Zalophus_californianus_-_Morro_Bay.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8f/Zalophus_californianus_-_Morro_Bay.jpg",
        author="Mike Baird from Morro Bay, USA",
        license=License.CC_BY_2_0,
    ),
)
A_PUSILLUS = Species(
    name="Arctocephalus pusillus",
    local_names={EN: "brown fur seal", PL: "uchatka karłowata, kotik karłowaty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Arctocephalus_pusillus_in_Tobu_Zoo_Park_003_%E2%80%93_cleaned_background_and_cropped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/74/Arctocephalus_pusillus_in_Tobu_Zoo_Park_003_%E2%80%93_cleaned_background_and_cropped.jpg",
        author="Ocdp",
        license=License.CC0,
    ),
)
O_ROSMARUS = Species(
    name="Odobenus rosmarus",
    local_names={EN: "walrus", PL: "mors arktyczny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Noaa-walrus22.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/ce/Noaa-walrus22.jpg",
        author="Captain Budd Christman, NOAA Corps",
        license=License.NOAA,
    ),
)

PHOCA = Genus(name="Phoca", children=[P_VITULINA])
MIROUNGA = Genus(name="Mirounga", children=[M_ANGUSTIROSTRIS])
ZALOPHUS = Genus(name="Zalophus", children=[Z_CALIFORNIANUS])
ARCTOCEPHALUS = Genus(name="Arctocephalus", children=[A_PUSILLUS])
ODOBENUS = Genus(name="Odobenus", children=[O_ROSMARUS])

PHOCIDAE = Family(name="Phocidae", children=[PHOCA, MIROUNGA])
OTARIIDAE = Family(name="Otariidae", children=[ZALOPHUS, ARCTOCEPHALUS])
ODOBENIDAE = Family(name="Odobenidae", children=[ODOBENUS])

PINNIPEDIA_A = Clade(children=[OTARIIDAE, ODOBENIDAE])
PINNIPEDIA = Clade(name="Pinnipedia", children=[PHOCIDAE, PINNIPEDIA_A])
