import requests

API_KEY           = "87bc5a5b3eb4f9d629def5deb9ed9fb9"
OWM_ENDPOINT      = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT            = 55.953251
MY_LONG           = -3.188267
UNITS             = "metric"
TIMESTEPS         = 5
TIMESTEP_INTERVAL = 3 # Number of hours between each timestep

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

def detect_precipitation(data):
    thunderstorm_detected = False
    drizzle_detected      = False
    rainfall_detected     = False
    snowfall_detected     = False

    for index in range(len(data["list"])):
        if 200 <= data["list"][index]["main"]["temp"] < 300:
            thunderstorm_detected = True
            thunderstorm_time = index * TIMESTEPS
        if 300 <= data["list"][index]["main"]["temp"] < 400:
            drizzle_detected = True
            drizzle_detect_time = index * TIMESTEPS
        if 500 <= data["list"][index]["main"]["temp"] < 600:
            rainfall_detected = True
            rainfall_detect_time = index * TIMESTEPS
        if 600 <= (data["list"][index]["weather"][0]["id"]) < 700:
            snowfall_detected = True
            snowfall_time     = index * TIMESTEP_INTERVAL

weather_data = request_weather(weather_parameters)
detect_precipitation(weather_data)

#TODO: Add documentation to functions
#TODO: Add detection message
#TODO: index * TIMESTEP_INTERVAL