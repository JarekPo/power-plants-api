from typing import List
from fastapi import HTTPException
from sqlalchemy import create_engine, text
from sqlmodel import Session
from models.power_plants_data import PowerPlantsData
from config import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}"


def get_all_plants() -> List[PowerPlantsData]:
    engine = create_engine(DATABASE_URL, echo=True)
    with Session(engine) as session:
        data_query = text(
            """
            SELECT * FROM powerplantsdata
            """
        )
    results = session.execute(data_query)
    data = []
    for row in results:
        country = row[0]
        country_long = row[1]
        name = row[2]
        gppd_idnr = row[3]
        capacity_mw = row[4]
        latitude = row[5]
        longitude = row[6]
        primary_fuel = row[7]
        power_plants_data = PowerPlantsData(
            country=country,
            country_long=country_long,
            name=name,
            gppd_idnr=gppd_idnr,
            capacity_mw=capacity_mw,
            latitude=latitude,
            longitude=longitude,
            primary_fuel=primary_fuel,
        )
        data.append(power_plants_data)

    if data:
        return data

    else:
        raise HTTPException(
            status_code=500, detail="Error occurred while fetching power plants data"
        )
