from typing import Dict, List, Union
from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models.countries_summary_data import CountriesSummaryData
from models.geonames_data import GeonamesData
from models.power_plants_data import PowerPlantsData, PowerPlantsDataInput

# from services.load_data_service import set_power_plants_data
from services.geonames_service import get_geonames_request
from services.power_plants_service import (
    get_all_plants,
    get_countries_summary,
    get_country_plants,
)

app = FastAPI(title="Power Plants API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://power-plants-ui.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"health": "OK"}


# @app.post("/load-data", response_model=PowerPlantsDataInput)
# def handle_data_load() -> Response:
#     return set_power_plants_data()


@app.get("/all-plants", response_model=List[PowerPlantsData])
def handle_get_all_plants_request() -> List[PowerPlantsData]:
    return get_all_plants()


@app.get("/countries-summary", response_model=List[CountriesSummaryData])
def handle_get_countries_summary_request() -> List[CountriesSummaryData]:
    return get_countries_summary()


@app.get("/country-plants", response_model=List[PowerPlantsData])
def handle_get_country_plants(
    country: str = Query(..., title="Country", description="Country of power plants.")
) -> List[PowerPlantsData]:
    return get_country_plants(country)


@app.get("/geonames")
def handle_get_geonames_request(
    latitude: str = Query(..., title="Latitude", description="Country's latitude"),
    longitude: str = Query(..., title="Longitude", description="Country's longitude"),
) -> Union[GeonamesData, Dict[None, None]]:
    return get_geonames_request(latitude, longitude)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
