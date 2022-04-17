from dataclasses import dataclass
from enum import Enum
from typing import Optional


class License(Enum):
    CDC = "Public Domain by Centers for Disease Control and Prevention"
    DARTHMOUTH = "Public Domain by Dartmouth Electron Microscope Facility"
    NIH = "Public Domain by National Institutes of Health"
    NASA = "Public Domain by the National Aeronautics and Space Administration"
    CC_BY_SA_3_0 = "Creative Commons Attribution-Share Alike 3.0 Unported"
    CC_BY_SA_4_0 = "Creative Commons Attribution-Share Alike 4.0 International"
    CC0 = "Creative Commons CC0 1.0 Universal Public Domain Dedication"


@dataclass
class Image:
    image_url: str
    url: str
    author: str
    license: License
    name: Optional[str] = None
