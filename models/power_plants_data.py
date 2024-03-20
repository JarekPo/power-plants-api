from typing import Optional
from sqlmodel import Field, SQLModel


class PowerPlantsDataInput(SQLModel):
    country: str
    country_long: str
    name: str
    gppd_idnr: str
    capacity_mw: float
    latitude: float
    longitude: float
    primary_fuel: str


class PowerPlantsData(PowerPlantsDataInput, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
