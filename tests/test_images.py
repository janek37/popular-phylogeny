from clade import Species
from constants import IMAGE


def test_images(life_clades):
    species_without_images = []
    for clade in life_clades:
        if isinstance(clade, Species):
            if not clade.image:
                species_without_images.append(clade.name)
    assert species_without_images == []


def test_no_images_in_local_names(life_clades):
    local_names_with_images = []
    for clade in life_clades:
        if IMAGE in clade.local_names:
            local_names_with_images.append(clade.name)
    assert local_names_with_images == []
