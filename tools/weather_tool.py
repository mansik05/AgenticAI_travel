import requests


def get_weather(latitude, longitude):

    """
    Get simplified weather forecast
    """

    try:

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&daily=temperature_2m_max,temperature_2m_min"
            f"&timezone=auto"
        )

        response = requests.get(url)

        data = response.json()

        forecast = []

        dates = data["daily"]["time"]
        max_temps = data["daily"]["temperature_2m_max"]
        min_temps = data["daily"]["temperature_2m_min"]

        for i in range(len(dates)):

            forecast.append({
                "date": dates[i],
                "max_temp": max_temps[i],
                "min_temp": min_temps[i]
            })

        return forecast

    except Exception as e:
        return {"error": str(e)}