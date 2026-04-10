import requests

API_KEY           = "87bc5a5b3eb4f9d629def5deb9ed9fb9"
OWM_ENDPOINT      = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT            = 33.1128
MY_LONG           = 139.7890
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
    """
    Makes a request to the OpenWeatherMap API using provided parameters.

    Args:
        params (dict): Dictionary of parameters including lat, lon, and appid.

    Returns:
        dict: The JSON response from the API.
    """
    response = requests.get(OWM_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    return data

def get_time_offset(index, interval):
    """
    Calculates the hour offset from now for a given forecast index.

    Args:
        index (int): The index in the forecast list.
        interval (int): The number of hours between each forecast step.

    Returns:
        int: The number of hours from the start time.
    """
    return index * interval

def detect_precipitation(data):
    """
    Analyzes the weather data to identify precipitation events.

    Args:
        data (dict): The weather forecast data from the OWM API.

    Returns:
        list: A list of dictionaries, each describing a weather event found.
              Format: [{"condition": str, "hour_offset": int}, ...]
    """
    detected_events = []

    for index, data_entry in enumerate(data["list"]):
        hour_offset = get_time_offset(index, TIMESTEP_INTERVAL)
        weather_id = data_entry["weather"][0]["id"]
        
        condition = None
        if 200 <= weather_id < 300:
            condition = "Thunderstorm"
        elif 300 <= weather_id < 400:
            condition = "Drizzle"
        elif 500 <= weather_id < 600:
            condition = "Rain"
        elif 600 <= weather_id < 700:
            condition = "Snow"

        if condition:
            detected_events.append({
                "condition": condition,
                "hour_offset": hour_offset
            })
            
    return detected_events


def output_message(detected_events):
    if detected_events:
        print("Precipitation detected:")
        for event in detected_events:
            if event['hour_offset'] == 0:
                print(f"    It is {event['condition'].lower()}ing right now.")
            else:
                print(f"    {event['condition']} in {event['hour_offset']} hours from now.")
    else:
        print("No precipitation detected in the forecast period.")

weather_data = request_weather(weather_parameters)
events = detect_precipitation(weather_data)
output_message(events)