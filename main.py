import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
import folium
from dotenv import load_dotenv
import os

# will first look for a .env file and if it finds one, it will load the environment variables
load_dotenv()
OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')

number = input("Entrer a phone number : ")
lang = "en"

# Parsing String to Phone number
number = phonenumbers.parse(number)
print(number)
# Get the country
localisation = geocoder.description_for_number(number, lang)
print(localisation)

# Get timezone from a phone number
timeZone = timezone.time_zones_for_number(number)

# Get mobile operator
operator = carrier.name_for_number(number, lang)
print(operator)

# Find latitude and longitude
key = OPENCAGE_API_KEY
geocoder = OpenCageGeocode(key)

query = str(localisation)  # "82 Clergywomen Road, London"
result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

# Create the map
map = folium.Map(location=[lat, lng],zoom_start=12)
folium.Marker(
    [lat, lng], popup=localisation, tooltip="Click me!"
).add_to(map)

map.save("index.html")