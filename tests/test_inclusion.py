import importlib
from collections import deque
from typing import List

import pytest

import clade
from clade import Species
from data import LIFE


@pytest.fixture
def code_clades(find_modules) -> List[clade.BaseClade]:
    clades = []
    for module_path in find_modules:
        module = importlib.import_module(module_path)
        for x in vars(module).values():
            if isinstance(x, clade.BaseClade):
                clades.append(x)
    return clades


@pytest.fixture
def life_clades() -> List[clade.BaseClade]:
    clades = []
    queue = deque()
    queue.append(LIFE)
    while queue:
        current_clade = queue.popleft()
        clades.append(current_clade)
        if not isinstance(current_clade, Species):
            for child in current_clade.children:
                queue.append(child)
    return clades


def test_inclusion(code_clades, life_clades):
    missing = []
    for code_clade in code_clades:
        if code_clade not in life_clades:
            missing.append(code_clade.name)
    assert missing == []
    missing = []
    for life_clade in life_clades:
        if life_clade not in code_clades:
            missing.append(life_clade.name)
    assert missing == []
