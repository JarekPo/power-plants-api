from fastapi import Response
from fastapi.responses import HTMLResponse

# import pandas as pd
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session, select

from config import DATABASE_PASSWORD, DATABASE_USER, DATABASE_HOST
from models.power_plants_data import PowerPlantsData

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}"


# def read_from_csv() -> pd.DataFrame:
#     power_plants_df = pd.read_csv(
#         "datasets/global_power_plants.csv",
#         usecols=[
#             "country",
#             "country_long",
#             "name",
#             "gppd_idnr",
#             "capacity_mw",
#             "latitude",
#             "longitude",
#             "primary_fuel",
#         ],
#         na_values=["NaN", ""],
#     )
#     return power_plants_df


# def set_power_plants_data() -> Response:
#     engine = create_engine(DATABASE_URL, echo=True)
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         existing_records = session.exec(select(PowerPlantsData)).first()
#         if not existing_records:
#             csv_data = read_from_csv()
#             for _, row in csv_data.iterrows():
#                 plant = PowerPlantsData(
#                     country=row["country"],
#                     country_long=row["country_long"],
#                     name=row["name"],
#                     gppd_idnr=row["gppd_idnr"],
#                     capacity_mw=row["capacity_mw"],
#                     latitude=row["latitude"],
#                     longitude=row["longitude"],
#                     primary_fuel=row["primary_fuel"],
#                 )
#                 session.add(plant)
#             session.commit()
#             return HTMLResponse(
#                 content="Data added successfully",
#                 status_code=200,
#             )
#         else:
#             return HTMLResponse(
#                 content="OK, Data already exists",
#                 status_code=200,
#             )
