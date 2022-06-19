from clade import Clade, Family, Genus, Species, Superfamily
from constants import EN, PL, URL
from image import Image, License

from .avialae import AVIALAE

C_BAURI = Species(
    name="Coelophysis bauri",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Coelophysis_size_flipped.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/37/Coelophysis_size_flipped.jpg",
        author="Michiel, Petrified ForestNPS@Flickr",
        license=License.NPS,
    ),
)
D_WETHERILLI = Species(
    name="Dilophosaurus wetherilli",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dilophosaurus_in_bird-like_resting_pose.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Dilophosaurus_in_bird-like_resting_pose.jpg",
        author="Heather Kyoht Luterman",
        license=License.CC_BY_2_5,
    ),
)
C_SASTREI = Species(
    name="Carnotaurus sastrei",
    known_for=[
        {
            EN: "villains from the film Dinosaur",
            URL: "https://disney.fandom.com/wiki/Carnotaurus",
        }
    ],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Carnotaurus_Reconstruction_(2022).png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/81/Carnotaurus_Reconstruction_%282022%29.png",
        author="Fred Wierum",
        license=License.CC_BY_SA_4_0,
    ),
)
C_NASICORNIS = Species(
    name="Ceratosaurus nasicornis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Ceratosaurus_nasicornis_DB_2.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c4/Ceratosaurus_nasicornis_DB_2.jpg",
        author="DiBgd at English Wikipedia, Bogdanov dmitrchel@mail.ru",
        license=License.CC_BY_SA_3_0,
    ),
)
S_AEGYPTIACUS = Species(
    name="Spinosaurus aegyptiacus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Spinosaurus_2020_reconstruction.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Spinosaurus_2020_reconstruction.jpg",
        author="Mariolanzas",
        license=License.CC_BY_SA_4_0,
    ),
)
B_WALKERI = Species(
    name="Baryonyx walkeri",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Baryonyx_walkeri_restoration.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/92/Baryonyx_walkeri_restoration.jpg",
        author="Lineart by Robinson Kunz (https://teratophoneus.deviantart.com/); Color by Rebecca Slater (https://paleocolour.deviantart.com/)",
        license=License.CC_BY_SA_3_0,
    ),
)
M_BUCKLANDII = Species(
    name="Megalosaurus bucklandii",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Megalosaurus_0289.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Megalosaurus_0289.JPG",
        author="Conty",
        license=License.CC_BY_SA_3_0,
    ),
)
A_FRAGILIS = Species(
    name="Allosaurus fragilis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Allosaurus_Revised.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/3/3d/Allosaurus_Revised.jpg",
        author="Fred Wierum",
        license=License.CC_BY_SA_4_0,
    ),
)
T_REX = Species(
    name="Tyrannosaurus rex",
    local_names={EN: "T-Rex", PL: "tyranozaur rex"},
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Rjpalmer_tyrannosaurusrex_(white_background).jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c0/Rjpalmer_tyrannosaurusrex_%28white_background%29.jpg",
        author="RJPalmerArt",
        license=License.CC_BY_SA_4_0,
    ),
)
C_LONGIPES = Species(
    name="Compsognathus longipes",
    known_for=[{EN: "one of the smallest known (non-avialan) dinosaurs"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Compsognathus_95898.jpg",
        image_url="https://upload.wikimedia.org/wikipedia/commons/8/8d/Compsognathus_95898.jpg",
        author="Conty",
        license=License.CC_BY_SA_4_0,
    ),
)
D_BREVITERTIUS = Species(
    name="Dromiceiomimus brevitertius",
    known_for=[{EN: "Ryan North's Dinosaur Comics", URL: "https://qwantz.com"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Dromiceiomimus_03747.JPG",
        image_url="https://upload.wikimedia.org/wikipedia/commons/9/9e/Dromiceiomimus_03747.JPG",
        author="Conty",
        license=License.CC_BY_3_0,
    ),
)
D_ANTIRRHOPUS = Species(
    name="Deinonychus antirrhopus",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Deinonychus_Restoration.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/1e/Deinonychus_Restoration.png",
        author="Fred Wierum",
        license=License.CC_BY_SA_4_0,
    ),
)
V_MONGOLIENSIS = Species(
    name="Velociraptor mongoliensis",
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Velociraptor_Restoration.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/5/55/Velociraptor_Restoration.png",
        author="Fred Wierum",
        license=License.CC_BY_SA_4_0,
    ),
)
U_OSTROMMAYSI = Species(
    name="Utahraptor ostrommaysi",
    known_for=[{EN: "Ryan North's Dinosaur Comics", URL: "https://qwantz.com"}],
    extinct=True,
    image=Image(
        url="https://commons.wikimedia.org/wiki/File:Utahraptor_ostrommaysorum.png",
        image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Utahraptor_ostrommaysorum.png",
        author="Ferahgo the Assassin (Emily Willoughby, e.deinonychus@gmail.com) https://emilywilloughby.com",
        license=License.CC_BY_SA_3_0,
    ),
)

COELOPHYSIS = Genus(name="Coelophysis", children=[C_BAURI])
DILOPHOSAURUS = Genus(name="Dilophosaurus", children=[D_WETHERILLI])
CARNOTAURUS = Genus(name="Carnotaurus", children=[C_SASTREI])
CERATOSAURUS = Genus(name="Ceratosaurus", children=[C_NASICORNIS])
SPINOSAURUS = Genus(name="Spinosaurus", children=[S_AEGYPTIACUS])
BARYONYX = Genus(name="Baryonyx", children=[B_WALKERI])
ALLOSAURUS = Genus(name="Allosaurus", children=[A_FRAGILIS])
TYRANNOSAURUS = Genus(name="Tyrannosaurus", children=[T_REX])
COMPSOGNATHUS = Genus(name="Compsognathus", children=[C_LONGIPES])
DROMICEIOMIMUS = Genus(name="Dromiceiomimus", children=[D_BREVITERTIUS])
DEINONYCHUS = Genus(name="Deinonychus", children=[D_ANTIRRHOPUS])
VELOCIRAPTOR = Genus(name="Velociraptor", children=[V_MONGOLIENSIS])
UTAHRAPTOR = Genus(name="Utahraptor", children=[U_OSTROMMAYSI])

COELOPHYSIDAE = Family(name="Coelophysidae", children=[COELOPHYSIS])
DILOPHOSAURIDAE = Family(name="Dilophosauridae", children=[DILOPHOSAURUS])
ABELISAURIDAE = Family(name="Abelisauridae", children=[CARNOTAURUS])
CERATOSAURIDAE = Family(name="Ceratosauridae", children=[CERATOSAURUS])
SPINOSAURIDAE = Family(name="Spinosauridae", children=[SPINOSAURUS, BARYONYX])
ALLOSAURIDAE = Family(name="Allosauridae", children=[ALLOSAURUS])
TYRANNOSAURIDAE = Family(name="Tyrannosauridae", children=[TYRANNOSAURUS])
COMPSOGNATHIDAE = Family(name="Compsognathidae", children=[COMPSOGNATHUS])
ORNITHOMIMIDAE = Family(name="Ornithomimidae", children=[DROMICEIOMIMUS])
# unresolved
DROMAEOSAURIDAE = Family(
    name="Dromaeosauridae", children=[DEINONYCHUS, VELOCIRAPTOR, UTAHRAPTOR]
)

COELOPHYSOIDEA = Superfamily(name="Coelophysoidea", children=[COELOPHYSIDAE])
MEGALOSAUROIDEA = Superfamily(name="Megalosauroidea", children=[SPINOSAURIDAE])
ALLOSAUROIDEA = Superfamily(name="Allosauroidea", children=[ALLOSAURIDAE])
TYRANNOSAUROIDEA = Superfamily(name="Tyrannosauroidea", children=[TYRANNOSAURIDAE])

CERATOSAURIA = Clade(name="Ceratosauria", children=[ABELISAURIDAE, CERATOSAURIDAE])
ORNITHOMIMOSAURIA = Clade(name="Ornithomimosauria", children=[ORNITHOMIMIDAE])

MANIRAPTORA = Clade(name="Maniraptora", children=[DROMAEOSAURIDAE, AVIALAE])
MANIRAPTORIFORMES = Clade(
    name="Maniraptoriformes", children=[ORNITHOMIMOSAURIA, MANIRAPTORA]
)
NEOCOELUROSAURIA = Clade(
    name="Neocoelurosauria", children=[COMPSOGNATHIDAE, MANIRAPTORIFORMES]
)
COELUROSAURIA = Clade(
    name="Coelurosauria", children=[TYRANNOSAUROIDEA, NEOCOELUROSAURIA]
)
AVETHEROPODA = Clade(name="Avetheropoda", children=[ALLOSAUROIDEA, COELUROSAURIA])
TETANURAE = Clade(name="Tetanurae", children=[MEGALOSAUROIDEA, AVETHEROPODA])
AVEROSTRA = Clade(name="Averostra", children=[CERATOSAURIA, TETANURAE])

THEROPODA_A = Clade(children=[DILOPHOSAURIDAE, AVEROSTRA])

THEROPODA = Clade(name="Theropoda", children=[COELOPHYSOIDEA, THEROPODA_A])
