from clade import Clade, Family, Genus, Order, Species, Suborder

S_STENOPS = Species(name="Stegosaurus stenops")
A_MAGNIVENTRIS = Species(name="Ankylosaurus magniventris")
P_ANDREWSI = Species(name="Protoceratops andrewsi")
T_HORRIDUS = Species(name="Triceratops horridus")
S_ALBERTENSIS = Species(name="Styracosaurus albertensis")
I_BERNISSARTENSIS = Species(name="Iguanodon bernissartensis")
S_OSBORNI = Species(name="Saurolophus osborni")

STEGOSAURUS = Genus(name="Stegosaurus", children=[S_STENOPS])
ANKYLOSAURUS = Genus(name="Ankylosaurus", children=[A_MAGNIVENTRIS])
PROTOCERATOPS = Genus(name="Protoceratops", children=[P_ANDREWSI])
TRICERATOPS = Genus(name="Triceratops", children=[T_HORRIDUS])
STYRACOSAURUS = Genus(name="Styracosaurus", children=[S_ALBERTENSIS])
IGUANODON = Genus(name="Iguanodon", children=[I_BERNISSARTENSIS])
SAUROLOPHUS = Genus(name="Saurolophus", children=[S_OSBORNI])

STEGOSAURIDAE = Family(name="Stegosauridae", children=[STEGOSAURUS])
ANKYLOSAURIDAE = Family(name="Ankylosauridae", children=[ANKYLOSAURUS])
PROTOCERATOPSIDAE = Family(name="Protoceratopsidae", children=[PROTOCERATOPS])
CERATOPSIDAE = Family(name="Ceratopsidae", children=[TRICERATOPS, STYRACOSAURUS])
IGUANODONTIDAE = Family(name="Iguanodontidae", children=[IGUANODON])
HADROSAURIDAE = Family(name="Hadrosauridae", children=[SAUROLOPHUS])

STEGOSAURIA = Suborder(name="Stegosauria", children=[STEGOSAURIDAE])
ANKYLOSAURIA = Suborder(name="Ankylosauria", children=[ANKYLOSAURIDAE])
CERATOPSIA = Suborder(name="Ceratopsia", children=[PROTOCERATOPSIDAE, CERATOPSIDAE])

ORNITHOPODA = Clade(name="Ornithopoda", children=[IGUANODONTIDAE, HADROSAURIDAE])

THYREOPHORA = Clade(name="Thyreophora", children=[STEGOSAURIA, ANKYLOSAURIA])
CERAPODA = Clade(name="Cerapoda", children=[CERATOPSIA, ORNITHOPODA])

ORNITHISCHIA = Order(name="Ornithischia", children=[THYREOPHORA, CERAPODA])
