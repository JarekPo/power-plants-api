from sqlmodel import SQLModel


class GeonamesData(SQLModel):
    country_name: str
