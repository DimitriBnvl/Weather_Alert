import requests

API_KEY = "87bc5a5b3eb4f9d629def5deb9ed9fb9"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 55.953251
MY_LONG = -3.188267
UNITS = "metric"
TIMESTEPS = 4

weather_parameters = {
    "lat"  : MY_LAT,
    "lon"  : MY_LONG,
    "appid": API_KEY,
    "units": UNITS,
    "cnt"  : TIMESTEPS,
}

def request_weather(params):
    response = requests.get(OWM_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    return data

print(request_weather(weather_parameters))