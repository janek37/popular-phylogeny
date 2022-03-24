from clade import Clade, Family, Genus, Species
from constants import EN, PL

P_VITULINA = Species(
    name="Phoca vitulina",
    local_names={EN: "harbour seal, common seal", PL: "foka pospolita"},
)
M_ANGUSTIROSTRIS = Species(
    name="Mirounga angustirostris",
    local_names={
        EN: "northern elephant seal",
        PL: "słoń morski północny, mirunga północna",
    },
)
Z_CALIFORNIANUS = Species(
    name="Zalophus californianus",
    local_names={
        EN: "California sea lion",
        PL: "uchatka kalifornijska, uszanka kalifornijska",
    },
)
A_PUSILLUS = Species(
    name="Arctocephalus pusillus",
    local_names={EN: "brown fur seal", PL: "uchatka karłowata, kotik karłowaty"},
)
O_ROSMARUS = Species(
    name="Odobenus rosmarus", local_names={EN: "walrus", PL: "mors arktyczny"}
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
