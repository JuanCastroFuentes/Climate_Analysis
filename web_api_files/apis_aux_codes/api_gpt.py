import requests
import pandas as pd
from datetime import datetime, timedelta

# Define the API endpoint and parameters
url = "https://marine-api.open-meteo.com/v1/marine"
params = {
    "latitude": 54.544587,
    "longitude": 10.227487,
    "daily": "wave_height_max",
    "timezone": "America/Sao_Paulo"
}

# Define a function to fetch data from the API
def fetch_weather_data(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# Fetch weather data
weather_data = fetch_weather_data(url, params)

if weather_data:
    # Process the response
    response = weather_data[0]
    print(f"Coordinates {response['latitude']}°N {response['longitude']}°E")
    print(f"Elevation {response['elevation']} m asl")
    print(f"Timezone {response['timezone']} {response['timezone_abbreviation']}")
    print(f"Timezone difference to GMT+0 {response['utc_offset_seconds']} s")

    # Process daily data
    daily = response['daily']
    daily_data = {"date": pd.date_range(
        start=datetime.utcfromtimestamp(daily['time']),
        end=datetime.utcfromtimestamp(daily['time_end']),
        freq=timedelta(seconds=daily['interval']),
        inclusive="left"
    )}
    daily_data["wave_height_max"] = daily['variables'][0]['values']

    daily_dataframe = pd.DataFrame(data=daily_data)
    print(daily_dataframe)
