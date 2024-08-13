from typing import Dict, Union
from fastapi import HTTPException, Query
import requests
from config import GEONAMES_API_URL, GEONAMES_USERNAME
from models.geonames_data import GeonamesData


def get_geonames_request(
    latitude: str = Query(..., title="Latitude", description="Country's latitude"),
    longitude: str = Query(..., title="Longitude", description="Country's longitude"),
) -> Union[GeonamesData, Dict[None, None]]:
    params = {
        "lat": latitude,
        "lng": longitude,
        "username": GEONAMES_USERNAME,
    }

    response = requests.get(
        f"{GEONAMES_API_URL}/findNearbyPlaceNameJSON", params=params
    )

    if response.status_code == 200:
        data = response.json()
        if "geonames" in data and data["geonames"]:
            return GeonamesData(country_name=data["geonames"][0]["countryName"])
        else:
            return {}
    elif response.status_code == 401:
        return HTTPException(satus_code=401, detail="Invalid username")
    elif response.status_code == 404:
        return HTTPException(status_code=404, detail="Not found")
    else:
        return HTTPException(
            status_code=response.status_code, details="Unexpected error"
        )
