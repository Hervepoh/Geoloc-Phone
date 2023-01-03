import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
import folium

# Get the country
number = "+237677782226"
lang = "en"
number = phonenumbers.parse(number)  # Parsing String to Phone number
print(number)
localisation = geocoder.description_for_number(number, lang)
print(localisation)

# Get timezone from a phone number
timeZone = timezone.time_zones_for_number(number)

# Get mobile operator
operator = carrier.name_for_number(number, lang)
print(operator)

# Find latitude and longitude
key = '651535c451da497a892f2fcab4d6678a'
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