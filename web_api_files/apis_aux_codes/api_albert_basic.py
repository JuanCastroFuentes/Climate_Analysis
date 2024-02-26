import requests

# Define the API endpoint and parameters
url = "https://marine-api.open-meteo.com/v1/marine"
params = {
    "latitude": 54.544587,
    "longitude": 10.227487,
    "daily": "wave_height_max",
    "timezone": "America/Sao_Paulo"
}

# Fetch weather data
try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    print(data)  # Print the response data
except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)