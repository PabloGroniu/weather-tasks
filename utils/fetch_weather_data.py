import requests

def convert_K_to_C(x):
    return round(int(x - 273.15))

def get_weather():
    API_KEY = "8e3a6d558d218eacfd708aff7aebb910"
    CITY = "Tenerife"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    return data

