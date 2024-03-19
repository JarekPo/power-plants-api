import pandas as pd
from pandas import DataFrame


power_plants_df: DataFrame


def read_from_csv() -> DataFrame:
    power_plants_df = pd.read_csv(
        "datasets/global_power_plants.csv",
        usecols=[
            "country",
            "country_long",
            "name",
            "gppd_idnr",
            "capacity_mw",
            "latitude",
            "longitude",
            "primary_fuel",
            "other_fuel1",
            "other_fuel2",
            "commissioning_year",
            "owner",
            "wepp_id",
        ],
    )
    return power_plants_df
