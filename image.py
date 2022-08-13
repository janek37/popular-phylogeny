from dataclasses import dataclass
from enum import Enum
from typing import Optional

PD = "Public Domain"
CC_BY = "Creative Commons Attribution"
CC_BY_SA = f"{CC_BY}-Share Alike"


class License(Enum):
    PUBLIC_DOMAIN_SELF = PD
    PUBLIC_DOMAIN_USER = PD
    PUBLIC_DOMAIN_AUTHOR = PD
    PUBLIC_DOMAIN_LINK = PD
    PUBLIC_DOMAIN_OLD = PD
    PUBLIC_DOMAIN_CHEM = PD
    PUBLIC_DOMAIN_INELIGIBLE = PD
    CDC = f"{PD} by Centers for Disease Control and Prevention"
    DARTHMOUTH = f"{PD} by Dartmouth Electron Microscope Facility"
    NIH = f"{PD} by National Institutes of Health"
    NASA = f"{PD} by the National Aeronautics and Space Administration"
    NOAA = f"{PD} by National Oceanic and Atmospheric Administration"
    USDA = f"{PD} by United States Department of Agriculture"
    FMIB = f"{PD} by Freshwater and Marine Image Bank, University of Washington"
    FWS = f"{PD} by United States Fish and Wildlife Service"
    USPOSTAL = f"{PD} by United Stated Postal Service"
    USDA_ARS = f"{PD} by Agricultural Research Service, United States Department of Agriculture"
    EPA = f"{PD} by Environmental Protection Agency"
    NPS = f"{PD} by National Park Service"
    USGS = f"{PD} by United States Geological Survey"
    ATTRIBUTION = "Attribution Only"
    CC_BY_2_0 = f"{CC_BY} 2.0 Generic"
    CC_BY_2_0_DE = f"{CC_BY} 2.0 Germany"
    CC_BY_2_5 = f"{CC_BY} 2.5 Generic"
    CC_BY_2_5_ES = f"{CC_BY} 2.5 Spain"
    CC_BY_3_0 = f"{CC_BY} 3.0 Unported"
    CC_BY_3_0_US = f"{CC_BY} 3.0 United States"
    CC_BY_4_0 = f"{CC_BY} 4.0 International"
    CC_BY_SA_2_0 = f"{CC_BY_SA} 2.0 Generic"
    CC_BY_SA_2_0_DE = f"{CC_BY_SA} 2.0 Germany"
    CC_BY_SA_2_5 = f"{CC_BY_SA} 2.5 Generic"
    CC_BY_SA_3_0 = f"{CC_BY_SA} 3.0 Unported"
    CC_BY_SA_3_0_US = f"{CC_BY_SA} 3.0 United States"
    CC_BY_SA_4_0 = f"{CC_BY_SA} 4.0 International"
    CC0 = "Creative Commons CC0 1.0 Universal Public Domain Dedication"


CC_BY_URL_TEMPLATE = "https://creativecommons.org/licenses/by/{version}/deed.en"
CC_BY_SA_URL_TEMPLATE = "https://creativecommons.org/licenses/by-sa/{version}/deed.en"

LICENSE_URLS = {
    License.CC_BY_2_0: CC_BY_URL_TEMPLATE.format(version="2.0"),
    License.CC_BY_2_0_DE: CC_BY_URL_TEMPLATE.format(version="2.0/de"),
    License.CC_BY_2_5: CC_BY_URL_TEMPLATE.format(version="2.5"),
    License.CC_BY_2_5_ES: CC_BY_URL_TEMPLATE.format(version="2.5/es"),
    License.CC_BY_3_0: CC_BY_URL_TEMPLATE.format(version="3.0"),
    License.CC_BY_3_0_US: CC_BY_URL_TEMPLATE.format(version="3.0/us"),
    License.CC_BY_4_0: CC_BY_URL_TEMPLATE.format(version="4.0"),
    License.CC_BY_SA_2_0: CC_BY_SA_URL_TEMPLATE.format(version="2.0"),
    License.CC_BY_SA_2_0_DE: CC_BY_SA_URL_TEMPLATE.format(version="2.0/de"),
    License.CC_BY_SA_2_5: CC_BY_SA_URL_TEMPLATE.format(version="2.5"),
    License.CC_BY_SA_3_0: CC_BY_SA_URL_TEMPLATE.format(version="3.0"),
    License.CC_BY_SA_3_0_US: CC_BY_SA_URL_TEMPLATE.format(version="3.0/us"),
    License.CC_BY_SA_4_0: CC_BY_SA_URL_TEMPLATE.format(version="4.0"),
    License.CC0: "https://creativecommons.org/share-your-work/public-domain/cc0/",
}


@dataclass
class Image:
    image_url: str
    url: str
    author: str
    license: License
    name: Optional[str] = None

    def serialize(self):
        return {
            "image_url": self.image_url,
            "url": self.url,
            "author": self.author,
            "license_code": self.license.name,
            "license_string": self.license.value,
            "license_url": LICENSE_URLS.get(self.license),
            "name": self.name,
        }
