import requests

class MarineOpenMeteoClient():
    BASE_URL = "https://marine-api.open-meteo.com/v1/marine"

    def __init__(self):
            pass
    def latest(self,latitude,longitude):
        return requests.get(f"{self.BASE_URL}?latitude={latitude}&longitude={longitude}&daily=wave_height_max,wave_direction_dominant,wave_period_max,wind_wave_height_max,wind_wave_direction_dominant,wind_wave_period_max,swell_wave_height_max,swell_wave_direction_dominant,swell_wave_period_max&timezone=America%2FSao_Paulo&past_days=3&forecast_days=3")
    