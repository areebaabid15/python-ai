import requests

def get_weather(city):
    url = f"https://wttr.in/{city}"
    params = {"format": "j1"}   # j1 = JSON format

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        temp_c  = current["temp_C"]
        feels_c = current["FeelsLikeC"]
        desc    = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        print(f"Weather in {city}:")
        print(f"  Condition : {desc}")
        print(f"  Temp      : {temp_c}°C (feels like {feels_c}°C)")
        print(f"  Humidity  : {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"Could not fetch weather: {e}")

get_weather("Karachi")
get_weather("London")