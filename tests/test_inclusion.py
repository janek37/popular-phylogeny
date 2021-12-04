import importlib
from queue import Queue

import pytest

import clade
from data.base import LIFE


@pytest.fixture
def code_clades(find_modules):
    clades = []
    for module_path in find_modules:
        module = importlib.import_module(module_path)
        for x in vars(module).values():
            if isinstance(x, clade.Clade):
                clades.append(x)
    return clades


@pytest.fixture
def life_clades():
    clades = []
    queue = Queue()
    queue.put(LIFE)
    while not queue.empty():
        current_clade = queue.get()
        clades.append(current_clade)
        for child in current_clade.children:
            queue.put(child)
    return clades


def test_inclusion(code_clades, life_clades):
    missing = []
    for code_clade in code_clades:
        if code_clade not in life_clades:
            missing.append(code_clade)
    assert missing == []
    missing = []
    for life_clade in life_clades:
        if life_clade not in code_clades:
            missing.append(life_clade)
    assert missing == []
