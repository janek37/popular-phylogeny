import importlib
from typing import List, Tuple

import pytest

from clade import BaseClade, Rank


@pytest.fixture
def named_clades(find_modules) -> List[Tuple[str, BaseClade]]:
    clades = []
    for module_path in find_modules:
        module = importlib.import_module(module_path)
        for name, x in vars(module).items():
            if isinstance(x, BaseClade):
                clades.append((name, x))
    return clades


EXCLUDED = [
    ("Chelonoidis niger complex", "C_NIGER"),
    ("Rhododendron Nova Zembla", "R_NOVA_ZEMBLA"),
    ("inverted repeat-lacking clade", "IRLC"),
    ("non-protein amino acid-accumulating clade", "NPAAA_CLADE"),
    ("Rosa 'Mister Lincoln'", "R_MISTER_LINCOLN"),
]


def normalize(s):
    return (
        s.lower()
        .replace("-", "_")
        .replace("‑", "_")
        .replace(" ", "_")
        .replace("sect.", "section")
    )


def test_names(named_clades):
    mismatches = []
    for name, clade in named_clades:
        if (clade.name, name) in EXCLUDED:
            continue
        if clade.rank == Rank.SPECIES:
            try:
                genus, *_, epithet = clade.name.split()
            except ValueError:
                mismatches.append((clade.name, name))
                continue
            if name.lower() not in (
                normalize(f"{genus[0]}_{epithet}"),
                normalize(f"{genus}_{epithet}"),
            ):
                mismatches.append((clade.name, name))
        elif clade.rank == Rank.SUBGENUS:
            if normalize(clade.name.replace("subg.", "subgenus")) != name.lower():
                mismatches.append((clade.name, name))
        elif clade.name or clade.rank != Rank.UNRANKED:
            if normalize(clade.name) != name.lower():
                mismatches.append((clade.name, name))
    assert mismatches == []
