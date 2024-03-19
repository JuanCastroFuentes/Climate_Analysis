import requests

class MarineOpenMeteoClient():
    WAVE_URL = "https://marine-api.open-meteo.com/v1/marine"

    def __init__(self):
        pass

    def latest(self, latitude, longitude):
        return requests.get(f"{self.WAVE_URL}?latitude={latitude}&longitude={longitude}&daily=wave_height_max,wave_direction_dominant&timezone=America%2FSao_Paulo&past_days=3&forecast_days=3")

class WindOpenMeteoClient():
    WIND_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self):
        pass

    def latest(self, latitude, longitude):
        return requests.get(f"{self.WIND_URL}?latitude={latitude}&longitude={longitude}&daily=wind_speed_10m_max,wind_direction_10m_dominant&timezone=America%2FSao_Paulo&past_days=3&forecast_days=3")
