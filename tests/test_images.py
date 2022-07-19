from clade import Species


def test_images(life_clades):
    species_without_images = []
    for clade in life_clades:
        if isinstance(clade, Species):
            if not clade.image:
                species_without_images.append(clade.name)
    assert species_without_images == []
