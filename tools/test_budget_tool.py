from tools.budget_tool import calculate_budget


result = calculate_budget(
    flight_price=5000,
    hotel_price_per_night=3000,
    days=3
)

print(result)