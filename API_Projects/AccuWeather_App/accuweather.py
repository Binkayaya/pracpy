import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

city = input('Eneter a city name: ')

url_location_id = f"http://dataservice.accuweather.com/locations/v1/search?apikey={API_KEY}&q={city}"
response = requests.get(url_location_id)
data = response.json()
location_id = data[0]["Key"]



url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_id}?apikey={API_KEY}"
response = requests.get(url)
data = response.json()
print(f"The temperature in {city} is", data[0]["Temperature"]["Metric"]["Value"], "°C")


