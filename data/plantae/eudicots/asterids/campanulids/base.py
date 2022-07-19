from clade import Clade, Family, Genus, Order, Species
from constants import EN, IMAGE, PL
from image import Image, License

from .apiales import APIALES
from .asterales import ASTERALES

I_AQUIFOLIUM = Species(
    name="Ilex aquifolium",
    local_names={EN: "common holly", PL: "ostrokrzew kolczasty"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ilex_aquifolium_Holly.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Ilex_aquifolium_Holly.jpg",
        author="AnemoneProjectors (talk)",
        license=License.CC_BY_SA_2_0,
    ),
)
I_PARAGUARIENSIS = Species(
    name="Ilex paraguariensis",
    local_names={EN: "yerba mate", PL: "ostrokrzew paragwajski"},
    known_for=[
        {
            EN: "mate",
            PL: "yerba mate",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Mate_en_calabaza.jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Mate_en_calabaza.jpg",
                author="Jorge Alfonso Hernández",
                license=License.CC_BY_SA_2_5,
            ),
        }
    ],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ilex_paraguariensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-074.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/2/28/Ilex_paraguariensis_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-074.jpg",
        author="Franz Eugen Köhler, Köhler's Medizinal-Pflanzen",
        license=License.PUBLIC_DOMAIN_OLD,
    ),
)
S_NIGRA = Species(
    name="Sambucus nigra",
    local_names={EN: "black elder, European elderberry", PL: "bez czarny"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:20130817Sambucus_nigra2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/62/20130817Sambucus_nigra2.jpg",
        author="AnRo0002",
        license=License.CC0,
    ),
)
V_OPULUS = Species(
    name="Viburnum opulus",
    local_names={EN: "guelder-rose", PL: "kalina koralowa"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Viburnum_opulus_-_kalyna_ukraine.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/6/66/Viburnum_opulus_-_kalyna_ukraine.jpg",
        author="Texnik",
        license=License.CC_BY_SA_3_0,
    ),
)
V_OFFICINALIS = Species(
    name="Valeriana officinalis",
    local_names={EN: "valerian", PL: "kozłek lekarski"},
    known_for=[{PL: "krople walerianowe"}],
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Valeriana_officinalis_-_Niitv%C3%A4lja.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/90/Valeriana_officinalis_-_Niitv%C3%A4lja.jpg",
        author="Ivar Leidus",
        license=License.CC_BY_SA_4_0,
    ),
)
V_LOCUSTA = Species(
    name="Valerianella locusta",
    local_names={EN: "lamb's lettuce, corn salad", PL: "roszpunka warzywna"},
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Valerianella_locusta_38359051.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/5c/Valerianella_locusta_38359051.jpg",
        author="spacecowboy",
        license=License.CC_BY_4_0,
    ),
)

ILEX = Genus(name="Ilex", children=[I_AQUIFOLIUM, I_PARAGUARIENSIS])
SAMBUCUS = Genus(name="Sambucus", children=[S_NIGRA])
VIBURNUM = Genus(name="Viburnum", children=[V_OPULUS])
VALERIANA = Genus(name="Valeriana", children=[V_OFFICINALIS])
VALERIANELLA = Genus(name="Valerianella", children=[V_LOCUSTA])

AQUIFOLIACEAE = Family(name="Aquifoliaceae", children=[ILEX])
ADOXACEAE = Family(name="Adoxaceae", children=[SAMBUCUS, VIBURNUM])
CAPRIFOLIACEAE = Family(name="Caprifoliaceae", children=[VALERIANA, VALERIANELLA])

AQUIFOLIALES = Order(name="Aquifoliales", children=[AQUIFOLIACEAE])
DIPSACALES = Order(name="Dipsacales", children=[ADOXACEAE, CAPRIFOLIACEAE])

CAMPANULIDS_B = Clade(children=[APIALES, DIPSACALES])
CAMPANULIDS_A = Clade(children=[ASTERALES, CAMPANULIDS_B])
CAMPANULIDS = Clade(name="campanulids", children=[AQUIFOLIALES, CAMPANULIDS_A])
