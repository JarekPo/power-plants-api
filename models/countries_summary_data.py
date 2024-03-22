from sqlmodel import SQLModel


class CountriesSummaryData(SQLModel):
    country_long: str
    plants_number: int
    total_capacity: float
