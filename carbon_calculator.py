def calculate_carbon_footprint(
    transport_km,
    vehicle_type,
    electricity_kwh,
    diet_type,
    shopping_orders
):
    # Transportation factors (kg CO2 per km)
    transport_factors = {
        "Petrol Car": 0.21,
        "Diesel Car": 0.24,
        "Electric Vehicle": 0.08,
        "Bus": 0.08,
        "Train": 0.05,
        "Bike": 0.0,
        "Walking": 0.0
    }

    transport_emission = (
        transport_km * 365 * transport_factors[vehicle_type]
    )

    # Electricity
    energy_emission = electricity_kwh * 12 * 0.82

    # Diet
    diet_factors = {
        "Vegetarian": 500,
        "Mixed": 1000,
        "Non-Vegetarian": 1500
    }

    food_emission = diet_factors[diet_type]

    # Shopping
    shopping_emission = shopping_orders * 12 * 5

    total = (
        transport_emission
        + energy_emission
        + food_emission
        + shopping_emission
    )

    return {
        "transport": round(transport_emission / 1000, 2),
        "energy": round(energy_emission / 1000, 2),
        "food": round(food_emission / 1000, 2),
        "shopping": round(shopping_emission / 1000, 2),
        "total": round(total / 1000, 2)
    }


def carbon_iq_score(total_emissions):
    score = max(0, 100 - int(total_emissions * 15))
    return score