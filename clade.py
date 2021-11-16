from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Mapping, Sequence


class Rank(Enum):
    UNRANKED = 'unranked'
    DOMAIN = 'Domain'
    KINGDOM = 'Kingdom'
    SUPERPHYLUM = 'Superphylum'
    PHYLUM = 'Phylum'
    CLASS = 'Class'
    ORDER = 'Order'
    FAMILY = 'Family'
    SUBFAMILY = 'Subfamily'
    GENUS = 'Genus'
    SUPERTRIBE = 'Supertribe'
    TRIBE = 'Tribe'
    SUBTRIBE = 'Subtribe'
    SPECIES = 'Species'


@dataclass
class Clade:
    name: str = ''
    children: Sequence['Clade'] = field(default_factory=list)
    local_names: Mapping[str, str] = field(default_factory=dict)
    known_for: Sequence[Mapping[str, str]] = field(default_factory=list)
    rank: ClassVar[Rank] = Rank.UNRANKED


@dataclass
class Domain(Clade):
    rank = Rank.DOMAIN


@dataclass
class Kingdom(Clade):
    rank = Rank.KINGDOM


@dataclass
class Superphylum(Clade):
    rank = Rank.SUPERPHYLUM


@dataclass
class Phylum(Clade):
    rank = Rank.PHYLUM


@dataclass
class Class(Clade):
    rank = Rank.CLASS


@dataclass
class Order(Clade):
    rank = Rank.ORDER


@dataclass
class Family(Clade):
    rank = Rank.FAMILY


@dataclass
class Subfamily(Clade):
    rank = Rank.SUBFAMILY


@dataclass
class Supertribe(Clade):
    rank = Rank.SUPERTRIBE


@dataclass
class Tribe(Clade):
    rank = Rank.TRIBE


@dataclass
class Subtribe(Clade):
    rank = Rank.SUBTRIBE


@dataclass
class Genus(Clade):
    rank = Rank.GENUS


@dataclass
class Species(Clade):
    rank = Rank.SPECIES
