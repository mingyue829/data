from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="kpop")
location = geolocator.geocode("Goyang")
print(location.address)
# Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
print(location.raw)
# {'place_id': '9167009604', 'type': 'attraction', ...}