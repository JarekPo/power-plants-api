from typing import Dict, Union
from fastapi import HTTPException, Query
import requests
from config import GEONAMES_API_URL, GEONAMES_USERNAME
from models.geonames_data import AlternativeNames, GeonamesCountry, GeonamesData


def get_geonames_request(
    latitude: str = Query(..., title="Latitude", description="Country's latitude"),
    longitude: str = Query(..., title="Longitude", description="Country's longitude"),
) -> Union[GeonamesCountry, Dict[None, None]]:
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
            return GeonamesCountry(country_name=data["geonames"][0]["countryName"])
        else:
            return {}
    elif response.status_code == 401:
        raise HTTPException(satus_code=401, detail="Invalid username")
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        raise HTTPException(
            status_code=response.status_code, details="Unexpected error"
        )


def search_country_request(
    name: str = Query(
        ..., title="City name", description="Search country details by city"
    )
) -> Union[GeonamesData, Dict[None, None]]:
    params = {
        "name": name,
        "username": GEONAMES_USERNAME,
    }

    response = requests.get(f"{GEONAMES_API_URL}/searchJSON", params=params)

    if response.status_code == 200:
        data = response.json()
        if "geonames" in data and data["geonames"]:
            return GeonamesData(
                country_name=data["geonames"][0]["countryName"],
                latitude=data["geonames"][0]["lat"],
                longitude=data["geonames"][0]["lng"],
            )
        else:
            return {}
    elif response.status_code == 401:
        raise HTTPException(satus_code=401, detail="Invalid username")
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        raise HTTPException(
            status_code=response.status_code, details="Unexpected error"
        )


def get_alternative_names_request(
    countryID: str = Query(..., title="Country ID", description="Country ID")
) -> Union[AlternativeNames, Dict[None, None]]:
    params = {
        "geonameId": countryID,
        "username": GEONAMES_USERNAME,
    }

    response = requests.get(f"{GEONAMES_API_URL}/getJSON", params=params)

    if response.status_code == 200:
        data = response.json()
        if "alternateNames" in data and data["alternateNames"]:
            names = [name_obj["name"] for name_obj in data.get("alternateNames", [])]
            return AlternativeNames(alternative_names=names)
        else:
            return {}
    elif response.status_code == 401:
        raise HTTPException(satus_code=401, detail="Invalid name ID")
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        raise HTTPException(
            status_code=response.status_code, details="Unexpected error"
        )
