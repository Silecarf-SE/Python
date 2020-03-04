from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Jeongwoo")
location = geolocator.geocode("Incheon, South Koera")
print(location.raw)