import os
import requests

city = "Delhi"
API_KEY = os.getenv("WEATHER_API_KEY")

if API_KEY is None:
    print("API key not found. Set WEATHER_API_KEY as an environment variable.")
else:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    print(response.json())
