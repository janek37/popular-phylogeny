import abc
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Iterator, List, Mapping, Sequence

from constants import IMAGE
from image import Image


class Rank(Enum):
    UNRANKED = "unranked"
    DOMAIN = "Domain"
    KINGDOM = "Kingdom"
    SUPERPHYLUM = "Superphylum"
    PHYLUM = "Phylum"
    SUBPHYLUM = "Subphylum"
    INFRAPHYLUM = "Infraphylum"
    SUPERCLASS = "Superclass"
    CLASS = "Class"
    SUBCLASS = "Subclass"
    INFRACLASS = "Infraclass"
    MEGACOHORT = "Megacohort"
    SUPERCOHORT = "Supercohort"
    COHORT = "Cohort"
    SUBCOHORT = "Subcohort"
    MAGNORDER = "Magnorder"
    SUPERORDER = "Superorder"
    GRANDORDER = "Grandorder"
    MIRORDER = "Mirorder"
    ORDER = "Order"
    SUBORDER = "Suborder"
    INFRAORDER = "Infraorder"
    PARVORDER = "Parvorder"
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
class BaseClade(abc.ABC):
    name: str = ""
    local_names: Mapping[str, str] = field(default_factory=dict)
    known_for: List[Mapping[str, str]] = field(default_factory=list)
    rank: ClassVar[Rank] = Rank.UNRANKED

    @property
    @abc.abstractmethod
    def is_extinct(self) -> bool:
        pass

    def serialize(self, id_iterator: Iterator[int]):
        known_for = [self._serialize_known_for_item(item) for item in self.known_for]
        return {
            "id": next(id_iterator),
            "name": self.name or None,
            "rank": self.rank.value,
            "extinct": self.is_extinct,
            "local_names": self.local_names,
            "known_for": known_for,
        }

    @staticmethod
    def _serialize_known_for_item(known_for_item):
        if IMAGE in known_for_item:
            item_copy = dict(known_for_item)
            item_copy[IMAGE] = item_copy[IMAGE].serialize()
            return item_copy
        return known_for_item


@dataclass
class Clade(BaseClade):
    children: Sequence[BaseClade] = field(default_factory=list)
    _is_extinct: bool = None

    @property
    def is_extinct(self) -> bool:
        if self._is_extinct is None:
            self._is_extinct = all(child.is_extinct for child in self.children)
        return self._is_extinct

    def serialize(self, id_iterator: Iterator[int]):
        serialized = super().serialize(id_iterator)
        serialized["children"] = [
            child.serialize(id_iterator) for child in self.children
        ]
        serialized["species_count"] = sum(
            child["species_count"] if "children" in child else 1
            for child in serialized["children"]
        )
        return serialized


class Domain(Clade):
    rank = Rank.DOMAIN


class Kingdom(Clade):
    rank = Rank.KINGDOM


class Superphylum(Clade):
    rank = Rank.SUPERPHYLUM


class Phylum(Clade):
    rank = Rank.PHYLUM


class Subphylum(Clade):
    rank = Rank.SUBPHYLUM


class Infraphylum(Clade):
    rank = Rank.INFRAPHYLUM


class Superclass(Clade):
    rank = Rank.SUPERCLASS


class Class(Clade):
    rank = Rank.CLASS


class Subclass(Clade):
    rank = Rank.SUBCLASS


class Infraclass(Clade):
    rank = Rank.INFRACLASS


class Megacohort(Clade):
    rank = Rank.MEGACOHORT


class Supercohort(Clade):
    rank = Rank.SUPERCOHORT


class Cohort(Clade):
    rank = Rank.COHORT


class Subcohort(Clade):
    rank = Rank.SUBCOHORT


class Magnorder(Clade):
    rank = Rank.MAGNORDER


class Superorder(Clade):
    rank = Rank.SUPERORDER


class Grandorder(Clade):
    rank = Rank.GRANDORDER


class Mirorder(Clade):
    rank = Rank.MIRORDER


class Order(Clade):
    rank = Rank.ORDER


class Suborder(Clade):
    rank = Rank.SUBORDER


class Infraorder(Clade):
    rank = Rank.INFRAORDER


class Parvorder(Clade):
    rank = Rank.PARVORDER


class Superfamily(Clade):
    rank = Rank.SUPERFAMILY


class Epifamily(Clade):
    rank = Rank.EPIFAMILY


class Family(Clade):
    rank = Rank.FAMILY


class Subfamily(Clade):
    rank = Rank.SUBFAMILY


class Supertribe(Clade):
    rank = Rank.SUPERTRIBE


class Tribe(Clade):
    rank = Rank.TRIBE


class Subtribe(Clade):
    rank = Rank.SUBTRIBE


class Genus(Clade):
    rank = Rank.GENUS


class Subgenus(Clade):
    rank = Rank.SUBGENUS


class Superspecies(Clade):
    rank = Rank.SUPERSPECIES


class Species(BaseClade):
    rank = Rank.SPECIES

    def __init__(self, image: Image, extinct: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.extinct = extinct
        self.image = image

    @property
    def is_extinct(self) -> bool:
        return self.extinct

    def serialize(self, id_iterator: Iterator[int]):
        serialized = super().serialize(id_iterator)
        return {
            "image": self.image.serialize(),
            **serialized,
        }
