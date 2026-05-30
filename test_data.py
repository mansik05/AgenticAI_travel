from utils.helpers import load_json

flights = load_json("data/flights.json")

print(type(flights))
print(len(flights))

print(flights[0])

hotels = load_json("data/hotels.json")
print(type(hotels))
print(len(hotels))
print(hotels[0])

places = load_json("data/places.json")
print(type(places))
print(len(places[0]))
print(places[0])