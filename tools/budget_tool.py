def calculate_budget(
    flight_price,
    hotel_price_per_night,
    days,
    daily_expense=1000
):

    """
    Calculate estimated trip budget
    """

    try:

        hotel_total = hotel_price_per_night * days

        food_and_transport = daily_expense * days

        total_budget = (
            flight_price
            + hotel_total
            + food_and_transport
        )

        return {
            "flight_cost": flight_price,
            "hotel_cost": hotel_total,
            "food_and_transport": food_and_transport,
            "total_budget": total_budget
        }

    except Exception as e:
        return {"error": str(e)}