from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Mapping, Sequence


class Rank(Enum):
    UNRANKED = "unranked"
    DOMAIN = "Domain"
    KINGDOM = "Kingdom"
    SUPERPHYLUM = "Superphylum"
    PHYLUM = "Phylum"
    SUBPHYLUM = "Subphylum"
    SUPERCLASS = "Superclass"
    CLASS = "Class"
    SUBCLASS = "Subclass"
    INFRACLASS = "Infraclass"
    SUPERCOHORT = "Supercohort"
    COHORT = "Cohort"
    SUBCOHORT = "Subcohort"
    SUPERORDER = "Superorder"
    ORDER = "Order"
    SUBORDER = "Suborder"
    INDRAORDER = "Infraorder"
    SUPERFAMILY = "Superfamily"
    EPIFAMILY = "Epifamily"
    FAMILY = "Family"
    SUBFAMILY = "Subfamily"
    SUPERTRIBE = "Supertribe"
    TRIBE = "Tribe"
    SUBTRIBE = "Subtribe"
    GENUS = "Genus"
    SUBGENUS = "Subgenus"
    SUPERSPECIES = "Superspecies"
    SPECIES = "Species"


@dataclass
class Clade:
    name: str = ""
    children: Sequence["Clade"] = field(default_factory=list)
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
class Subphylum(Clade):
    rank = Rank.SUBPHYLUM


@dataclass
class Superclass(Clade):
    rank = Rank.SUPERCLASS


@dataclass
class Class(Clade):
    rank = Rank.CLASS


@dataclass
class Subclass(Clade):
    rank = Rank.SUBCLASS


@dataclass
class Infraclass(Clade):
    rank = Rank.INFRACLASS


@dataclass
class Supercohort(Clade):
    rank = Rank.SUPERCOHORT


@dataclass
class Cohort(Clade):
    rank = Rank.COHORT


@dataclass
class Subcohort(Clade):
    rank = Rank.SUBCOHORT


@dataclass
class Superorder(Clade):
    rank = Rank.SUPERORDER


@dataclass
class Order(Clade):
    rank = Rank.ORDER


@dataclass
class Suborder(Clade):
    rank = Rank.SUBORDER


@dataclass
class Infraorder(Clade):
    rank = Rank.INDRAORDER


@dataclass
class Superfamily(Clade):
    rank = Rank.SUPERFAMILY


@dataclass
class Epifamily(Clade):
    rank = Rank.EPIFAMILY


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
class Subgenus(Clade):
    rank = Rank.SUBGENUS


@dataclass
class Superspecies(Clade):
    rank = Rank.SUPERSPECIES


@dataclass
class Species(Clade):
    rank = Rank.SPECIES
