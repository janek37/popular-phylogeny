from dataclasses import dataclass
from enum import Enum
from typing import Optional


class License(Enum):
    pass


@dataclass
class Image:
    image_url: str
    url: str
    author: str
    license: License
    name: Optional[str] = None
