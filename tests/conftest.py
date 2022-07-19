# https://stackoverflow.com/a/54323162/245594
import importlib
import pkgutil
import sys
from collections import deque
from typing import List

import pytest

import clade
import data


@pytest.fixture
def find_modules():
    module = data
    path_list = []
    spec_list = []
    for importer, modname, ispkg in pkgutil.walk_packages(module.__path__):
        import_path = f"{module.__name__}.{modname}"
        if ispkg:
            spec = pkgutil._get_spec(importer, modname)
            importlib._bootstrap._load(spec)
            spec_list.append(spec)
        else:
            path_list.append(import_path)
    for spec in spec_list:
        del sys.modules[spec.name]
    return path_list


@pytest.fixture
def life_clades() -> List[clade.BaseClade]:
    clades = []
    queue = deque()
    queue.append(data.LIFE)
    while queue:
        current_clade = queue.popleft()
        clades.append(current_clade)
        if not isinstance(current_clade, clade.Species):
            for child in current_clade.children:
                queue.append(child)
    return clades
