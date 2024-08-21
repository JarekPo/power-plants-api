from typing import List
from sqlmodel import SQLModel


class GeonamesCountry(SQLModel):
    country_name: str


class GeonamesData(GeonamesCountry):
    latitude: str
    longitude: str


class AlternativeNames(SQLModel):
    alternative_names: List[str]
