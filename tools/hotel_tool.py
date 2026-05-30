import json


def search_hotels(city, max_price=5000):

    """
    Search hotels by city and budget.
    """

    try:

        with open("data/hotels.json", "r", encoding="utf-8") as f:
            hotels = json.load(f)

        matching_hotels = []

        for hotel in hotels:

            if (
                hotel["city"].lower() == city.lower()
                and hotel["price_per_night"] <= max_price
            ):

                matching_hotels.append(hotel)

        # Sort by stars descending
        matching_hotels = sorted(
            matching_hotels,
            key=lambda x: x["stars"],
            reverse=True
        )

        return matching_hotels[:5]

    except Exception as e:
        return {"error": str(e)}