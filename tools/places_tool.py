import json


def search_places(city):

    """
    Search tourist places by city.
    """

    try:

        with open("data/places.json", "r", encoding="utf-8") as f:
            places = json.load(f)

        matching_places = []

        for place in places:

            if place["city"].lower() == city.lower():

                matching_places.append(place)

        # Sort by rating
        matching_places = sorted(
            matching_places,
            key=lambda x: x["rating"],
            reverse=True
        )

        return matching_places[:5]

    except Exception as e:
        return {"error": str(e)}