from sqlmodel import SQLModel


class GeonamesCountry(SQLModel):
    country_name: str


class GeonamesData(GeonamesCountry):
    latitude: str
    longitude: str
