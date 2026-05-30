from tools.weather_tool import get_weather


# Goa coordinates
latitude = 15.2993
longitude = 74.1240

result = get_weather(latitude, longitude)

print(result)