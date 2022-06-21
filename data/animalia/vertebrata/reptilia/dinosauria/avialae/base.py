from clade import Clade, Class, Family, Genus, Infraclass, Species, Superorder
from constants import EN, IMAGE
from image import Image, License

from .anseriformes import ANSERIFORMES
from .galliformes import GALLIFORMES
from .neoaves import NEOAVES
from .palaeognathe import PALAEOGNATHAE

A_SIEMENSII = Species(
    name="Archaeopteryx siemensii",
    known_for=[
        {
            EN: "famous fossil of the Berlin specimen",
            IMAGE: Image(
                url="https://commons.wikimedia.org/wiki/File:Archaeopteryx_lithographica_(Berlin_specimen).jpg",
                image_url="https://upload.wikimedia.org/wikipedia/commons/9/9d/Archaeopteryx_lithographica_%28Berlin_specimen%29.jpg",
                author="H. Raab (User: Vesta)",
                license=License.CC_BY_SA_3_0,
            ),
        }
    ],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:202010_Archaeopteryx_lithographica.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/0/00/202010_Archaeopteryx_lithographica.png",
        author="DataBase Center for Life Science (DBCLS)",
        license=License.CC_BY_4_0,
    ),
)

ARCHAEOPTERYX = Genus(name="Archaeopteryx", children=[A_SIEMENSII])

ARCHAEOPTERYGIDAE = Family(name="Archaeopterygidae", children=[ARCHAEOPTERYX])

GALLOANSERAE = Superorder(name="Galloanserae", children=[GALLIFORMES, ANSERIFORMES])

NEOGNATHAE = Infraclass(name="Neognathae", children=[GALLOANSERAE, NEOAVES])

AVES = Class(name="Aves", children=[PALAEOGNATHAE, NEOGNATHAE])

AVIALAE = Clade(name="Avialae", children=[ARCHAEOPTERYGIDAE, AVES])
