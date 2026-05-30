import json


def search_flights(source, destination):

    """
    Search flights between source and destination
    """

    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    results = []

    for flight in flights:

        if (
            flight["from"].lower() == source.lower()
            and flight["to"].lower() == destination.lower()
        ):
            results.append(flight)

    results = sorted(results, key=lambda x: x["price"])

    return results[:5]