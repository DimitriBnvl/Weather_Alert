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
        timestep = index * TIMESTEP_INTERVAL
        weather_condition = data["list"][index]["main"]["temp"]

        if 200 <= weather_condition < 300:
            thunderstorm_detected = True
            thunderstorm_time = timestep
        if 300 <= weather_condition < 400:
            drizzle_detected = True
            drizzle_time = timestep
        if 500 <= weather_condition < 600:
            rainfall_detected = True
            rainfall_time = timestep
        if 600 <= weather_condition < 700:
            snowfall_detected = True
            snowfall_time = timestep


weather_data = request_weather(weather_parameters)
detect_precipitation(weather_data)

#TODO: Add documentation to functions
#TODO: Add detection message
#TODO: index * TIMESTEP_INTERVAL